#!/usr/bin/env python3
"""
Generate Valet brand assets: wordmark (SVG + PNG 2x/3x) and icon mark (SVG + ICO + PNG).

Design decisions (locked April 2026):
  - Accent: Bronze B·04 #9D7E49 · oklch(0.54 0.075 82)
  - Icon: The Binding (I·02 a·03) — three horizontal bars, thickened center
  - Wordmark: Bebas Neue, letter-spacing 0.12em

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue TTF must be installed — run scripts/install-fonts.py first.

Usage:
  python3 scripts/generate-valet.py
"""

import base64
import struct
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont

BASE = Path(__file__).parent.parent
WORDMARK_DIR = BASE / "brand" / "valet" / "wordmark"
ICON_DIR = BASE / "brand" / "valet" / "icon"

FONT_PATH = Path.home() / "Library" / "Fonts" / "BebasNeue-Regular.ttf"

# Locked accent — Bronze B·04
BRONZE = "#9D7E49"
WHITE = "#F2F2EC"

# Product identity — the only axis that differs between valet and steward
PRODUCT = "VALET"
PRODUCT_LC = "valet"

# Wordmark layout constants (match Factory convention)
WM_CANVAS_H = 72
WM_FONT_SIZE = 72.0
WM_LETTER_SPACING_EM = 0.12
WM_X_START = 3.0
WM_Y_BASELINE = 66.0  # ~4px top clearspace for Bebas Neue cap height at 72px


def load_font_b64() -> str:
    with open(FONT_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def measure_text_width(text: str, font_size: float, letter_spacing_em: float) -> float:
    """Ink width — sum of advances + (n-1) letter-spacing gaps, no trailing gap."""
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
    """Valet wordmark — unadorned Bebas Neue in the requested color on transparent."""
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
        f'        fill="{text_color}">{PRODUCT}</text>\n'
        f"</svg>\n"
    )


def icon_svg() -> str:
    """
    Valet icon mark — The Binding (I·02 a·03).

    Three horizontal bars on a 64×64 canvas, representing the visible
    bookbinding marks on a well-kept spine. Continuity, record, enduring form.

    Geometry (locked):
      - Top bar: x=22→42, y=20 · stroke 2.5 · width 20 px
      - Center bar: x=14→50, y=32 · stroke 3.5 · width 36 px (accent, thicker)
      - Bottom bar: x=22→42, y=44 · stroke 2.5 · width 20 px
      - Vertical spacing: 12 px between bar centers
      - Color: #9D7E49 (Bronze B·04) on transparent

    Legibility check:
      64×64 (1:1): bars 20/36/20 px wide, 12px spacing — clear binding register
      32×32 (1/2): bars 10/18/10 px — legible
      16×16 (1/4): bars 5/9/5 px — narrow-wide-narrow silhouette preserved
    """
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">\n'
        '  <!-- Valet icon: The Binding — three horizontal marks, thickened center -->\n'
        '  <!-- Center bar is heavier (stroke 3.5) — the gather emphasis -->\n'
        '  <!-- Top bar: head band -->\n'
        '  <line x1="22" y1="20" x2="42" y2="20"\n'
        f'        stroke="{BRONZE}" stroke-width="2.5" stroke-linecap="square"/>\n'
        '  <!-- Center bar: gather, thickened -->\n'
        '  <line x1="14" y1="32" x2="50" y2="32"\n'
        f'        stroke="{BRONZE}" stroke-width="3.5" stroke-linecap="square"/>\n'
        '  <!-- Bottom bar: tail band -->\n'
        '  <line x1="22" y1="44" x2="42" y2="44"\n'
        f'        stroke="{BRONZE}" stroke-width="2.5" stroke-linecap="square"/>\n'
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
    """Manually build multi-frame ICO with PNG-embedded frames at each size."""
    png_list = [
        cairosvg.svg2png(
            bytestring=svg_content.encode("utf-8"),
            output_width=s,
            output_height=s,
        )
        for s in sizes
    ]

    n = len(sizes)
    header = struct.pack("<HHH", 0, 1, n)

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
    text_width = measure_text_width(PRODUCT, WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    print(f"  '{PRODUCT}' at {WM_FONT_SIZE}px, {WM_LETTER_SPACING_EM}em spacing → {text_width:.2f}px")

    canvas_w = int(text_width + WM_X_START + 3)

    print("\nGenerating wordmark SVGs…")
    wm_dark = wordmark_svg(WHITE, font_b64, canvas_w)
    wm_bronze = wordmark_svg(BRONZE, font_b64, canvas_w)

    dark_svg = WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-dark.svg"
    bronze_svg = WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-bronze.svg"
    dark_svg.write_text(wm_dark, encoding="utf-8")
    print(f"  {dark_svg.relative_to(BASE)}")
    bronze_svg.write_text(wm_bronze, encoding="utf-8")
    print(f"  {bronze_svg.relative_to(BASE)}")

    print("\nRasterizing wordmarks…")
    svg_to_png(wm_dark,   WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-dark@2x.png",   canvas_w * 2, WM_CANVAS_H * 2)
    svg_to_png(wm_dark,   WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-dark@3x.png",   canvas_w * 3, WM_CANVAS_H * 3)
    svg_to_png(wm_bronze, WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-bronze@2x.png", canvas_w * 2, WM_CANVAS_H * 2)
    svg_to_png(wm_bronze, WORDMARK_DIR / f"{PRODUCT_LC}-wordmark-bronze@3x.png", canvas_w * 3, WM_CANVAS_H * 3)

    print("\nGenerating icon SVG…")
    icon = icon_svg()
    icon_svg_path = ICON_DIR / f"{PRODUCT_LC}-icon-dark.svg"
    icon_svg_path.write_text(icon, encoding="utf-8")
    print(f"  {icon_svg_path.relative_to(BASE)}")

    print("\nRasterizing icon…")
    svg_to_png(icon, ICON_DIR / f"{PRODUCT_LC}-icon-dark@2x.png", 128, 128)
    svg_to_png(icon, ICON_DIR / f"{PRODUCT_LC}-icon-dark@3x.png", 192, 192)

    print("\nGenerating ICO…")
    svg_to_ico(icon, ICON_DIR / f"{PRODUCT_LC}-icon-dark.ico", [16, 32, 48])

    print("\nDone.")
    print(f"\nAll {PRODUCT.title()} brand assets written to:")
    print(f"  {WORDMARK_DIR.relative_to(BASE)}/")
    print(f"  {ICON_DIR.relative_to(BASE)}/")


if __name__ == "__main__":
    main()
