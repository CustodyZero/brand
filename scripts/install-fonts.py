#!/usr/bin/env python3
"""
Download and install Bebas Neue (latin subset) for use with cairosvg.

cairosvg resolves fonts via fontconfig / system font paths, not via SVG
@font-face data URIs. This script places the TTF in the correct location
so that rasterize.py produces output using the actual brand typeface.

Prerequisites:
  pip install fonttools brotli requests

Idempotent: safe to run multiple times.
"""
import os
import sys
import urllib.request
from pathlib import Path


WOFF2_URL = (
    "https://fonts.gstatic.com/s/bebasneue/v16/"
    "JTUSjIg69CK48gW7PXoo9WlhyyTh89Y.woff2"
)
FONT_NAME = "BebasNeue-Regular.ttf"


def font_dir() -> Path:
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Fonts"
    elif sys.platform.startswith("linux"):
        d = Path.home() / ".local" / "share" / "fonts"
        d.mkdir(parents=True, exist_ok=True)
        return d
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")


def main():
    dest = font_dir() / FONT_NAME
    if dest.exists():
        print(f"Already installed: {dest}")
        return

    print(f"Downloading Bebas Neue (latin) from Google Fonts…")
    woff2_path = Path("/tmp/bebas-neue-install.woff2")
    urllib.request.urlretrieve(WOFF2_URL, woff2_path)

    print("Converting woff2 → TTF (requires fonttools + brotli)…")
    from fontTools.ttLib import TTFont
    font = TTFont(str(woff2_path))
    font.flavor = None
    font.save(str(dest))
    print(f"Installed: {dest}")

    if sys.platform.startswith("linux"):
        os.system("fc-cache -f")
        print("Font cache refreshed.")


if __name__ == "__main__":
    main()
