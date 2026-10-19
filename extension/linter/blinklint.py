#!/usr/bin/env python3
"""BlinkOps workflow YAML linter.

  blinklint.py FILE|-  [--json]  [--data DIR]

Checks: YAML syntax, JSON-Schema structure, step ids, {{ }} expressions
(inputs/steps references, functions), flow-control shape, action catalog
(unknown action / input keys / commonly-set keys), cron, formatting.
Exit code 1 if any error-severity diagnostic. Needs PyYAML + jsonschema.
"""
import argparse, json, re, sys
from pathlib import Path

import yaml
from jsonschema import Draft7Validator

HERE = Path(__file__).resolve().parent
ERROR, WARNING, INFO, HINT = "error", "warning", "info", "hint"


def load_data(data_dir):
    d = Path(data_dir)
    return (json.loads((d / "blink-workflow.schema.json").read_text()),
            json.loads((d / "action-index.json").read_text()),
            json.loads((d / "core.json").read_text()))


# ---------------------------------------------------------------- YAML + marks
class Doc:
    """Plain python value tree + path -> source range maps."""

    def __init__(self, text):
        self.text = text
        self.vals = {}   # path -> (sl, sc, el, ec) of value
        self.keys = {}   # path -> range of the key that holds the value
        self.multiline_lines = set()
        root = yaml.compose(text)
        self.data = None if root is None else self._build(root, ())

    @staticmethod
    def _rng(n):
        return (n.start_mark.line, n.start_mark.column, n.end_mark.line, n.end_mark.column)

    def _build(self, node, path):
        self.vals[path] = self._rng(node)
        if isinstance(node, yaml.MappingNode):
            out = {}
            for k, v in node.value:
                key = str(k.value)
                self.keys[path + (key,)] = self._rng(k)
                out[key] = self._build(v, path + (key,))
            return out
        if isinstance(node, yaml.SequenceNode):
            return [self._build(v, path + (i,)) for i, v in enumerate(node.value)]
        if node.end_mark.line > node.start_mark.line:
            self.multiline_lines.update(range(node.start_mark.line, node.end_mark.line + 1))
        return yaml.SafeLoader.construct_object(_C, node)


_C = yaml.SafeLoader("")


class Diags:
    def __init__(self):
        self.items = []

    def add(self, rng, sev, code, msg):
        sl, sc, el, ec = rng
        self.items.append({"line": sl, "col": sc, "endLine": el, "endCol": max(ec, sc + 1) if el == sl else ec,
                           "severity": sev, "code": code, "message": msg})

    def at(self, doc, path, sev, code, msg, key=False):
        rng = (doc.keys.get(path) if key else None) or doc.vals.get(path)
        while rng is None and path:
            path = path[:-1]
            rng = doc.vals.get(path)
        self.add(rng or (0, 0, 0, 1), sev, code, msg)


# ---------------------------------------------------------------- expressions
EXPR = re.compile(r"\{\{(.*?)\}\}", re.S)
STR_LIT = re.compile(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'')
FN_CALL = re.compile(r"(?<![\w.])([A-Za-z_]\w*)\s*\(")
REF = re.compile(r"(?<![\w.])(inputs|steps)\s*\.\s*([A-Za-z_][\w-]*)")
ROOT_REF = re.compile(r"(?<![\w.\"'])([A-Za-z_]\w*)\s*[.\[]")
KEYWORDS = {"true", "false", "nil", "null", "not", "and", "or", "in", "len", "let", "if", "else"}


def scan_expressions(s):
    """Yield (body, index) for each {{ }} and a list of structural problems."""
    problems = []
    pos = 0
    out = []
    for m in EXPR.finditer(s):
        out.append((m.group(1), m.start(1)))
        pos = m.end()
    rest = s[pos:] if out else s
    if "{{" in rest and "}}" not in rest[rest.rfind("{{"):]:
        problems.append("unclosed '{{'")
    return out, problems


# ---------------------------------------------------------------- linter
class Linter:
    def __init__(self, schema, index, core, schema_checks=True):
        self.do_schema = schema_checks
        self.validator = Draft7Validator(schema)
        self.index = index
        self.core = core
        self.funcs = set(core["expression_functions"])
        self.roots = set(core["expression_roots"])
        self.prefixes = {a.split(".")[0] for a in index} | {"automations"}

    # -- entry
    def lint(self, text):
        d = Diags()
        self.format_checks(text, d, None)
        try:
            doc = Doc(text)
        except yaml.YAMLError as e:
            m = getattr(e, "problem_mark", None)
            ln, col = (m.line, m.column) if m else (0, 0)
            prob = getattr(e, "problem", None) or str(e) or "YAML syntax error"
            if "\\t" in prob or "tab" in prob.lower():
                d.add((ln, 0, ln, col + 1), ERROR, "tab-indent", "Tabs are not allowed for indentation; use 2 spaces")
            else:
                d.add((ln, col, ln, col + 1), ERROR, "yaml-syntax", prob)
            return d.items
        self.format_checks(text, d, doc)  # indentation check needs scalar ranges
        if not isinstance(doc.data, dict):
            d.add((0, 0, 0, 1), ERROR, "not-a-mapping", "Workflow must be a YAML mapping")
            return d.items
        if self.do_schema:
            self.schema_checks(doc, d)
        self.semantic_checks(doc, d)
        return d.items

    # -- formatting
    def format_checks(self, text, d, doc):
        lines = text.split("\n")
        for i, ln in enumerate(lines):
            if doc is None:
                if ln != ln.rstrip() and ln.strip():
                    d.add((i, len(ln.rstrip()), i, len(ln)), HINT, "trailing-space", "Trailing whitespace")
            elif i not in doc.multiline_lines and ln.strip() and not ln.lstrip().startswith("#"):
                ind = len(ln) - len(ln.lstrip(" "))
                if ln[ind:ind + 1] == "\t":
                    d.add((i, 0, i, ind + 1), ERROR, "tab-indent", "Tabs are not allowed for indentation")
                elif ind % 2:
                    d.add((i, 0, i, ind), WARNING, "indent-2", "Indentation should be a multiple of 2 spaces")
        if doc is None and text and not text.endswith("\n"):
            d.add((len(lines) - 1, 0, len(lines) - 1, max(len(lines[-1]), 1)), HINT, "final-newline", "File should end with a newline")

    # -- JSON schema
    def schema_checks(self, doc, d):
        for e in self.validator.iter_errors(doc.data):
            path = tuple(e.absolute_path)
            msg, key = e.message, False
            if e.validator == "additionalProperties":
                m = re.search(r"\('([^']+)'", msg)
                if m and path + (m.group(1),) in doc.keys:
                    path, key = path + (m.group(1),), True
                msg = "Unknown property " + (f"'{m.group(1)}'" if m else "") + " (check spelling)"
            elif e.validator == "required":
                m = re.search(r"'([^']+)' is a required", msg)
                msg = f"Missing required property '{m.group(1) if m else ''}'"
            elif len(msg) > 160:
                msg = msg[:157] + "..."
            d.at(doc, path, ERROR, "schema", msg, key=key)

    # -- semantics
    def semantic_checks(self, doc, d):
        data = doc.data
        declared = data.get("inputs") if isinstance(data.get("inputs"), dict) else {}
        self.used_inputs = set()
        self.seen = {}      # lower id -> path (doc order)
        self.all_ids = {}   # lower id -> first path anywhere (for forward-ref detection)
        self.collect_ids(data.get("workflow"), ("workflow",), doc, d)
        self.declared = declared
        for si, sec in enumerate(data.get("workflow") or []):
            if isinstance(sec, dict):
                self.walk(sec.get("steps"), ("workflow", si, "steps"), doc, d, parent=None)
        self.string_refs(data.get("outputs"), ("outputs",), doc, d, len(self.all_ids) + 1)
        self.triggers(data, doc, d)
        for k in declared:
            if k not in self.used_inputs and not self._maybe_dynamic(data):
                d.at(doc, ("inputs", k), HINT, "unused-input", f"Input '{k}' is declared but never referenced", key=True)

    def _maybe_dynamic(self, data):
        return False

    def collect_ids(self, sections, path, doc, d):
        def rec(steps, p):
            for i, s in enumerate(steps or []):
                if not isinstance(s, dict):
                    continue
                sid = s.get("id")
                if isinstance(sid, str):
                    low = sid.lower()
                    if low in self.all_ids:
                        d.at(doc, p + (i, "id"), ERROR, "duplicate-id", f"Duplicate step id '{sid}' (first used at line {doc.vals[self.all_ids[low]][0] + 1})")
                    else:
                        self.all_ids[low] = p + (i, "id")
                rec(s.get("steps"), p + (i, "steps"))
                for ti, t in enumerate(s.get("transitions") or []):
                    if isinstance(t, dict):
                        rec(t.get("steps"), p + (i, "transitions", ti, "steps"))
        for si, sec in enumerate(sections or []):
            if isinstance(sec, dict):
                rec(sec.get("steps"), path + (si, "steps"))

    def walk(self, steps, path, doc, d, parent):
        for i, s in enumerate(steps or []):
            if not isinstance(s, dict):
                continue
            p = path + (i,)
            sid = s.get("id")
            if isinstance(sid, str):
                self.seen[sid.lower()] = p
            action = s.get("action")
            if isinstance(action, str):
                self.check_action(s, action, p, doc, d, parent)
            order = len(self.seen)
            for k in ("inputs", "when", "configuration", "connections"):
                if k in s:
                    self.string_refs(s[k], p + (k,), doc, d, order, action=action)
            self.walk(s.get("steps"), p + ("steps",), doc, d, parent=action)
            for ti, t in enumerate(s.get("transitions") or []):
                if isinstance(t, dict):
                    self.walk(t.get("steps"), p + ("transitions", ti, "steps"), doc, d, parent=action)

    def string_refs(self, obj, path, doc, d, order, action=None):
        if isinstance(obj, dict):
            for k, v in obj.items():
                self.string_refs(v, path + (k,), doc, d, order, action)
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                self.string_refs(v, path + (i,), doc, d, order, action)
        elif isinstance(obj, str) and "{{" in obj:
            self.check_string(obj, path, doc, d, action)

    def check_string(self, s, path, doc, d, action):
        bodies, problems = scan_expressions(s)
        for pr in problems:
            d.at(doc, path, ERROR, "expr-unbalanced", f"Unbalanced expression: {pr}")
        for body, _ in bodies:
            code = STR_LIT.sub('""', body)
            for fn in FN_CALL.findall(code):
                if fn not in self.funcs and fn not in KEYWORDS:
                    d.at(doc, path, WARNING, "expr-unknown-function", f"Unknown expression function '{fn}'")
            for root, name in REF.findall(code):
                if root == "inputs":
                    self.used_inputs.add(name)
                    if name not in self.declared:
                        d.at(doc, path, ERROR, "undeclared-input", f"'inputs.{name}' is not declared in 'inputs'")
                else:
                    low = name.lower()
                    if low == "last" or low in self.seen:
                        continue
                    if low in self.all_ids:
                        d.at(doc, path, WARNING, "step-ref-forward", f"'steps.{name}' is defined later in the workflow")
                    else:
                        d.at(doc, path, ERROR, "step-ref-undefined", f"'steps.{name}' does not match any step id")
            for r in set(ROOT_REF.findall(code)):
                if r not in self.roots and r not in self.funcs and r not in KEYWORDS:
                    d.at(doc, path, INFO, "expr-unknown-root", f"Unknown variable root '{r}' (expected one of {', '.join(sorted(self.roots))})")

    def check_action(self, s, action, p, doc, d, parent):
        inputs = s.get("inputs") if isinstance(s.get("inputs"), dict) else {}
        child_actions = [c.get("action") for c in s.get("steps") or [] if isinstance(c, dict)]
        if action == "internal.for":
            if "items" not in inputs:
                d.at(doc, p + ("action",), ERROR, "for-items", "internal.for needs inputs.items")
            if not s.get("steps"):
                d.at(doc, p + ("action",), WARNING, "for-empty", "internal.for has no child steps")
        elif action == "internal.ifCondition":
            if "condition" not in inputs:
                d.at(doc, p + ("action",), ERROR, "if-condition", "internal.ifCondition needs inputs.condition")
            if "internal.ifTrueBranch" not in child_actions:
                d.at(doc, p + ("action",), ERROR, "if-branch", "internal.ifCondition needs an internal.ifTrueBranch child step")
        elif action == "internal.if":
            if not s.get("transitions") and not s.get("steps"):
                d.at(doc, p + ("action",), WARNING, "if-transitions", "internal.if has no transitions (on: true / on: false)")
        elif action in ("internal.ifTrueBranch", "internal.ifFalseBranch") and parent != "internal.ifCondition":
            d.at(doc, p + ("action",), WARNING, "branch-parent", f"{action} must be a direct child of internal.ifCondition")
        elif action == "internal.while" and "condition" not in inputs:
            d.at(doc, p + ("action",), ERROR, "while-condition", "internal.while needs inputs.condition")
        elif action == "internal.try" and "internal.catch" not in child_actions:
            d.at(doc, p + ("action",), WARNING, "try-catch", "internal.try usually has an internal.catch child")
        # catalog
        prefix = action.split(".")[0]
        if action.startswith("internal.") or action.startswith("automations."):
            return
        if prefix not in self.prefixes:
            d.at(doc, p + ("action",), WARNING, "unknown-integration", f"Unknown integration '{prefix}' in action '{action}'")
            return
        meta = self.index.get(action)
        if meta is None:
            d.at(doc, p + ("action",), INFO, "unknown-action", f"Action '{action}' not found in the catalog (catalog is built from public workflows and may be incomplete)")
            return
        if meta["uses"] >= 5:
            known = meta["inputs"]
            for k in inputs:
                if k not in known:
                    d.at(doc, p + ("inputs", k), WARNING, "unknown-input", f"Input '{k}' has never been used with {action}; known: {', '.join(list(known)[:8])}", key=True)
            miss = [k for k in meta["common"] if k not in inputs]
            if miss:
                d.at(doc, p + ("action",), INFO, "missing-common-input", f"{action} usually sets: {', '.join(miss)}")

    def triggers(self, data, doc, d):
        at = data.get("automation_type") or data.get("workflow_type")
        trig = data.get("triggers") if isinstance(data.get("triggers"), dict) else {}
        if at == "scheduled" and not trig.get("scheduled"):
            d.at(doc, ("automation_type",), INFO, "no-schedule", "scheduled workflow has no triggers.scheduled entry", key=True)
        if at == "event" and not (trig.get("polling") or trig.get("webhooks") or trig.get("webforms")):
            d.at(doc, ("automation_type",), WARNING, "no-event-trigger", "event workflow has no event trigger under 'triggers'", key=True)
        for i, t in enumerate(trig.get("scheduled") or []):
            if isinstance(t, dict) and isinstance(t.get("cron"), str):
                err = check_cron(t["cron"])
                if err:
                    d.at(doc, ("triggers", "scheduled", i, "cron"), ERROR, "cron", err)


CRON_RANGES = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 7)]


def check_cron(expr):
    parts = expr.split()
    if len(parts) != 5:
        return f"cron needs 5 fields (min hour day month weekday), got {len(parts)}"
    for part, (lo, hi) in zip(parts, CRON_RANGES):
        for piece in part.split(","):
            m = re.fullmatch(r"(\*|\d+|\d+-\d+|[A-Za-z]{3}(?:-[A-Za-z]{3})?)(?:/(\d+))?", piece)
            if not m:
                return f"invalid cron field '{part}'"
            for n in re.findall(r"\d+", m.group(1)):
                if not lo <= int(n) <= hi:
                    return f"cron value {n} out of range {lo}-{hi} in '{part}'"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-schema", action="store_true", help="skip JSON-Schema checks (another tool does them)")
    ap.add_argument("--data", default=str(HERE.parent / "data"))
    ap.add_argument("--explain", choices=["md", "json"], help="explain the workflow instead of linting")
    ap.add_argument("--workspace", help="folder of other workflows for relationship hints")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else Path(a.file).read_text()
    if a.explain:
        import explain
        flows = []
        for f in sorted(Path(a.workspace).rglob("*.y*ml")) if a.workspace else []:
            try:
                dd = yaml.safe_load(f.read_text())
                if isinstance(dd, dict) and "workflow" in dd:
                    subs = sorted(set(re.findall(r"automations\.([0-9a-f-]{36})", f.read_text())))
                    flows.append({"file": str(f), "name": dd.get("name", f.name), "subflows": subs})
            except Exception:
                pass
        res = explain.explain(text, a.data, flows)
        print(json.dumps(res) if a.explain == "json" else explain.to_markdown(res))
        return
    diags = Linter(*load_data(a.data), schema_checks=not a.no_schema).lint(text)
    if a.json:
        print(json.dumps(diags))
    else:
        for x in diags:
            print(f"{a.file}:{x['line'] + 1}:{x['col'] + 1}: {x['severity']} [{x['code']}] {x['message']}")
        print(f"{len(diags)} problem(s)", file=sys.stderr)
    sys.exit(1 if any(x["severity"] == ERROR for x in diags) else 0)


if __name__ == "__main__":
    main()
