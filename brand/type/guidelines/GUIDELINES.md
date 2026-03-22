# Type Brand Guidelines

**Parent document:** `type-brand-guide.html` (visual reference)
**Status:** Assets generated v1.0
**Version:** 1.0 · March 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 1 — Wordmark

### Specification

| Property | Value |
|---|---|
| Canvas | 149 × 98 px |
| Background | Transparent |
| Font | Cormorant Light (weight 300); fallback: Georgia, serif |
| Letter-spacing | `-0.03em` |
| Font-size | `72px` |
| Text alignment | Left-aligned (`x: 3, text-anchor: start`) |
| Baseline y | `72px` |
| Case | Sentence case — always "Type", never "TYPE" or "type" |

### Generated Files

| File | Dimensions | Use |
|---|---|---|
| `type-wordmark-light.svg` | 149 × 98 | Primary — ink on transparent, for paper/light backgrounds |
| `type-wordmark-light@2x.png` | 298 × 196 | Retina / HiDPI screens |
| `type-wordmark-light@3x.png` | 447 × 294 | Ultra-HiDPI / print at small physical size |
| `type-wordmark-dark.svg` | 149 × 98 | Paper-bright on transparent, for dark backgrounds |
| `type-wordmark-dark@2x.png` | 298 × 196 | Dark variant retina |
| `type-wordmark-dark@3x.png` | 447 × 294 | Dark variant ultra-HiDPI |

### Usage

**Primary usage (light variant):** ink-colored wordmark `#1C1917` (--ink) on paper or light backgrounds.
This is the canonical form. Type lives on paper — the light variant is default.

**Dark variant:** paper-bright wordmark `#FAF8F3` (--paper-bright) on dark backgrounds. For contexts where Type appears on the CustodyZero parent site or other dark surfaces.

---

## 2 — Icon Mark

### Design Description

A vertical line intersected by a horizontal line extending rightward from it — "The Margin and Line."

- **Vertical stroke (margin):** the left-side margin rule, the boundary that defines the writing column
- **Horizontal stroke (text line):** a single line of text extending from the margin, the act of writing

The mark is asymmetric by design. The vertical sits at the left third of the canvas; the horizontal extends rightward. This mirrors the page layout of the Type interface — margin on the left, text flowing right.

### Specification

| Property | Value |
|---|---|
| Canvas | 64 × 64 px |
| Background | Transparent |
| Vertical (margin) | `x1=20, y1=8, x2=20, y2=56, stroke-width=2.5` |
| Horizontal (text) | `x1=20, y1=32, x2=54, y2=32, stroke-width=2` |
| Stroke linecap | `square` |
| Light variant color | `#8B3A3A` (--pencil) on transparent |
| Dark variant color | `#FAF8F3` (--paper-bright) on transparent |
| Fill | None |

### Generated Files

| File | Format | Dimensions | Use |
|---|---|---|---|
| `type-icon-light.svg` | SVG | 64 × 64 | Source — pencil on transparent, for light backgrounds |
| `type-icon-light@2x.png` | PNG/RGBA | 128 × 128 | Screen 2× density |
| `type-icon-light@3x.png` | PNG/RGBA | 192 × 192 | Screen 3× density |
| `type-icon-light.ico` | ICO | 16, 32, 48 | Favicon, OS icon |
| `type-icon-dark.svg` | SVG | 64 × 64 | Paper-bright on transparent, for dark backgrounds |
| `type-icon-dark@2x.png` | PNG/RGBA | 128 × 128 | Dark variant 2× |
| `type-icon-dark@3x.png` | PNG/RGBA | 192 × 192 | Dark variant 3× |

### Usage

- The light variant (pencil `#8B3A3A`) is primary — it appears on paper and light backgrounds
- The dark variant (paper-bright `#FAF8F3`) is for dark backgrounds only
- Minimum size: 16 × 16 px (covered by the ICO)
- The icon mark may appear alongside the wordmark with clear visual separation, or alone in compact contexts

---

## 3 — Color Tokens

These are the canonical values from the Type brand guide. All brand assets reference tokens — never raw hex values in code.

### Surfaces

| Token | Hex | Usage |
|---|---|---|
| `--t-paper` | `#F5F0E8` | The ground — warm, like quality typing paper |
| `--t-paper-bright` | `#FAF8F3` | The page itself — slightly lifted from the ground |
| `--t-surface-1` | `#EDE8DC` | Recessed panels, sidebars |
| `--t-surface-2` | `#E4DDD0` | Input wells, deeper recesses |
| `--t-surface-3` | `#D8D0C4` | Borders, dividers, structural lines |

### Ink

| Token | Hex | Usage |
|---|---|---|
| `--t-ink` | `#1C1917` | Primary text — warm near-black |
| `--t-ink-secondary` | `#4A4540` | Secondary text, body in chrome |
| `--t-ink-muted` | `#8A8070` | Annotations, labels, timestamps |
| `--t-ink-ghost` | `#B8AFA0` | Structural rules, placeholder text |

### Semantic Accents

| Token | Hex | Usage |
|---|---|---|
| `--t-pencil` | `#8B3A3A` | Editor's pencil — focus, active, primary accent |
| `--t-pencil-soft` | `#8B3A3A18` | Pencil at low opacity for backgrounds |
| `--t-assist` | `#4A6178` | Assistant ink — AI-contributed content marker |
| `--t-assist-soft` | `#4A617812` | Assist at low opacity for backgrounds |

### Color Rules

- Paper is the ground. The page floats on it, slightly brighter.
- No pure white (`#FFFFFF`). No pure black (`#000000`). Warmth everywhere.
- No gradients. No drop shadows except the page itself (subtle, structural).
- Pencil is earned — it marks focus, active cursors, margin lines. Sparingly.
- Assist is informational, never alarming. AI text is a different ink, not a warning.

---

## 4 — Typography

Type uses three typefaces, each with a defined role:

| Role | Typeface | Weights | Usage |
|---|---|---|---|
| Display & wordmark | Cormorant | 300 (wordmark/display), 400 (headings), 500 max (rare emphasis) | Wordmark, chapter titles, section heads |
| Writing surface & body | Literata | 300 (body), 400 (small body), 500 (inline emphasis) | Primary writing surface, footnotes, captions |
| Chrome & UI | DM Mono | 300 (annotations), 400 (primary), 500 (button labels) | Status bars, sidebars, labels, metadata |

### Type Scale

| Token | Size | Face | Usage |
|---|---|---|---|
| `--t-text-4xl` | 80px | Cormorant 300 | Display, wordmark |
| `--t-text-3xl` | 56px | Cormorant 300 | Hero specimen |
| `--t-text-2xl` | 40px | Cormorant 300 | Document title |
| `--t-text-xl` | 30px | Cormorant 400 | Chapter heading |
| `--t-text-lg` | 22px | Cormorant 400 | Section heading |
| `--t-text-md` | 18px | Literata 300 | Writing surface body |
| `--t-text-base` | 16px | Literata 400 | Secondary body |
| `--t-text-sm` | 13px | DM Mono 400 | Chrome body text |
| `--t-text-xs` | 11px | DM Mono 400 | Labels, metadata |

### Rules

- Cormorant is never bold. Weight 300 for the wordmark and large display. Weight 400 for headings. 500 is the ceiling.
- DM Mono is the voice of the tool, not the writing. It never appears on the writing surface.
- Literata was designed for long reading sessions on screens. It is the default writing surface font.
- These typefaces are Type's interface voice. The user's own writing uses their chosen fonts.

---

## 5 — Social Card

| File | Dimensions | Use |
|---|---|---|
| `type-social-card.svg` | 1200 × 630 | Open Graph / social preview source |
| `type-social-card.png` | 2400 × 1260 | Open Graph / social preview raster (2× for HiDPI) |

The social card shows the wordmark centered on a page rectangle, on the paper ground, with the margin line visible. CustodyZero attribution at the bottom.

---

## 6 — Clearspace Rules

### Wordmark

Minimum clearspace on all four sides = the cap height of the "T" in the wordmark.
At native SVG size (72px font): cap height ≈ **52px**.

No logotype, text, graphic, or edge may intrude within this zone.

### Icon Mark

Minimum clearspace = **12px** on all sides (relative to the 64px canvas).
The icon must not appear in a container smaller than 88 × 88px.

---

## 7 — Minimum Size Rules

| Asset | Minimum display size | Reason |
|---|---|---|
| Wordmark SVG | 75 × 40 px | Below this, Cormorant's fine strokes lose legibility |
| Wordmark PNG | Use `@2x` or `@3x` file | Never upscale rasters |
| Icon SVG | 24 × 24 px | Margin + line remain distinct |
| Icon ICO | 16 × 16 px | Minimum viable favicon |

---

## 8 — Background Usage

### Light variant (primary)

Valid backgrounds for the light/pencil variant:

- `#FAF8F3` (paper-bright) — **primary**
- `#F5F0E8` (paper)
- `#EDE8DC` (surface-1)
- Any light neutral surface

### Dark variant

Valid backgrounds for the dark variant:

- `#1C1917` (ink) — **primary**
- `#0A0A0A` (CustodyZero house --black)
- `#111111` (CustodyZero house --dark)
- Any near-black background

---

## 9 — Color on Color

| Foreground | Background | Status |
|---|---|---|
| Ink wordmark (`#1C1917`) | paper-bright (`#FAF8F3`) | **Approved — primary** |
| Ink wordmark (`#1C1917`) | paper (`#F5F0E8`) | **Approved** |
| Paper-bright wordmark (`#FAF8F3`) | ink (`#1C1917`) | **Approved** |
| Paper-bright wordmark (`#FAF8F3`) | CZ house --black (`#0A0A0A`) | **Approved** |
| Pencil icon (`#8B3A3A`) | paper-bright (`#FAF8F3`) | **Approved — primary** |
| Pencil icon (`#8B3A3A`) | paper (`#F5F0E8`) | **Approved** |
| Paper-bright icon (`#FAF8F3`) | ink (`#1C1917`) | **Approved** |
| Any mark | Pure white (`#FFFFFF`) | **Never** |
| Any mark | Pure black (`#000000`) | **Never** |
| Any mark | Blue, purple, or gradient surface | **Never** |

---

## 10 — Asset Naming Convention

```
type-{asset-type}-{variant}[@scale].{ext}
```

| Segment | Values |
|---|---|
| `{asset-type}` | `wordmark`, `icon`, `social-card` |
| `{variant}` | `light` (for light backgrounds — primary), `dark` (for dark backgrounds) |
| `[@scale]` | Omit for 1x SVG; `@2x`, `@3x` for raster |
| `{ext}` | `svg`, `png`, `ico` |

Examples: `type-wordmark-light.svg`, `type-icon-dark@2x.png`, `type-social-card.png`

---

## 11 — What Not To Do

- Do not set the wordmark in all caps ("TYPE") or all lowercase ("type"). Always "Type."
- Do not use Cormorant above weight 500 in any Type context.
- Do not recolor the wordmark. Ink or paper-bright only.
- Do not stretch, skew, or scale the wordmark non-uniformly.
- Do not add drop shadows, glows, gradients, or any treatment to the wordmark or icon.
- Do not place the light variant on dark backgrounds or the dark variant on light backgrounds.
- Do not use the CustodyZero amber (`#D4880A`) as an accent in Type product contexts. Amber is house-level only.
- Do not use the Archon blue (`#4FC3F7`) in Type contexts. Type has its own accent system (pencil + assist).
- Do not place text on the writing surface in DM Mono. Mono is for chrome only.
- Do not use pure white or pure black anywhere. Type is warm.
- Do not use purple.
- Do not use gradients on any surface.
- Do not add border-radius greater than 2px to any element.

---

## 12 — Relationship to CustodyZero House

Type is a CustodyZero product. CustodyZero's identity is **local data custody** — your data, your machine, your control. This principle is expressed differently across products:

- **CustodyZero house** and **Archon** express it through the dark visual language: near-black backgrounds, amber/blue accents, Bebas Neue display type.
- **Type** expresses it through warmth and the physical metaphor of paper: light backgrounds, ink and pencil, Cormorant display type.

The brand principle is shared. The visual language is distinct.

### Inheritance

- Type inherits the CustodyZero **ethos**: local-first, user-owned, no cloud dependency.
- Type does **not** inherit the CustodyZero visual stack (dark backgrounds, Bebas Neue, amber).
- On pages that link back to CustodyZero, the parent brand appears in a footer or secondary attribution only — it does not compete with the Type identity.
- The CustodyZero wordmark and Type wordmark must not compete on the same surface. One leads, one supports.

---

## Asset Generation

Assets in this directory are generated by `scripts/generate-type.py`.

To regenerate:
```sh
python3 scripts/install-cormorant.py   # install Cormorant Light if not present
python3 scripts/generate-type.py
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
