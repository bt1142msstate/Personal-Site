from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
SOURCE_HTML = ROOT / "resume.html"
OUTPUT_PDF = ROOT / "Brandon_Temple_MSU_Resume.pdf"


def find_chrome() -> str | None:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    return next((candidate for candidate in candidates if candidate and Path(candidate).exists()), None)


def file_url(path: Path) -> str:
    return f"file://{quote(str(path.resolve()))}"


def build_pdf() -> int:
    chrome = find_chrome()
    if chrome is None:
        print("Could not find a Chromium-based browser for PDF export.", file=sys.stderr)
        print("Install Google Chrome or Chromium, then rerun this script.", file=sys.stderr)
        return 1

    if not SOURCE_HTML.exists():
        print(f"Missing source file: {SOURCE_HTML}", file=sys.stderr)
        return 1

    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        file_url(SOURCE_HTML),
    ]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        if result.stderr.strip():
            print(result.stderr.strip(), file=sys.stderr)
        if result.stdout.strip():
            print(result.stdout.strip(), file=sys.stderr)
        return result.returncode

    print(f"Generated: {OUTPUT_PDF.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(build_pdf())
