# StationZero Brand Guidelines

**Parent document:** CustodyZero Design System v1.1 · StationZero Product Identity Addendum
**Status:** Assets generated v1.0
**Version:** 1.0 · April 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 1 — Brand Character

StationZero is the CustodyZero platform for home edge automation — local, operator-defined, and private by construction. It begins with WiFi camera surveillance and monitoring, and expands into adversarial detection (toddler escaping, pool falls, fire, robbery), device control (door locks, lighting), and whole-home automation.

StationZero is a **platform product house** within CustodyZero, following the `[X]Zero` naming convention. It will contain its own sub-products and modules as the platform expands.

| Attribute | Value |
|---|---|
| Category | Home edge automation |
| Product structure | Platform product house (`[X]Zero` naming convention) |
| Accent color | Signal Red `#C04848` |
| Accent dim | `#7A2E2E` (for reduced-emphasis contexts) |
| Voice serif | Zilla Slab |
| Design register | Operational domestic |
| Audience | Dual — privacy-conscious homeowners + regulated enterprise operators |

### Design Register: Operational Domestic

The phrase "operational domestic" carries dual meaning:

- **For consumer audiences:** domestic = home. Your home, your infrastructure, your control panel.
- **For enterprise audiences:** domestic = internal, in-house, theirs. Not outsourced, not cloud-hosted, not someone else's.

Both readings converge on the same emotional note: **this is yours, running on your ground.**

### Dual Audience

StationZero serves two distinct audiences whose needs must both be served without compromise:

**Self-hosting privacy-conscious consumers**
- They want plain language and clear ownership.
- They are choosing StationZero specifically because they do not trust cloud-hosted alternatives.
- Brand language: direct, human, translate technical truth into plain promise.

**Regulated enterprise operators** (healthcare, schools, institutions)
- They need compliance-ready infrastructure, documented data residency, and institutional trust signals.
- Brand language: architectural, precise, contractual. Specs and behavior, not feelings.

These audiences share one core requirement: they need to know exactly where their footage is and who can access it. StationZero's brand must make this concrete, not aspirational.

---

## 2 — Wordmark

### Generated files

| File | Format | Canvas | Usage |
|---|---|---|---|
| `stationzero-wordmark-dark.svg` | SVG | 470 × 80 px | Primary — split-color mark for dark backgrounds |
| `stationzero-wordmark-dark@2x.png` | PNG/RGBA | 940 × 160 px | Screen 2× density |
| `stationzero-wordmark-dark@3x.png` | PNG/RGBA | 1410 × 240 px | Screen 3× density |
| `stationzero-wordmark-red.svg` | SVG | 470 × 80 px | Variant — single-color Signal Red |
| `stationzero-wordmark-red@2x.png` | PNG/RGBA | 940 × 160 px | Screen 2× density, red mark |
| `stationzero-wordmark-red@3x.png` | PNG/RGBA | 1410 × 240 px | Screen 3× density, red mark |

### Wordmark anatomy

- **Typeface:** Bebas Neue Regular (embedded as base64 in SVG + Google Fonts CDN fallback)
- **Font size:** 83.7 px on 80 px canvas height (calibrated for Bebas Neue at CustodyZero house standard)
- **Letter-spacing:** 0.15 em (CustodyZero house standard)
- **Baseline:** y = 69.5 px
- **Color split technique:** Two identical `<text>` elements rendered at the same position, clipped at the split boundary using `clipPath`. Left clip renders STATION in `#F2F2EC` (--white), right clip renders ZERO in `#C04848` (Signal Red).
- **Split boundary:** x = 299.81 px (measured from glyph advance widths via fontTools, nudged 2 px left into the N–Z letter-spacing gap to compensate for sub-pixel rounding between font metrics and browser SVG text layout)
- **Canvas:** transparent background, 470 × 80 px — text is left-aligned at x = 3 px

### Usage

**Primary usage (dark variant):** split-color wordmark — STATION in `#F2F2EC` (--white), ZERO in `#C04848` (Signal Red) — on dark backgrounds. This is the canonical form. Use this form in all product, marketing, and documentation contexts.

**Red variant:** single-color Signal Red wordmark `#C04848` for surfaces where the split-color mark would not read — for example, on white or light surfaces where the white portion would disappear. Use sparingly; the dark variant is strongly preferred.

### Clearspace

Maintain minimum clearspace equal to the cap height of the wordmark on all four sides. The cap height is approximately 68 px at native SVG size (80 px canvas).

At raster sizes: minimum clearspace = (output height / 80) × 68 px.

### Minimum size

- **SVG:** 120 px wide minimum. Do not use below this size.
- **PNG 2×:** The 2× assets are production minimum. Do not use the 1× native SVG dimensions for screen display.

### What never to do

- Do not stretch or distort the wordmark.
- Do not rotate the wordmark.
- Do not recolor outside the approved dark and red variants.
- Do not apply drop shadows, glows, gradients, or any effects to the wordmark.
- Do not reduce the white portion's opacity below 100%.
- Do not change the split point. STATION is always white; ZERO is always Signal Red. Do not reverse the color assignment.
- Do not separate STATION and ZERO into two lines or two elements. It is one word.
- Do not place the wordmark on purple, violet, or red backgrounds that would cause the Signal Red portion to disappear.
- Do not use amber (`#D4880A`) on or adjacent to StationZero brand elements — amber belongs to the CustodyZero house only.
- Do not use electric blue (`#4FC3F7`) on or adjacent to StationZero brand elements — blue belongs to Archon only.
- Do not use industrial green (`#5A9A6E`) on or adjacent to StationZero brand elements — green belongs to Factory only.

---

## 3 — Icon Mark

### Generated files

| File | Format | Dimensions | Usage |
|---|---|---|---|
| `stationzero-icon-dark.svg` | SVG | 64 × 64 px | Source master |
| `stationzero-icon-dark.ico` | ICO | 3 frames: 16 × 16, 32 × 32, 48 × 48 | Favicon, OS icon |
| `stationzero-icon-dark@2x.png` | PNG/RGBA | 128 × 128 px | Screen 2× density |
| `stationzero-icon-dark@3x.png` | PNG/RGBA | 192 × 192 px | Screen 3× density |

### Icon mark anatomy

**Design:** The Squared Slashed Zero — a geometric zero glyph rendered as an architectural mark.

- **Frame:** `<rect>` at x = 12, y = 6, width = 40, height = 52. Stroke-width 5 px. No border-radius. This is the zero form — a squared-off rectangle, no curves.
- **Slash:** `<line>` from (18.0, 50.8) to (46.0, 13.2). Stroke-width 3 px, stroke-linecap square. The slash follows the corner-to-corner angle of the interior void but is pulled inward to 80% of the full diagonal length, centered. This creates breathing room between the slash endpoints and the frame walls while preserving the precise diagonal alignment.
- **Color:** `#C04848` (Signal Red) on transparent.

The slash distinguishes the zero from the letter O and from a generic rectangle. The squared form (no border-radius) enforces the CustodyZero house geometry constraint at the glyph level. The mark is typographic, not illustrative — it says exactly what the product is (a Zero product) without metaphor.

**Construction geometry:**
- Inner void corners: bottom-left (14.5, 55.5), top-right (49.5, 8.5)
- Full diagonal vector: dx = 35, dy = −47, length ≈ 58.6 px
- Slash is 80% of full diagonal, centered on the midpoint (32, 32)

**Legibility at small sizes:**

| Size | Frame stroke | Slash stroke | Notes |
|---|---|---|---|
| 64 × 64 | 5 px | 3 px | Master size — clear slashed zero |
| 48 × 48 | 3.75 px | 2.25 px | ICO frame 3 |
| 32 × 32 | 2.5 px | 1.5 px | ICO frame 2 — legible |
| 16 × 16 | 1.25 px | 0.75 px | ICO frame 1 — distinct slashed rectangle |

### Usage

- Use the icon mark for favicon, app icon, and all small-format contexts where the wordmark is not legible.
- The icon mark appears in `#C04848` (Signal Red) on dark backgrounds (primary).
- Minimum size: 16 × 16 px (covered by the ICO).

### What never to do

- Do not fill the frame. The zero is a stroked outline, not a solid block.
- Do not remove the slash. Without it, the mark is a generic rectangle.
- Do not change the slash angle. It is derived from the interior corner-to-corner diagonal.
- Do not round the corners. The squared form is a house constraint.
- Do not add drop shadows or glows to the icon.
- Do not combine the icon with text at small sizes (< 32 px). Let the icon stand alone.
- Do not stretch or distort the icon.
- Do not use surveillance camera, eye, lens, or shield imagery as an alternative mark.

---

## 4 — Color System

### Signal Red

| Token | Value | Usage |
|---|---|---|
| `--signal-red` | `#C04848` | Primary accent — wordmark "ZERO" portion, icon mark, dividers, status dots, alerts |
| `--signal-red-dim` | `#7A2E2E` | Reduced-emphasis contexts — disabled states, secondary indicators |

### Signal Red Usage Rules

Signal Red is a **brand accent**, not a UI interaction color. It appears in brand marks, dividers, status indicators, and alert states. It does **not** appear on buttons, form controls, or interactive elements where it would be confused with destructive/error actions.

**Approved uses:**
- Wordmark "ZERO" color
- Icon mark fill
- Horizontal rules / dividers
- Status indicator dots (active, recording, alert)
- Alert and notification accents
- Section headings in brand contexts

**Not approved for:**
- Button backgrounds or borders
- Form input focus states
- Link text
- Large background fills
- Decorative gradients

The UI interactive palette (buttons, links, focus states) is a separate design decision made at the product UI level, not at the brand level. Signal Red stays in the brand layer.

### Contrast on Dark Stack

| Foreground | Background | Contrast ratio | WCAG AA (text) | WCAG AA (UI) |
|---|---|---|---|---|
| `#C04848` | `#0A0A0A` | 3.8:1 | Fail | Pass |
| `#C04848` | `#111111` | 3.5:1 | Fail | Pass |
| `#C04848` | `#1A1A1A` | 3.1:1 | Fail | Pass |
| `#F2F2EC` | `#0A0A0A` | 16.4:1 | Pass | Pass |
| `#F2F2EC` | `#111111` | 14.9:1 | Pass | Pass |

Signal Red passes WCAG AA for UI components (3:1) but fails for body text (4.5:1). Use Signal Red for large display text, icons, and UI elements only. Body text must use `--white` (`#F2F2EC`) or approved gray values.

---

## 5 — Typography

### Type Stack

| Role | Typeface | Weight | Usage |
|---|---|---|---|
| Display | Bebas Neue | Regular (400) | Headings, wordmark, section titles. Always uppercase. |
| UI / System | DM Mono | 300–500 | Navigation, labels, CTAs, code, metadata. |
| Voice / Body | Zilla Slab | 400, 400i, 600 | Long-form body text, onboarding copy, notification content, editorial passages. |

### Zilla Slab Usage Rules

Zilla Slab is StationZero's **voice serif** — the typeface that carries the product's written personality. It appears in body text, onboarding flows, alert descriptions, and any context where the product speaks in full sentences.

**Why Zilla Slab:** It reads as infrastructure documentation, not literary prose. The slab serifs are mechanical and grounded. It is legible at body sizes on dark backgrounds. It does not compete with Bebas Neue for display presence.

**Zilla Slab does not appear in:**
- Navigation labels (DM Mono)
- Button text (DM Mono)
- Status indicators (DM Mono)
- Section headings (Bebas Neue)

**Zilla Slab does not leave StationZero.** It is not a CustodyZero house font. It does not appear on Archon, Factory, Type, or Edit surfaces. Each product earns its own voice serif (or chooses not to have one).

---

## 6 — Color on Color

| Foreground | Background | Status |
|---|---|---|
| Split wordmark (white + red) | `--black` (`#0A0A0A`) | **Approved — primary** |
| Split wordmark (white + red) | `--dark` (`#111111`) | **Approved** |
| Split wordmark (white + red) | `--mid` (`#1A1A1A`) | **Approved** |
| Red wordmark (`#C04848`) | `--black` (`#0A0A0A`) | **Approved** |
| Red wordmark (`#C04848`) | `--dark` (`#111111`) | **Approved** |
| Red wordmark (`#C04848`) | `--white` (`#F2F2EC`) | **Approved — light surface variant** |
| Red icon (`#C04848`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| Red icon (`#C04848`) | `--dark` (`#111111`) | **Approved** |
| Split wordmark (white + red) | White or light surface | **Never** (white portion disappears) |
| Red wordmark (`#C04848`) | Red or warm surface | **Never** |
| Any mark | Purple or gradient background | **Never** |
| Any mark | Amber background | **Never** |
| Any mark | Blue (`#4FC3F7`) background | **Never** |
| Any mark | Green (`#5A9A6E`) background | **Never** |

---

## 7 — What Not To Do

### Brand Identity

- **Do not use surveillance camera, eye, lens, or shield imagery.** StationZero's visual identity is architectural and typographic. No illustrative security metaphors.
- **Do not use the word "smart" in any product copy.** StationZero is infrastructure, not a gadget.
- **Do not imply cloud connectivity as a feature.** StationZero is edge-native. Cloud is not the model.
- **Do not use "monitoring" or "watching" as primary brand language.** StationZero owns and protects. It does not surveil.

### Color Boundaries

- **Do not apply amber to StationZero brand elements.** Amber (`#D4880A`) is the CustodyZero house accent and is not used as a StationZero accent. It may appear in house-level navigation or footer contexts linking back to CustodyZero only.
- **Do not apply electric blue to StationZero brand elements.** Blue (`#4FC3F7`) belongs to Archon exclusively.
- **Do not apply industrial green to StationZero brand elements.** Green (`#5A9A6E`) belongs to Factory exclusively.
- **Do not use purple, blue-purple, or violet anywhere.** House-level prohibition.
- **Do not use Signal Red for interactive UI elements** (buttons, links, form controls). Signal Red is a brand accent, not a UI interaction color.

### Typography Boundaries

- **Do not use Zilla Slab outside StationZero contexts.** It is product-specific, not a house font.
- **Do not use Fraunces in StationZero contexts.** Fraunces is a CustodyZero house voice font. It does not appear on StationZero surfaces.
- **Do not use Cormorant or Literata in StationZero contexts.** These belong to Type.

### Mark Usage

- **Do not use the white wordmark at opacity below 100%.** The mark is either present at full opacity or absent.
- **The StationZero wordmark and CustodyZero wordmark must not compete on the same surface.** One leads, one supports. In most StationZero product contexts, the CustodyZero wordmark appears in a footer or secondary attribution only.
- **Do not name competitors by name** (Ring, Nest, Google Home, etc.) in StationZero brand copy adjacent to the mark.

---

## 8 — Asset Naming Convention

```
stationzero-wordmark-[variant].[ext]
stationzero-wordmark-[variant]@[scale].png
stationzero-icon-[variant].[ext]
stationzero-icon-[variant]@[scale].png
```

**Variants:**
- `dark` — split-color mark on transparent background (primary)
- `red` — single-color Signal Red on transparent background

**Scale suffixes:**
- `@2x` — 2× screen density
- `@3x` — 3× screen density
- No suffix — native/1× dimensions (SVG only)

**Extensions in use:** `.svg`, `.png`, `.ico`

---

## 9 — Relationship to CustodyZero House

- **Amber belongs to CustodyZero house only.** StationZero amber does not exist. The StationZero accent is `#C04848` (Signal Red).
- **Blue belongs to Archon only.** StationZero blue does not exist.
- **Green belongs to Factory only.** StationZero green does not exist.
- On pages that link back to CustodyZero, amber may appear in the parent brand link context only — not on StationZero-branded elements.
- **The StationZero wordmark and CustodyZero wordmark must not compete on the same surface.** One leads, one supports. In most StationZero product contexts, the CustodyZero wordmark appears in a footer or secondary attribution only.
- StationZero inherits the full CustodyZero house foundation: dark background stack, Bebas Neue and DM Mono typefaces, square geometry constraint.
- StationZero's visual language is **operational domestic** — professional infrastructure that lives comfortably in a home. Not a military command center (too aggressive), not a consumer gadget app (too disposable), not a cloud dashboard (wrong ownership model).
- As a **platform product house**, StationZero will contain sub-products and modules. Sub-product identity rules will be defined as those products emerge, following the CustodyZero design system's platform product house conventions.

---

## 10 — Signal Red vs Type Pencil

Signal Red (`#C04848`) and Type's Pencil (`#8B3A3A`) are both in the red family. They are distinct:

| Property | Signal Red | Pencil |
|---|---|---|
| Hex | `#C04848` | `#8B3A3A` |
| Character | Bright, alert, operational | Dark, warm, literary |
| Lightness | Higher — reads as an active signal | Lower — reads as aged/earthy |
| Context | Infrastructure, alerts, status | Text, editing, annotation |

These two reds serve different products with different emotional registers and are not interchangeable. If both appear on a CustodyZero house-level page (e.g., a product lineup), they are visually distinguishable side by side.

---

## Asset Generation

Assets in this directory are generated by `scripts/generate-stationzero.py`.

To regenerate:
```sh
python3 scripts/install-fonts.py   # install Bebas Neue if not present
python3 scripts/generate-stationzero.py
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
