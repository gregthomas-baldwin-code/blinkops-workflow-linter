#!/usr/bin/env python3
"""Build catalog/core.json from the crawled workflow docs + mined library stats."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "catalog/workflow-docs"
E = "workflows__building-workflows__dynamic-variables__expression-language__"
funcs_md = (D / (E + "workflow-engine-functions.md")).read_text()
funcs = sorted(set(re.findall(r"^\s*\| `([A-Za-z_][A-Za-z0-9_]*)\(", funcs_md, re.M)))
mined = json.loads((ROOT / "catalog/mined.json").read_text())
funcs = sorted(set(funcs) | set(mined["expression_functions"]))
ops = sorted(set(k for k in mined["condition_ops"] if k))
core = {
    "expression_functions": funcs,
    "expression_roots": ["inputs", "steps", "variables", "event", "metadata", "globals", "context", "ioc"],
    "condition_ops": ops,
    "input_types": sorted(mined["input_types"]),
    "automation_types": ["on_demand", "event", "scheduled"],
    "step_extra_keys": sorted(mined["step_keys"]),
}
(ROOT / "catalog/core.json").write_text(json.dumps(core, indent=1))
print(len(funcs), "functions;", ops)
