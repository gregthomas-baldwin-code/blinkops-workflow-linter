#!/usr/bin/env python3
"""Run the linter over every library workflow; histogram diagnostics (false-positive check)."""
import json, sys
from collections import Counter
from pathlib import Path
R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "extension/linter"))
import blinklint
L = blinklint.Linter(*blinklint.load_data(R / "extension/data"))
ents = [e for e in json.loads((R / "catalog/library/entities.json").read_text()) if e.get("playbook")]
cnt, ex, wf = Counter(), {}, Counter()
for e in ents:
    seen = set()
    for x in L.lint(e["playbook"]):
        k = (x["severity"], x["code"])
        cnt[k] += 1
        if k not in seen:
            wf[k] += 1; seen.add(k)
        ex.setdefault(k, (e["name"][:45], x["message"][:110]))
print(f"{len(ents)} workflows")
for k, n in sorted(cnt.items(), key=lambda kv: (["error","warning","info","hint"].index(kv[0][0]), -kv[1])):
    print(f"{k[0]:7} {k[1]:24} {n:6} diags in {wf[k]:5} wfs | {ex[k][0]} | {ex[k][1]}")
