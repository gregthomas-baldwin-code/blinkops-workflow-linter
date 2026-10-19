# BlinkOps Workflow Linter

Lints BlinkOps workflow YAML in VS Code. Files named `*.blink.yaml` are always linted; any other YAML
that looks like a workflow (top-level `workflow:` + `automation_type:`/`name:`) is linted too.

Ships a standalone linter binary for supported platforms (darwin-arm64, darwin-x64, win32-x64, linux-x64). On other platforms it falls back to `python3` with `pyyaml` and `jsonschema`.


Run "Blink: Explain Workflow" from the Command Palette for a step-by-step report (what each step does, what it talks to, data flow, related workflows). Hover an `action:` line for the same detail.

Optional: install the Red Hat YAML extension for schema-driven autocomplete/hover on `*.blink.yaml`
(this extension then skips its own schema squiggles to avoid duplicates).
