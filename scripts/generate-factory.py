#!/usr/bin/env python3
"""
Generate Factory brand assets: wordmarks (SVG + PNG 2x/3x) and icon mark (SVG + ICO + PNG).

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue TTF must be installed — run scripts/install-fonts.py first.

Usage:
  python3 scripts/generate-factory.py
"""

import base64
import os
import struct
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont

BASE = Path(__file__).parent.parent
WORDMARK_DIR = BASE / "brand" / "factory" / "wordmark"
ICON_DIR = BASE / "brand" / "factory" / "icon"

FONT_PATH = Path.home() / "Library" / "Fonts" / "BebasNeue-Regular.ttf"

GREEN = "#5A9A6E"
WHITE = "#F2F2EC"

# Wordmark layout constants
WM_CANVAS_H = 72
WM_FONT_SIZE = 72.0
WM_LETTER_SPACING_EM = 0.12
WM_X_START = 3.0
WM_Y_BASELINE = 66.0  # ~4px top clearspace for Bebas Neue cap height at 72px


def load_font_b64() -> str:
    with open(FONT_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def measure_text_width(text: str, font_size: float, letter_spacing_em: float) -> float:
    """
    Compute the visual ink width of `text` using actual glyph advance widths.
    Excludes trailing letter-spacing (matches visual extent, not advance extent).
    """
    tt = TTFont(str(FONT_PATH))
    cmap = tt.getBestCmap()
    hmtx = tt["hmtx"].metrics
    upm = tt["head"].unitsPerEm

    advances = []
    for char in text:
        gid = cmap.get(ord(char))
        if gid is None:
            raise ValueError(f"Glyph not found for character '{char}' (U+{ord(char):04X})")
        adv, _ = hmtx[gid]
        advances.append(adv / upm * font_size)

    # Ink extent: sum of advances + (n-1) letter-spacing gaps (no trailing gap)
    spacing_px = letter_spacing_em * font_size
    return sum(advances) + (len(text) - 1) * spacing_px


def font_face(b64: str) -> str:
    return (
        "@font-face {\n"
        "  font-family: 'Bebas Neue';\n"
        "  font-style: normal;\n"
        "  font-weight: 400;\n"
        f'  src: url("data:font/truetype;base64,{b64}") format("truetype"),\n'
        "       url('https://fonts.gstatic.com/s/bebasneue/v16/JTUSjIg69CK48gW7PXoo9WlhyyTh89Y.woff2') format('woff2');\n"
        "}"
    )


def wordmark_svg(text_color: str, font_b64: str, canvas_w: int) -> str:
    """Generate a wordmark SVG for the given text color. No decorative element."""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"'
        f' viewBox="0 0 {canvas_w} {WM_CANVAS_H}"'
        f' width="{canvas_w}" height="{WM_CANVAS_H}">\n'
        f"  <defs>\n"
        f"    <style>{font_face(font_b64)}</style>\n"
        f"  </defs>\n"
        f'  <text x="{WM_X_START}" y="{WM_Y_BASELINE}" text-anchor="start"\n'
        f"        font-family=\"'Bebas Neue', sans-serif\"\n"
        f"        font-size=\"{WM_FONT_SIZE}\" letter-spacing=\"{WM_LETTER_SPACING_EM}em\"\n"
        f'        fill="{text_color}">FACTORY</text>\n'
        f"</svg>\n"
    )


def icon_svg() -> str:
    """
    Generate the Factory icon mark SVG.

    Design: The Gate — two vertical bars with a horizontal threshold line
    between them. Packets must pass through to be verified.

    The vertical bars represent the boundary of the factory process.
    The horizontal threshold represents the verification gate that all
    work must cross. Stroke-based, square geometry, transparent background.

    Legibility check:
      64×64 (1:1): bars 36px tall, gap 24px — clear gate form
      32×32 (1/2): bars 18px, gap 12px — legible
      16×16 (1/4): bars 9px, gap 6px — distinctive H-like shape
    """
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">\n'
        '  <!-- Factory icon: The Gate — two vertical bars + horizontal threshold -->\n'
        '  <!-- Vertical bars define the process boundary; threshold is the verification gate -->\n'
        '  <!-- Left bar -->\n'
        '  <line x1="16" y1="14" x2="16" y2="50"\n'
        '        stroke="#5A9A6E" stroke-width="2.5" stroke-linecap="square"/>\n'
        '  <!-- Right bar -->\n'
        '  <line x1="48" y1="14" x2="48" y2="50"\n'
        '        stroke="#5A9A6E" stroke-width="2.5" stroke-linecap="square"/>\n'
        '  <!-- Horizontal threshold -->\n'
        '  <line x1="16" y1="32" x2="48" y2="32"\n'
        '        stroke="#5A9A6E" stroke-width="2.5" stroke-linecap="square"/>\n'
        '</svg>\n'
    )


def svg_to_png(svg_content: str, out_path: Path, width: int, height: int):
    cairosvg.svg2png(
        bytestring=svg_content.encode("utf-8"),
        write_to=str(out_path),
        output_width=width,
        output_height=height,
    )
    print(f"  {out_path.relative_to(BASE)} ({width}×{height})")


def svg_to_ico(svg_content: str, out_path: Path, sizes: list):
    """
    Build a multi-size ICO by embedding one PNG frame per requested size.

    Pillow's ICO saver does not reliably produce multi-frame ICOs; we write
    the ICO binary manually using the modern PNG-embedded ICO format so that
    all three sizes (16, 32, 48) are faithfully encoded in the file.
    """
    png_list = [
        cairosvg.svg2png(
            bytestring=svg_content.encode("utf-8"),
            output_width=s,
            output_height=s,
        )
        for s in sizes
    ]

    # ICO header: reserved=0, type=1 (ICO), count=N
    n = len(sizes)
    header = struct.pack("<HHH", 0, 1, n)

    # Directory entries begin at byte 6; each entry is 16 bytes
    data_offset = 6 + n * 16
    entries = b""
    data = b""
    offset = data_offset
    for size, png in zip(sizes, png_list):
        w = size if size < 256 else 0
        h = size if size < 256 else 0
        entries += struct.pack("<BBBBHHII", w, h, 0, 0, 1, 32, len(png), offset)
        data += png
        offset += len(png)

    out_path.write_bytes(header + entries + data)
    print(f"  {out_path.relative_to(BASE)} (ICO frames: {sizes})")


def main():
    WORDMARK_DIR.mkdir(parents=True, exist_ok=True)
    ICON_DIR.mkdir(parents=True, exist_ok=True)

    if not FONT_PATH.exists():
        raise FileNotFoundError(
            f"Bebas Neue TTF not found at {FONT_PATH}. "
            "Run scripts/install-fonts.py first."
        )

    print("Loading font…")
    font_b64 = load_font_b64()

    print("Measuring text width…")
    text_width = measure_text_width("FACTORY", WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    print(f"  'FACTORY' at {WM_FONT_SIZE}px, {WM_LETTER_SPACING_EM}em spacing → {text_width:.2f}px")

    # Canvas width: text width + x start padding + right padding
    canvas_w = int(text_width + WM_X_START + 3)

    print("\nGenerating wordmark SVGs…")
    wm_dark = wordmark_svg(WHITE, font_b64, canvas_w)
    wm_green = wordmark_svg(GREEN, font_b64, canvas_w)

    dark_svg = WORDMARK_DIR / "factory-wordmark-dark.svg"
    green_svg = WORDMARK_DIR / "factory-wordmark-green.svg"
    dark_svg.write_text(wm_dark, encoding="utf-8")
    print(f"  {dark_svg.relative_to(BASE)}")
    green_svg.write_text(wm_green, encoding="utf-8")
    print(f"  {green_svg.relative_to(BASE)}")

    print("\nRasterizing wordmarks…")
    svg_to_png(wm_dark, WORDMARK_DIR / "factory-wordmark-dark@2x.png", canvas_w * 2, WM_CANVAS_H * 2)
    svg_to_png(wm_dark, WORDMARK_DIR / "factory-wordmark-dark@3x.png", canvas_w * 3, WM_CANVAS_H * 3)
    svg_to_png(wm_green, WORDMARK_DIR / "factory-wordmark-green@2x.png", canvas_w * 2, WM_CANVAS_H * 2)
    svg_to_png(wm_green, WORDMARK_DIR / "factory-wordmark-green@3x.png", canvas_w * 3, WM_CANVAS_H * 3)

    print("\nGenerating icon SVG…")
    icon = icon_svg()
    icon_svg_path = ICON_DIR / "factory-icon-dark.svg"
    icon_svg_path.write_text(icon, encoding="utf-8")
    print(f"  {icon_svg_path.relative_to(BASE)}")

    print("\nRasterizing icon…")
    svg_to_png(icon, ICON_DIR / "factory-icon-dark@2x.png", 128, 128)
    svg_to_png(icon, ICON_DIR / "factory-icon-dark@3x.png", 192, 192)

    print("\nGenerating ICO…")
    svg_to_ico(icon, ICON_DIR / "factory-icon-dark.ico", [16, 32, 48])

    print("\nDone.")
    print(f"\nAll Factory brand assets written to:")
    print(f"  {WORDMARK_DIR.relative_to(BASE)}/")
    print(f"  {ICON_DIR.relative_to(BASE)}/")


if __name__ == "__main__":
    main()
