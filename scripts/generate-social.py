#!/usr/bin/env python3
"""
Generate CustodyZero social card at 1200×630px.

Output: brand/custodyzero/social/custodyzero-social-card.png

Prerequisites:
  pip install cairosvg Pillow fonttools brotli
  Bebas Neue TTF must already be installed (run scripts/install-fonts.py first).
  This script auto-installs Fraunces and DM Mono from Google Fonts if absent.

Grain is seeded (random.Random(42)) — output is fully deterministic given the
same fonts and input parameters.
"""

import base64
import io
import random
import re
import struct
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
OUT_DIR = BASE / "brand" / "custodyzero" / "social"
OUT_PATH = OUT_DIR / "custodyzero-social-card.png"

FONT_BEBAS = FONT_DIR / "BebasNeue-Regular.ttf"
FONT_FRAUNCES = FONT_DIR / "Fraunces-LightItalic.ttf"
FONT_DMMONO = FONT_DIR / "DMMono-Regular.ttf"

# ---------------------------------------------------------------------------
# Card geometry
# ---------------------------------------------------------------------------

W, H = 1200, 630

# Wordmark
WM_FONT_SIZE = 110.0
WM_LS_EM = 0.15          # matching the house standard
WM_Y_BASELINE = 305.0

# Derived from WM_Y_BASELINE at build time (see build_svg)
# Amber rule: 2px, full wordmark width, sits 26px below baseline
RULE_OFFSET_Y = 26        # from wordmark baseline

# Tagline
TL_FONT_SIZE = 26.0
TL_Y_BASELINE = 385.0     # WM_Y_BASELINE + rule_h + gaps + cap_height

# URL
URL_FONT_SIZE = 13.0
URL_Y_BASELINE = 420.0

# Glow
GLOW_CX_FRAC = 0.5        # fraction of canvas width
GLOW_CY_FRAC = 0.46       # fraction of canvas height (slightly above centre)
GLOW_R_FRAC = 0.45        # radial gradient radius as fraction of canvas width

# Grid
GRID_STEP = 80
GRID_COLOR = "#242424"
GRID_OPACITY = 0.30

# Grain
GRAIN_OPACITY = 0.035     # 3.5% — subtle
GRAIN_SEED = 42

# ---------------------------------------------------------------------------
# Colors (verbatim from design system)
# ---------------------------------------------------------------------------

BG = "#0A0A0A"
WHITE = "#F2F2EC"
AMBER = "#D4880A"
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
    """Return the first woff2 URL in css that contains hint (case-insensitive)."""
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


def ensure_fraunces() -> None:
    if FONT_FRAUNCES.exists():
        return
    print("  Installing Fraunces Light Italic…")
    # Request: italic (ital=1), opsz=36 (display range), wght=300
    css = _fetch_gf_css("family=Fraunces:ital,opsz,wght@1,9..144,300")
    url = _woff2_url_from_css(css)
    _download_ttf(url, FONT_FRAUNCES)


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


def x_after(text: str, font_path: Path, font_size: float, ls_em: float) -> float:
    """Advance width INCLUDING trailing letter-spacing (start-x for next char)."""
    cmap, hmtx, upm = _load_cmap_hmtx(font_path)
    ls_px = ls_em * font_size
    total = 0.0
    for ch in text:
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
    wm_full = "CUSTODYZERO"
    wm_prefix = "CUSTODY"  # white portion

    wm_total_w = measure_width(wm_full, FONT_BEBAS, WM_FONT_SIZE, WM_LS_EM)
    wm_x = (W - wm_total_w) / 2.0

    # x position where "ZERO" starts (after "CUSTODY" + its trailing ls gap)
    zero_x = wm_x + x_after(wm_prefix, FONT_BEBAS, WM_FONT_SIZE, WM_LS_EM)

    # --- amber rule: full wordmark width, centered ---
    rule_y = WM_Y_BASELINE + RULE_OFFSET_Y
    rule_x1 = wm_x
    rule_x2 = wm_x + wm_total_w

    # --- tagline: centered ---
    tl_text = "The capability is yours."
    tl_w = measure_width(tl_text, FONT_FRAUNCES, TL_FONT_SIZE, 0.0)
    tl_x = (W - tl_w) / 2.0

    # --- url: centered ---
    url_text = "custodyzero.com"
    url_w = measure_width(url_text, FONT_DMMONO, URL_FONT_SIZE, 0.0)
    url_x = (W - url_w) / 2.0

    # --- glow centre ---
    glow_cx = W * GLOW_CX_FRAC
    glow_cy = H * GLOW_CY_FRAC
    glow_r = W * GLOW_R_FRAC

    # --- font face declarations ---
    styles = "\n".join([
        _font_face("Bebas Neue", FONT_BEBAS, "normal", "400"),
        _font_face("Fraunces", FONT_FRAUNCES, "italic", "300"),
        _font_face("DM Mono", FONT_DMMONO, "normal", "400"),
    ])

    # --- grid path: build horizontal + vertical lines ---
    grid_lines = []
    # vertical
    x = 0
    while x <= W:
        grid_lines.append(f"M {x} 0 L {x} {H}")
        x += GRID_STEP
    # horizontal
    y = 0
    while y <= H:
        grid_lines.append(f"M 0 {y} L {W} {y}")
        y += GRID_STEP
    grid_d = " ".join(grid_lines)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <style>{styles}</style>

    <!-- Amber radial glow -->
    <radialGradient id="amberGlow" cx="{glow_cx:.1f}" cy="{glow_cy:.1f}" r="{glow_r:.1f}"
                    fx="{glow_cx:.1f}" fy="{glow_cy:.1f}" gradientUnits="userSpaceOnUse">
      <stop offset="0%"   stop-color="#D4880A" stop-opacity="0.08"/>
      <stop offset="60%"  stop-color="#D4880A" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="#D4880A" stop-opacity="0"/>
    </radialGradient>

    <!-- White clip: covers left portion of wordmark up to where ZERO starts -->
    <clipPath id="clipWhite">
      <rect x="0" y="0" width="{zero_x:.2f}" height="{H}"/>
    </clipPath>

    <!-- Amber clip: covers right portion of wordmark from ZERO onwards -->
    <clipPath id="clipAmber">
      <rect x="{zero_x:.2f}" y="0" width="{W}" height="{H}"/>
    </clipPath>
  </defs>

  <!-- 1. Solid background -->
  <rect width="{W}" height="{H}" fill="{BG}"/>

  <!-- 2. Geometric grid lines -->
  <path d="{grid_d}"
        fill="none" stroke="{GRID_COLOR}" stroke-width="1" opacity="{GRID_OPACITY}"/>

  <!-- 3. Amber ambient glow -->
  <rect width="{W}" height="{H}" fill="url(#amberGlow)"/>

  <!-- 4. Wordmark: white portion (CUSTODY) -->
  <text x="{wm_x:.2f}" y="{WM_Y_BASELINE}"
        font-family="'Bebas Neue', sans-serif"
        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LS_EM}em"
        fill="{WHITE}" clip-path="url(#clipWhite)">{wm_full}</text>

  <!-- 4b. Wordmark: amber portion (ZERO) -->
  <text x="{wm_x:.2f}" y="{WM_Y_BASELINE}"
        font-family="'Bebas Neue', sans-serif"
        font-size="{WM_FONT_SIZE}" letter-spacing="{WM_LS_EM}em"
        fill="{AMBER}" clip-path="url(#clipAmber)">{wm_full}</text>

  <!-- 5. Amber horizontal rule -->
  <line x1="{rule_x1:.2f}" y1="{rule_y}" x2="{rule_x2:.2f}" y2="{rule_y}"
        stroke="{AMBER}" stroke-width="2"/>

  <!-- 6. Tagline -->
  <text x="{tl_x:.2f}" y="{TL_Y_BASELINE}"
        font-family="'Fraunces', Georgia, serif"
        font-style="italic" font-weight="300"
        font-size="{TL_FONT_SIZE}" fill="{TEXT_SECONDARY}"
        letter-spacing="0.01em">{tl_text}</text>

  <!-- 7. URL -->
  <text x="{url_x:.2f}" y="{URL_Y_BASELINE}"
        font-family="'DM Mono', 'Courier New', monospace"
        font-size="{URL_FONT_SIZE}" fill="{TEXT_MUTED}"
        letter-spacing="0.05em">{url_text}</text>
</svg>
"""
    return svg


# ---------------------------------------------------------------------------
# Grain overlay (no numpy — seeded random for determinism)
# ---------------------------------------------------------------------------

def add_grain(img: Image.Image, opacity: float = GRAIN_OPACITY, seed: int = GRAIN_SEED) -> Image.Image:
    """
    Overlay monochromatic film grain at the given opacity.
    Uses a seeded RNG so output is fully deterministic.
    """
    w, h = img.size
    rng = random.Random(seed)
    noise_bytes = rng.randbytes(w * h)
    noise = Image.frombytes("L", (w, h), noise_bytes)
    # Scale L channel to target opacity via paste with alpha mask
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
    ensure_fraunces()
    ensure_dmmono()

    print("Measuring text positions…")
    svg = build_svg()

    # Write SVG for reference / debugging
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    svg_path = OUT_DIR / "custodyzero-social-card.svg"
    svg_path.write_text(svg, encoding="utf-8")
    print(f"  SVG reference: {svg_path.relative_to(BASE)}")

    print("Rasterizing to PNG…")
    png_bytes = cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        output_width=W,
        output_height=H,
    )
    img = Image.open(io.BytesIO(png_bytes))

    print("Adding grain overlay…")
    img = add_grain(img, opacity=GRAIN_OPACITY, seed=GRAIN_SEED)

    img.save(str(OUT_PATH), format="PNG", optimize=False)
    print(f"  {OUT_PATH.relative_to(BASE)} ({W}×{H})")

    print("\nDone.")


if __name__ == "__main__":
    main()
