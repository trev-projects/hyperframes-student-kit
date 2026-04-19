# Digiwell Marketing — Storyboard (30s)

**Format:** 1920×1080, 30fps
**Palette:** Amber `#f9a72c`/`#ff8a2a`, Growth Teal `#3de0a6`, Chrome gradient `#fff → #f7d99a → #f9a72c`, Canvas `#07080c`
**Type:** Inter 700/800 for words, JetBrains Mono 500/600 for numbers
**Backbone:** Grid floor + vignette + grain overlay on every beat. Amber whip-streak between beats.

---

### Beat 1 — Hook (0.0–3.5s) · `01-hook.html`

**VO:** "Your growth engine wasn't built for the A I era."

Chrome kinetic-type reveal. Words cascade in word-by-word, land-and-hold, then the hero phrase **"AI ERA"** in solid amber punches in at scale and blows through the camera.

- `Your` `growth` `engine` `wasn't` `built` `for the` — warm chrome, 96–120px, staggered slide-ins (360→120→60→25→12→25 px) with `expo.out` 0.25–0.33s
- **`AI ERA`** — amber solid (`#f9a72c`), 240px, `back.out(1.4)` settle, then `scale 1→6 + opacity 1→0` in 1.0s `power2.in`
- Grid floor tilts 5° at exit, amber whip-streak fires at 3.15s
- Transition OUT: whip-streak + blur ramp

### Beat 2 — Problem (3.5–7.5s) · `02-problem.html`

**VO:** "Cold leads. Dead lists. Campaigns that never convert."

Three broken-state cards cascade into view — amber-hot, glassy, slightly jittered — landing one per narration phrase.

- Card 1: **COLD LEADS** — icy envelope icon, stat crossed out (`0.2%`)
- Card 2: **DEAD LISTS** — trash-pile icon, "-43% engagement"
- Card 3: **NEVER CONVERT** — downward arrow, red strikethrough "$0 ROI"
- Stagger: 0.0s, 1.0s, 2.0s. Each card: `y: 80, opacity: 0 → 0` for 0.5s `power3.out`, hold, then subtle jitter.
- All three dim together on exit (`opacity 1 → 0.2, scale 0.95`) + amber whip-streak at 7.15s

### Beat 3 — Turn / Brand Reveal (7.5–10.5s) · `03-turn.html`

**VO:** "Digiwell builds growth systems that do."

Particle-trail background awakens — amber dots in a loose conic swirl orbiting center. The **Digiwell** wordmark crystallizes in warm chrome, with tracked-caps **MARKETING** underneath. Shimmer-sweep passes.

- 60 amber particles, Canvas 2D, seeded PRNG positions + harmonic-sin orbit, GSAP proxy for time
- Wordmark: `Digiwell` Inter 800 at 180px, warm-chrome gradient, amber halo
- Tagline: `MARKETING` Inter 600 at 40px, `0.4em` tracked, amber 80%, underneath wordmark
- Reveal: `scale: 0.9 → 1, opacity: 0 → 1`, 0.8s `power3.out` at 0.4s in
- Shimmer at 1.8s — 0.6s chrome-gradient sweep across wordmark
- Hold 1.2s then dim, amber whip-streak at 10.15s

### Beat 4 — Pillars (10.5–16.0s) · `04-pillars.html`

**VO:** "AI-assisted newsletters. CRM automation. Segmented nurture flows."

Three pillar cards in a horizontal row, each with a line-icon + label + micro-description. Cascade-in, hold, glow-cycle, exit.

- **Card A** — envelope icon + "AI-ASSISTED NEWSLETTERS" + "Done-for-you campaigns"
- **Card B** — lightning-bolt icon + "CRM AUTOMATION" + "Warm every lead"
- **Card C** — branching-tree icon + "SEGMENTED NURTURE" + "Flows that convert"
- Glass cards, 1px amber border at 22% opacity, inner highlight 1px `rgba(255,255,255,.18)`, outer halo `box-shadow: 0 0 60px rgba(249,167,44,.18)`
- Stagger: 0.0, 1.8, 3.6s. Each: `y: 60, opacity 0 → 0`, 0.6s `power3.out`. Icon strokes draw in (`stroke-dashoffset` 1 → 0) over 0.5s after card lands.
- Exit: all three `opacity 1 → 0.15, y: -40`, 0.4s `power2.in`. Whip-streak at 15.7s.

### Beat 5 — Proof (16.0–20.5s) · `05-proof.html`

**VO:** "Forty seven percent open rates. Subscribers who actually buy."

Dashboard-bento reveal. Big **47%** stat dominates, flanked by a live-drawing sparkline chart.

- Stat card center-left: `47%` teal mono (`#3de0a6`), 240px, counts up 0 → 47 in 1.4s
- Label above stat: `OPEN RATE` mono, 28px, `0.18em` tracked, amber
- Sparkline right side: SVG path, amber dashed baseline + teal solid growth arc drawn via `stroke-dashoffset` from 1 → 0 over 1.8s `power2.inOut`
- Small stat chip below sparkline: `8.6% CLICK` teal mono
- Grid floor reverses direction at 17.0s for subtle continuity
- Exit: `scale: 1 → 1.05, opacity 1 → 0` at 20.1s, whip-streak at 20.2s

### Beat 6 — Promise (20.5–24.5s) · `06-promise.html`

**VO:** "Cold leads become loyal buyers. In thirty days."

Morph beat. **COLD LEADS** (amber hot, small, greyed) on left transforms → **LOYAL BUYERS** (growth teal, big, bright) on right. Curved amber arrow draws between them with "30 DAYS" label.

- Left text: `COLD LEADS` Inter 700, 64px, starts at `#ff8a2a` with `opacity 0.4`
- Right text: `LOYAL BUYERS` Inter 800, 88px, teal `#3de0a6`, enters with `scale 0.8 → 1, opacity 0 → 1`, 0.7s `back.out(1.3)`
- Arrow: SVG path, `stroke: #f9a72c, stroke-dasharray` drawn 1 → 0 over 1.0s
- Label along arrow: `30 DAYS` mono 36px, amber, fades in at arrow midpoint
- Cold text dims further (`opacity → 0.15`) as loyal text grows. Callback: arrow's end particle re-uses the Beat-3 particle color
- Exit: whole scene blurs + lifts to match CTA entry

### Beat 7 — CTA (24.5–30.0s) · `07-cta.html`

**VO:** "Digiwell Marketing. Book your free audit at digiwellmarketing dot com."

**Hero shot. Hold 5+ seconds.** Particle-trail background (denser than Beat 3), centered wordmark, URL in amber mono, **FREE AUDIT** pill. Shimmer sweep once at 27.5s.

- Same particle canvas from Beat 3 — callback texture
- Wordmark `Digiwell` Inter 800, 240px, warm chrome + amber halo
- Tagline `MARKETING` tracked caps below
- URL: `digiwellmarketing.com` JetBrains Mono 48px, amber `#f9a72c`, `0.04em` tracked, 120px below wordmark
- **FREE AUDIT** pill — amber border, transparent fill, tracked caps, 80px below URL
- Entry: wordmark `opacity 0 → 1` + `scale 0.95 → 1`, 0.8s `power3.out` at 0.0s
- URL + pill fade in staggered 0.4s, 0.8s
- Shimmer-sweep across wordmark at 3.0s (0.6s chrome-sweep)
- Hold still through end-of-composition — `tl.to({}, { duration: 5.5 }, 0)` anchor

---

## Asset Audit

| Asset                 | Status                                   | Used in             |
|-----------------------|------------------------------------------|---------------------|
| Digiwell logo         | Not captured (sandbox blocked). Wordmark rendered in pure CSS.              | Beats 3, 7          |
| Particle-trail hero   | Site art not captured. Recreated as Canvas 2D procedural (seeded PRNG).     | Beats 3, 7          |
| Amber chart curve     | Site art not captured. Recreated as SVG with `stroke-dashoffset` animation. | Beat 5              |
| Open-rate `47.2%`     | Real number from screenshot (rounded to 47%).                               | Beat 5 VO + visual  |
| Click-rate `8.6%`     | Real number from screenshot.                                                | Beat 5              |
| Service icons         | Not captured. Recreated as inline SVG line icons, 1.5px stroke, amber.      | Beats 2, 4          |

---

## Production Architecture

```
digiwell-promo/
├── index.html                  root — orchestrates 7 beats + captions
├── DESIGN.md                   brand reference
├── SCRIPT.md                   narration text
├── STORYBOARD.md               THIS FILE
├── assets/                     (empty — everything is CSS/SVG/Canvas for now)
├── renders/                    render outputs (gitignored)
└── compositions/
    ├── 01-hook.html
    ├── 02-problem.html
    ├── 03-turn.html
    ├── 04-pillars.html
    ├── 05-proof.html
    ├── 06-promise.html
    └── 07-cta.html
```
