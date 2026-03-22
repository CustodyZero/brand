# Factory Brand Guidelines

**Parent document:** CustodyZero Design System v1.0 · Factory Product Identity Addendum
**Status:** Assets generated v1.0
**Version:** 1.0 · March 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 1 — Wordmark

### Generated files

| File | Format | Canvas | Usage |
|---|---|---|---|
| `factory-wordmark-dark.svg` | SVG | dynamic × 72 px | Primary — white mark for dark backgrounds |
| `factory-wordmark-dark@2x.png` | PNG/RGBA | 2× canvas | Screen 2× density, white mark |
| `factory-wordmark-dark@3x.png` | PNG/RGBA | 3× canvas | Screen 3× density, white mark |
| `factory-wordmark-green.svg` | SVG | dynamic × 72 px | Variant — green mark for surfaces where white does not read |
| `factory-wordmark-green@2x.png` | PNG/RGBA | 2× canvas | Screen 2× density, green mark |
| `factory-wordmark-green@3x.png` | PNG/RGBA | 3× canvas | Screen 3× density, green mark |

### Wordmark anatomy

- **Typeface:** Bebas Neue Regular (embedded as base64 in SVG + Google Fonts CDN fallback)
- **Font size:** 72 px on 72 px canvas height
- **Letter-spacing:** 0.12 em
- **Decoration:** None. The wordmark is unadorned — Factory's restraint is its identity.
- **Canvas:** transparent background, dynamic width based on glyph metrics — text is left-aligned at x = 3 px

### Usage

**Primary usage (dark variant):** white wordmark `#F2F2EC` (--white) on dark backgrounds.
This is the canonical form. Use this form in all technical, operator-facing, and documentation contexts.

**Green variant:** industrial green wordmark `#5A9A6E` (--green) for surfaces where the white mark would not read — for example, on white, light grey, or very light neutral surfaces. Use sparingly; the dark variant is strongly preferred.

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
- Do not recolor outside the approved dark and green variants (white on dark, green on light).
- Do not apply drop shadows, glows, gradients, or any effects to the wordmark.
- Do not add a horizontal rule, underline, or other decorative element to the wordmark.
- Do not reduce the white wordmark opacity below 100%.
- Do not place the wordmark on purple, violet, or green backgrounds that would clash with the green variant.
- Do not use amber (`#D4880A`) on or adjacent to Factory brand elements — amber belongs to the CustodyZero house only.
- Do not use electric blue (`#4FC3F7`) on or adjacent to Factory brand elements — blue belongs to Archon only.

---

## 2 — Icon Mark

### Generated files

| File | Format | Dimensions | Usage |
|---|---|---|---|
| `factory-icon-dark.svg` | SVG | 64 × 64 px | Source master |
| `factory-icon-dark.ico` | ICO | 3 frames: 16 × 16, 32 × 32, 48 × 48 | Favicon, OS icon |
| `factory-icon-dark@2x.png` | PNG/RGBA | 128 × 128 px | Screen 2× density |
| `factory-icon-dark@3x.png` | PNG/RGBA | 192 × 192 px | Screen 3× density |

### Icon mark anatomy

**Design:** The Gate — two vertical bars with a horizontal threshold line between them.

- **Left bar:** vertical line at x = 16, from y = 14 to y = 50 (36 px)
- **Right bar:** vertical line at x = 48, from y = 14 to y = 50 (36 px)
- **Threshold:** horizontal line from x = 16 to x = 48, at y = 32 (centered)
- **Stroke:** 2.5 px, stroke-linecap square
- **Color:** `#5A9A6E` (--green) on transparent

The vertical bars represent the boundary of the governed process. The horizontal threshold represents the verification gate that all work must cross before acceptance. The form is architectural — no illustrative, metaphorical, or manufacturing imagery.

**Legibility at small sizes:**

| Size | Bar height | Gap width | Notes |
|---|---|---|---|
| 64 × 64 | 36 px | 32 px | Master size |
| 48 × 48 | 27 px | 24 px | ICO frame 3 |
| 32 × 32 | 18 px | 16 px | ICO frame 2 |
| 16 × 16 | 9 px | 8 px | ICO frame 1 — distinctive gate shape |

### Usage

- Use the icon mark for favicon, app icon, and all small-format contexts where the wordmark is not legible.
- The icon mark appears in `#5A9A6E` (--green) on dark backgrounds (primary).
- Minimum size: 16 × 16 px (covered by the ICO).

### What never to do

- Do not fill the strokes or add a background fill.
- Do not add drop shadows or glows to the icon.
- Do not combine the icon with text at small sizes (< 32 px). Let the icon stand alone.
- Do not stretch or distort the icon.
- Do not add arrows, chevrons, or flow indicators to the gate form.

---

## 3 — Color on Color

| Foreground | Background | Status |
|---|---|---|
| White wordmark (`#F2F2EC`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | `--dark` (`#111111`) | **Approved** |
| White wordmark (`#F2F2EC`) | `--mid` (`#1A1A1A`) | **Approved** |
| Green wordmark (`#5A9A6E`) | `--black` (`#0A0A0A`) | **Approved** |
| Green wordmark (`#5A9A6E`) | `--dark` (`#111111`) | **Approved** |
| Green icon (`#5A9A6E`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | White or light surface | **Never** |
| Green wordmark (`#5A9A6E`) | Green surface | **Never** |
| Any mark | Purple or gradient background | **Never** |
| Any mark | Amber background | **Never** |
| Any mark | Blue (`#4FC3F7`) background | **Never** |

---

## 4 — What Not To Do

- **Do not use the Factory mark to imply automation or AI autonomy.** Factory governs change. It does not generate, create, or decide. The mark must not appear in contexts that suggest autonomous production.
- **Do not apply amber to Factory brand elements.** Amber (`#D4880A`) is the CustodyZero house accent and is not used as a Factory accent. It may appear in house-level navigation or footer contexts linking back to CustodyZero only.
- **Do not apply electric blue to Factory brand elements.** Blue (`#4FC3F7`) belongs to Archon exclusively.
- **Do not use purple, blue-purple, or violet adjacent to the Factory mark.**
- **Do not add decorative elements to the wordmark.** No rules, underlines, brackets, or ornaments. The unadorned form is intentional.
- **Do not use the white wordmark at opacity below 100%.** The mark is either present at full opacity or absent.
- **Do not use manufacturing, assembly line, or conveyor belt imagery** adjacent to or as part of the Factory brand. The name is metaphorical; the visual language is architectural.
- **Do not use Fraunces or any humanist serif** adjacent to or in Factory brand contexts. Fraunces is a CustodyZero house voice font. It does not appear on Factory surfaces.

---

## 5 — Asset Naming Convention

```
factory-wordmark-[variant].[ext]
factory-wordmark-[variant]@[scale].png
factory-icon-[variant].[ext]
factory-icon-[variant]@[scale].png
```

**Variants:**
- `dark` — white mark on transparent background (primary)
- `green` — green mark on transparent background

**Scale suffixes:**
- `@2x` — 2× screen density
- `@3x` — 3× screen density
- No suffix — native/1× dimensions (SVG only)

**Extensions in use:** `.svg`, `.png`, `.ico`

---

## 6 — Relationship to CustodyZero House

- **Amber belongs to CustodyZero house only.** Factory amber does not exist. The Factory accent is `#5A9A6E` (--green).
- **Blue belongs to Archon only.** Factory blue does not exist.
- On pages that link back to CustodyZero, amber may appear in the parent brand link context only — not on Factory-branded elements.
- **The Factory wordmark and CustodyZero wordmark must not compete on the same surface.** One leads, one supports. In most Factory product contexts, the CustodyZero wordmark appears in a footer or secondary attribution only.
- Factory inherits the full CustodyZero house foundation: dark background stack, Bebas Neue and DM Mono typefaces, square geometry constraint.
- Factory's visual language is the most restrained in the product house. No decorative elements, no ambient effects, no interface theatrics. Utilitarian by design.

---

## Asset Generation

Assets in this directory are generated by `scripts/generate-factory.py`.

To regenerate:
```sh
python3 scripts/install-fonts.py   # install Bebas Neue if not present
python3 scripts/generate-factory.py
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
