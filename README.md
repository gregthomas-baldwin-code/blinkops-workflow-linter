# BlinkOps Workflow Linter

A VS Code extension that checks [BlinkOps](https://www.blinkops.com) workflow YAML as you type and explains what a workflow does.

## What it does

**Lints** (red/yellow squiggles in the editor):
- YAML syntax, tabs, indentation, trailing whitespace
- Structure against a JSON Schema: top-level keys, sections, steps, triggers, conditions, input types
- Step ids: duplicates, missing ids
- `{{ }}` expressions: undeclared `inputs.x`, `steps.Sx` that is undefined or defined later, unclosed `{{`, unknown functions
- Flow control: `internal.for` without `items`, `internal.ifCondition` without a true branch, `while` without a condition
- Actions: unknown integration, unknown input keys, commonly-set inputs that are missing
- Scheduled triggers: cron validity

**Explains** a workflow ("Blink: Explain Workflow" command, or hover an `action:` line): what each step does, what it reads from or talks to (integration/connection, Blink Tables, runner, subflow), where its data comes from, which steps use its output, how the workflow starts, and related subflows.

Calibrated against ~8,200 public library workflows: the schema accepts 8,245 of 8,246, and the linter's errors there are genuine defects (undeclared inputs, deleted-step references, a duplicate id, a `{{inputs.x}` typo).

## Install

### From a release / CI build (recommended)
1. Run the **build-vsix** GitHub Action (Actions tab → build-vsix → Run workflow) and download the `vsix` artifact. It bundles standalone linter binaries for macOS (arm64, x64), Windows and Linux, so no Python is needed.
2. In VS Code: Extensions panel → `…` menu → **Install from VSIX…**, or:
   ```bash
   code --install-extension blink-workflow-linter-0.1.0.vsix
   ```
3. Reload the window.

### Build locally (macOS/Linux/Windows with Python 3.9+)
```bash
python3 -m pip install --user pyyaml jsonschema pyinstaller
python3 scripts/build_binary.py   # standalone linter for this OS -> extension/bin/
python3 scripts/build_vsix.py     # -> dist/blink-workflow-linter-0.1.0.vsix
```
Without a binary the extension falls back to `python3` (needs `pyyaml` and `jsonschema`; set `blink.pythonPath` if needed).

> The binaries are unsigned. macOS may quarantine a downloaded `.vsix`: run `xattr -dr com.apple.quarantine ~/.vscode/extensions/blinkops-local.*`. Windows SmartScreen may warn.

## Use
- Files named `*.blink.yaml` / `*.blink.yml` are always linted. Other YAML is linted if it looks like a workflow (top-level `workflow:` plus `automation_type:` or `name:`).
- **Blink: Explain Workflow** from the Command Palette opens a Markdown report; hovering an `action:` line shows the same detail for that step.
- Optional: install the Red Hat YAML extension for schema autocomplete/hover on `*.blink.yaml`.
- Settings: `blink.pythonPath`, `blink.filePatterns`, `blink.sniffWorkflows`, `blink.lintOnType`, `blink.dataPath`.

CLI (no VS Code): `python3 extension/linter/blinklint.py my.blink.yaml` or `... --explain md`.

## Limitations
- Action inputs are checked against what appears in public library workflows, not an official catalog, so "required" is inferred and only ever reported as info/warning. An authoritative catalog would need the Blink API.
- Library exports omit `connections`, so connection/action matching is only explained, not validated.
- Subflows are referenced by id (`automations.<uuid>`); names and "who calls this workflow" aren't in the YAML.
- Action descriptions come from fuzzy-matching action ids to docs pages (~80% match).

## Repo layout
| Path | What |
|---|---|
| `extension/` | the VS Code extension (plain JS) + `linter/` (Python source) + `data/` (shipped catalogs) |
| `schemas/blink-workflow.schema.json` | workflow structure schema |
| `catalog/` | crawled docs, mined action index, action→docs map |
| `scripts/` | crawlers, miners, binary and `.vsix` builders |
| `tests/` | fixtures with `# expect:` codes, corpus validators |
| `.github/workflows/build.yml` | builds binaries for 4 platforms and packages the `.vsix` |

## Refresh the catalog
```bash
python3 -m pip install --user pyyaml jsonschema
python3 scripts/build_catalog.py        # docs.blinkops.com -> catalog/actions.json
python3 scripts/fetch_library.py        # library.blinkops.com public API -> catalog/library/ (git-ignored)
python3 scripts/mine_library.py && python3 scripts/build_action_index.py
python3 scripts/build_core.py && python3 scripts/build_action_docs.py
python3 scripts/sync_extension_data.py
```

## Test
```bash
python3 tests/test_fixtures.py      # fixtures
python3 tests/validate_corpus.py    # schema vs real workflows (needs the library download)
python3 tests/lint_corpus.py        # false-positive check
```

## Findings worth knowing
- Step `inputs:` keys are internal parameter names (`registryName`, `sku__name`), not display names.
- `if` is `internal.ifCondition` with child `internal.ifTrueBranch` / `ifFalseBranch` steps; `transitions` is rare.
- Event triggers live under `triggers.polling` (`trigger_type: <integration>.<Event>`).
- `library.blinkops.com/api/library/entities` is public; paginate with `?q={"limit":200,"offset":N}` (plain `offset=` is ignored).
