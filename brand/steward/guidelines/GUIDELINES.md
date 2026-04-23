# Steward Brand Guidelines

**Parent document:** CustodyZero Design System v1.1 · Steward Product Identity Addendum
**Status:** Assets generated v1.0 · All design decisions locked · Parallel to Valet
**Version:** 1.0 · April 2026

All assets are proprietary. See `../../../LICENSE` for terms.
**All rights reserved. CustodyZero.**

---

## 0 — What Steward Is

Steward is the **pre-vetted fallback name** for the local-inference personal intelligence product currently provisional-named Valet. Every design decision — accent color, icon, motion, voice serif, register — is identical between Valet and Steward. If the Valet trademark path fails, Steward ships with the full brand already in place.

Steward is a standalone product in the CustodyZero product naming convention — single plain-English word, classical role, parallels Archon. The word *steward* carries a slightly broader scope than *valet* (a steward manages a domain; a valet attends a principal) — but the product behavior and brand register are the same.

See the Valet guidelines (`../../valet/guidelines/GUIDELINES.md`) for the full design rationale. This document captures the Steward-specific file paths; all design rules are identical.

---

## 1 — Wordmark

### Generated files

| File | Format | Canvas | Usage |
|---|---|---|---|
| `steward-wordmark-dark.svg` | SVG | 264 × 72 px | Primary — white mark for dark backgrounds |
| `steward-wordmark-dark@2x.png` | PNG/RGBA | 528 × 144 | Screen 2× density, white mark |
| `steward-wordmark-dark@3x.png` | PNG/RGBA | 792 × 216 | Screen 3× density, white mark |
| `steward-wordmark-bronze.svg` | SVG | 264 × 72 px | Variant — bronze mark for surfaces where white does not read |
| `steward-wordmark-bronze@2x.png` | PNG/RGBA | 528 × 144 | Screen 2× density, bronze mark |
| `steward-wordmark-bronze@3x.png` | PNG/RGBA | 792 × 216 | Screen 3× density, bronze mark |

### Wordmark anatomy

- **Typeface:** Bebas Neue Regular (embedded as base64 in SVG + Google Fonts CDN fallback)
- **Font size:** 72 px on 72 px canvas height
- **Letter-spacing:** `0.12 em`
- **Decoration:** None.
- **Canvas:** transparent background, dynamic width based on glyph metrics — text is left-aligned at `x = 3 px`

STEWARD is seven letters, so the canvas is wider than Valet's by design — the visual weight grows with the word. Both wordmarks share identical type, tracking, and baseline metrics.

### Usage

**Primary usage (dark variant):** white wordmark `#F2F2EC` (`--white`) on dark backgrounds.
**Bronze variant:** bronze wordmark `#9D7E49` (`--bronze`) for surfaces where the white mark would not read.

### Clearspace

Maintain minimum clearspace equal to the cap height of the wordmark on all four sides.
Cap height ≈ 62 px at native SVG size.

### Minimum size

- **SVG:** 160 px wide minimum. Do not use below this size.
- **PNG 2×:** 2× assets are production minimum.

### What never to do

Identical to Valet's wordmark prohibitions. See `../../valet/guidelines/GUIDELINES.md#1-wordmark` — all prohibitions apply equally to the Steward wordmark. In particular:

- Do not apply amber, blue, pencil, industrial green, or signal red to Steward brand elements.
- Do not apply effects (shadows, glows, gradients) to the wordmark.
- Do not stretch, rotate, or distort.

---

## 2 — Icon Mark

### Generated files

| File | Format | Dimensions | Usage |
|---|---|---|---|
| `steward-icon-dark.svg` | SVG | 64 × 64 px | Source master |
| `steward-icon-dark.ico` | ICO | 3 frames: 16 × 16, 32 × 32, 48 × 48 | Favicon, OS icon |
| `steward-icon-dark@2x.png` | PNG/RGBA | 128 × 128 px | Screen 2× density |
| `steward-icon-dark@3x.png` | PNG/RGBA | 192 × 192 px | Screen 3× density |

### Icon mark anatomy

The Steward icon is **identical** to the Valet icon — The Binding. Three horizontal marks of varying width, stacked, with a thickened center bar representing the bound gather.

- Top bar: `x=22→42, y=20` · stroke 2.5 · 20 px wide
- Center bar: `x=14→50, y=32` · stroke 3.5 · 36 px wide (accent, thicker)
- Bottom bar: `x=22→42, y=44` · stroke 2.5 · 20 px wide
- Color: `#9D7E49` (`--bronze`) · stroke-linecap square

See Valet's guidelines for full rationale, legibility table, and prohibitions: `../../valet/guidelines/GUIDELINES.md#2-icon-mark`.

---

## 3 — Icon Motion · The Thinking/Busy State

The Steward icon animates identically to the Valet icon — the **Sweep** motion. Full specification including CSS keyframes, cycle timings (2.4 s ambient, 1.6–1.8 s busy), easing (`cubic-bezier(0.37, 0, 0.63, 1)`), and `prefers-reduced-motion` fallback is in Valet's guidelines: `../../valet/guidelines/GUIDELINES.md#3-icon-motion--the-thinkingbusy-state`.

Apply the Valet motion CSS to Steward by substituting class names (`.valet-icon` → `.steward-icon`). Parameters are otherwise unchanged.

---

## 4 — Voice Serif · Cardo

Same voice serif as Valet: Cardo by David J. Perry, loaded from Google Fonts, 400 regular + 700 bold + 400 italic. Same roles (body prose, pull quotes, tagline copy, inline emphasis), same pairing with Bebas Neue (display) and DM Mono (UI chrome).

Full specification: `../../valet/guidelines/GUIDELINES.md#4-voice-serif--cardo`.

---

## 5 — Color on Color

Identical to Valet. All contrast ratios carry (Bronze clears WCAG UI-component 3:1 on every house background; clears AA Normal 4.5:1 on `#0A0A0A` and `#111111`). See `../../valet/guidelines/GUIDELINES.md#5-color-on-color`.

---

## 6 — Accent Tokens

Identical to Valet:

| Token | Hex | OKLCH | Role |
|---|---|---|---|
| `--bronze` | `#9D7E49` | `oklch(0.54 0.075 82)` | Primary accent |
| `--bronze-dim` | `#5C4A2D` | `oklch(0.34 0.050 82)` | Reduced emphasis |

---

## 7 — What Not To Do

All Valet prohibitions apply. See `../../valet/guidelines/GUIDELINES.md#7-what-not-to-do`.

Special note on the *steward* connotation: the word *steward* carries a slightly administrative register compared to *valet*'s personal-attendant register. Do not lean into stewardship-of-resources framing (management, allocation, oversight of distributed things) — that language pulls toward "platform" positioning, which this product is not. The classical service framing (at-post, attentive, discreet) is carried by the name already and does not need amplification in marketing.

---

## 8 — Asset Naming Convention

```
steward-wordmark-[variant].[ext]
steward-wordmark-[variant]@[scale].png
steward-icon-[variant].[ext]
steward-icon-[variant]@[scale].png
steward-social-card.[ext]
```

Variants and scale suffixes are identical to Valet.

---

## 9 — Relationship to CustodyZero House

Identical to Valet. See `../../valet/guidelines/GUIDELINES.md#9-relationship-to-custodyzero-house`.

---

## 10 — Register and Voice

Identical to Valet — **Discrete. Attentive. Enduring.** See `../../valet/guidelines/GUIDELINES.md#10-register-and-voice`.

---

## 11 — Asset Generation

Assets in this directory are generated by `scripts/generate-steward.py` and `scripts/generate-steward-social.py`.

To regenerate:
```sh
python3 scripts/install-fonts.py        # install Bebas Neue if not present
python3 scripts/generate-steward.py     # wordmark + icon (SVG / PNG / ICO)
python3 scripts/generate-steward-social.py   # social card (SVG + PNG)
```

Prerequisites: `pip install cairosvg Pillow fonttools brotli`

---

## 12 — Parallel Product: Valet

This product is the fallback name for the same product that ships as Valet. Every design decision in `../../valet/guidelines/GUIDELINES.md` applies here identically. If Steward becomes the primary (i.e. Valet TM clearance fails), the Valet assets are retired and the Steward assets ship unchanged.

---

For permissions: **brand@custodyzero.com**
All rights reserved. CustodyZero.
