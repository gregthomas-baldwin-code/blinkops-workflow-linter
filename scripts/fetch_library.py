#!/usr/bin/env python3
"""Download the public Blink library (library.blinkops.com/api/library/entities)
into catalog/library/entities.json. Each entity has a real `playbook` YAML string
plus an `actions` list. Stdlib only.
"""
import json, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "catalog" / "library"
URL = "https://library.blinkops.com/api/library/entities?q={q}"
PAGE = 200


def get(offset):
    for i in range(4):
        try:
            req = urllib.request.Request(URL.format(q=urllib.parse.quote(json.dumps({"limit": PAGE, "offset": offset}))),
                                         headers={"User-Agent": "blink-linter-catalog/0.1"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print(f"  retry offset={offset}: {e}", file=sys.stderr)
            time.sleep(2 + i * 2)
    raise SystemExit(f"giving up at offset {offset}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    first = get(0)
    total = first["total"]
    entities = list(first["results"]["entities"])
    print(f"total={total}, first page={len(entities)}")
    step = len(entities) or PAGE
    off = step
    while off < total:
        entities += get(off)["results"]["entities"]
        off += step
        if (off // step) % 5 == 0:
            print(f"  {len(entities)}/{total}")
    uniq = {e["lib_id"]: e for e in entities}
    (OUT / "entities.json").write_text(json.dumps(list(uniq.values())))
    print(f"wrote {len(uniq)} unique entities ({len(entities)} fetched)")


if __name__ == "__main__":
    main()
