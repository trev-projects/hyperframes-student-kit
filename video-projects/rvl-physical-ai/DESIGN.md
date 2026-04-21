# RVL — Design System

> Source: RVL header screenshot. Newsletter tagline "Revealing The Future Of Brands, Startups, And Venture Capital." Aesthetic: **loud, punk-futurist VC**. Think *Vice Magazine × Bloomberg Terminal × Anthropic launch trailer*. Acid lime on black, bold display type, hard-edge cropping, zero decoration.

## Overview

RVL is a newsletter in the venture-capital / AI / startup space. The brand is aggressive, high-contrast, and built around **one color + one type move**: acid-lime headlines slammed against pure black, with display type cropped so hard it extrudes out of the frame. Everything else is negative space. The weekly video's job is to generate *two seconds of scroll-stop energy* — match that loudness, carry the tagline, deliver a hook, ship a read-more CTA. No pastels, no glass, no chrome. Hard lines, big type, snappy cuts.

## Colors

- **Canvas / Void** — `#0a0a0a` (near-black; pure `#000` reads as a browser default on small screens)
- **RVL Lime** — `#c3f53b` — the only brand color. Used on headline type, arrows, percent bars, outro wordmark. Never tinted.
- **Lime Hot** — `#b6ff1a` — punchier variant for glow / halo only.
- **White** — `#ffffff` — secondary text (taglines, subtitles), at 85% opacity default.
- **Grey Rail** — `#4a4a4a` — very sparing use, thin dividers only.

Discipline: **two colors per beat max** (lime + white on black, or lime alone on black). If you're reaching for a third hue, you've lost the thread.

## Typography

- **Display / hero** — a condensed, high-contrast display face. `Archivo Black`, `Bebas Neue`, or `Anton` all match the screenshot's RVL wordmark vibe. Weight 800–900. Letter-spacing `-0.02em` to `-0.04em` (tight). Line-height `0.85` for stacked impact. **This face does the storytelling.**
- **Secondary / body / labels** — `Space Grotesk` or `Inter` weight 500–700, letter-spacing `0.01em`. Used for taglines, sub-copy, counters.
- **Numeric / stats** — `JetBrains Mono` weight 700 for fundraise amounts and numbers. Mono reads "data".

Scale discipline: hero type is `font-size: 320–520px` (literally screen-filling). Body is 36–56px. Mono numerics are 120–220px.

**Signature move:** hero type deliberately **clips off the frame edges** — letters exit the viewport on left/right to telegraph "more than fits". This is RVL's visual fingerprint; use it on every act-break beat.

## Elevation / Texture

Depth comes from **type contrast and crop**, not from depth effects. No drop shadows. No gradients inside type (unless it's a specific lime→white ramp for a callback). No glass cards.

- Optional: faint film grain `opacity: 0.04` over everything. Texture, not decoration.
- Optional: one-pixel lime hairline under section labels when needed for structure.

The entire aesthetic runs on **type × color × pacing**. That's it.

## Components

- **Kinetic-Type Slab** — single word or short phrase in display face, lime or white, clipped to frame edges. Slams in from offset (x: ±400, scale: 1.15 → 1, 0.4s `expo.out`). Exits via whip-wipe or scale-through.
- **Marquee Row** — single word repeated with spacing scrolling horizontally, lime-on-black, used as transition element between beats.
- **Stat Block** — mono numeric (lime) + tiny uppercase label (white, 60%). Counts up over 0.8–1.4s.
- **Deal Rail** — 3 stacked rows, each `COMPANY → $AMOUNT`, slide-in staggered 0.3s. Amounts in lime mono.
- **Ticker Strip** — thin row at bottom or top with small mono text, scrolling left slowly (2–3px/frame). Lends "market data" energy.
- **Block Wipe** — solid lime rectangle slides across the frame covering scene-to-scene cuts (0.4s). Replaces the amber whip-streak from Digiwell.
- **RVL Mark** — "R V L" set in display face, lime, with intentional negative-space crop at first/last letter. Used as persistent corner bug (top-left, 96px) and as the outro headline (560px).

## Do's and Don'ts

### Do's

- Land type that exceeds the frame. If a headline fits comfortably, it's too small.
- Use lime for the ONE thing the viewer should look at in the beat. Everything else is white or grey.
- Snap-cut with a block-wipe between beats. Hard cuts are fine — softness is not.
- Mono for every number. No floating text numbers.
- Bottom bug: small RVL wordmark visible in the corner for 80%+ of the runtime (callback + channel identity).

### Don'ts

- No drop shadows. No glass. No gradients inside icons.
- No colors other than lime + white + black. Pure discipline.
- No decorative particles, swirls, or grid floors (that was Digiwell's aesthetic — stays there).
- No mixed type weights in a single word. Either bold-display, or mono — pick one per element.
- No generic stock iconography. If you need an icon, it's a thick-line unicursal glyph in lime.

## Weekly-Swap Template

To reuse this design for every week's issue, the following values are the *only* things that change week-to-week:

| Token               | Where it lives                  | Example (this week)                                                |
|---------------------|---------------------------------|--------------------------------------------------------------------|
| `ISSUE_HEADLINE`    | Beat 1 hero type + caption 1    | "Physical AI"                                                      |
| `ISSUE_SUBHEAD`     | Beat 2 secondary line           | "Just became its own investment category."                         |
| `CONTRAST_PAIR`     | Beat 3 "X → Y" pair             | "Pixels → Atoms"                                                   |
| `DEAL_ROWS`         | Beat 4 deal rail (3 rows)       | `Figure $1.5B` · `Physical Intelligence $400M` · `Skild $300M`     |
| `THESIS_LINE`       | Beat 5 kinetic thesis           | "Every major fund has a physical AI thesis."                       |
| `SIGNOFF_LINE`      | Beat 6 tagline                  | "Software ate the world. Physical AI will move it."                |
| `CTA_URL`           | Beat 7 outro URL                | `rvl.tech/p/physical-ai`                                           |

Everything else — brand colors, fonts, grid, transitions, pacing — stays locked. Drop in 7 new strings and re-render for next week.
