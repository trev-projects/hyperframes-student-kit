# AI Operated — Design System

> Extracted from the Issue 04 Beehiiv paste HTML (`The free data analyst hiding in your Claude`).
> **This brand overrides `MOTION_PHILOSOPHY.md`.** AI Operated is a *warm-light editorial* brand,
> not the dark chrome aesthetic. Keep the philosophy's **discipline** (one idea per beat, motion at
> every cut, hold the outro, Law #11 timeline anchors, one unifying texture, callbacks) but invert
> the palette and texture.

## The brand in one line

`AI Operated.` is a Digiwell newsletter for business owners — "Your AI operating system, every
Thursday." Warm paper, editorial typography, terracotta accents. It reads like a well-set print
letter, not a tech dashboard. Calm, literate, practical.

## Colors

| Token | Hex | Role |
|---|---|---|
| **Paper** | `#F1ECE3` | Canvas. Backs every beat. (Beehiiv "Post Background") |
| **Paper Deep** | `#E8E0CF` | Outer background / secondary panels |
| **Ink** | `#1F1B17` | Headlines, wordmark, primary type |
| **Body** | `#4B433A` | Body copy |
| **Muted** | `#8B8173` | Eyebrow labels, captions, de-emphasis |
| **Terracotta** | `#B5532E` | THE accent. Section labels, links, the wordmark period, CTA card fill |
| **Sand** | `#DDB892` | Highlighter swash under "Operated", CTA button fill |
| **Card** | `#FFFFFF` | Card surfaces |
| **Card Border** | `#C49A70` | Tan 1px card border, 14px radius |
| **Card Divider** | `#E0D6C4` | Inner row dividers |
| **Rule** | `rgba(31,27,23,0.12)` | Hairline section rules — the unifying texture |
| **On-Terracotta** | `#F1ECE3` / `#F8F1E9` / `#F4E7DC` | Type on the terracotta CTA card |

**Discipline:** terracotta is the only recurring accent. Sand appears as the highlighter and the
button. Everything else is paper, ink, and warm grey. No blue, no lime, no chrome gradients.

## Typography

- **Sora** 700–800 — display. Wordmark, all headlines. Tight tracking (`-0.5px` to `-1px`).
- **Manrope** 500 — body copy and subheads. `line-height: 1.55–1.7`.
- **JetBrains Mono** 600 — eyebrow labels, issue meta, list numerals. Uppercase, `1.5–2.4px`
  letter-spacing.

No serif, no italic. Mono is for labels and numerals only, never body.

## The wordmark (the signature element)

```
AI Operated.
```

- Sora 800, ink `#1F1B17`
- "Operated" sits on a **sand highlighter swash**: `linear-gradient(to top, #DDB892 0, #DDB892 26%, transparent 26%)` — a marker stroke covering the bottom 26% of the line box, `padding: 0 4px`
- The trailing period is **terracotta** `#B5532E`

**Motion treatment:** the swash wipes in left-to-right (`scaleX 0 → 1`, `transform-origin: left`,
`power3.out`), then the period pops. This is the brand's hero moment. It appears on the cover and
returns on the CTA — that's the **callback**.

## Texture (the unifying spine)

The dark-brand grid/vignette does not apply. AI Operated's spine is:

1. **Hairline rules** — `1px rgba(31,27,23,0.12)` above every section eyebrow. Present on every beat.
2. **Mono eyebrow** — `01 / NEWS` style label in terracotta, uppercase, tracked. Every beat.
3. **Paper grain** — very faint warm noise over the cream, `opacity: 0.035`, dark dots (not white).
4. **Warm vignette** — barely-there radial darkening at the edges so the paper doesn't read flat.

## Motion

- **Transition:** terracotta `#B5532E` block-wipe across the frame at each cut, 0.4s `power3.in`.
  Never a hard cut.
- **Headline entry:** word-grouped per-character rise (`y: 30 → 0`, stagger `0.012–0.014`).
  Words must stay unbroken — wrap each word in a non-breaking span so lines only break at spaces.
- **Numerals:** count-up via a GSAP proxy where a stat is shown.
- **Outro:** the CTA holds ~8s with a slow button-glow pulse.

## Layout

1920×1080, left-aligned editorial grid:

- Left margin `100px`, right margin `100px`
- Eyebrow at `top: 150px`, hairline rule directly above it
- Headline block vertically centered
- Footer wordmark bottom-left at `80px`

## Do's / Don'ts

**Do:** lead with the mono eyebrow, land on a Sora headline. Keep the paper warm. Let the terracotta
do all the pointing. Hold the CTA. Bring the wordmark back at the end.

**Don't:** add chrome gradients, perspective grids, lime, or cool-white halos — those belong to other
brands in this workspace. Don't put mono in body copy. Don't introduce a fifth colour.
