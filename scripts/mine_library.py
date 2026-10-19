#!/usr/bin/env python3
"""Mine catalog/library/entities.json -> catalog/mined.json.

Walks every playbook YAML and records: top-level / section / step key frequency,
input types, trigger shapes, condition ops, and per-action observed input keys,
connection keys and usage counts. Needs PyYAML.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
ents = {e["lib_id"]: e for e in json.loads((ROOT / "catalog/library/entities.json").read_text())}
print(len(ents), "unique entities")

top, section_keys, step_keys, input_types, input_fields = Counter(), Counter(), Counter(), Counter(), Counter()
automation_types, trigger_keys, ops, errcfg = Counter(), defaultdict(Counter), Counter(), Counter()
actions = defaultdict(lambda: {"count": 0, "input_keys": Counter(), "connections": Counter(), "step_keys": Counter()})
transitions_on, bad = Counter(), 0
expr_funcs, expr_roots = Counter(), Counter()
import re

def walk_steps(steps):
    for s in steps or []:
        if not isinstance(s, dict):
            continue
        step_keys.update(s.keys())
        a = s.get("action")
        if a:
            r = actions[a]
            r["count"] += 1
            if isinstance(s.get("inputs"), dict):
                r["input_keys"].update(s["inputs"].keys())
            if isinstance(s.get("connections"), dict):
                r["connections"].update(s["connections"].keys())
            r["step_keys"].update(s.keys())
        for k in ("error_handling", "on_error", "retries", "timeout", "continue_on_error"):
            if k in s:
                errcfg[k] += 1
        walk_steps(s.get("steps"))
        for t in s.get("transitions") or []:
            if isinstance(t, dict):
                transitions_on[str(t.get("on"))] += 1
                walk_steps(t.get("steps"))
        scan(s)

def scan(o):
    if isinstance(o, dict):
        if "op" in o and "lvalue" in o:
            ops[str(o["op"])] += 1
        for v in o.values():
            scan(v)
    elif isinstance(o, list):
        for v in o:
            scan(v)
    elif isinstance(o, str):
        for m in re.finditer(r"\{\{(.*?)\}\}", o, re.S):
            body = m.group(1)
            for f in re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", body):
                expr_funcs[f] += 1
            for r_ in re.findall(r"(?<![\w.])([A-Za-z_][A-Za-z0-9_]*)\s*[.\[]", body):
                expr_roots[r_] += 1

for e in ents.values():
    try:
        pb = yaml.safe_load(e.get("playbook") or "")
    except Exception:
        bad += 1
        continue
    if not isinstance(pb, dict):
        bad += 1
        continue
    top.update(pb.keys())
    automation_types[str(pb.get("automation_type"))] += 1
    for k, v in (pb.get("inputs") or {}).items():
        if isinstance(v, dict):
            input_types[str(v.get("type"))] += 1
            input_fields.update(v.keys())
    for kind, lst in (pb.get("triggers") or {}).items():
        for t in lst or []:
            if isinstance(t, dict):
                trigger_keys[kind].update(t.keys())
    for sec in pb.get("workflow") or []:
        if isinstance(sec, dict):
            section_keys.update(sec.keys())
            walk_steps(sec.get("steps"))
    walk_steps(pb.get("steps"))
    scan(pb.get("outputs"))

out = {
    "unparsable_playbooks": bad,
    "top_level_keys": top, "automation_types": automation_types,
    "section_keys": section_keys, "step_keys": step_keys,
    "input_types": input_types, "input_fields": input_fields,
    "trigger_keys": {k: v for k, v in trigger_keys.items()},
    "condition_ops": ops, "transition_on": transitions_on, "error_cfg": errcfg,
    "expression_functions": expr_funcs, "expression_roots": expr_roots,
    "actions": {a: {"count": r["count"], "input_keys": dict(r["input_keys"].most_common()),
                    "connections": dict(r["connections"]), "step_keys": dict(r["step_keys"])}
                for a, r in sorted(actions.items())},
}
(ROOT / "catalog/mined.json").write_text(json.dumps(out, indent=1, default=dict))
for k in ("unparsable_playbooks", "top_level_keys", "automation_types", "section_keys", "step_keys",
          "input_types", "input_fields", "trigger_keys", "transition_on", "error_cfg"):
    print(k, "=>", json.dumps(out[k], default=dict)[:900])
print("condition ops =>", dict(ops.most_common(40)))
print("expr roots =>", dict(expr_roots.most_common(25)))
print("expr funcs =>", dict(expr_funcs.most_common(40)))
print("distinct actions:", len(actions))
