// BlinkOps workflow linter: runs linter/blinklint.py on YAML documents and
// publishes the result as VS Code diagnostics. No npm dependencies.
const vscode = require('vscode');
const cp = require('child_process');
const path = require('path');

const SEV = {
  error: vscode.DiagnosticSeverity.Error,
  warning: vscode.DiagnosticSeverity.Warning,
  info: vscode.DiagnosticSeverity.Information,
  hint: vscode.DiagnosticSeverity.Hint,
};

let collection, output, timers = new Map(), warnedSetup = false;

function cfg() { return vscode.workspace.getConfiguration('blink'); }

function globToRegExp(glob) {
  const re = glob.replace(/[.+^${}()|\\]/g, '\\$&')
    .replace(/\*\*\//g, '(?:.*/)?').replace(/\*\*/g, '.*').replace(/\*/g, '[^/]*').replace(/\?/g, '[^/]');
  return new RegExp('(?:^|/)' + re + '$');
}

function isBlinkDoc(doc) {
  if (doc.languageId !== 'yaml' || doc.uri.scheme === 'output') return false;
  const p = doc.uri.path;
  if (cfg().get('filePatterns', []).some((g) => globToRegExp(g.replace(/^\*\*\//, '')).test(p))) return true;
  if (!cfg().get('sniffWorkflows', true)) return false;
  const head = doc.getText();
  return /^workflow:\s*$/m.test(head) && /^(automation_type|name):/m.test(head);
}

function usesRedHatSchema(doc) {
  return !!vscode.extensions.getExtension('redhat.vscode-yaml') && /\.blink\.ya?ml$/.test(doc.uri.path);
}

function lint(doc, ctx) {
  if (!isBlinkDoc(doc)) { collection.delete(doc.uri); return; }
  const custom = cfg().get('dataPath', '');
  const dataDir = custom || path.join(ctx.extensionPath, 'data');
  const bin = path.join(ctx.extensionPath, 'bin', `${process.platform}-${process.arch}`, process.platform === 'win32' ? 'blinklint.exe' : 'blinklint');
  const useBin = require('fs').existsSync(bin);
  const args = useBin ? ['-', '--json', '--data', dataDir]
    : [path.join(ctx.extensionPath, 'linter', 'blinklint.py'), '-', '--json', '--data', dataDir];
  if (usesRedHatSchema(doc)) args.push('--no-schema');
  const child = cp.spawn(useBin ? bin : cfg().get('pythonPath', 'python3'), args);
  let out = '', err = '';
  child.stdout.on('data', (b) => (out += b));
  child.stderr.on('data', (b) => (err += b));
  child.on('error', (e) => setupProblem(`Cannot run ${useBin ? bin : cfg().get('pythonPath')}: ${e.message}`));
  child.on('close', () => {
    let items;
    try { items = JSON.parse(out); } catch (e) {
      if (err) { output.appendLine(err); setupProblem('Linter failed; see "Blink Linter" output.' + (/No module named/.test(err) ? ' Run: python3 -m pip install --user pyyaml jsonschema' : '')); }
      return;
    }
    collection.set(doc.uri, items.map((x) => {
      const d = new vscode.Diagnostic(new vscode.Range(x.line, x.col, x.endLine, x.endCol), x.message, SEV[x.severity]);
      d.source = 'blink';
      d.code = x.code;
      return d;
    }));
  });
  child.stdin.on('error', () => {});
  child.stdin.end(doc.getText());
}

function runner(ctx, extra, text, cb) {
  const bin = path.join(ctx.extensionPath, 'bin', `${process.platform}-${process.arch}`, process.platform === 'win32' ? 'blinklint.exe' : 'blinklint');
  const useBin = require('fs').existsSync(bin);
  const data = cfg().get('dataPath', '') || path.join(ctx.extensionPath, 'data');
  const args = (useBin ? [] : [path.join(ctx.extensionPath, 'linter', 'blinklint.py')]).concat(['-', '--data', data], extra);
  const ws = vscode.workspace.workspaceFolders;
  if (ws) args.push('--workspace', ws[0].uri.fsPath);
  const child = cp.spawn(useBin ? bin : cfg().get('pythonPath', 'python3'), args);
  let out = '', err = '';
  child.stdout.on('data', (b) => (out += b));
  child.stderr.on('data', (b) => (err += b));
  child.on('error', (e) => cb(e.message));
  child.on('close', () => cb(err && !out ? err : null, out));
  child.stdin.on('error', () => {});
  child.stdin.end(text);
}

const explainCache = new Map();
function getExplain(doc, ctx) {
  const key = doc.uri.toString();
  const hit = explainCache.get(key);
  if (hit && hit.version === doc.version) return hit.promise;
  const promise = new Promise((resolve) => runner(ctx, ['--explain', 'json'], doc.getText(), (e, out) => {
    try { resolve(JSON.parse(out)); } catch (x) { resolve(null); }
  }));
  explainCache.set(key, { version: doc.version, promise });
  return promise;
}

function explainCommand(ctx) {
  const ed = vscode.window.activeTextEditor;
  if (!ed) return;
  runner(ctx, ['--explain', 'md'], ed.document.getText(), async (e, out) => {
    if (e) { vscode.window.showErrorMessage('Blink explain failed: ' + e.slice(0, 200)); return; }
    const md = await vscode.workspace.openTextDocument({ language: 'markdown', content: out });
    await vscode.commands.executeCommand('markdown.showPreviewToSide', md.uri);
  });
}

function setupProblem(msg) {
  if (warnedSetup) return;
  warnedSetup = true;
  vscode.window.showErrorMessage('BlinkOps Linter: ' + msg);
}

function schedule(doc, ctx, delay) {
  const key = doc.uri.toString();
  clearTimeout(timers.get(key));
  timers.set(key, setTimeout(() => lint(doc, ctx), delay));
}

function activate(ctx) {
  collection = vscode.languages.createDiagnosticCollection('blink');
  output = vscode.window.createOutputChannel('Blink Linter');
  ctx.subscriptions.push(collection, output);
  ctx.subscriptions.push(
    vscode.workspace.onDidOpenTextDocument((d) => schedule(d, ctx, 0)),
    vscode.workspace.onDidSaveTextDocument((d) => schedule(d, ctx, 0)),
    vscode.workspace.onDidChangeTextDocument((e) => { if (cfg().get('lintOnType', true)) schedule(e.document, ctx, 300); }),
    vscode.workspace.onDidCloseTextDocument((d) => collection.delete(d.uri)),
    vscode.workspace.onDidChangeConfiguration((e) => { if (e.affectsConfiguration('blink')) vscode.workspace.textDocuments.forEach((d) => schedule(d, ctx, 0)); }),
    vscode.commands.registerCommand('blink.lintFile', () => {
      const ed = vscode.window.activeTextEditor;
      if (ed) lint(ed.document, ctx);
    }),
    vscode.commands.registerCommand('blink.explain', () => explainCommand(ctx)),
    vscode.languages.registerHoverProvider('yaml', {
      async provideHover(doc, pos) {
        if (!isBlinkDoc(doc)) return;
        const line = doc.lineAt(pos.line).text;
        if (!/^\s*(-\s+)?action:\s/.test(line)) return;
        const ex = await getExplain(doc, ctx);
              const step = ex && ex.steps.find((x) => line.includes(x.action) && Math.abs(x.line - pos.line) <= 3);
        if (!step) return;
        const m = new vscode.MarkdownString();
        m.appendMarkdown(`**${step.id} — ${step.name || step.action}** (${step.kind})\n\n${step.what}\n\n`);
        if (step.reads_from) m.appendMarkdown(`**Reads from:** ${step.reads_from}\n\n`);
        if (step.runs_on) m.appendMarkdown(`**Runs on:** ${step.runs_on}\n\n`);
        if (step.data_from.length) m.appendMarkdown(`**Uses data from:** ${step.data_from.join('; ')}\n\n`);
        if (step.feeds.length) m.appendMarkdown(`**Feeds:** ${step.feeds.join(', ')}`);
        return new vscode.Hover(m);
      },
    }),
    vscode.commands.registerCommand('blink.about', () =>
      vscode.window.showInformationMessage(`BlinkOps Workflow Linter ${ctx.extension.packageJSON.version} — catalog: ${cfg().get('dataPath') || 'bundled'}`)),
  );
  vscode.workspace.textDocuments.forEach((d) => schedule(d, ctx, 0));
}

function deactivate() { timers.forEach(clearTimeout); }

module.exports = { activate, deactivate };
