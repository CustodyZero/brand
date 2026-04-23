#!/usr/bin/env python3
"""
Generate Valet social card at 1200×630px.

Output: brand/valet/social/valet-social-card.{svg,png}

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue and DM Mono TTFs must be installed (run scripts/install-fonts.py first).

Grain is seeded (random.Random(42)) — output is fully deterministic given the
same fonts and input parameters.

Design follows Valet brand (locked April 2026):
  - Dark background (#0A0A0A)
  - Bronze accent (#9D7E49) — no amber, no blue, no purple
  - Bebas Neue wordmark, DM Mono secondary text
  - No Fraunces (house-only serif)
  - The Binding icon as structural accent (three bars, thickened center)
  - Geometric grid (architectural house constraint)
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
OUT_DIR = BASE / "brand" / "valet" / "social"

FONT_BEBAS = FONT_DIR / "BebasNeue-Regular.ttf"
FONT_DMMONO = FONT_DIR / "DMMono-Regular.ttf"

# ---------------------------------------------------------------------------
# Card geometry
# ---------------------------------------------------------------------------

W, H = 1200, 630

WM_FONT_SIZE = 110.0
WM_LS_EM = 0.12
WM_Y_BASELINE = 305.0

RULE_OFFSET_Y = 26

TL_FONT_SIZE = 16.0
TL_Y_BASELINE = 385.0

URL_FONT_SIZE = 13.0
URL_Y_BASELINE = 420.0

GLOW_CX_FRAC = 0.5
GLOW_CY_FRAC = 0.46
GLOW_R_FRAC = 0.45

GRID_STEP = 80
GRID_COLOR = "#242424"
GRID_OPACITY = 0.30

GRAIN_OPACITY = 0.035
GRAIN_SEED = 42

# ---------------------------------------------------------------------------
# Valet content
# ---------------------------------------------------------------------------

PRODUCT_WM = "VALET"
TAGLINE = "A lifelong attendant on your hardware."
URL_TEXT = "valet.custodyzero.com"

# ---------------------------------------------------------------------------
# Colors (Valet palette)
# ---------------------------------------------------------------------------

BG = "#0A0A0A"
WHITE = "#F2F2EC"
BRONZE = "#9D7E49"
TEXT_SECONDARY = "#C8C8C0"
TEXT_MUTED = "#444444"

# ---------------------------------------------------------------------------
# Font install helpers (for DM Mono)
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


# ---------------------------------------------------------------------------
# Font metrics
# ---------------------------------------------------------------------------

def _load_cmap_hmtx(path: Path):
    tt = TTFont(str(path))
    return tt.getBestCmap(), tt["hmtx"].metrics, tt["head"].unitsPerEm


def measure_width(text: str, font_path: Path, font_size: float, ls_em: float) -> float:
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


# ---------------------------------------------------------------------------
# Font embedding
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
    wm_total_w = measure_width(PRODUCT_WM, FONT_BEBAS, WM_FONT_SIZE, WM_LS_EM)
    wm_x = (W - wm_total_w) / 2.0

    rule_y = WM_Y_BASELINE + RULE_OFFSET_Y
    rule_x1 = wm_x
    rule_x2 = wm_x + wm_total_w

    tl_w = measure_width(TAGLINE, FONT_DMMONO, TL_FONT_SIZE, 0.0)
    tl_x = (W - tl_w) / 2.0

    url_w = measure_width(URL_TEXT, FONT_DMMONO, URL_FONT_SIZE, 0.0)
    url_x = (W - url_w) / 2.0

    glow_cx = W * GLOW_CX_FRAC
    glow_cy = H * GLOW_CY_FRAC
    glow_r = W * GLOW_R_FRAC

    # The Binding icon — scaled and positioned top-left
    # Source viewBox 64×64 with bars at y=20, 32, 44 and x-ranges 22-42, 14-50, 22-42
    bind_scale = 0.75
    bind_x = 40
    bind_y = 40
    bind_stroke_outer = 2.5 * bind_scale
    bind_stroke_center = 3.5 * bind_scale

    # Bar endpoints (scaled)
    b_top_x1    = bind_x + 22 * bind_scale
    b_top_x2    = bind_x + 42 * bind_scale
    b_top_y     = bind_y + 20 * bind_scale
    b_center_x1 = bind_x + 14 * bind_scale
    b_center_x2 = bind_x + 50 * bind_scale
    b_center_y  = bind_y + 32 * bind_scale
    b_bot_x1    = bind_x + 22 * bind_scale
    b_bot_x2    = bind_x + 42 * bind_scale
    b_bot_y     = bind_y + 44 * bind_scale

    styles = "\n".join([
        _font_face("Bebas Neue", FONT_BEBAS, "normal", "400"),
        _font_face("DM Mono", FONT_DMMONO, "normal", "400"),
    ])

    # Grid
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

    <!-- Bronze radial glow -->
    <radialGradient id="bronzeGlow" cx="{glow_cx:.1f}" cy="{glow_cy:.1f}" r="{glow_r:.1f}"
                    fx="{glow_cx:.1f}" fy="{glow_cy:.1f}" gradientUnits="userSpaceOnUse">
      <stop offset="0%"   stop-color="{BRONZE}" stop-opacity="0.06"/>
      <stop offset="60%"  stop-color="{BRONZE}" stop-opacity="0.02"/>
      <stop offset="100%" stop-color="{BRONZE}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- 1. Solid background -->
  <rect width="{W}" height="{H}" fill="{BG}"/>

  <!-- 2. Geometric grid -->
  <path d="{grid_d}"
        fill="none" stroke="{GRID_COLOR}" stroke-width="1" opacity="{GRID_OPACITY}"/>

  <!-- 3. Bronze ambient glow -->
  <rect width="{W}" height="{H}" fill="url(#bronzeGlow)"/>

  <!-- 4. The Binding icon — top left -->
  <line x1="{b_top_x1:.1f}" y1="{b_top_y:.1f}" x2="{b_top_x2:.1f}" y2="{b_top_y:.1f}"
        stroke="{BRONZE}" stroke-width="{bind_stroke_outer}" stroke-linecap="square"/>
  <line x1="{b_center_x1:.1f}" y1="{b_center_y:.1f}" x2="{b_center_x2:.1f}" y2="{b_center_y:.1f}"
        stroke="{BRONZE}" stroke-width="{bind_stroke_center}" stroke-linecap="square"/>
  <line x1="{b_bot_x1:.1f}" y1="{b_bot_y:.1f}" x2="{b_bot_x2:.1f}" y2="{b_bot_y:.1f}"
        stroke="{BRONZE}" stroke-width="{bind_stroke_outer}" stroke-linecap="square"/>

  <!-- 5. Wordmark: white on dark -->
  <text x="{wm_x:.2f}" y="{WM_Y_BASELINE}"
        font-family="'Bebas Neue', sans-serif"
        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LS_EM}em"
        fill="{WHITE}">{PRODUCT_WM}</text>

  <!-- 6. Bronze horizontal rule -->
  <line x1="{rule_x1:.2f}" y1="{rule_y}" x2="{rule_x2:.2f}" y2="{rule_y}"
        stroke="{BRONZE}" stroke-width="2"/>

  <!-- 7. Tagline -->
  <text x="{tl_x:.2f}" y="{TL_Y_BASELINE}"
        font-family="'DM Mono', 'Courier New', monospace"
        font-size="{TL_FONT_SIZE}" fill="{TEXT_SECONDARY}"
        letter-spacing="0.02em">{TAGLINE}</text>

  <!-- 8. URL -->
  <text x="{url_x:.2f}" y="{URL_Y_BASELINE}"
        font-family="'DM Mono', 'Courier New', monospace"
        font-size="{URL_FONT_SIZE}" fill="{TEXT_MUTED}"
        letter-spacing="0.05em">{URL_TEXT}</text>
</svg>
"""
    return svg


# ---------------------------------------------------------------------------
# Grain overlay (seeded random — deterministic)
# ---------------------------------------------------------------------------

def add_grain(img: Image.Image, opacity: float = GRAIN_OPACITY, seed: int = GRAIN_SEED) -> Image.Image:
    w, h = img.size
    rng = random.Random(seed)
    noise_bytes = rng.randbytes(w * h)
    noise = Image.frombytes("L", (w, h), noise_bytes)
    alpha_val = int(255 * opacity)
    alpha_mask = Image.new("L", (w, h), alpha_val)
    grain_rgba = Image.merge("RGBA", [noise, noise, noise, alpha_mask])
    result = img.convert("RGBA")
    result = Image.alpha_composite(result, grain_rgba)
    return result.convert("RGB")


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

    print("Measuring text positions…")
    svg = build_svg()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    svg_path = OUT_DIR / "valet-social-card.svg"
    svg_path.write_text(svg, encoding="utf-8")
    print(f"  SVG: {svg_path.relative_to(BASE)}")

    SCALE = 2
    out_w, out_h = W * SCALE, H * SCALE

    print(f"Rasterizing to PNG at {SCALE}x ({out_w}×{out_h})…")
    png_bytes = cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        output_width=out_w,
        output_height=out_h,
    )
    img = Image.open(io.BytesIO(png_bytes))

    # Grain skipped at 2x — same rationale as Factory social generator.
    out_png = OUT_DIR / "valet-social-card.png"
    img.save(str(out_png), format="PNG", optimize=True)
    size_kb = out_png.stat().st_size / 1024
    print(f"  PNG: {out_png.relative_to(BASE)} ({out_w}×{out_h}, {size_kb:.0f}KB)")

    print("\nDone.")


if __name__ == "__main__":
    main()
