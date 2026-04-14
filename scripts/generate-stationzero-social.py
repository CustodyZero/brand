#!/usr/bin/env python3
"""
Generate StationZero social card at 1200×630px.

Output: brand/stationzero/social/stationzero-social-card.{svg,png}

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue and DM Mono TTFs must be installed (run scripts/install-fonts.py first).
  Zilla Slab will be auto-installed from Google Fonts if missing.

Design follows StationZero brand guidelines:
  - Dark background only (#0A0A0A)
  - Signal Red accent (#C04848) — no amber, no blue, no green, no purple
  - Split-color wordmark: STATION (white) + ZERO (Signal Red)
  - Zilla Slab for tagline (voice serif)
  - DM Mono for URL (system font)
  - Squared slashed zero icon mark as structural accent
  - Geometric grid (house architectural constraint theme)
  - Signal Red ambient glow (subtle)
"""

import base64
import io
import random
import re
import urllib.request
from pathlib import Path

import cairosvg
from fontTools.ttLib import TTFont
from PIL import Image

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

BASE = Path(__file__).parent.parent
FONT_DIR = Path.home() / "Library" / "Fonts"
OUT_DIR = BASE / "brand" / "stationzero" / "social"

FONT_BEBAS = FONT_DIR / "BebasNeue-Regular.ttf"
FONT_DMMONO = FONT_DIR / "DMMono-Regular.ttf"
FONT_ZILLA = FONT_DIR / "ZillaSlab-Regular.ttf"

# ---------------------------------------------------------------------------
# Card geometry
# ---------------------------------------------------------------------------

W, H = 1200, 630

# Wordmark
WM_FONT_SIZE = 83.7
WM_LS_EM = 0.15          # CustodyZero house standard
WM_Y_BASELINE = 310.0

# Signal Red rule: 2px, full wordmark width, 22px below baseline
RULE_OFFSET_Y = 22

# Tagline (Zilla Slab — voice serif)
TL_FONT_SIZE = 22.0
TL_Y_BASELINE = 385.0

# URL (DM Mono — system font)
URL_FONT_SIZE = 13.0
URL_Y_BASELINE = 420.0

# Glow
GLOW_CX_FRAC = 0.5
GLOW_CY_FRAC = 0.46
GLOW_R_FRAC = 0.45

# Grid
GRID_STEP = 80
GRID_COLOR = "#242424"
GRID_OPACITY = 0.30

# ---------------------------------------------------------------------------
# Colors (StationZero palette — no amber, no blue, no green)
# ---------------------------------------------------------------------------

BG = "#0A0A0A"
WHITE = "#F2F2EC"
SIGNAL_RED = "#C04848"
TEXT_SECONDARY = "#C8C8C0"
TEXT_MUTED = "#444444"

# ---------------------------------------------------------------------------
# Font installation helpers
# ---------------------------------------------------------------------------

_GF_UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def _fetch_gf_css(family_query: str) -> str:
    url = f"https://fonts.googleapis.com/css2?{family_query}&display=swap"
    req = urllib.request.Request(url, headers={"User-Agent": _GF_UA})
    with urllib.request.urlopen(req) as r:
        return r.read().decode("utf-8")


def _woff2_url_from_css(css: str, hint: str = "") -> str:
    matches = re.findall(r"url\(([^)]+\.woff2)\)", css)
    if hint:
        for m in matches:
            if hint.lower() in m.lower():
                return m
    if matches:
        return matches[0]
    raise RuntimeError(f"No woff2 URL found in CSS\n{css[:400]}")


def _download_ttf(woff2_url: str, dest: Path) -> None:
    tmp = Path("/tmp") / (dest.stem + ".woff2")
    print(f"    Downloading {woff2_url}")
    urllib.request.urlretrieve(woff2_url, tmp)
    font = TTFont(str(tmp))
    font.flavor = None
    font.save(str(dest))
    tmp.unlink(missing_ok=True)
    print(f"    Installed → {dest}")


def ensure_dmmono() -> None:
    if FONT_DMMONO.exists():
        return
    print("  Installing DM Mono Regular…")
    css = _fetch_gf_css("family=DM+Mono:wght@400")
    url = _woff2_url_from_css(css)
    _download_ttf(url, FONT_DMMONO)


def ensure_zilla_slab() -> None:
    if FONT_ZILLA.exists():
        return
    print("  Installing Zilla Slab Regular…")
    css = _fetch_gf_css("family=Zilla+Slab:wght@400")
    url = _woff2_url_from_css(css)
    _download_ttf(url, FONT_ZILLA)


# ---------------------------------------------------------------------------
# Font metrics
# ---------------------------------------------------------------------------

def _load_cmap_hmtx(path: Path):
    tt = TTFont(str(path))
    return tt.getBestCmap(), tt["hmtx"].metrics, tt["head"].unitsPerEm


def measure_width(text: str, font_path: Path, font_size: float, ls_em: float) -> float:
    """Visual ink width (no trailing letter-spacing gap)."""
    cmap, hmtx, upm = _load_cmap_hmtx(font_path)
    advances = []
    for ch in text:
        gid = cmap.get(ord(ch))
        if gid is None:
            raise ValueError(f"Glyph missing for '{ch}' in {font_path.name}")
        adv, _ = hmtx[gid]
        advances.append(adv / upm * font_size)
    ls_px = ls_em * font_size
    return sum(advances) + (len(text) - 1) * ls_px


def measure_split_x(prefix: str, font_path: Path, font_size: float, ls_em: float) -> float:
    """Measure the advance width of a prefix (including trailing letter-spacing)."""
    cmap, hmtx, upm = _load_cmap_hmtx(font_path)
    ls_px = ls_em * font_size
    total = 0.0
    for ch in prefix:
        gid = cmap.get(ord(ch))
        adv, _ = hmtx[gid]
        total += adv / upm * font_size + ls_px
    return total


# ---------------------------------------------------------------------------
# Font base64 embedding
# ---------------------------------------------------------------------------

def _b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


def _font_face(family: str, path: Path, style: str = "normal", weight: str = "400") -> str:
    b64 = _b64(path)
    return (
        f"@font-face {{\n"
        f"  font-family: '{family}';\n"
        f"  font-style: {style};\n"
        f"  font-weight: {weight};\n"
        f'  src: url("data:font/truetype;base64,{b64}") format("truetype");\n'
        f"}}"
    )


# ---------------------------------------------------------------------------
# SVG builder
# ---------------------------------------------------------------------------

def build_svg() -> str:
    # --- measure wordmark ---
    wm_text = "STATIONZERO"
    wm_total_w = measure_width(wm_text, FONT_BEBAS, WM_FONT_SIZE, WM_LS_EM)
    wm_x = (W - wm_total_w) / 2.0

    # --- color split: STATION (white) / ZERO (red) ---
    split_offset = measure_split_x("STATION", FONT_BEBAS, WM_FONT_SIZE, WM_LS_EM)
    # Nudge 2px left into N–Z gap for sub-pixel rounding compensation
    split_abs = wm_x + split_offset - 2.0

    # --- Signal Red rule: full wordmark width, centered ---
    rule_y = WM_Y_BASELINE + RULE_OFFSET_Y
    rule_x1 = wm_x
    rule_x2 = wm_x + wm_total_w

    # --- tagline: Zilla Slab, centered ---
    tl_text = "Your home. Your cameras. Your data. No cloud."
    tl_w = measure_width(tl_text, FONT_ZILLA, TL_FONT_SIZE, 0.0)
    tl_x = (W - tl_w) / 2.0

    # --- url: DM Mono, centered ---
    url_text = "github.com/CustodyZero/stationzero"
    url_w = measure_width(url_text, FONT_DMMONO, URL_FONT_SIZE, 0.0)
    url_x = (W - url_w) / 2.0

    # --- glow centre (Signal Red, not amber) ---
    glow_cx = W * GLOW_CX_FRAC
    glow_cy = H * GLOW_CY_FRAC
    glow_r = W * GLOW_R_FRAC

    # --- Icon mark: squared slashed zero, positioned top-left ---
    # Original: 64x64 canvas, rect(12,6,40,52), slash(18.0,50.8 → 46.0,13.2)
    # Scale to ~48px mark (0.75x), positioned at top-left with clearspace
    icon_scale = 0.75
    icon_x = 40
    icon_y = 40
    # Frame
    f_x = icon_x + 12 * icon_scale
    f_y = icon_y + 6 * icon_scale
    f_w = 40 * icon_scale
    f_h = 52 * icon_scale
    f_stroke = 5 * icon_scale
    # Slash
    s_x1 = icon_x + 18.0 * icon_scale
    s_y1 = icon_y + 50.8 * icon_scale
    s_x2 = icon_x + 46.0 * icon_scale
    s_y2 = icon_y + 13.2 * icon_scale
    s_stroke = 3 * icon_scale

    # --- font face declarations ---
    styles = "\n".join([
        _font_face("Bebas Neue", FONT_BEBAS, "normal", "400"),
        _font_face("DM Mono", FONT_DMMONO, "normal", "400"),
        _font_face("Zilla Slab", FONT_ZILLA, "normal", "400"),
    ])

    # --- grid path ---
    grid_lines = []
    x = 0
    while x <= W:
        grid_lines.append(f"M {x} 0 L {x} {H}")
        x += GRID_STEP
    y = 0
    while y <= H:
        grid_lines.append(f"M 0 {y} L {W} {y}")
        y += GRID_STEP
    grid_d = " ".join(grid_lines)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <style>{styles}</style>

    <!-- Signal Red radial glow -->
    <radialGradient id="redGlow" cx="{glow_cx:.1f}" cy="{glow_cy:.1f}" r="{glow_r:.1f}"
                    fx="{glow_cx:.1f}" fy="{glow_cy:.1f}" gradientUnits="userSpaceOnUse">
      <stop offset="0%"   stop-color="{SIGNAL_RED}" stop-opacity="0.06"/>
      <stop offset="60%"  stop-color="{SIGNAL_RED}" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="{SIGNAL_RED}" stop-opacity="0"/>
    </radialGradient>

    <!-- Wordmark color split clipPaths -->
    <clipPath id="clipWhite">
      <rect x="0" y="0" width="{split_abs:.2f}" height="{H}"/>
    </clipPath>
    <clipPath id="clipRed">
      <rect x="{split_abs:.2f}" y="0" width="{W}" height="{H}"/>
    </clipPath>
  </defs>

  <!-- 1. Solid background -->
  <rect width="{W}" height="{H}" fill="{BG}"/>

  <!-- 2. Geometric grid lines -->
  <path d="{grid_d}"
        fill="none" stroke="{GRID_COLOR}" stroke-width="1" opacity="{GRID_OPACITY}"/>

  <!-- 3. Signal Red ambient glow -->
  <rect width="{W}" height="{H}" fill="url(#redGlow)"/>

  <!-- 4. Icon mark: squared slashed zero — top left -->
  <rect x="{f_x:.1f}" y="{f_y:.1f}" width="{f_w:.1f}" height="{f_h:.1f}"
        fill="none" stroke="{SIGNAL_RED}" stroke-width="{f_stroke:.2f}"/>
  <line x1="{s_x1:.1f}" y1="{s_y1:.1f}" x2="{s_x2:.1f}" y2="{s_y2:.1f}"
        stroke="{SIGNAL_RED}" stroke-width="{s_stroke:.2f}" stroke-linecap="square"/>

  <!-- 5. Wordmark: split-color STATION (white) + ZERO (Signal Red) -->
  <text x="{wm_x:.2f}" y="{WM_Y_BASELINE}"
        font-family="'Bebas Neue', sans-serif"
        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LS_EM}em"
        fill="{WHITE}" clip-path="url(#clipWhite)">STATIONZERO</text>
  <text x="{wm_x:.2f}" y="{WM_Y_BASELINE}"
        font-family="'Bebas Neue', sans-serif"
        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LS_EM}em"
        fill="{SIGNAL_RED}" clip-path="url(#clipRed)">STATIONZERO</text>

  <!-- 6. Signal Red horizontal rule -->
  <line x1="{rule_x1:.2f}" y1="{rule_y}" x2="{rule_x2:.2f}" y2="{rule_y}"
        stroke="{SIGNAL_RED}" stroke-width="2"/>

  <!-- 7. Tagline (Zilla Slab — voice serif) -->
  <text x="{tl_x:.2f}" y="{TL_Y_BASELINE}"
        font-family="'Zilla Slab', serif"
        font-size="{TL_FONT_SIZE}" fill="{TEXT_SECONDARY}"
        letter-spacing="0.02em">{tl_text}</text>

  <!-- 8. URL -->
  <text x="{url_x:.2f}" y="{URL_Y_BASELINE}"
        font-family="'DM Mono', 'Courier New', monospace"
        font-size="{URL_FONT_SIZE}" fill="{TEXT_MUTED}"
        letter-spacing="0.05em">{url_text}</text>
</svg>
"""
    return svg


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not FONT_BEBAS.exists():
        raise FileNotFoundError(
            f"Bebas Neue not found at {FONT_BEBAS}. Run scripts/install-fonts.py first."
        )

    print("Ensuring required fonts are installed…")
    ensure_dmmono()
    ensure_zilla_slab()

    print("Measuring text positions…")
    svg = build_svg()

    # Write SVG
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    svg_path = OUT_DIR / "stationzero-social-card.svg"
    svg_path.write_text(svg, encoding="utf-8")
    print(f"  SVG: {svg_path.relative_to(BASE)}")

    # Rasterize at 2x for retina/HiDPI (LinkedIn, Twitter, etc.)
    SCALE = 2
    out_w, out_h = W * SCALE, H * SCALE

    print(f"Rasterizing to PNG at {SCALE}x ({out_w}×{out_h})…")
    png_bytes = cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        output_width=out_w,
        output_height=out_h,
    )
    img = Image.open(io.BytesIO(png_bytes))

    out_png = OUT_DIR / "stationzero-social-card.png"
    img.save(str(out_png), format="PNG", optimize=True)
    size_kb = out_png.stat().st_size / 1024
    print(f"  PNG: {out_png.relative_to(BASE)} ({out_w}×{out_h}, {size_kb:.0f}KB)")

    print("\nDone.")


if __name__ == "__main__":
    main()
