#!/usr/bin/env python3
"""
Generate StationZero brand assets: wordmarks (SVG + PNG 2x/3x) and icon mark (SVG + ICO + PNG).

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue TTF must be installed — run scripts/install-fonts.py first.

Usage:
  python3 scripts/generate-stationzero.py
"""

import base64
import os
import struct
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont

BASE = Path(__file__).parent.parent
WORDMARK_DIR = BASE / "brand" / "stationzero" / "wordmark"
ICON_DIR = BASE / "brand" / "stationzero" / "icon"

FONT_PATH = Path.home() / "Library" / "Fonts" / "BebasNeue-Regular.ttf"

SIGNAL_RED = "#C04848"
SIGNAL_RED_DIM = "#7A2E2E"
WHITE = "#F2F2EC"

# Wordmark layout constants
# Canvas height matches CustodyZero house standard (80px)
WM_CANVAS_H = 80
WM_FONT_SIZE = 83.7  # Same as CustodyZero — calibrated for Bebas Neue at 80px canvas
WM_LETTER_SPACING_EM = 0.15  # House standard
WM_X_START = 3.0
WM_Y_BASELINE = 69.5  # Same as CustodyZero


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

    spacing_px = letter_spacing_em * font_size
    return sum(advances) + (len(text) - 1) * spacing_px


def measure_split_x(prefix: str, font_size: float, letter_spacing_em: float) -> float:
    """
    Compute the x-position where the color split occurs: the advance width
    of the prefix text including its trailing letter-spacing (since a character
    follows). This is the boundary between STATION and ZERO.
    """
    tt = TTFont(str(FONT_PATH))
    cmap = tt.getBestCmap()
    hmtx = tt["hmtx"].metrics
    upm = tt["head"].unitsPerEm

    advances = []
    for char in prefix:
        gid = cmap.get(ord(char))
        if gid is None:
            raise ValueError(f"Glyph not found for character '{char}' (U+{ord(char):04X})")
        adv, _ = hmtx[gid]
        advances.append(adv / upm * font_size)

    spacing_px = letter_spacing_em * font_size
    # Include trailing spacing because ZERO follows immediately
    return sum(advances) + len(prefix) * spacing_px


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


def wordmark_svg(font_b64: str, full_width: float, split_x: float, canvas_w: int) -> str:
    """
    Generate the StationZero wordmark SVG.

    Uses the CustodyZero clipPath technique: two identical text elements
    rendered at the same position, clipped at the split boundary.
    Left clip shows STATION in --white, right clip shows ZERO in Signal Red.
    """
    # Nudge split 2px left into the N–Z letter-spacing gap to compensate
    # for sub-pixel rounding differences between fontTools metrics and
    # browser SVG text layout. The gap is ~12.5px so this is invisible.
    split_abs = WM_X_START + split_x - 2.0
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"'
        f' viewBox="0 0 {canvas_w} {WM_CANVAS_H}"'
        f' width="{canvas_w}" height="{WM_CANVAS_H}">\n'
        f"  <defs>\n"
        f"    <style>{font_face(font_b64)}</style>\n"
        f'    <clipPath id="a"><rect x="0" y="0" width="{split_abs:.2f}" height="{WM_CANVAS_H}"/></clipPath>\n'
        f'    <clipPath id="b"><rect x="{split_abs:.2f}" y="0" width="{canvas_w}" height="{WM_CANVAS_H}"/></clipPath>\n'
        f"  </defs>\n"
        f'  <text x="{WM_X_START}" y="{WM_Y_BASELINE}" text-anchor="start"\n'
        f"        font-family=\"'Bebas Neue', sans-serif\"\n"
        f'        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LETTER_SPACING_EM}em"\n'
        f'        fill="{WHITE}" clip-path="url(#a)">STATIONZERO</text>\n'
        f'  <text x="{WM_X_START}" y="{WM_Y_BASELINE}" text-anchor="start"\n'
        f"        font-family=\"'Bebas Neue', sans-serif\"\n"
        f'        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LETTER_SPACING_EM}em"\n'
        f'        fill="{SIGNAL_RED}" clip-path="url(#b)">STATIONZERO</text>\n'
        f"</svg>\n"
    )


def wordmark_red_svg(font_b64: str, full_width: float, canvas_w: int) -> str:
    """
    Generate a single-color Signal Red variant for light backgrounds
    (if ever needed — not primary, but following the Archon/Factory pattern
    of providing an accent-color variant).
    """
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg"'
        f' viewBox="0 0 {canvas_w} {WM_CANVAS_H}"'
        f' width="{canvas_w}" height="{WM_CANVAS_H}">\n'
        f"  <defs>\n"
        f"    <style>{font_face(font_b64)}</style>\n"
        f"  </defs>\n"
        f'  <text x="{WM_X_START}" y="{WM_Y_BASELINE}" text-anchor="start"\n'
        f"        font-family=\"'Bebas Neue', sans-serif\"\n"
        f'        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LETTER_SPACING_EM}em"\n'
        f'        fill="{SIGNAL_RED}">STATIONZERO</text>\n'
        f"</svg>\n"
    )


def icon_svg() -> str:
    """
    Generate the StationZero icon mark SVG.

    Design: a squared-off slashed zero — the "Zero" in StationZero rendered as
    a geometric mark. No curves, no border-radius. The slash runs corner-to-corner
    of the interior void, anchored to the frame walls.

    Construction:
      Outer rect: x=12 y=6 w=40 h=52, stroke-width=5 (center-stroked)
      Inner void corners: bottom-left (14.5, 55.5), top-right (49.5, 8.5)
      Slash: 80% of corner-to-corner diagonal, same angle, centered.
             Pulled inward from both ends for breathing room.
             Endpoints: (18.0, 50.8) → (46.0, 13.2)
             stroke-width=3 — lighter than frame to create hierarchy

    No surveillance camera, eye, or lens imagery. Typographic, not illustrative.

    Legibility check:
      64×64 (1:1): frame 5px, slash 3px — clear slashed zero
      32×32 (1/2): frame ~2.5px, slash ~1.5px — legible
      16×16 (1/4): frame ~1.25px, slash ~0.75px — distinct slashed rectangle
    """
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">\n'
        '  <!-- StationZero icon: squared slashed zero -->\n'
        '  <!-- Frame: the zero glyph, squared off -->\n'
        '  <rect x="12" y="6" width="40" height="52"\n'
        '        fill="none" stroke="#C04848" stroke-width="5"/>\n'
        '  <!-- Slash: 80% of corner diagonal, centered, same angle -->\n'
        '  <line x1="18.0" y1="50.8" x2="46.0" y2="13.2"\n'
        '        stroke="#C04848" stroke-width="3" stroke-linecap="square"/>\n'
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
    """
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

    print("Measuring text widths…")
    full_width = measure_text_width("STATIONZERO", WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    split_x = measure_split_x("STATION", WM_FONT_SIZE, WM_LETTER_SPACING_EM)
    print(f"  'STATIONZERO' at {WM_FONT_SIZE}px, {WM_LETTER_SPACING_EM}em spacing → {full_width:.2f}px")
    print(f"  Split point (after STATION): {split_x:.2f}px from x_start")

    # Canvas width: text width + start padding + end padding
    canvas_w = int(full_width + WM_X_START * 2 + 0.5)
    print(f"  Canvas: {canvas_w} × {WM_CANVAS_H}")

    # --- Wordmarks ---
    print("\nGenerating wordmark SVGs…")

    wm_dark = wordmark_svg(font_b64, full_width, split_x, canvas_w)
    wm_dark_path = WORDMARK_DIR / "stationzero-wordmark-dark.svg"
    wm_dark_path.write_text(wm_dark)
    print(f"  {wm_dark_path.relative_to(BASE)}")

    wm_red = wordmark_red_svg(font_b64, full_width, canvas_w)
    wm_red_path = WORDMARK_DIR / "stationzero-wordmark-red.svg"
    wm_red_path.write_text(wm_red)
    print(f"  {wm_red_path.relative_to(BASE)}")

    print("\nRasterizing wordmarks…")
    for variant, svg_content in [("dark", wm_dark), ("red", wm_red)]:
        for scale in [2, 3]:
            out = WORDMARK_DIR / f"stationzero-wordmark-{variant}@{scale}x.png"
            svg_to_png(svg_content, out, canvas_w * scale, WM_CANVAS_H * scale)

    # --- Icon mark ---
    print("\nGenerating icon mark…")
    icon = icon_svg()

    icon_path = ICON_DIR / "stationzero-icon-dark.svg"
    icon_path.write_text(icon)
    print(f"  {icon_path.relative_to(BASE)}")

    print("\nRasterizing icon…")
    for scale in [2, 3]:
        out = ICON_DIR / f"stationzero-icon-dark@{scale}x.png"
        svg_to_png(icon, out, 64 * scale, 64 * scale)

    print("\nGenerating ICO…")
    ico_path = ICON_DIR / "stationzero-icon-dark.ico"
    svg_to_ico(icon, ico_path, [16, 32, 48])

    print("\nDone.")


if __name__ == "__main__":
    main()
