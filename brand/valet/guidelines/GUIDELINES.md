# Valet Brand Guidelines

**Parent document:** CustodyZero Design System v1.1 · Valet Product Identity Addendum
**Status:** Assets generated v1.0 · All design decisions locked
**Version:** 1.0 · April 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 0 — What Valet Is

Valet is the CustodyZero product that runs a silicon-optimized Gemma 4 model as a **lifelong local personal intelligence** on user hardware. It learns the user over time, acts through user-provided substrate (Drive, iCloud, OneDrive), and runs unlimited local inference. The brand register is a **classical gentleman's valet** — present but not forward, attentive but not servile, enduring by design.

Valet is a standalone product in the CustodyZero product naming convention — single plain-English word, classical role, parallels Archon.

**Parallel product:** *Steward* is the pre-vetted fallback name. Every design decision in this document applies identically to Steward — only wordmark text differs. If the Valet trademark path fails, Steward ships with the full brand in place.

---

## 1 — Wordmark

### Generated files

| File | Format | Canvas | Usage |
|---|---|---|---|
| `valet-wordmark-dark.svg` | SVG | 174 × 72 px | Primary — white mark for dark backgrounds |
| `valet-wordmark-dark@2x.png` | PNG/RGBA | 348 × 144 | Screen 2× density, white mark |
| `valet-wordmark-dark@3x.png` | PNG/RGBA | 522 × 216 | Screen 3× density, white mark |
| `valet-wordmark-bronze.svg` | SVG | 174 × 72 px | Variant — bronze mark for surfaces where white does not read |
| `valet-wordmark-bronze@2x.png` | PNG/RGBA | 348 × 144 | Screen 2× density, bronze mark |
| `valet-wordmark-bronze@3x.png` | PNG/RGBA | 522 × 216 | Screen 3× density, bronze mark |

### Wordmark anatomy

- **Typeface:** Bebas Neue Regular (embedded as base64 in SVG + Google Fonts CDN fallback)
- **Font size:** 72 px on 72 px canvas height
- **Letter-spacing:** `0.12 em`
- **Decoration:** None. The wordmark is unadorned — Valet's restraint is its identity.
- **Canvas:** transparent background, dynamic width based on glyph metrics — text is left-aligned at `x = 3 px`

### Usage

**Primary usage (dark variant):** white wordmark `#F2F2EC` (`--white`) on dark backgrounds.
This is the canonical form. Use in all user-facing, documentation, and integration contexts.

**Bronze variant:** bronze wordmark `#9D7E49` (`--bronze`) for surfaces where the white mark would not read — for example, on light neutral surfaces. Use sparingly; the dark variant is strongly preferred.

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
- Do not recolor outside the approved dark and bronze variants.
- Do not apply drop shadows, glows, gradients, or any effects to the wordmark.
- Do not add a horizontal rule, underline, or other decorative element to the wordmark.
- Do not reduce the white wordmark opacity below 100%.
- Do not place the wordmark on purple or amber backgrounds.
- Do not use amber (`#D4880A`) on or adjacent to Valet brand elements — amber belongs to the CustodyZero house only.
- Do not use electric blue (`#4FC3F7`) on or adjacent to Valet brand elements — blue belongs to Archon only.
- Do not use pencil (`#8B3A3A`) on or adjacent to Valet brand elements — pencil belongs to Type only.
- Do not use industrial green (`#5A9A6E`) on or adjacent to Valet brand elements — green belongs to Factory only.
- Do not use signal red (`#C04848`) on or adjacent to Valet brand elements — signal red belongs to StationZero only.

---

## 2 — Icon Mark

### Generated files

| File | Format | Dimensions | Usage |
|---|---|---|---|
| `valet-icon-dark.svg` | SVG | 64 × 64 px | Source master |
| `valet-icon-dark.ico` | ICO | 3 frames: 16 × 16, 32 × 32, 48 × 48 | Favicon, OS icon |
| `valet-icon-dark@2x.png` | PNG/RGBA | 128 × 128 px | Screen 2× density |
| `valet-icon-dark@3x.png` | PNG/RGBA | 192 × 192 px | Screen 3× density |

### Icon mark anatomy

**Design:** The Binding — three horizontal marks of varying width, stacked. The form references the visible bookbinding marks on a well-kept spine: the evidence of pages gathered, bound, and enduring.

- **Top bar (head band):** horizontal line from `x = 22` to `x = 42`, at `y = 20` (20 px wide)
- **Center bar (gather):** horizontal line from `x = 14` to `x = 50`, at `y = 32` (36 px wide — widest)
- **Bottom bar (tail band):** horizontal line from `x = 22` to `x = 42`, at `y = 44` (20 px wide)
- **Stroke weights:** 2.5 px for top and bottom bars · **3.5 px for center bar** (the emphasized gather)
- **Stroke-linecap:** square
- **Color:** `#9D7E49` (`--bronze`) on transparent
- **Vertical spacing:** 12 px between bar centers

The center bar is intentionally thicker. It represents the bound gather — the main line of thought held together by the binding. Outer bars represent head and tail bands. The register is architectural, not illustrative: no literal books, no pages, no binding tools.

**Legibility at small sizes:**

| Size | Top / bottom bars | Center bar | Notes |
|---|---|---|---|
| 64 × 64 | 20 px wide · stroke 2.5 | 36 px wide · stroke 3.5 | Master size |
| 48 × 48 | 15 px · stroke 1.9 | 27 px · stroke 2.6 | ICO frame 3 |
| 32 × 32 | 10 px · stroke 1.25 | 18 px · stroke 1.75 | ICO frame 2 |
| 16 × 16 | 5 px · stroke 0.625 | 9 px · stroke 0.875 | ICO frame 1 — narrow-wide-narrow silhouette preserved |

### Usage

- Use the icon mark for favicon, app icon, and all small-format contexts where the wordmark is not legible.
- The icon mark appears in `#9D7E49` (`--bronze`) on dark backgrounds (primary).
- Minimum size: 16 × 16 px (covered by the ICO).

### What never to do

- Do not equalize the bar widths. The narrow-wide-narrow silhouette is structural — equal widths collapse the icon into a hamburger-menu reading.
- Do not equalize the stroke weights. The thicker center bar is the accent; the outer bars must be thinner.
- Do not add a fourth bar or remove one. Three bars is the locked geometry.
- Do not fill between the bars or add a background box.
- Do not add drop shadows or glows to the icon.
- Do not combine the icon with text at small sizes (< 32 px). Let the icon stand alone.
- Do not stretch or distort the icon.
- Do not rotate the icon to a vertical orientation.

---

## 3 — Icon Motion · The Thinking/Busy State

### When Valet is thinking

When the product is processing, considering, or actively working, the icon animates with the **Sweep** motion — sequential opacity illumination of the three bars, top → center → bottom.

### Sweep specification

```css
/* The bars dim to 0.40 opacity at rest; each lifts to 1.00 in sequence */
.valet-icon .bar                  { opacity: 0.40; }
.valet-icon .bar-top    { animation: valet-sweep 2.4s cubic-bezier(0.37, 0, 0.63, 1) infinite;                       }
.valet-icon .bar-center { animation: valet-sweep 2.4s cubic-bezier(0.37, 0, 0.63, 1) infinite; animation-delay: 0.4s; }
.valet-icon .bar-bottom { animation: valet-sweep 2.4s cubic-bezier(0.37, 0, 0.63, 1) infinite; animation-delay: 0.8s; }

@keyframes valet-sweep {
  0%, 100% { opacity: 0.40; }
  20%, 30% { opacity: 1.00; }
  50%      { opacity: 0.40; }
}

@media (prefers-reduced-motion: reduce) {
  .valet-icon .bar,
  .valet-icon .bar-top,
  .valet-icon .bar-center,
  .valet-icon .bar-bottom {
    animation: none !important;
    opacity: 1.00 !important;
  }
}
```

### States

| State | Cycle duration | When |
|---|---|---|
| **Ambient (thinking)** | 2.4 s | Idle between prompts · watching · ready |
| **Active (busy)** | 1.6–1.8 s | Active inference · processing · writing |

**Only the cycle duration changes between states.** Opacity range, easing, delays, and amplitude are held constant — the brand does not break register when working harder.

### Motion constraints

- Animate **only `opacity`**. No transform, no layout animation.
- Do not speed up past 1.6 s — faster reads as consumer-AI frantic, breaking register.
- Do not slow past 3.0 s — slower reads as stalled.
- Do not add second-tier animations (rotation, scale pulse, color shift). The sweep is the entire motion vocabulary.
- **Always** ship with the `prefers-reduced-motion` fallback. Users who have opted out of motion see the static icon at full opacity.

---

## 4 — Voice Serif · Cardo

### What Cardo is for

Cardo is Valet's **reading and speaking voice** — body prose, pull quotes, tagline copy, inline emphasis, anywhere a warmer voice than DM Mono is needed. It is not the display type (Bebas Neue holds that) and it is not UI chrome (DM Mono holds that).

### Specification

- **Typeface:** Cardo · David J. Perry · open-source scholar's typeface, transitional classification based on Renaissance forms
- **Source:** Google Fonts
- **Weights in use:** 400 regular · 700 bold · 400 italic (this is Cardo's full weight palette)
- **Import URL:**
  ```
  https://fonts.googleapis.com/css2?family=Cardo:ital,wght@0,400;0,700;1,400&display=swap
  ```

### Roles

| Context | Weight | Size |
|---|---|---|
| Body prose (long-form) | 400 | 17 px · 1.65 leading · max 65 ch line |
| Body prose (UI) | 400 | 15–16 px · 1.6 leading |
| Pull quote | 400 | 32–40 px · 1.25 leading |
| Inline emphasis | 400 italic | inherit size |
| Strong emphasis | 700 | inherit size |
| Lede / opening paragraph | 400 | 18 px · 1.6 leading |

### Pairing with the house

Cardo coexists with:

- **Bebas Neue** — display type (wordmark, headings, eyebrows). Does not overlap with Cardo's role.
- **DM Mono** — UI chrome (labels, metadata, code, navigation). Uppercase, tight tracking.

On any Valet surface, the three-font system resolves like this: Bebas Neue for identification and hierarchy, Cardo for what the product says, DM Mono for what the product shows. Do not use Cardo for UI labels. Do not use DM Mono for prose. Do not use Bebas Neue for body.

### What never to do

- Do not substitute Cardo with Fraunces. Fraunces is Type's voice — the products must be typographically distinct.
- Do not substitute Cardo with Cormorant, Crimson, Playfair Display, EB Garamond, or any other "classical reflex" serif.
- Do not use Cardo at weights other than 400 or 700. Intermediate weights do not exist in the font.
- Do not use Cardo for body text below 14 px — the transitional contrast thins at small sizes.

---

## 5 — Color on Color

| Foreground | Background | Status |
|---|---|---|
| White wordmark (`#F2F2EC`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | `--dark` (`#111111`) | **Approved** |
| White wordmark (`#F2F2EC`) | `--mid` (`#1A1A1A`) | **Approved** |
| Bronze wordmark (`#9D7E49`) | `--black` (`#0A0A0A`) | **Approved — 5.20 : 1** |
| Bronze wordmark (`#9D7E49`) | `--dark` (`#111111`) | **Approved — 4.81 : 1** |
| Bronze wordmark (`#9D7E49`) | `--mid` (`#1A1A1A`) | **Approved — 4.36 : 1** |
| Bronze icon (`#9D7E49`) | `--black` (`#0A0A0A`) | **Approved — primary** |
| White wordmark (`#F2F2EC`) | White or light surface | **Never** |
| Bronze wordmark (`#9D7E49`) | Bronze surface | **Never** |
| Bronze wordmark (`#9D7E49`) | Amber (`#D4880A`) surface | **Never** — house-member confusion |
| Any mark | Purple or gradient background | **Never** |

---

## 6 — Accent Tokens

| Token | Hex | OKLCH | Role |
|---|---|---|---|
| `--bronze` | `#9D7E49` | `oklch(0.54 0.075 82)` | Primary accent — wordmark, icon, filled buttons, active state |
| `--bronze-dim` | `#5C4A2D` | `oklch(0.34 0.050 82)` | Reduced emphasis — tags, inactive borders, quiet backgrounds, muted state |

Single-token system. The bronze anchor clears WCAG UI-component 3:1 on all house backgrounds, and clears 4.5:1 AA Normal on `#0A0A0A` and `#111111` — no split decorative/functional token pair required.

---

## 7 — What Not To Do

- **Do not use the Valet mark to imply agentic autonomy.** Valet is present, attentive, and acts on behalf of the user. It is not an "agent" that executes autonomous tasks in the builder-economy sense. The mark must not appear in contexts that suggest Valet replaces the user's judgment.
- **Do not use "personal intelligence" or "Personal Intelligence" as a category descriptor in Valet marketing.** That phrase is Google/Apple's marketing category for cloud-tenanted AI (Gemini Personal Intelligence, Apple Intelligence). Valet is a different architecture — say what it is (local, resident, continuous) rather than what category it's in.
- **Do not apply amber to Valet brand elements.** Amber (`#D4880A`) is the CustodyZero house accent. It may appear in house-level navigation or footer contexts linking back to CustodyZero only.
- **Do not apply any sibling product accent to Valet brand elements.** Blue (Archon), pencil (Type), green (Factory), signal red (StationZero) are product-scoped and must not cross.
- **Do not use purple, violet, or blue-purple** adjacent to the Valet mark.
- **Do not use consumer-AI visual language:** gradient orbs, glowing sparkles, anthropomorphic blobs, pulsing hearts, spinning loaders.
- **Do not use service-worker iconography:** bells, keys, keyholes, trays, silver platters, butler silhouettes, doorbells. The valet register is carried by the word and the bookbinding mark, not by props.
- **Do not use Fraunces or Cormorant or any other "classical reflex" serif** adjacent to or in Valet brand contexts. Valet's voice serif is Cardo. Fraunces is Type's voice.
- **Do not animate the icon with motions outside the specified Sweep.** No rotation, no pulse-and-glow, no breathing scale, no character animation of the bars.
- **Do not omit the `prefers-reduced-motion` fallback.** The motion must gracefully disable for users who have opted out.

---

## 8 — Asset Naming Convention

```
valet-wordmark-[variant].[ext]
valet-wordmark-[variant]@[scale].png
valet-icon-[variant].[ext]
valet-icon-[variant]@[scale].png
valet-social-card.[ext]
```

**Variants:**
- `dark` — white mark on transparent background (primary)
- `bronze` — bronze mark on transparent background

**Scale suffixes:**
- `@2x` — 2× screen density
- `@3x` — 3× screen density
- No suffix — native/1× dimensions (SVG only)

**Extensions in use:** `.svg`, `.png`, `.ico`

---

## 9 — Relationship to CustodyZero House

- **Amber belongs to CustodyZero house only.** Valet amber does not exist. The Valet accent is `#9D7E49` (`--bronze`).
- **Each sibling product accent is scoped to its product.** Valet bronze does not appear in Archon, Factory, Type, or StationZero contexts.
- On pages that link back to CustodyZero, amber may appear in the parent brand link context only — not on Valet-branded elements.
- **The Valet wordmark and CustodyZero wordmark must not compete on the same surface.** One leads, one supports. In most Valet product contexts, the CustodyZero wordmark appears in a footer or secondary attribution only.
- Valet inherits the CustodyZero house foundation: dark background stack (`#0A0A0A` → `#111111` → `#1A1A1A`), Bebas Neue and DM Mono typefaces, square geometry constraint, no purple.
- Valet's voice serif (Cardo) is product-scoped. It does not appear in house-level CustodyZero surfaces, which use Fraunces (Type-adjacent) or no serif at all.

---

## 10 — Register and Voice

**Three words:** Discrete. Attentive. Enduring.

**Material register:** Hand-bound leather, tarnished brass, felt-lined wood, engraved type on a door plate, the polished silver of a well-tended service set. The discipline those materials carry — tactile warmth, restraint, permanence, refined quiet.

**Voice:** Classical but rendered in contemporary execution. No faux-Victorian cliché. No nostalgia. The prose is direct, quiet, and honest about what the product does — *it is present, it lives on your hardware, it does not leave*.

**Anti-voice:** Consumer-AI cheer, builder-economy hype, surveillance-as-service reassurance, subscription upsell, agent-swarm pitch decks.

---

## 11 — Asset Generation

Assets in this directory are generated by `scripts/generate-valet.py` and `scripts/generate-valet-social.py`.

To regenerate:
```sh
python3 scripts/install-fonts.py     # install Bebas Neue if not present
python3 scripts/generate-valet.py    # wordmark + icon (SVG / PNG / ICO)
python3 scripts/generate-valet-social.py   # social card (SVG + PNG)
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

Output is fully deterministic given the same fonts and input parameters.

---

## 12 — Parallel Product: Steward

Every decision in this document applies identically to Steward (`../steward/guidelines/GUIDELINES.md`) — only the wordmark text differs. Steward is the pre-vetted fallback name; the brand is ready to ship under either identity pending trademark clearance.

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
