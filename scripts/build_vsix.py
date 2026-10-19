#!/usr/bin/env python3
"""Package extension/ into dist/<name>-<version>.vsix without npm/vsce (a vsix is a zip)."""
import json, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

R = Path(__file__).resolve().parent.parent
E = R / "extension"
pkg = json.loads((E / "package.json").read_text())
name, ver = pkg["name"], pkg["version"]
manifest = f'''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">
  <Metadata>
    <Identity Language="en-US" Id="{name}" Version="{ver}" Publisher="{pkg["publisher"]}"/>
    <DisplayName>{escape(pkg["displayName"])}</DisplayName>
    <Description xml:space="preserve">{escape(pkg["description"])}</Description>
    <Categories>{",".join(pkg.get("categories", []))}</Categories>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{pkg["engines"]["vscode"]}"/>
      <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value=""/>
    </Properties>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
  </Assets>
</PackageManifest>
'''
content_types = '''<?xml version="1.0" encoding="utf-8"?>
<Types><Default Extension=".json" ContentType="application/json"/><Default Extension=".js" ContentType="application/javascript"/>
<Default Extension=".py" ContentType="text/x-python"/><Default Extension=".md" ContentType="text/markdown"/>
<Default Extension=".vsixmanifest" ContentType="text/xml"/></Types>
'''
out = R / "dist" / f"{name}-{ver}.vsix"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("extension.vsixmanifest", manifest)
    for f in sorted(E.rglob("*")):
        if f.is_file() and "__pycache__" not in f.parts and f.name != ".vscodeignore":
            z.write(f, "extension/" + f.relative_to(E).as_posix())
print(out, f"{out.stat().st_size // 1024} KB")
