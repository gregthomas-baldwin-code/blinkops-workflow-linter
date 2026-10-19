#!/usr/bin/env python3
"""Crawl docs.blinkops.com into catalog/actions.json and catalog/workflow-docs/.

Stdlib only. Raw pages are cached in .cache/ so reruns are cheap.

  python3 scripts/build_catalog.py            # integrations + workflow docs
  python3 scripts/build_catalog.py --limit 5  # first 5 integrations (smoke test)
  python3 scripts/build_catalog.py --only workflows
"""
import argparse, hashlib, json, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache"
OUT = ROOT / "catalog"
BASE = "https://docs.blinkops.com"
WORKERS = 10


def fetch(url, retries=3):
    key = CACHE / (hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if key.exists():
        return key.read_text()
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "blink-linter-catalog/0.1"})
            with urllib.request.urlopen(req, timeout=30) as r:
                text = r.read().decode("utf-8", "replace")
            CACHE.mkdir(exist_ok=True)
            key.write_text(text)
            return text
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return ""
            time.sleep(1 + i)
        except Exception:
            time.sleep(1 + i)
    print(f"  FAILED {url}", file=sys.stderr)
    return ""


def links(text):
    return re.findall(r"\[([^\]]+)\]\((https://docs\.blinkops\.com/[^)\s]+)\)", text)


def parse_action(md):
    m = re.search(r"^# (.+)$", md, re.M)
    if not m:
        return None
    name = m.group(1).strip()
    after = md[m.end():]
    desc = ""
    for line in after.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "<", "|", ">", "```")):
            desc = s
            break
    params, section = [], None
    for line in md.splitlines():
        h = re.match(r"^##+ (.+)$", line)
        if h:
            section = h.group(1).strip().lower()
            continue
        if section and "parameters" in section and line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or cells[0] in ("Parameter", "-") or set(cells[0]) <= set("-: "):
                continue
            params.append({"name": cells[0], "description": cells[1],
                           "advanced": "advanced" in section})
    return {"action": name, "description": desc, "params": params}


def crawl_integrations(limit):
    idx = fetch(f"{BASE}/_llms/integrations/integrations.txt")
    entries = [(t, u) for t, u in links(idx) if u.endswith(".txt")]
    if limit:
        entries = entries[:limit]
    print(f"{len(entries)} integrations")

    def one(entry):
        title, url = entry
        slug = url.rsplit("/", 1)[1][:-4]
        display = re.sub(r"\s*\(\d+ pages\)$", "", title).split(" / ")[-1]
        listing = fetch(url)
        action_urls = [(t, u) for t, u in links(listing)
                       if "/actions/" in u and t != "Overview"]
        actions = []
        for t, u in action_urls:
            a = parse_action(fetch(u))
            if a:
                a["docs_url"] = u
                a["custom"] = a["action"].endswith("Custom Action")
                actions.append(a)
        return {"integration": display, "slug": slug, "actions": actions}

    with ThreadPoolExecutor(WORKERS) as ex:
        result = list(ex.map(one, entries))
    OUT.mkdir(exist_ok=True)
    (OUT / "actions.json").write_text(json.dumps(result, indent=1))
    n = sum(len(i["actions"]) for i in result)
    print(f"wrote catalog/actions.json: {len(result)} integrations, {n} actions")


def crawl_workflows():
    idx = fetch(f"{BASE}/_llms/workflows.txt")
    urls = sorted({u for _, u in links(idx) if u.endswith(".md")})
    print(f"{len(urls)} workflow doc pages")
    d = OUT / "workflow-docs"
    d.mkdir(parents=True, exist_ok=True)

    def one(u):
        md = fetch(u)
        rel = u.split("/docs/", 1)[1][:-3].replace("/", "__")
        (d / f"{rel}.md").write_text(md)
        return u, md

    with ThreadPoolExecutor(WORKERS) as ex:
        pages = list(ex.map(one, urls))
    # Collect every yaml code block for later schema inference.
    blocks = []
    for u, md in pages:
        for m in re.finditer(r"```ya?ml[^\n]*\n(.*?)```", md, re.S):
            blocks.append({"source": u, "yaml": m.group(1)})
    (OUT / "yaml-examples.json").write_text(json.dumps(blocks, indent=1))
    print(f"wrote {len(pages)} pages, {len(blocks)} yaml blocks")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int)
    ap.add_argument("--only", choices=["integrations", "workflows"])
    a = ap.parse_args()
    if a.only != "workflows":
        crawl_integrations(a.limit)
    if a.only != "integrations":
        crawl_workflows()
