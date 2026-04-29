# Gathered — Landing Page Hero Video (Storyboard)

> **First-pass plan for review** — no code yet. Goal: lock the structure, then build.
>
> **Format:** 1920×1080, 30fps, ~24s · **Audience:** landing-page visitors who haven't signed up yet · **Goal:** in 24 seconds, communicate (a) what the app does, (b) what's visually different about it, (c) why a person who saves recipes should care · **Audio:** music bed only by default; optional single VO line ("All the recipes. None of the noise.") at the open. **Plays muted on hero.**

---

## Beat plan (5 beats · 24s)

| # | Beat                       | Window        | One-line idea                                                  |
|---|----------------------------|---------------|----------------------------------------------------------------|
| 0 | Editorial cold open        | 0.0 – 4.0s    | "All the recipes. None of the noise." — pure type, calm        |
| 1 | The signature comparison   | 4.0 – 11.0s   | Messy blog → arrow → clean Gathered recipe card                |
| 2 | Recipe collection grid     | 11.0 – 16.0s  | 2×2 of recipe cards cascading, "100+ Chef-Curated" pill on top |
| 3 | One-tap scaling moment     | 16.0 – 20.0s  | "Cooking for 2 or 12?" — slider tap, ingredient amounts shift  |
| 4 | CTA hero hold              | 20.0 – 24.0s  | Gathered wordmark + amber "Get Started Free" + URL, hold 4s    |

---

## BEAT 0 · Editorial cold open (0.0 – 4.0s) · `00-cold-open.html`

**Concept.** The video opens like a cookbook page. Cream canvas, no UI yet, just type. A subtle sprig glyph drifts in behind the headline. This beat sets the *mood* — calm, considered, warm — before any product is shown.

**Visual.**
- Background: cream `#f8f1e4`, faint paper-grain texture, no chrome.
- Center stage: two-line hero
  - Line 1: **`All the recipes.`** — Instrument Serif 152px, espresso `#1f160f`, fades up from `y +14, opacity 0, blur(6px)` over 0.7s starting at 0.3s
  - Line 2: **`None of the noise.`** — Instrument Serif **italic** 152px, terracotta `#c44a30`, lands 1.0s after line 1 with the same drop-in
- Top-right small mark: `GATHERED · RECIPE COMPANION` tracked caps in espresso, fades in at 0.1s
- Behind the hero, a subtle olive/espresso sprig drifts diagonally bottom-right → top-left at 8% opacity, slow

**Exit.** Both lines fade out with a soft up-shift while a cream paper-sweep transitions to Beat 1.

---

## BEAT 1 · The signature comparison (4.0 – 11.0s) · `01-url-to-card.html`

**Concept.** This is the brand's central image — the "before/after" of recipe-saving. Show the messy blog, show the clean Gathered card, let the contrast do the work.

**Visual layout.**
- Left half (cream panel, fades to ~50% opacity): a stylized recipe-blog mock
  - Tiny URL bar: `recipeblog.com/my-italian-nonnas-secret-pasta-bake-summer-…` truncated
  - Grey "ADVERTISEMENT" rectangle
  - Long blog-post title: *"My Italian nonna's secret pasta bake (and the summer I spent learning to cook in Tuscany)…"* in serif italic
  - Three lorem-ipsum bar rows
  - Second "ADVERTISEMENT" rectangle
  - The whole panel sits at ~45% opacity to read as "noisy / tuned out"
- Center column: a small amber play button (`#f5a73a`) + "GATHERED" tracked-caps below it
- Right half (espresso panel, dark `#231a14` card with rounded corners): the clean Gathered recipe card
  - Top: small `· GATHERED ✓` mark in amber
  - Hero photo placeholder (warm gradient stand-in for the real pasta photo)
  - Title: **`Nonna's Tuscan Pasta Bake`** Instrument Serif 56px white
  - Three pills: `55 min` (terracotta), `Serves 6` (terracotta), `Vegetarian` (olive)
  - Ingredient rows fade in line-by-line with stagger:
    - `Rigatoni — 500g`
    - `Passata — 700ml`
    - `Mozzarella — 250g`
    - `Fresh basil — 1 handful`

**Choreography.**
- 4.0–4.6s: messy blog panel slides in from left at 60% speed, lands faded
- 4.5–4.8s: amber play button + "GATHERED" mark fade in center
- 4.7–6.0s: dark Gathered card slides in from right with a slight scale settle (`back.out(1.3)`)
- 6.0–7.0s: ingredients drop in row-by-row with stagger 0.18s
- 7.0–8.5s: a subtle "Recipe Saved! · Added to To Try" toast pulses in the bottom-left of the dark card, then fades
- 8.5–10.5s: hold + slow drift on both panels for breathing room
- 10.5–11.0s: cream paper-sweep exit

**Why this beat.** It's the single image that makes Gathered's value-prop instantly legible. Anyone who's ever tried to read a recipe past 4 ads gets it in a half-second.

---

## BEAT 2 · Recipe collection grid (11.0 – 16.0s) · `02-collection-grid.html`

**Concept.** Show that Gathered is also a beautiful library, not just a clipper. Cards cascade in like a deal of cards.

**Visual.**
- Cream background. At top: small terracotta eyebrow `100+ CHEF-CURATED RECIPES` tracked caps, peach pill behind it.
- Center: 2×2 grid of recipe cards (white cards on cream)
  - Card 1: photo placeholder + `Tuscan Chicken` / `by Gina Homolka`
  - Card 2: photo + `Honey Garlic Salmon` / `by Tieghan Gerard`
  - Card 3: photo + `Buddha Bowl` / `by [Author]`
  - Card 4: photo + `Sheet Pan Fajitas` / `by Alex Snodgrass`
- Subtle "Recipe Saved! Added to To Try" toast pulses bottom-right at ~13s

**Choreography.**
- 11.0–11.5s: peach pill fades in
- 11.3–12.5s: 4 cards cascade in with `y +40, opacity 0 → 0` stagger 0.18s, `back.out(1.2)`
- 12.5–14.5s: hold; cards have a very subtle 1.01× breathe
- 14.5–15.0s: toast pulses bottom-right
- 15.0–16.0s: cream paper-sweep exit

**Why this beat.** Reinforces "library you'll actually want to look at" — counters the perception that recipe apps look utilitarian.

---

## BEAT 3 · One-tap scaling moment (16.0 – 20.0s) · `03-scale-tap.html`

**Concept.** Pick the most magical, demonstrable feature: **scale a recipe with one tap**. Show ingredients changing live. This is "wow" + "useful" in 4 seconds.

**Visual.**
- Cream background, centered card.
- Top: `SCALE IN ONE TAP` terracotta tracked-caps eyebrow.
- Card center: a serving selector — a row showing `2 · 4 · 6 · 8 · 12` with an animated cursor + tap. `6` is selected at start, then taps `12` mid-beat.
- Below: ingredient rows showing amounts shifting. E.g.:
  - `Rigatoni     500g  → 1000g`
  - `Passata      700ml → 1400ml`
  - `Mozzarella   250g  → 500g`
  - `Fresh basil  1 handful → 2 handfuls`
  - Numbers cross-fade rather than tick — feels editorial, not transactional.

**Choreography.**
- 16.0–16.4s: card slides up from below
- 16.4–17.5s: ingredient amounts visible at 6 servings
- 17.5–17.8s: cursor moves to "12", taps with a soft amber ripple
- 17.8–18.6s: numbers cross-fade to the doubled amounts; serving counter selects "12"
- 18.6–19.5s: hold
- 19.5–20.0s: cream paper-sweep exit

---

## BEAT 4 · CTA hero hold (20.0 – 24.0s) · `04-cta.html`

**Concept.** Land the brand. Make signup obvious. Hold 4s so it loops cleanly back to Beat 0.

**Visual.**
- Cream background, sprig glyph drifts slowly center → off-screen.
- Centered:
  - **`Gathered`** wordmark in Instrument Serif 240px espresso, with a tiny amber dot above the `i` (the brand spark)
  - Below it small tracked caps `RECIPE COMPANION` espresso 50% opacity
  - Below that a soft hairline 1px terracotta sweeping in
  - Below the rule, the tagline: `All the recipes. None of the noise.` (line 2 italic terracotta, smaller — 56px)
  - 32px below, the **amber pill button** `Get Started Free` espresso text + amber fill, soft glow pulse
  - Below the button, small mono `gatheredrecipes.com` espresso 60% opacity

**Choreography.**
- 20.0–20.6s: wordmark per-character fade-up with stagger 0.06s
- 20.6–21.0s: tracked-caps tagline fades in
- 21.0–21.4s: hairline sweeps L→R
- 21.2–21.7s: italic tagline fades in
- 21.5–21.9s: button settles in with `back.out(1.3)`
- 21.9–24.0s: button pulses gently every 1.0s; sprig drifts slowly
- 24.0s: end frame matches start frame for seamless loop

---

## Audio plan

- **Music bed** (entire 24s): warm-acoustic ambient — fingerpicked guitar + soft pad + light shaker. ~80 BPM. Different from RVL's synth bed. **Need to source or generate.** First pass: simple procedural pad in C-major (numpy + soundfile, similar approach to RVL's bed but warmer harmonic content).
- **VO** (optional): single line at 0.3s — "All the recipes. None of the noise." in `af_heart` voice @ 0.92×. Adds 2.5s of audio. Optional because hero loops are usually muted.
- **SFX** (optional): single soft "save" chime when the toast pops at ~7.5s. Light, almost subliminal.

**Recommendation: ship V1 with music bed only, no VO.** Add VO in V2 if it adds something.

---

## Production architecture

```
gathered-promo/
├── DESIGN.md                 brand reference (cream + espresso + amber + terracotta)
├── STORYBOARD.md             THIS FILE
├── SCRIPT.md                 (optional — single-line VO)
├── meta.json                 1920x1080, 30fps, 24s
├── hyperframes.json          CLI config
├── index.html                root — wires 5 beats + music bed
├── assets/
│   ├── gsap.min.js           bundled (sandbox)
│   ├── music.wav             warm-ambient bed (TBD)
│   └── (optional VO files when added)
└── compositions/
    ├── 00-cold-open.html       "All the recipes. None of the noise."
    ├── 01-url-to-card.html     blog → arrow → Gathered recipe card
    ├── 02-collection-grid.html 2×2 recipe cards
    ├── 03-scale-tap.html       servings 6 → 12 with ingredient cross-fade
    └── 04-cta.html             wordmark + Get Started Free + URL
```

## Open questions before I build

1. **Real recipe photos?** First pass uses warm gradient placeholders. If you have 5 food photos (Tuscan Chicken, Honey Garlic Salmon, Buddha Bowl, Sheet Pan Fajitas, and a pasta-bake hero shot), drop them into `assets/photos/` and I'll wire them in. Otherwise placeholders are fine for review.
2. **VO yes / no?** Default no. Easy to add the one line if you want it.
3. **CTA copy.** Is it "Get Started Free" (matches the live button) or do you want it different in the video (e.g. "Start Saving Recipes" matches the other CTA on the page)?
4. **Length.** 24s is the proposed default. If 12–15s is better for the hero (loops faster, less attention required), I'll cut Beats 2 + 3 down to one combined "feature flash" beat.
5. **Sprig glyph.** I see the small leaf/pinecone glyph in the bottom-corner badge. If you have an SVG of the actual mark, drop it in `assets/sprig.svg`. Otherwise I'll recreate it in CSS.

Once you sign off on the structure (or redirect any beat), I'll build it end-to-end.
