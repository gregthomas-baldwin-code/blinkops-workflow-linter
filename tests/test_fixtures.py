#!/usr/bin/env python3
"""Each fixture's first line `# expect: a, b` lists diagnostic codes that must appear;
an empty list means no error/warning at all."""
import sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(R / "extension/linter"))
import blinklint
L = blinklint.Linter(*blinklint.load_data(R / "extension/data"))
fail = 0
for f in sorted((R / "tests/fixtures").glob("*.yaml")):
    text = f.read_text()
    expect = {c.strip() for c in text.splitlines()[0].split(":", 1)[1].split(",") if c.strip()}
    got = L.lint(text)
    codes = {x["code"] for x in got}
    bad = {x["code"] for x in got if x["severity"] in ("error", "warning")}
    ok = expect <= codes if expect else not bad
    print(("PASS" if ok else "FAIL"), f.name, "got:", sorted(codes))
    if not ok:
        fail += 1
        print("   expected:", sorted(expect), "missing:", sorted(expect - codes))
sys.exit(fail)
