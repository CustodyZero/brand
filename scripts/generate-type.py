#!/usr/bin/env python3
"""
Generate Type brand assets: wordmarks (SVG + PNG 2x/3x), icon rasters (PNG + ICO),
and social card (SVG + PNG).

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Cormorant Light TTF must be installed — run scripts/install-cormorant.py first.

Usage:
  python3 scripts/generate-type.py
"""

import base64
import io
import os
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont
from PIL import Image


BASE = Path(__file__).parent.parent
BRAND_DIR = BASE / "brand" / "type"
WORDMARK_DIR = BRAND_DIR / "wordmark"
ICON_DIR = BRAND_DIR / "icon"
SOCIAL_DIR = BRAND_DIR / "social"

FONT_PATH = Path.home() / "Library" / "Fonts" / "Cormorant-Light.ttf"

# Brand tokens
PENCIL = "#8B3A3A"
PAPER_BRIGHT = "#FAF8F3"
PAPER = "#F5F0E8"
INK = "#1C1917"
INK_MUTED = "#8A8070"
INK_GHOST = "#B8AFA0"

# Wordmark layout constants
# Cormorant metrics at 72px: ascender ~66.5px, descender ~20.7px, total ~87.2px
# Canvas sized to contain full glyph with ~5px clearspace top and bottom
WM_TEXT = "Type"
WM_FONT_SIZE = 72.0
WM_LETTER_SPACING_EM = -0.03
WM_Y_BASELINE = 72.0   # ~5.5px top clearspace above ascender
WM_X_START = 3.0
WM_CANVAS_H = 98        # baseline(72) + descender(21) + clearspace(5) = 98


def load_font_b64() -> str:
    with open(FONT_PATH, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def measure_text_width(text: str, font_size: float, letter_spacing_em: float) -> float:
    """Compute visual ink width using actual glyph advance widths."""
    tt = TTFont(str(FONT_PATH))
    cmap = tt.getBestCmap()
    hmtx = tt["hmtx"].metrics
    upm = tt["head"].unitsPerEm

    advances = []
    for char in text:
        gid = cmap.get(ord(char))
        if gid is None:
            raise ValueError(f"Glyph not found for '{char}' (U+{ord(char):04X})")
        adv, _ = hmtx[gid]
        advances.append(adv / upm * font_size)

    spacing_px = letter_spacing_em * font_size
    return sum(advances) + (len(text) - 1) * spacing_px


def font_face(b64: str) -> str:
    return (
        "@font-face {\n"
        "  font-family: 'Cormorant';\n"
        "  font-style: normal;\n"
        "  font-weight: 300;\n"
        f'  src: url("data:font/truetype;base64,{b64}") format("truetype");\n'
        "}"
    )


def wordmark_svg(text_color: str, font_b64: str, text_width: float) -> str:
    canvas_w = int(WM_X_START + text_width + 10)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_w}" height="{WM_CANVAS_H}" viewBox="0 0 {canvas_w} {WM_CANVAS_H}">
  <defs>
    <style>{font_face(font_b64)}</style>
  </defs>
  <text
    x="{WM_X_START}"
    y="{WM_Y_BASELINE}"
    font-family="'Cormorant', Georgia, serif"
    font-size="{WM_FONT_SIZE}"
    font-weight="300"
    letter-spacing="{WM_LETTER_SPACING_EM}em"
    fill="{text_color}"
    text-anchor="start"
  >{WM_TEXT}</text>
</svg>"""


def social_card_svg(font_b64: str) -> str:
    """Open Graph social preview card — 1200x630."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <style>{font_face(font_b64)}</style>
  </defs>

  <!-- Background: paper -->
  <rect width="1200" height="630" fill="{PAPER}"/>

  <!-- Page rectangle (centered, paper-bright) -->
  <rect x="380" y="80" width="440" height="470" fill="{PAPER_BRIGHT}"
        stroke="{INK_GHOST}" stroke-width="1"/>

  <!-- Margin line -->
  <line x1="420" y1="80" x2="420" y2="550" stroke="{PENCIL}" stroke-width="1" opacity="0.15"/>

  <!-- Wordmark -->
  <text x="600" y="340" text-anchor="middle"
        font-family="'Cormorant', Georgia, serif"
        font-size="96" font-weight="300" letter-spacing="-0.03em"
        fill="{INK}">Type</text>

  <!-- Tagline -->
  <text x="600" y="390" text-anchor="middle"
        font-family="'Cormorant', Georgia, serif"
        font-size="18" font-weight="300"
        fill="{INK_MUTED}">A long-form writing instrument</text>

  <!-- CustodyZero attribution -->
  <text x="600" y="590" text-anchor="middle"
        font-family="monospace"
        font-size="11" letter-spacing="0.1em"
        fill="{INK_GHOST}">CUSTODYZERO</text>
</svg>"""


def svg_to_png(svg_content: str, out_path: Path, width: int, height: int):
    cairosvg.svg2png(
        bytestring=svg_content.encode("utf-8"),
        write_to=str(out_path),
        output_width=width,
        output_height=height,
    )
    print(f"  {out_path.name} ({width}x{height})")


def svg_to_png_from_file(svg_path: Path, out_path: Path, width: int, height: int):
    cairosvg.svg2png(
        url=str(svg_path),
        write_to=str(out_path),
        output_width=width,
        output_height=height,
    )
    print(f"  {out_path.name} ({width}x{height})")


def svg_to_ico(svg_path: Path, out_path: Path, sizes: list[int]):
    max_size = max(sizes)
    png_bytes = cairosvg.svg2png(url=str(svg_path), output_width=max_size, output_height=max_size)
    img = Image.open(io.BytesIO(png_bytes)).convert("RGBA")
    img.save(str(out_path), format="ICO", sizes=[(s, s) for s in sizes])
    print(f"  {out_path.name} (ICO {sizes})")


def main():
    for d in [WORDMARK_DIR, ICON_DIR, SOCIAL_DIR]:
        d.mkdir(parents=True, exist_ok=True)

    if not FONT_PATH.exists():
        print(f"ERROR: Cormorant Light not found at {FONT_PATH}")
        print("Run: python3 scripts/install-cormorant.py")
        return

    font_b64 = load_font_b64()
    text_width = measure_text_width(WM_TEXT, WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    canvas_w = int(WM_X_START + text_width + 10)

    # --- Wordmark SVGs ---
    print("Generating wordmark SVGs...")

    light_svg = wordmark_svg(INK, font_b64, text_width)
    light_svg_path = WORDMARK_DIR / "type-wordmark-light.svg"
    light_svg_path.write_text(light_svg)
    print(f"  {light_svg_path.name} ({canvas_w}x{WM_CANVAS_H})")

    dark_svg = wordmark_svg(PAPER_BRIGHT, font_b64, text_width)
    dark_svg_path = WORDMARK_DIR / "type-wordmark-dark.svg"
    dark_svg_path.write_text(dark_svg)
    print(f"  {dark_svg_path.name} ({canvas_w}x{WM_CANVAS_H})")

    # --- Wordmark PNGs ---
    print("Rasterizing wordmark PNGs...")
    for variant, svg_content in [("light", light_svg), ("dark", dark_svg)]:
        svg_to_png(
            svg_content,
            WORDMARK_DIR / f"type-wordmark-{variant}@2x.png",
            canvas_w * 2, WM_CANVAS_H * 2,
        )
        svg_to_png(
            svg_content,
            WORDMARK_DIR / f"type-wordmark-{variant}@3x.png",
            canvas_w * 3, WM_CANVAS_H * 3,
        )

    # --- Icon PNGs ---
    print("Rasterizing icon PNGs...")
    for variant in ["light", "dark"]:
        svg_path = ICON_DIR / f"type-icon-{variant}.svg"
        svg_to_png_from_file(
            svg_path,
            ICON_DIR / f"type-icon-{variant}@2x.png",
            128, 128,
        )
        svg_to_png_from_file(
            svg_path,
            ICON_DIR / f"type-icon-{variant}@3x.png",
            192, 192,
        )

    # --- Icon ICO ---
    print("Generating ICO...")
    svg_to_ico(
        ICON_DIR / "type-icon-light.svg",
        ICON_DIR / "type-icon-light.ico",
        [16, 32, 48],
    )

    # --- Social card ---
    print("Generating social card...")
    social_svg_content = social_card_svg(font_b64)
    social_svg_path = SOCIAL_DIR / "type-social-card.svg"
    social_svg_path.write_text(social_svg_content)
    print(f"  {social_svg_path.name} (1200x630)")

    svg_to_png(
        social_svg_content,
        SOCIAL_DIR / "type-social-card.png",
        2400, 1260,
    )

    print("\nDone. All Type brand assets generated.")


if __name__ == "__main__":
    main()
