# CustodyZero Brand Guidelines

Parent document: `../../design-system/custodyzero-design-system.docx`
Version: 1.0 · February 2026

---

## Wordmark

**File:** `../wordmark/custodyzero-wordmark-dark.svg`

### Specification

| Property | Value |
|---|---|
| Canvas | 480 × 80 px |
| Background | Transparent |
| Font | Bebas Neue (display); fallback: sans-serif condensed stack |
| `CUSTODY` color | `#F2F2EC` (token: `--white`) |
| `ZERO` color | `#D4880A` (token: `--amber`) |
| Letter-spacing | `0.15em` |
| Font-size | `83.7px` (calibrated to fill 474px at 0.15em spacing) |
| Text alignment | Left-aligned (`x: 3, text-anchor: start`) |
| Baseline y | `69.5px` (approx. 10.5px top clearspace, 10.5px bottom) |
| Color split technique | Two overlapping text elements, `clipPath` at `x=318.6px` (font advance boundary between Y and Z) |

### Available Files

| File | Dimensions | Use |
|---|---|---|
| `custodyzero-wordmark-dark.svg` | 480 × 80 | Primary, all digital contexts |
| `custodyzero-wordmark-dark@2x.png` | 960 × 160 | Retina / HiDPI screens |
| `custodyzero-wordmark-dark@3x.png` | 1440 × 240 | Ultra-HiDPI / print at small physical size |
| `custodyzero-cz-dark.svg` | 154 × 80 | CZ monogram, compact contexts |
| `custodyzero-cz-dark@2x.png` | 308 × 160 | CZ monogram retina |
| `custodyzero-cz-dark@3x.png` | 462 × 240 | CZ monogram ultra-HiDPI |

---

## Icon Mark

**File:** `../icon/custodyzero-icon-dark.svg`

### Design Description

A circle outline bisected by a horizontal line that extends 4px beyond the circle boundary on each side.

- **Circle:** boundary, containment, zero — the enclosing constraint
- **Horizontal line:** threshold — the defined limit the system enforces

The mark is architectural, not illustrative. It contains no locks, shields, or surveillance imagery. It reads as a cross-section or dimension annotation drawn in plan view.

### Specification

| Property | Value |
|---|---|
| Canvas | 64 × 64 px |
| Background | Transparent |
| Circle | `cx=32, cy=32, r=22, stroke-width=2.5` |
| Threshold line | `x1=6, y1=32, x2=58, y2=32, stroke-width=2.5, stroke-linecap=square` |
| Stroke color | `#D4880A` (token: `--amber`) |
| Fill | None |

### Available Files

| File | Contents | Use |
|---|---|---|
| `custodyzero-icon-dark.svg` | 64 × 64 source | All vector use, app icons |
| `custodyzero-icon-dark.ico` | 16 × 16, 32 × 32, 48 × 48 | Favicon, Windows icon |

---

## Color Tokens

These are the canonical values from the design system. All brand assets reference tokens — never raw hex values in code.

| Token | Hex | Usage |
|---|---|---|
| `--black` | `#0A0A0A` | Primary background |
| `--dark` | `#111111` | Card / panel background |
| `--mid` | `#1A1A1A` | Hover state background |
| `--border` | `#242424` | Dividers, outlines |
| `--muted` | `#444444` | Disabled text |
| `--text` | `#C8C8C0` | Body copy |
| `--light` | `#E8E8E0` | Secondary display text |
| `--white` | `#F2F2EC` | Primary display text, wordmark `CUSTODY` |
| `--amber` | `#D4880A` | Primary accent, wordmark `ZERO`, icon mark |
| `--amber-bright` | `#F0A020` | Amber hover state |
| `--amber-dim` | `#8A5500` | Tags, secondary amber |

Amber is the only accent color in the CustodyZero house palette. It appears sparingly. Product sub-brands (Archon, Sentinel) define their own accent colors — those colors do not appear in house-level contexts.

---

## Asset Naming Convention

```
{brand}-{asset-type}-{variant}[@scale].{ext}
```

| Segment | Values |
|---|---|
| `{brand}` | `custodyzero`, `archon`, `sentinel` |
| `{asset-type}` | `wordmark`, `icon` |
| `{variant}` | `dark` (dark background; only defined variant) |
| `[@scale]` | omit for 1x SVG; `@2x`, `@3x` for raster |
| `{ext}` | `svg`, `png`, `ico` |

Examples: `custodyzero-wordmark-dark.svg`, `custodyzero-icon-dark@2x.png`

---

## Clearspace Rules

Minimum clearspace on all four sides = the cap height of the wordmark.

At 1x: cap height ≈ **44px**. No logotype, text, graphic, or edge may intrude within this zone.

For the icon mark: minimum clearspace = **12px** on all sides (relative to the 64px canvas — i.e., the icon must not appear in a container smaller than 88 × 88px).

---

## Minimum Size Rules

| Asset | Minimum display size | Reason |
|---|---|---|
| Wordmark SVG | 240 × 40 px | Below this, letter-spacing collapses legibility |
| Wordmark PNG | Use `@2x` or `@3x` file | Never upscale rasters |
| Icon SVG | 24 × 24 px | Circle + line remain distinct |
| Icon ICO | 16 × 16 px | Minimum viable favicon |

---

## Background Usage

The wordmark is defined for **dark backgrounds only**. The only valid background stack is:

- `#0A0A0A` (Black)
- `#111111` (Dark)
- `#1A1A1A` (Mid)

A light-background / reverse variant is not yet defined. Do not place the wordmark on light backgrounds until that variant is produced.

---

## What Not To Do

- Do not recolor `CUSTODY` or `ZERO`. Both colors are fixed.
- Do not stretch, skew, or scale the wordmark non-uniformly.
- Do not add drop shadows, glows, or any treatment to the wordmark.
- Do not place the wordmark on a light or colored background.
- Do not reduce letter-spacing or change the typeface.
- Do not combine the wordmark with a product name (Archon, Sentinel). Product names stand alone with clear visual separation.
- Do not use the icon mark in amber on any non-dark background.
- Do not substitute Inter, Roboto, or system-default fonts for Bebas Neue in any brand context.
- Do not add border-radius to any button or interactive element in CustodyZero contexts. Square edges are required.
- Do not use purple or purple gradients anywhere. This is an explicit constraint from the design system.

---

## Rights

All assets in this directory are proprietary.
See `../../../LICENSE` for terms.
All rights reserved. CustodyZero.
