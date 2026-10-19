#!/usr/bin/env python3
"""Link real action ids (library) to docs entries (display name + description) -> catalog/action-docs.json.
Matching is fuzzy (token overlap) and carries a `match` score; low scores are dropped."""
import json, re
from pathlib import Path
R = Path(__file__).resolve().parent.parent
ents = json.loads((R / "catalog/library/entities.json").read_text())
docs = json.loads((R / "catalog/actions.json").read_text())
index = json.loads((R / "catalog/action-index.json").read_text())

norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
def toks(s):
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", s)
    s = re.sub(r"V(\d+)$", r" v\1", s)
    return {t for t in re.split(r"[^A-Za-z0-9]+", s.lower()) if t and t not in ("v2", "v1")}

vendor = {}  # prefix -> display name
for e in ents:
    for a in e.get("actions") or []:
        vendor.setdefault(a["collection_name"], a["name"])
by_norm = {}
for i in docs:
    by_norm[norm(i["integration"])] = i
    by_norm.setdefault(norm(i["slug"]), i)

out, hit = {}, 0
for aid in index:
    p, _, rest = aid.partition(".")
    integ = by_norm.get(norm(p)) or by_norm.get(norm(vendor.get(p, "")))
    rec = {"integration": (integ or {}).get("integration") or vendor.get(p) or p}
    if integ:
        t = toks(rest)
        best, score = None, 0
        for a in integ["actions"]:
            at = toks(a["action"]) - toks(integ["integration"])
            if not at or not t:
                continue
            s = len(t & at) / len(t | at)
            if s > score:
                best, score = a, s
        if best and score >= 0.5:
            rec.update(action=best["action"], description=best["description"], docs_url=best["docs_url"], match=round(score, 2))
            hit += 1
    out[aid] = rec
(R / "catalog/action-docs.json").write_text(json.dumps(out, separators=(",", ":")))
print(f"{len(out)} actions, {hit} matched to a docs page ({100*hit//len(out)}%)")
