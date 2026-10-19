#!/usr/bin/env python3
"""catalog/mined.json -> catalog/action-index.json (compact, shipped with the extension).

For each real action id: usage count and, per observed input key, the fraction of
uses that set it. `ratio >= 0.95` over >= 5 uses is flagged "common" (likely
required); this is inferred, NOT authoritative, so the linter should warn only.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
mined = json.loads((ROOT / "catalog/mined.json").read_text())
out = {}
for a, r in mined["actions"].items():
    n = r["count"]
    keys = {k: round(c / n, 3) for k, c in r["input_keys"].items()}
    out[a] = {"uses": n, "inputs": keys,
              "common": sorted(k for k, v in keys.items() if v >= 0.95) if n >= 5 else []}
    if r["connections"]:
        out[a]["connections"] = sorted(r["connections"])
(ROOT / "catalog/action-index.json").write_text(json.dumps(out, separators=(",", ":"), sort_keys=True))
print(len(out), "actions;", sum(1 for v in out.values() if v["uses"] >= 5), "with >=5 uses")
