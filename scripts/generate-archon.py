#!/usr/bin/env python3
"""
Generate Archon brand assets: wordmarks (SVG + PNG 2x/3x) and icon mark (SVG + ICO + PNG).

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue TTF must be installed — run scripts/install-fonts.py first.

Usage:
  python3 scripts/generate-archon.py
"""

import base64
import os
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont

BASE = Path(__file__).parent.parent
WORDMARK_DIR = BASE / "brand" / "archon" / "wordmark"
ICON_DIR = BASE / "brand" / "archon" / "icon"

FONT_PATH = Path.home() / "Library" / "Fonts" / "BebasNeue-Regular.ttf"

BLUE = "#4FC3F7"
WHITE = "#F2F2EC"

# Wordmark layout constants
WM_CANVAS_W = 400
WM_CANVAS_H = 72
WM_FONT_SIZE = 72.0
WM_LETTER_SPACING_EM = 0.12
WM_X_START = 3.0
WM_Y_BASELINE = 66.0  # ~4px top clearspace for Bebas Neue cap height at 72px
WM_Y_RULE = 69.0      # 3px below baseline


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
        f"  src: url(\"data:font/truetype;base64,{b64}\") format(\"truetype\"),\n"
        "       url('https://fonts.gstatic.com/s/bebasneue/v16/JTUSjIg69CK48gW7PXoo9WlhyyTh89Y.woff2') format('woff2');\n"
        "}"
    )


def wordmark_svg(text_color: str, font_b64: str, text_width: float) -> str:
    """Generate a wordmark SVG for the given text color."""
    x_rule_end = WM_X_START + text_width
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"'
        f' viewBox="0 0 {WM_CANVAS_W} {WM_CANVAS_H}"'
        f' width="{WM_CANVAS_W}" height="{WM_CANVAS_H}">\n'
        f"  <defs>\n"
        f"    <style>{font_face(font_b64)}</style>\n"
        f"  </defs>\n"
        f'  <text x="{WM_X_START}" y="{WM_Y_BASELINE}" text-anchor="start"\n'
        f"        font-family=\"'Bebas Neue', sans-serif\"\n"
        f"        font-size=\"{WM_FONT_SIZE}\" letter-spacing=\"{WM_LETTER_SPACING_EM}em\"\n"
        f'        fill="{text_color}">ARCHON</text>\n'
        f'  <line x1="{WM_X_START}" y1="{WM_Y_RULE}"'
        f' x2="{x_rule_end:.2f}" y2="{WM_Y_RULE}"'
        f' stroke="{BLUE}" stroke-width="1"/>\n'
        f"</svg>\n"
    )


def icon_svg() -> str:
    """
    Generate the Archon icon mark SVG.

    Design: two L-shaped corner brackets (top-left, bottom-right) on a diagonal
    axis, with a small centered circle implying a validation/enforcement node.
    Stroke-based, 2px, stroke-linecap square. Transparent background.

    Legibility check:
      64×64 (1:1): 14px arms, corner inset 8px, center dot r=3.5
      32×32 (1/2): arms ~7px, dot ~1.75px — legible
      16×16 (1/4): arms ~3.5px, dot ~0.875px — distinct diagonal shape
    """
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">\n'
        '  <!-- Archon icon: diagonal corner brackets + center enforcement node -->\n'
        '  <!-- Two L-brackets on the top-left / bottom-right diagonal axis -->\n'
        '  <!-- imply a containment boundary and validation threshold -->\n'
        '  <polyline points="8,22 8,8 22,8"\n'
        '            fill="none" stroke="#4FC3F7" stroke-width="2"\n'
        '            stroke-linecap="square" stroke-linejoin="miter"/>\n'
        '  <polyline points="42,56 56,56 56,42"\n'
        '            fill="none" stroke="#4FC3F7" stroke-width="2"\n'
        '            stroke-linecap="square" stroke-linejoin="miter"/>\n'
        '  <!-- Center node: enforcement validation point -->\n'
        '  <circle cx="32" cy="32" r="3.5" fill="#4FC3F7"/>\n'
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
    import struct

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

    print("Measuring text width for underline rule…")
    text_width = measure_text_width("ARCHON", WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    print(f"  'ARCHON' at {WM_FONT_SIZE}px, {WM_LETTER_SPACING_EM}em spacing → {text_width:.2f}px")

    print("\nGenerating wordmark SVGs…")
    wm_dark = wordmark_svg(WHITE, font_b64, text_width)
    wm_blue = wordmark_svg(BLUE, font_b64, text_width)

    dark_svg = WORDMARK_DIR / "archon-wordmark-dark.svg"
    blue_svg = WORDMARK_DIR / "archon-wordmark-blue.svg"
    dark_svg.write_text(wm_dark, encoding="utf-8")
    print(f"  {dark_svg.relative_to(BASE)}")
    blue_svg.write_text(wm_blue, encoding="utf-8")
    print(f"  {blue_svg.relative_to(BASE)}")

    print("\nRasterizing wordmarks…")
    svg_to_png(wm_dark, WORDMARK_DIR / "archon-wordmark-dark@2x.png", 800, 144)
    svg_to_png(wm_dark, WORDMARK_DIR / "archon-wordmark-dark@3x.png", 1200, 216)
    svg_to_png(wm_blue, WORDMARK_DIR / "archon-wordmark-blue@2x.png", 800, 144)
    svg_to_png(wm_blue, WORDMARK_DIR / "archon-wordmark-blue@3x.png", 1200, 216)

    print("\nGenerating icon SVG…")
    icon = icon_svg()
    icon_svg_path = ICON_DIR / "archon-icon-dark.svg"
    icon_svg_path.write_text(icon, encoding="utf-8")
    print(f"  {icon_svg_path.relative_to(BASE)}")

    print("\nRasterizing icon…")
    svg_to_png(icon, ICON_DIR / "archon-icon-dark@2x.png", 128, 128)
    svg_to_png(icon, ICON_DIR / "archon-icon-dark@3x.png", 192, 192)

    print("\nGenerating ICO…")
    svg_to_ico(icon, ICON_DIR / "archon-icon-dark.ico", [16, 32, 48])

    print("\nDone.")
    print(f"\nAll Archon brand assets written to:")
    print(f"  {WORDMARK_DIR.relative_to(BASE)}/")
    print(f"  {ICON_DIR.relative_to(BASE)}/")


if __name__ == "__main__":
    main()
