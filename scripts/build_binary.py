#!/usr/bin/env python3
"""Build the standalone linter with PyInstaller into extension/bin/<os>-<arch>/.
Must run on each target OS (see .github/workflows/build.yml)."""
import platform, shutil, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent
osn = {"Darwin": "darwin", "Windows": "win32", "Linux": "linux"}[platform.system()]
arch = {"x86_64": "x64", "AMD64": "x64", "arm64": "arm64", "aarch64": "arm64"}[platform.machine()]
out = R / "extension" / "bin" / f"{osn}-{arch}"
work = R / "build"
subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile", "--clean", "--name", "blinklint",
    "--distpath", str(out), "--workpath", str(work), "--specpath", str(work),
    str(R / "extension/linter/blinklint.py")])
shutil.rmtree(work, ignore_errors=True)
print("built", out)
