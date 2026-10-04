#!/usr/bin/env python3
"""Prepare the site for GitHub Pages in _site/ (run automatically by GitHub Actions).

Copies the page and its icon, then downloads the Google Fonts the page uses and
serves them from this site, so visitors' browsers never contact Google.
If the download fails, the font links are removed and the page falls back to
system fonts; it never links Google directly.

Try it locally:
    python publish.py
    python -m http.server -d _site 8000     # then open http://localhost:8000
"""
import hashlib
import re
import shutil
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_site"
FILES = ["index.html", "favicon.svg"]
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
FONT_LINK = re.compile(r'<link[^>]+href="(https://fonts\.googleapis\.com/css2?[^"]+)"[^>]*>\n?')
PRECONNECT = re.compile(
    r'<link[^>]+rel="preconnect"[^>]+href="https://fonts\.(?:googleapis|gstatic)\.com"[^>]*>\n?')


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": BROWSER_UA})
    return urllib.request.urlopen(req, timeout=30).read()


def download_fonts(css_url, font_dir):
    """Save the stylesheet and its font files in font_dir; return the number of files."""
    css = fetch(css_url).decode("utf-8")
    font_dir.mkdir(parents=True, exist_ok=True)

    def grab(match):
        url = match.group(1)
        name = hashlib.md5(url.encode()).hexdigest()[:12] + Path(url).suffix
        if not (font_dir / name).exists():
            (font_dir / name).write_bytes(fetch(url))
        return f"url(./{name})"

    css = re.sub(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", grab, css)
    (font_dir / "fonts.css").write_text(css, encoding="utf-8")
    return len(list(font_dir.glob("*.woff2")))


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for name in FILES:
        shutil.copy2(ROOT / name, OUT / name)

    page = OUT / "index.html"
    html = PRECONNECT.sub("", page.read_text(encoding="utf-8"))
    m = FONT_LINK.search(html)
    if m:
        try:
            n = download_fonts(m.group(1).replace("&amp;", "&"), OUT / "fonts")
            html = FONT_LINK.sub('<link rel="stylesheet" href="fonts/fonts.css">\n', html, count=1)
            print(f"Fonts: self-hosted {n} files")
        except Exception as exc:  # offline, blocked, etc.
            html = FONT_LINK.sub("", html, count=1)
            print(f"Fonts: could not download ({exc}); using system fonts")
    page.write_text(html, encoding="utf-8")
    print(f"Ready in {OUT.name}/")


if __name__ == "__main__":
    main()
