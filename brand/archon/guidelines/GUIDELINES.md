# Archon Brand Guidelines

**Parent document:** CustodyZero Design System v1.0 · Archon Product Identity Addendum
**Status:** Assets generated v1.0
**Version:** 1.0 · February 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 1 — Wordmark

### Generated files

| File | Format | Canvas | Usage |
|---|---|---|---|
| `archon-wordmark-dark.svg` | SVG | 400 × 72 px | Primary — white mark for dark backgrounds |
| `archon-wordmark-dark@2x.png` | PNG/RGBA | 800 × 144 px | Screen 2× density, white mark |
| `archon-wordmark-dark@3x.png` | PNG/RGBA | 1200 × 216 px | Screen 3× density, white mark |
| `archon-wordmark-blue.svg` | SVG | 400 × 72 px | Variant — blue mark for surfaces where white does not read |
| `archon-wordmark-blue@2x.png` | PNG/RGBA | 800 × 144 px | Screen 2× density, blue mark |
| `archon-wordmark-blue@3x.png` | PNG/RGBA | 1200 × 216 px | Screen 3× density, blue mark |

### Wordmark anatomy

- **Typeface:** Bebas Neue Regular (embedded as base64 in SVG + Google Fonts CDN fallback)
- **Font size:** 72 px on 72 px canvas height
- **Letter-spacing:** 0.12 em
- **Rule:** 1 px horizontal line in `#4FC3F7` (--blue), positioned 3 px below the text baseline, spanning the full visual text width
- **Canvas:** transparent background, 400 × 72 px artboard — text is left-aligned at x = 3 px

### Usage

**Primary usage (dark variant):** white wordmark `#F2F2EC` (--white) on dark backgrounds.
This is the canonical form. Use this form in all technical, operator-facing, and documentation contexts.

**Blue variant:** electric blue wordmark `#4FC3F7` (--blue) for surfaces where the white mark would not read — for example, on white, light grey, or very light neutral surfaces. Use sparingly; the dark variant is strongly preferred.

### Clearspace

Maintain minimum clearspace equal to the cap height of the wordmark on all four sides.
The cap height is approximately 62 px at native SVG size (72 px canvas).

At raster sizes: minimum clearspace = (output height / 72) × 62 px.

### Minimum size

- **SVG:** 120 px wide minimum. Do not use below this size.
- **PNG 2×:** The 2× assets are production minimum. Do not use the 1× native SVG dimensions for screen display.

### What never to do

- Do not stretch or distort the wordmark.
- Do not rotate the wordmark.
- Do not recolor outside the approved dark and blue variants (white on dark, blue on light).
- Do not apply drop shadows, glows, gradients, or any effects to the wordmark.
- Do not combine the wordmark with the tagline as a lockup — they are used independently.
- Do not reduce the white wordmark opacity below 100%.
- Do not apply the sci-fi panel geometry (corner brackets, scan lines) directly to the wordmark or icon.
- Do not place the wordmark on purple, violet, or blue-purple backgrounds.
- Do not use amber (`#D4880A`) on or adjacent to Archon brand elements — amber belongs to the CustodyZero house only.

---

## 2 — Icon Mark

### Generated files

| File | Format | Dimensions | Usage |
|---|---|---|---|
| `archon-icon-dark.svg` | SVG | 64 × 64 px | Source master |
| `archon-icon-dark.ico` | ICO | 3 frames: 16 × 16, 32 × 32, 48 × 48 | Favicon, OS icon |
| `archon-icon-dark@2x.png` | PNG/RGBA | 128 × 128 px | Screen 2× density |
| `archon-icon-dark@3x.png` | PNG/RGBA | 192 × 192 px | Screen 3× density |

### Icon mark anatomy

**Design:** two L-shaped corner brackets on a top-left / bottom-right diagonal axis, with a small filled circle at center.

- **Top-left bracket:** horizontal arm + vertical arm, corner at (8, 8), arms 14 px
- **Bottom-right bracket:** horizontal arm + vertical arm, corner at (56, 56), arms 14 px
- **Center node:** filled circle, center (32, 32), radius 3.5 px
- **Stroke:** 2 px, stroke-linecap square, stroke-linejoin miter
- **Color:** `#4FC3F7` (--blue) on transparent

The diagonal bracket pair implies a containment boundary. The center node implies a validation or enforcement point. Both elements are architectural — no illustrative, metaphorical, or surveillance imagery.

**Legibility at small sizes:**

| Size | Bracket arm length | Center dot radius | Notes |
|---|---|---|---|
| 64 × 64 | 14 px | 3.5 px | Master size |
| 48 × 48 | 10.5 px | 2.6 px | ICO frame 3 |
| 32 × 32 | 7 px | 1.75 px | ICO frame 2 |
| 16 × 16 | 3.5 px | ~1 px | ICO frame 1 — distinctive diagonal shape |

### Usage

- Use the icon mark for favicon, app icon, and all small-format contexts where the wordmark is not legible.
- The icon mark appears in `#4FC3F7` (--blue) on dark backgrounds (primary), or in `#F2F2EC` (--white) on dark backgrounds where blue is not appropriate.
- Minimum size: 16 × 16 px (covered by the ICO).

### What never to do

- Do not fill the strokes.
- Do not add drop shadows or glows to the icon.
- Do not combine the icon with text at small sizes (< 32 px). Let the icon stand alone.
- Do not stretch or distort the icon.
- Do not use the icon on light backgrounds — it is designed for dark contexts only.

---

## 3 — Color on Color

| Foreground | Background | Status |
|---|---|---|
| White wordmark (`#F2F2EC`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | `--dark` (`#111111`) | **Approved** |
| White wordmark (`#F2F2EC`) | `--mid` (`#1A1A1A`) | **Approved** |
| Blue wordmark (`#4FC3F7`) | `--black` (`#0A0A0A`) | **Approved** |
| Blue wordmark (`#4FC3F7`) | `--dark` (`#111111`) | **Approved** |
| Blue icon (`#4FC3F7`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | White or light surface | **Never** |
| Blue wordmark (`#4FC3F7`) | Blue surface | **Never** |
| Any mark | Purple or gradient background | **Never** |
| Any mark | Amber background | **Never** |

---

## 4 — What Not To Do

- **Do not use the Archon mark to imply intelligence or autonomy.** Archon enforces rules. It does not think, decide, or recommend. The mark must not appear in contexts that suggest AI agency.
- **Do not apply amber to Archon brand elements.** Amber (`#D4880A`) is the CustodyZero house accent and is not used as an Archon accent. It may appear in house-level navigation or footer contexts linking back to CustodyZero only.
- **Do not use purple, blue-purple, or violet adjacent to the Archon mark.** The boundary between electric blue and purple is the boundary between system and hype.
- **Do not combine the wordmark with a tagline as a lockup.** The taglines ("The coordination layer that doesn't guess." / "Your AI. Your rules. Finally.") are used independently in copy — never embedded in or below the wordmark.
- **Do not use the white wordmark at opacity below 100%.** The mark is either present at full opacity or absent.
- **Do not apply the sci-fi panel geometry (corner brackets, scan lines) directly to the wordmark or icon.** Panel geometry belongs to surrounding UI elements, not the mark itself.
- **Do not use Fraunces or any humanist serif** adjacent to or in Archon brand contexts. Fraunces is a CustodyZero house voice font. It does not appear on Archon surfaces.
- **Do not name competitors by name** in Archon brand copy adjacent to the mark.

---

## 5 — Asset Naming Convention

```
archon-wordmark-[variant].[ext]
archon-wordmark-[variant]@[scale].png
archon-icon-[variant].[ext]
archon-icon-[variant]@[scale].png
```

**Variants:**
- `dark` — white mark on transparent background (primary)
- `blue` — blue mark on transparent background

**Scale suffixes:**
- `@2x` — 2× screen density
- `@3x` — 3× screen density
- No suffix — native/1× dimensions (SVG only)

**Extensions in use:** `.svg`, `.png`, `.ico`

---

## 6 — Relationship to CustodyZero House

- **Amber belongs to CustodyZero house only.** Archon amber does not exist. The Archon accent is `#4FC3F7` (--blue).
- On pages that link back to CustodyZero, amber may appear in the parent brand link context only — not on Archon-branded elements.
- **The Archon wordmark and CustodyZero wordmark must not compete on the same surface.** One leads, one supports. In most Archon product contexts, the CustodyZero wordmark appears in a footer or secondary attribution only.
- Archon inherits the full CustodyZero house foundation: dark background stack, Bebas Neue and DM Mono typefaces, all three brand attitudes.
- The sci-fi interface language (scan lines, panel geometry, ambient blue glow) is Archon-specific. It does not appear on CustodyZero house pages.

---

## Asset Generation

Assets in this directory are generated by `scripts/generate-archon.py`.

To regenerate:
```sh
python3 scripts/install-fonts.py   # install Bebas Neue if not present
python3 scripts/generate-archon.py
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
