#!/usr/bin/env python3
"""
Rasterize CustodyZero brand SVGs to PNG and ICO.

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  The Bebas Neue TTF must be installed in ~/Library/Fonts/ (macOS) or
  /usr/share/fonts/ (Linux) for cairosvg to resolve it via fontconfig.
  Run scripts/install-fonts.py to install it automatically.

Usage:
  python3 scripts/rasterize.py
"""
import os
import cairosvg
from PIL import Image
import io

BASE         = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORDMARK_DIR = os.path.join(BASE, "brand/custodyzero/wordmark")
ICON_DIR     = os.path.join(BASE, "brand/custodyzero/icon")

ASSETS = [
    # (svg_path, out_path, width, height)
    (
        os.path.join(WORDMARK_DIR, "custodyzero-wordmark-dark.svg"),
        os.path.join(WORDMARK_DIR, "custodyzero-wordmark-dark@2x.png"),
        960, 160,
    ),
    (
        os.path.join(WORDMARK_DIR, "custodyzero-wordmark-dark.svg"),
        os.path.join(WORDMARK_DIR, "custodyzero-wordmark-dark@3x.png"),
        1440, 240,
    ),
    (
        os.path.join(WORDMARK_DIR, "custodyzero-cz-dark.svg"),
        os.path.join(WORDMARK_DIR, "custodyzero-cz-dark@2x.png"),
        308, 160,
    ),
    (
        os.path.join(WORDMARK_DIR, "custodyzero-cz-dark.svg"),
        os.path.join(WORDMARK_DIR, "custodyzero-cz-dark@3x.png"),
        462, 240,
    ),
]

ICO_ASSET = (
    os.path.join(ICON_DIR, "custodyzero-icon-dark.svg"),
    os.path.join(ICON_DIR, "custodyzero-icon-dark.ico"),
    [16, 32, 48],
)


def svg_to_png(svg_path, out_path, width, height):
    cairosvg.svg2png(url=svg_path, write_to=out_path, output_width=width, output_height=height)
    print(f"  {out_path} ({width}x{height})")


def svg_to_ico(svg_path, out_path, sizes):
    # Render at the largest size; Pillow resamples each ICO frame.
    max_size = max(sizes)
    png_bytes = cairosvg.svg2png(url=svg_path, output_width=max_size, output_height=max_size)
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    img.save(out_path, format="ICO", sizes=[(s, s) for s in sizes])
    print(f"  {out_path} (ICO {sizes})")


def main():
    print("Rasterizing PNGs...")
    for svg, out, w, h in ASSETS:
        svg_to_png(svg, out, w, h)

    print("Generating ICO...")
    svg_to_ico(*ICO_ASSET)

    print("Done.")


if __name__ == "__main__":
    main()
