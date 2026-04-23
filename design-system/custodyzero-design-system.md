# CustodyZero Design System

**Version:** 1.1 · April 2026
**Confidential — Internal Use**

This document defines the visual language, brand voice, and design tokens for CustodyZero and its product house. All product identities — StationZero, Archon, and future products — inherit from this foundation.

---

## 01 — Brand Foundation

### Mission

CustodyZero builds powerful technology that stays where it belongs. On your hardware. Under your rules. Out of everyone else's hands.

### North Star

**Empowering people, not the company providing the technology.**

Every product decision runs through this filter. If it empowers CustodyZero more than it empowers the user, it does not ship. This is not a marketing principle — it is an engineering constraint.

### The Thesis

The industry built useful technology on top of a bad trade: capability in exchange for data. Google Home works — and sends your footage to Google. AI agents coordinate — and no one knows exactly how. Smart devices learn your patterns — and so does every company behind them.

CustodyZero's answer is that the trade is not necessary. Capability and custody are not in conflict. We prove it with every product we ship.

### Brand Attitudes

**01 — We don't apologize for having opinions.**
CustodyZero has a thesis: the current model is a bad trade. We say that plainly — with calm confidence, not contempt. The opinion is always about the paradigm, never the people who built or use it. "Emergent orchestration was a necessary first step. What we build is what comes next."

**02 — We respect the user's intelligence.**
No hype. No "revolutionary." No "seamless." No "powerful." We say what things do. We use verbs. We trust the reader to evaluate the claim. Intelligence-respecting does not mean cold — it means precise and direct, with enough warmth that the reader feels invited, not audited.

**03 — We make the implicit explicit.**
This is both a product truth and a brand truth. Archon enforces explicit rules. StationZero keeps footage local and visible. CustodyZero products say what they do and do what they say. Translated to a human promise: you always know what a CustodyZero product is doing and why.

---

## 02 — Voice & Copy

### Voice Principles

**Short sentences win.**
CustodyZero does not meander. Every sentence earns its place or gets cut. If a sentence can be shorter without losing meaning, it should be.

**Verbs over adjectives.**
Do not say a product is powerful. Say what it does. Gates. Enforces. Validates. Prevents. Detects. The verb is the claim. The adjective is the hope.

**Name the problem. Don't dramatize it.**
Wrong: "Chaos reigns in agentic systems today." Right: "Most agent systems don't know what they're allowed to do. Archon does." Precision is more frightening than drama.

### Tone by Audience

| Audience | What They Need | How We Speak |
|---|---|---|
| Mature Operator | Technical precision, no hand-holding, proof over promise | Direct, architectural, specific. Specs and behavior, not feelings. |
| AI Enthusiast | Something worth belonging to, easy setup, clear control | Confident, clear, a degree of warmth. Smart but not cold. |
| Privacy-Conscious Consumer | Trust, plain language, no jargon, clear ownership | Human, direct. Translate technical truth into plain promise. |

### Words We Use / Words We Don't

| Use | Avoid |
|---|---|
| Enforces, gates, validates, prevents | Powerful, seamless, revolutionary |
| Your data stays yours | We take privacy seriously |
| On your hardware | Cloud-optional |
| Operator-defined | AI-powered |
| Deterministic | Smart |
| Decisions you authorized | Inference (for non-technical audiences) |
| The adult way | Next-generation |

---

## 03 — Color System

The CustodyZero palette is built around authority and restraint. Near-black foundations signal infrastructure. A single amber accent carries all the warmth, energy, and attention the brand needs. The palette does not decorate — it enforces hierarchy.

### Core Palette

| Token | Hex | Usage |
|---|---|---|
| Black | `#0A0A0A` | Primary background — page, hero, sections |
| Dark | `#111111` | Elevated background — cards, panels |
| Mid | `#1A1A1A` | Hover states, subtle elevation |
| Border | `#242424` | Dividers, grid lines, outlines |
| Muted | `#444444` | Disabled text, secondary labels |
| Text | `#C8C8C0` | Body copy on dark backgrounds |
| Light | `#E8E8E0` | Subheadings, secondary display text |
| White | `#F2F2EC` | Primary display text, hero headings |
| Amber | `#D4880A` | Primary accent — CTAs, highlights, dividers |
| Amber Bright | `#F0A020` | Hover state for amber elements |
| Amber Dim | `#8A5500` | Subtle amber — tags, secondary labels |

### Usage Rules

- Amber is the only accent color in the CustodyZero house palette. It appears sparingly — on interactive elements, dividers, status indicators, and emphasis. Never use amber for decoration.
- Product sub-brands (Archon, StationZero) may introduce their own accent colors. These accents must not appear in house-level contexts. Amber is always the house color.
- Never use pure white (`#FFFFFF`) or pure black (`#000000`). The slight warmth of the palette is intentional — it reads as engineered, not sterile.
- Background layering follows a strict order: Black → Dark → Mid. Never skip a level. Depth is created through this stack, not through shadows.

---

## 04 — Typography

Three typefaces. Each has a strict role. They do not substitute for each other.

| Typeface | Role | Usage |
|---|---|---|
| Bebas Neue | Display / Authority | Hero titles, product names, section headers, the wordmark. Uppercase always. Tight tracking. Never for body copy. |
| Fraunces | Optical Serif / Voice | Pull quotes, narrative body copy, the human voice of the brand. Light weight (300), italic for emphasis. Provides warmth inside the severity. |
| DM Mono | Monospace / Function | Navigation, labels, CTAs, eyebrows, code, tags, form inputs. The default UI font. Signals precision and function. |

### Type Scale

| Role | Size | Font | Notes |
|---|---|---|---|
| Hero / Display | `clamp(4rem–9rem)` | Bebas Neue | Line height 0.95. Tight letter-spacing. |
| Section Header | `3.5rem` | Bebas Neue | Used with section label above. |
| Product Name | `3rem` | Bebas Neue | Inside product cards. |
| Manifesto H2 | `clamp(1.8–2.6rem)` | Fraunces 300 | Italic emphasis in amber. |
| Body / Narrative | `clamp(1–1.25rem)` | Fraunces 300 | Line height 1.6. Max-width 580px. |
| UI / Navigation | `0.72–0.8rem` | DM Mono | Uppercase. Letter-spacing 0.12–0.25em. |
| Labels / Eyebrows | `0.65rem` | DM Mono | Uppercase. Amber. Spacing 0.25em. |
| Code / Tokens | `0.78–0.9rem` | DM Mono | Amber color on dark background. |

---

## 05 — Design Tokens

These are the CSS custom properties that implement the color system. All components reference tokens, never raw hex values. This ensures global changes propagate correctly.

### CSS Custom Properties

| Token | Value | Usage |
|---|---|---|
| `--black` | `#0A0A0A` | Primary background |
| `--dark` | `#111111` | Card / panel background |
| `--mid` | `#1A1A1A` | Hover state background |
| `--border` | `#242424` | All borders and dividers |
| `--muted` | `#444444` | Disabled / secondary text |
| `--text` | `#C8C8C0` | Body copy |
| `--light` | `#E8E8E0` | Secondary display text |
| `--white` | `#F2F2EC` | Primary display text |
| `--amber` | `#D4880A` | Primary accent |
| `--amber-bright` | `#F0A020` | Amber hover state |
| `--amber-dim` | `#8A5500` | Subtle amber / tags |

### Spacing Scale

All spacing is based on a 8px base unit. Components use multiples of this unit.

| Token | Value | Typical Use |
|---|---|---|
| `--space-1` | `8px` | Micro gaps, icon padding |
| `--space-2` | `16px` | Inline element spacing |
| `--space-3` | `24px` | Component internal padding |
| `--space-4` | `32px` | Section sub-element gaps |
| `--space-6` | `48px` | Card padding, section dividers |
| `--space-8` | `64px` | Large component margins |
| `--space-12` | `96px` | Section padding (mobile) |
| `--space-16` | `128px` | Section padding (desktop) |

---

## 06 — Component Patterns

### Buttons

**Primary Button**
Background: `--amber`. Text: `--black`. Font: DM Mono, `0.75rem`, uppercase, letter-spacing `0.15em`. Padding: `1rem 2.5rem`. No border-radius — square edges. Hover: `--amber-bright`, `translateY(-1px)`.

**Ghost / Text Button**
No background, no border. Text: `--muted`. Font: DM Mono, `0.72rem`, uppercase. Hover: `--light`. Used for secondary actions alongside a primary button.

**Outline Button (Nav)**
Border: `1px solid --amber-dim`. Text: `--amber`. Hover: background `--amber`, text `--black`. Used in navigation context only.

### Form Inputs

Background: `--mid`. Border: `1px solid --border`. Focus border: `--amber`. Text: `--white`. Placeholder: `--muted`. Font: DM Mono, `0.8rem`. Padding: `1rem 1.2rem`. No border-radius. Connects flush to submit button with right border removed.

### Cards / Product Panels

Background: `--dark`. Hover: `--mid`. Top border animated on hover: `2px solid --amber`, `scaleX` from 0 to 1 with `transform-origin: left`. Padding: `3rem`. No border-radius. `1px --border` gap between adjacent cards.

### Section Labels / Eyebrows

Font: DM Mono. Size: `0.65rem`. Color: `--amber`. Uppercase. Letter-spacing: `0.25em`. Always appear above a heading. Never standalone.

### Dividers

Two types: standard (`1px solid --border`) and accent (`2px solid --amber`, used sparingly for section breaks). Never decorative — always structural.

### Status Indicators

"Coming soon" — DM Mono, `0.65rem`, uppercase, `--muted`. Active / In Development — DM Mono, `0.65rem`, uppercase, `--amber` with a 6px pulsing dot before it.

---

## 07 — Motion & Animation

Motion is used for exactly two purposes: revealing content as it enters the viewport, and providing feedback on interactive elements. It is never decorative.

### Page Load Sequence

Hero elements animate in with a staggered fadeUp pattern. Delay increments of `0.2s`. Duration: `0.8s ease`. The sequence runs once on load and does not repeat.

```
opacity: 0 → 1  |  translateY: 20px → 0  |  duration: 0.8s ease
```

### Scroll Reveal

Elements outside the initial viewport use an `IntersectionObserver` with threshold `0.1`. On entry, the element transitions to `opacity: 1` and `translateY: 0` over `0.7s`. Stagger delay of `80ms` per element in a batch.

### Hover States

- Button backgrounds: `0.2s ease`
- Card backgrounds: `0.3s ease`
- Top border reveal on cards: `0.4s ease`, `transform-origin: left`
- Nav link underlines: `0.2s ease`
- No duration exceeds `0.4s` for interactive feedback.

### Pulse Animation

Used only for active status indicators. `2s infinite`, `opacity 1 → 0.3 → 1`. Amber color. 6px circle.

---

## 08 — Layout & Grid

### Page Structure

Full-width sections with `max-width: 1100px` content container, centered. Section padding: `8rem 3rem` desktop, `5rem 1.5rem` mobile. Sections separated by `1px --border` top border, not whitespace.

### Grid Patterns

**Two Column (Manifesto pattern)**
`1fr / 2fr`. Left column: sticky label. Right column: content. Gap: `4rem`. Collapses to single column on mobile.

**Two Column (Equal)**
`1fr / 1fr` with `1px --border` gap, background `--border`. Used for product cards. Collapses to single column on mobile.

**Two Column (Capture pattern)**
`1fr / 1fr`. Left: copy. Right: form. Gap: `4rem`. Collapses to single column on mobile.

### Navigation

Fixed position. Transparent until scroll > 40px, then: `border-bottom: 1px solid --border`, `background: rgba(10,10,10,0.92)`, `backdrop-filter: blur(12px)`. Padding: `1.5rem 3rem`. Logo left, CTA right.

### Breakpoints

| Breakpoint | Value | Behavior |
|---|---|---|
| Mobile | `≤ 768px` | Single column. Padding `1.5rem`. Nav padding `1.2rem`. |
| Desktop | `> 768px` | Multi-column grids active. Full padding and spacing. |

---

## 09 — Product Identity

CustodyZero is the house. Each product inherits the house foundation and adds its own identity layer. Products are distinct but recognizably related.

### Inheritance Rules

- **Dark foundation:** all products share the near-black background stack.
- **Typefaces:** Bebas Neue and DM Mono carry across all products. Fraunces is a house-level voice font — product pages may substitute a different serif.
- **Voice:** all three brand attitudes apply to all products. Tone calibrates per audience, attitudes do not change.
- **Amber is the house accent.** Products have their own accent color. The house accent does not appear as primary on product pages.

### Product Naming Convention

CustodyZero products fall into two structural categories. The naming convention signals which category a product belongs to.

**Standalone products** are named with a single plain English word. They do one thing. They do not expand into adjacent domains, contain sub-products, or become platforms. The name describes what the product is or what the user does with it.

Examples: Type, Factory, Edit

Standalone names are:

- One word
- Plain English — no jargon, no acronyms, no invented words
- Grounded and literal — the name describes the product through direct reference, not metaphor
- Archon is the sole exception to the literal register — its classical name predates this convention

**Platform product houses** are named with a compound word using the `[X]Zero` suffix. They are products that, by nature, expand into multiple capability domains and contain sub-products or modules. The `Zero` suffix signals that the product is a CustodyZero platform — a product house within the product house.

Examples: StationZero

The `[X]Zero` pattern:

- Immediately identifies the product as a CustodyZero platform
- Carries the house thesis: zero cloud dependency, zero compromise, zero unauthorized access
- Visually mirrors the parent brand construction (CustodyZero → StationZero)
- Is reserved for products that genuinely earn platform status — a product that does one thing does not use this pattern, regardless of ambition or roadmap

**Choosing between the two:** if a product will always be a single tool with a defined scope, it is standalone. If a product will contain multiple capability domains, expand into adjacent functions, and operate as its own product house, it uses the `[X]Zero` pattern. This is a structural decision, not a branding preference. A product does not graduate from standalone to platform — if the scope is uncertain, resolve it before naming.

**A standalone product does not graduate to platform status.** If a product was designed as standalone and later feels constrained by that scope, the constraint is correct — the original design intent was single-purpose. Expanding a standalone product into a platform is a failure of forethought, not a natural progression.

The legitimate path to a new `[X]Zero` platform is **convergence**: when multiple standalone products reveal a shared substrate or natural integration surface that justifies unifying them under a single platform identity. This is consolidation — distinct products merging into a coherent whole — not a single product accumulating features. The distinction matters: one is architectural recognition, the other is scope creep.

### Product Register

| Product | Category | Structure | Accent Color | Design Character |
|---|---|---|---|---|
| Archon | Agent Coordination | Standalone | Electric blue `#4FC3F7` | Architectural, system-like, brutalist precision. Enforcement as aesthetic. |
| StationZero | Home Edge Automation | Platform product house | Signal red `#C04848` | Operational clarity with domestic confidence. |
| Type | Writing | Standalone | Pencil `#8B3A3A` | Warm, paper metaphor, literary. |
| Factory | Software Production | Standalone | Industrial green `#5A9A6E` | Utilitarian, restrained, unadorned. |
| Valet | Local Inference Personal Intelligence | Standalone | Bronze B·04 `#9D7E49` | Classical attendance, bookbound continuity, refined restraint. |

*Valet is also published under the fallback name **Steward** pending trademark clearance. Both names share every brand decision; only the wordmark text differs.*

### Wordmark

The CustodyZero wordmark is the product house logotype. "Custody" in `--white`, "Zero" in `--amber`. Font: Bebas Neue. Letter-spacing: `0.15em`. Used on dark backgrounds only. For light context use the full-dark reverse variant (not yet defined — avoid light backgrounds).

The wordmark is not modified, stretched, recolored, or combined with product names. Product names stand alone beneath or beside the wordmark with clear separation.

### Icon Mark

A minimal geometric mark is required for favicon, app icon, and small-format use where the wordmark is not legible. The mark should imply boundary, threshold, or containment — architectural rather than illustrative. No locks, shields, or surveillance iconography.

Status: To be designed. The mark will be defined and added to this document in v1.1.

---

## 10 — What We Never Do

These are not guidelines. They are constraints.

- **No purple.** No purple gradients. No purple anything. This is the single most common AI brand color and we are not an AI company — we are a hardware and infrastructure company that uses AI.
- **No border-radius on primary interactive elements.** Buttons and inputs are square. Rounded corners signal approachability. We signal precision.
- **No stock imagery.** No lifestyle photography. No hands holding devices. No smiling people in front of computers. Visuals are geometric, architectural, or typographic.
- **No emojis in brand contexts.** Not in copy, not in documentation headers, not in social posts under the CustodyZero handle.
- **No passive copy.** "Your data may be kept local" is not acceptable. "Your data stays on your hardware" is the standard.
- **No Inter, Roboto, or system fonts in brand contexts.** These are defaults. Defaults signal that no decision was made.
- **No naming competitors by name in brand copy.** The challenger position is implicit. Name the paradigm, not the company.
- **No sending user data to third-party services without explicit documentation and user consent.** This applies to analytics, email capture, error tracking, and any other instrumentation.

---

CustodyZero Design System v1.1
April 2026 · Internal Use Only
*Empowering people, not the company providing the technology.*
