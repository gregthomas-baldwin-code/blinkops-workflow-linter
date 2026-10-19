"""Explain a Blink workflow: what each step does, what it reads from, and how steps/workflows connect."""
import json, re
from pathlib import Path
from blinklint import Doc, EXPR, STR_LIT, REF

SUBFLOW = re.compile(r"^automations\.([0-9a-f-]{36})$")
ANY_REF = re.compile(r"(?<![\w.])(inputs|steps|variables|event|metadata|globals)\s*\.\s*([A-Za-z_][\w-]*)")


def refs_in(obj, out):
    if isinstance(obj, dict):
        for v in obj.values():
            refs_in(v, out)
    elif isinstance(obj, list):
        for v in obj:
            refs_in(v, out)
    elif isinstance(obj, str):
        for m in EXPR.finditer(obj):
            out.update(ANY_REF.findall(STR_LIT.sub('""', m.group(1))))


def load_docs(data_dir):
    d = Path(data_dir)
    return (json.loads((d / "action-docs.json").read_text()), json.loads((d / "builtin-actions.json").read_text()))


def explain(text, data_dir, workspace_flows=None):
    docs, builtin = load_docs(data_dir)
    doc = Doc(text)
    data = doc.data if isinstance(doc.data, dict) else {}
    inputs = data.get("inputs") if isinstance(data.get("inputs"), dict) else {}
    wf_conn = data.get("connections") if isinstance(data.get("connections"), dict) else {}
    runner = data.get("runner") or "default (Blink cloud)"
    steps, by_id = [], {}

    def rec(items, path, depth, parent):
        for i, s in enumerate(items or []):
            if not isinstance(s, dict) or "action" not in s:
                continue
            p = path + (i,)
            sid = str(s.get("id", ""))
            action = str(s["action"])
            prefix = action.split(".")[0]
            b, dc = builtin.get(action, {}), docs.get(action, {})
            sub = SUBFLOW.match(action)
            conn = (s.get("connections") or {}) if isinstance(s.get("connections"), dict) else {}
            kind = ("flow control" if prefix == "internal" else "subflow call" if sub else
                    "runner script/CLI" if prefix == "core" and b.get("runs_on", "").startswith("Runner") else
                    "Blink platform" if prefix in ("core", "system") else "integration action")
            what = b.get("what") or dc.get("description") or ""
            if not what and sub:
                what = "Calls another Blink workflow (subflow)."
            if not what:
                words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", action.split(".", 1)[1]).replace("_", " ")
                what = f"{dc.get('integration', prefix.title())}: {words} (no description in the docs catalog)"
            reads = b.get("reads")
            if not reads and kind == "integration action":
                cname = conn.get(prefix) or next(iter(conn.values()), None) or wf_conn.get(prefix)
                reads = (f"{dc.get('integration', prefix)} API via connection "
                         f"'{cname}'" if cname else f"{dc.get('integration', prefix)} API via the '{prefix}' connection (name not set in this file; chosen at run time)")
                if action.endswith("CustomAction") or "custom" in action.lower():
                    url = (s.get("inputs") or {}).get("Request URL Or API Endpoint")
                    if url:
                        reads += f"; endpoint {url}"
            if reads and conn and kind != "integration action":
                reads += " — connection: " + ", ".join(f"{k}='{v}'" for k, v in conn.items())
            if sub:
                reads = f"Subflow {sub.group(1)} (runs {'async' if (s.get('configuration') or {}).get('run_async') else 'and waits'})"
            r = set()
            refs_in(s.get("inputs"), r)
            refs_in(s.get("when"), r)
            sources = []
            for root, name in sorted(r):
                if root == "inputs":
                    sources.append(f"workflow input '{(inputs.get(name) or {}).get('display_name', name)}' ({name})")
                elif root == "steps":
                    other = by_id.get(name.lower())
                    sources.append(f"output of step {name}" + (f" ({other['name']})" if other and other.get("name") else ""))
                elif root == "event":
                    sources.append("trigger event payload")
                elif root == "variables":
                    sources.append(f"workflow variable '{name}'")
                else:
                    sources.append(f"{root}.{name}")
            rec_ = {"id": sid, "name": s.get("name", ""), "action": action, "line": doc.vals[p][0], "depth": depth,
                    "parent": parent, "kind": kind, "what": what, "runs_on": b.get("runs_on") or (
                        f"Runner: {runner}" if kind == "integration action" else ""),
                    "reads_from": reads or "", "data_from": sources, "feeds": [],
                    "subflow": sub.group(1) if sub else None, "docs_url": dc.get("docs_url", ""),
                    "continue_on_error": bool(s.get("continue_on_error")), "skipped": str(s.get("when")).lower() == "false"}
            steps.append(rec_)
            by_id[sid.lower()] = rec_
            rec(s.get("steps"), p + ("steps",), depth + 1, sid)
            for ti, t in enumerate(s.get("transitions") or []):
                if isinstance(t, dict):
                    rec(t.get("steps"), p + ("transitions", ti, "steps"), depth + 1, sid)

    for si, sec in enumerate(data.get("workflow") or []):
        if isinstance(sec, dict):
            rec(sec.get("steps"), ("workflow", si, "steps"), 0, None)
    for st in steps:
        for src in st["data_from"]:
            m = re.match(r"output of step (\S+)", src)
            if m and m.group(1).lower() in by_id:
                by_id[m.group(1).lower()]["feeds"].append(st["id"])

    trig = data.get("triggers") if isinstance(data.get("triggers"), dict) else {}
    triggers = []
    for t in trig.get("scheduled") or []:
        triggers.append(f"Schedule: cron `{t.get('cron')}`")
    for t in trig.get("webhooks") or []:
        triggers.append(f"Webhook: {t.get('name', 'unnamed')}")
    for t in trig.get("polling") or []:
        triggers.append(f"Integration event: {t.get('trigger_type')} ({t.get('name', '')})")
    for t in trig.get("webforms") or []:
        triggers.append("Web form")
    if not triggers:
        triggers.append({"on_demand": "On demand (manual / Self Service Portal)"}.get(data.get("automation_type"), "Not specified"))
    subs = sorted({st["subflow"] for st in steps if st["subflow"]})
    related = []
    for f in workspace_flows or []:
        shared = sorted(set(subs) & set(f["subflows"]))
        if shared and f["name"] != data.get("name"):
            related.append({"file": f["file"], "name": f["name"], "via": "calls the same subflow " + ", ".join(shared)})
    return {"name": data.get("name"), "desc": data.get("desc"), "type": data.get("type", "Flow"), "runner": runner,
            "triggers": triggers, "inputs": {k: (v or {}).get("display_name", k) for k, v in inputs.items()},
            "connections": wf_conn, "steps": steps, "subflows": subs, "related": related,
            "integrations": sorted({docs.get(s["action"], {}).get("integration", s["action"].split(".")[0])
                                    for s in steps if s["kind"] == "integration action"})}


def to_markdown(e):
    L = [f"# {e['name']}", "", e["desc"] or "", "", f"**Type:** {e['type']}  ·  **Runner:** {e['runner']}", "",
         "## How it starts", *[f"- {t}" for t in e["triggers"]], ""]
    if e["inputs"]:
        L += ["## Inputs", *[f"- `{k}` — {v}" for k, v in e["inputs"].items()], ""]
    L += ["## Systems touched", *([f"- {i}" for i in e["integrations"]] or ["- none beyond Blink itself"]), ""]
    L += ["## Steps", ""]
    for s in e["steps"]:
        ind = "  " * s["depth"]
        L.append(f"{ind}### {s['id']} — {s['name'] or s['action']}")
        L.append(f"{ind}`{s['action']}` · {s['kind']} · line {s['line'] + 1}" + (" · **skipped (when: false)**" if s["skipped"] else ""))
        L.append(f"{ind}- **Does:** {s['what']}" + (f" ([docs]({s['docs_url'][:-3]}))" if s["docs_url"] else ""))
        if s["reads_from"]:
            L.append(f"{ind}- **Reads from / talks to:** {s['reads_from']}")
        if s["runs_on"]:
            L.append(f"{ind}- **Runs on:** {s['runs_on']}")
        if s["data_from"]:
            L.append(f"{ind}- **Uses data from:** " + "; ".join(s["data_from"]))
        if s["feeds"]:
            L.append(f"{ind}- **Feeds:** " + ", ".join(s["feeds"]))
        if s["continue_on_error"]:
            L.append(f"{ind}- Continues even if this step fails")
        L.append("")
    L += ["## Related workflows"]
    if e["subflows"]:
        L += [f"- Calls subflow `{u}` (name not stored in the YAML; resolve it in Blink)" for u in e["subflows"]]
    L += [f"- `{r['file']}` ({r['name']}) {r['via']}" for r in e["related"]]
    if not e["subflows"] and not e["related"]:
        L.append("- No subflow calls. Who calls *this* workflow isn't recorded in the YAML (check the workflow's usage in Blink).")
    return "\n".join(L) + "\n"
