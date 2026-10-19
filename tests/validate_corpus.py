#!/usr/bin/env python3
"""Validate every library workflow against the JSON Schema; summarise failures."""
import json, sys
from collections import Counter
from pathlib import Path
import yaml
from jsonschema import Draft7Validator

ROOT = Path(__file__).resolve().parent.parent
schema = json.loads((ROOT / "schemas/blink-workflow.schema.json").read_text())
v = Draft7Validator(schema)
ents = json.loads((ROOT / "catalog/library/entities.json").read_text())
ok = bad = 0
reasons, ex = Counter(), {}
for e in ents:
    if not e.get("playbook"):
        continue
    doc = yaml.safe_load(e["playbook"])
    errs = list(v.iter_errors(doc))
    if not errs:
        ok += 1
        continue
    bad += 1
    # best_match-ish: report the deepest/most specific error per workflow
    for er in errs[:3]:
        path = "/".join(str(p) for p in er.absolute_path if not isinstance(p, int))
        key = f"{path} :: {er.message[:90]}"
        reasons[key] += 1
        ex.setdefault(key, e["name"])
print(f"valid={ok} invalid={bad}")
for k, n in reasons.most_common(25):
    print(n, k, "| e.g.", ex[k][:50])
