#!/usr/bin/env python3
"""Compile the Typst entrypoint, then add shared reading styles atomically."""
from pathlib import Path
import argparse
import os
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"


def build():
    if not shutil.which("typst"):
        raise RuntimeError("找不到 typst；請安裝 Typst 0.15.1。")
    SITE.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="learning-notes-") as directory:
        output = Path(directory) / "index.html"
        subprocess.run([
            "typst", "compile", "--root", str(ROOT), "--features", "html",
            str(ROOT / "main.typ"), str(output),
        ], cwd=ROOT, check=True)
        document = output.read_text(encoding="utf-8")
        if document.count("</head>") != 1:
            raise RuntimeError("Typst HTML 結構改變：找不到唯一的 head。")
        document = document.replace("</head>",
            '<link rel="stylesheet" href="styles.css"></head>', 1)
        # Publish HTML last, so failed compilation preserves the last good page.
        css = SITE / ".styles.css.tmp"
        shutil.copyfile(ROOT / "styles/reading.css", css)
        os.replace(css, SITE / "styles.css")
        temporary = SITE / ".index.html.tmp"
        temporary.write_text(document, encoding="utf-8")
        os.replace(temporary, SITE / "index.html")
        (SITE / ".nojekyll").touch()
    print(f"HTML: {SITE / 'index.html'}", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        build()
    except (RuntimeError, subprocess.CalledProcessError) as error:
        raise SystemExit(str(error))
