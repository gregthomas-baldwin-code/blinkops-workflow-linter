#!/usr/bin/env python3
"""Copy schema + catalog files the extension ships with into extension/data/."""
import shutil
from pathlib import Path
R = Path(__file__).resolve().parent.parent
for src in ("schemas/blink-workflow.schema.json", "catalog/action-index.json", "catalog/core.json", "catalog/action-docs.json"):
    shutil.copy(R / src, R / "extension/data" / Path(src).name)
print("synced")
