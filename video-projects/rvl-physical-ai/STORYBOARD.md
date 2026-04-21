# RVL — Physical AI — Storyboard (30s)

**Format:** 1920×1080, 30fps
**Palette:** RVL Lime `#c3f53b`, White `#ffffff` (85%), Canvas `#0a0a0a`
**Type:** Archivo Black / Bebas Neue for display · Space Grotesk for body · JetBrains Mono for numerics
**Persistent:** small RVL corner bug + faint film grain, both on from 0.0s → 30.0s

---

### BEAT 1 — COLD OPEN (0.0–2.0s) · `01-cold-open.html`

**VO:** "Pixels are out."

Instant impact. No fade, no silence. **"PIXELS"** slams into frame from the right, display face at 480px, clipped off both edges. White. **"ARE OUT."** lands a half-second later, smaller, bottom-right, white with the OUT word struck through by a lime bar.

- Scroll-stop energy in the first 200ms
- Hard edge to the left — type literally extrudes past the viewport
- Block-wipe lime rect exits the scene to the right at 1.8s

### BEAT 2 — FLIP (2.0–3.8s) · `02-flip.html`

**VO:** "Atoms are in."

Mirror beat. **"ATOMS"** slams in from the LEFT, lime, 480px, clipped off. **"ARE IN."** lands right-aligned, white. Same pacing as Beat 1 — the visual rhyme is the point.

- Callback #1: identical rhythm to Beat 1
- Lime has "won" this beat — "ATOMS" is *colored*, where "PIXELS" was not
- Block-wipe exit at 3.6s

### BEAT 3 — CATEGORY LAND (3.8–11.0s) · `03-category-land.html`

**VO:** "Physical AI — humanoids, factory robots, self-driving — just became its own investment category."

The hero beat. **"PHYSICAL"** stacks on line 1, white. **"AI"** massive on line 2, lime, 720px — clipped aggressively. Below, in a thin Space Grotesk row, three words cycle through with 0.6s stagger: `HUMANOIDS` → `FACTORY ROBOTS` → `SELF-DRIVING`. Each appears, holds 0.4s, morphs to the next. On the last word, an RVL lime underline streaks across, and the secondary caption "**its own investment category**" lands bottom-right in mono, all-caps.

- Longest beat — holds the concept
- Type crop + scale = the RVL signature move
- Mono subcaption grounds it with data-energy
- Exit: block-wipe + whole scene scale 1 → 1.15 with blur ramp

### BEAT 4 — DEAL RAIL (11.0–19.0s) · `04-deal-rail.html`

**VO:** "Figure — 1.5 billion. Physical Intelligence — 400 million. Skild AI — 300 million."

Three stacked rows. Each is `[COMPANY NAME] → $[AMOUNT]`. Company name in white display face (200px), amount in lime mono (220px, weight 700). Rows enter staggered (0.0s, 2.4s, 5.0s) from right with x: +200, clipped off. A thin lime hairline draws under each row as it lands, left-to-right, `stroke-dashoffset` 1.0 → 0 in 0.6s.

- **Row 1:** `FIGURE → $1.5B`
- **Row 2:** `PHYSICAL INTELLIGENCE → $400M`
- **Row 3:** `SKILD AI → $300M`
- Counters on the $ amounts: 0 → final in 1.0s `power2.out`
- Row 3 entrance is slightly more kinetic (tiny overshoot + scale bounce) to signal the rail is "full"
- Exit: all three rows lift up together `y: -80, opacity: 0` on block-wipe

### BEAT 5 — THESIS (19.0–22.5s) · `05-thesis.html`

**VO:** "Every top fund now has a Physical AI thesis."

Text-only. Four lines, stacked, single-word-per-line reveal with 0.25s stagger, display face white except **"PHYSICAL AI THESIS"** on the final line which is all lime. Hero moment: the final line holds 0.8s, then the entire block rotates -2° and lifts off-screen.

```
EVERY
TOP FUND
NOW HAS A
PHYSICAL AI THESIS.
```

- Low decoration, high type-impact
- Mono aside in bottom-right (very small, 28px): `SOURCE: RVL ANALYSIS` — gives data-credibility
- Exit: block-wipe left-to-right

### BEAT 6 — SIGNOFF (22.5–27.0s) · `06-signoff.html`

**VO:** "Software ate the world. Physical AI will move it."

Two-line signoff, paced exactly to VO.

- Line 1: **"SOFTWARE ATE THE WORLD."** — white display, 220px, centered, appears in full (`back.out(1.3)` scale) at 0.0s, holds 1.4s
- Line 2: **"PHYSICAL AI WILL MOVE IT."** — lime, same size, appears at 1.8s, the word **"MOVE"** subtly rotates on its axis (a tiny Y-axis wobble, 4° amplitude) to sell the word
- Exit: both lines slide down out of frame as RVL mark scales up from behind

### BEAT 7 — CTA OUTRO (27.0–30.0s) · `07-cta.html`

**VO:** "Read this week's RVL. Link in bio."

The hero shot. **"RVL"** in massive display lime (640px), clipped off left and right edges, centered vertically. Below in Space Grotesk at 48px white: "Revealing The Future Of Brands, Startups, And Venture Capital." Below that, in JetBrains Mono 40px lime: "rvl.tech/p/physical-ai". Held still for 3 seconds (the longest single shot) with an optional marquee of the issue title scrolling as a thin bottom strip.

- Full 3s hold — the breathing moment
- RVL bug corner mark has been visible all video; here it scales UP to become the piece
- End state: everything locked, lime pulse glow on the URL for the last 0.5s

---

## Persistent Elements (all beats)

- **RVL Corner Bug:** `<div>` absolutely positioned top-left, 96px wide, `RVL` in Archivo Black lime. Always on. Track-index: 10 (above beats). Duration: 0–30s.
- **Film Grain:** `<div>` with CSS radial-gradient noise, opacity 0.04, `pointer-events: none`, `z-index: 40`. Duration: 0–30s.

## Transitions

| Between beats  | Type                                                             |
|----------------|------------------------------------------------------------------|
| 1 → 2          | Lime block-wipe right-to-left (mirrors the flip)                 |
| 2 → 3          | Lime block-wipe left-to-right                                    |
| 3 → 4          | Whole-scene scale-blur + block-wipe                              |
| 4 → 5          | Rows lift off + block-wipe                                       |
| 5 → 6          | Block-wipe left-to-right                                         |
| 6 → 7          | Signoff slides down as RVL mark scales up from behind (no wipe)  |

## Asset Audit

All visuals are type + CSS. Zero external assets needed:

- GSAP: `assets/gsap.min.js` (already installed)
- Fonts: Google Fonts (Archivo Black, Bebas Neue, Space Grotesk, JetBrains Mono) via inline CDN import — Hyperframes' compiler injects @font-face rules deterministically
- No images, no video, no audio required for the draft (TTS added in pass 2)

## Production Architecture

```
rvl-physical-ai/
├── index.html                 root — 7 beats + persistent RVL bug + captions
├── DESIGN.md                  RVL brand system
├── SCRIPT.md                  narration
├── STORYBOARD.md              THIS FILE
├── assets/
│   └── gsap.min.js            bundled (sandbox blocks CDN)
└── compositions/
    ├── 01-cold-open.html
    ├── 02-flip.html
    ├── 03-category-land.html
    ├── 04-deal-rail.html
    ├── 05-thesis.html
    ├── 06-signoff.html
    └── 07-cta.html
```
