#!/usr/bin/env python3
"""
Download and install Cormorant Light (weight 300) for use with cairosvg.

cairosvg resolves fonts via fontconfig / system font paths, not via SVG
@font-face data URIs. This script places the TTF in the correct location
so that generate-type.py produces output using the actual brand typeface.

Idempotent: safe to run multiple times.
"""
import sys
import os
import urllib.request
from pathlib import Path


# Cormorant Light (300) — full latin from Google Fonts (TTF served directly)
TTF_URL = (
    "https://fonts.gstatic.com/s/cormorant/v24/"
    "H4c2BXOCl9bbnla_nHIA47NMUjsNbCVrFk9TQ7Q.ttf"
)
FONT_NAME = "Cormorant-Light.ttf"


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

    print("Downloading Cormorant Light (300) from Google Fonts...")
    urllib.request.urlretrieve(TTF_URL, dest)
    print(f"Installed: {dest}")

    if sys.platform.startswith("linux"):
        os.system("fc-cache -f")
        print("Font cache refreshed.")


if __name__ == "__main__":
    main()
