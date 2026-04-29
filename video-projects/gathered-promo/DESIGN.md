# Gathered — Design System

> Source: gatheredrecipes.com landing page screenshots (April 2026). The brand is a warm **editorial / cooking-magazine** aesthetic — anti-noise, reader-friendly, more "good cookbook" than "Silicon Valley app".

## Overview

Gathered is a recipe-collection app: paste a URL, AI extracts the recipe (ingredients, instructions, cook time), saved into "My Recipes" or "To Try". Tagline: **"All the recipes. None of the noise."** The brand reads as the antidote to ad-littered recipe blogs — calm, focused, beautiful. Visual identity is **cream + espresso + amber + terracotta**, with a **serif headline + sans body** pairing that signals "considered, not engineered."

## Colors

- **Cream / Canvas** — `#f8f1e4` — primary background. Warm, not paper-white.
- **Espresso / Ink** — `#1f160f` — header bar, dark recipe-card fill, body text on cream.
- **Amber Brand** — `#f5a73a` — primary CTA button, "Gathered" logo wordmark accent on the dot above the i, "Get Chrome Extension" outline link, "Get Started Free" pill.
- **Terracotta** — `#c44a30` — second-line emphasis ("None of the noise"), feature-section eyebrow ("FEATURES", "HOW IT WORKS"), the small "55 min" pill on the dark recipe card.
- **Olive / Sage** — `#5e7140` — dietary tag chip ("Vegetarian"), "Recipe Saved!" toast checkmark. Restful green, not a "success-state" green.
- **Soft Peach** — `#fde4d3` — pill backgrounds (e.g. "100+ Chef-Curated Recipes Inside"), feature-icon backgrounds.
- **Warm Grey** — `#a8978a` — body copy on cream, secondary labels.
- **White Card** — `#ffffff` at 95% — feature cards on cream background.

Discipline: amber + terracotta carry CTAs and emphasis. Sage carries success. Cream is the room. Espresso is the body. Never introduce a sixth hue.

## Typography

- **Display Serif** — `Instrument Serif` (or fallback `Playfair Display`). Used on hero headlines, recipe titles, section headlines. Weight 400. Italic available for the second line of hero copy ("None of the noise."). Letter-spacing `0` (default), line-height tight (0.95).
- **Body / UI Sans** — `Inter` weight 500–700. Used for buttons, body copy, pills, labels, ingredient lists, navigation, and sub-copy. Letter-spacing slightly tracked (`0.01em`).
- **Tracked Caps** — `Inter` weight 600–700 in `0.18em` letter-spacing, uppercase. Used for `RECIPE COMPANION` under the wordmark, "FEATURES" and "HOW IT WORKS" eyebrows, and the "GATHERED" mark in the hero comparison.

Scale per beat:
- Hero headline: **140–160px** (display serif)
- Hero second line: **140–160px italic** (terracotta accent)
- Section headline: 96px display serif
- Pill text: 24–28px sans tracked caps
- Body / sub-copy: 28–34px sans
- Recipe title in card: 36–44px serif
- Recipe title in dark card: 56px serif

## Visual signature — the "URL → Recipe Card" comparison

The strongest single image on the landing page. Worth recreating in motion:

- **Left side (cream panel):** a cluttered recipe-blog mock — URL bar at top with `recipeblog.com/my-italian-nonnas-secret-pasta-bake-summer-...`, then a grey "ADVERTISEMENT" placeholder, then a long blog-post intro headline ("My Italian nonna's secret pasta bake (and the summer I spent learning to cook in Tuscany)…"), followed by lorem-ipsum paragraph bars and another ad placeholder. **Faded out / desaturated.**
- **Center:** a small amber play button with "GATHERED" tracked caps below.
- **Right side (espresso panel — DARK card):** clean recipe card "Nonna's Tuscan Pasta Bake" with three pills (`55 min` terracotta, `Serves 6` terracotta, `Vegetarian` sage), a pasta photo, then ingredient rows: `Rigatoni — 500g` / `Passata — 700ml` / `Mozzarella — 250g` / `Fresh basil — 1 handful`.

This is the brand's central metaphor. **Use it.**

## Components / motion vocabulary

- **Soft serif drop-in**: hero type fades from `opacity 0, y +14px, blur(6px)` → resolved over 0.7s `power2.out`. Slower than RVL's punk slams.
- **Recipe card slide-up**: cards enter `y +30px, opacity 0` with stagger 0.12s. Subtle, layered.
- **Recipe Saved toast**: `scale 0.9, y +12, opacity 0` → settled with `back.out(1.4)`. The sage check icon does a tiny `rotate(-12)` → `rotate(0)` settle.
- **Counter / scale-by-tap**: ingredient amounts change with a soft cross-fade (no hard count-up, more elegant). Use `power2.inOut`.
- **Sprig accent drift**: the small leaf/sprig glyph from the corner of the brand drifts in slowly behind hero type for warmth. Optional.
- **Page-turn transition**: between major beats, a soft cream-paper sweep replaces RVL's lime block-wipe. Subtle, editorial. Easing: `power2.inOut`, duration 0.5s.

## Don'ts

- No lime / acid green. (RVL aesthetic — wrong project.)
- No dark cinematic blacks — Gathered uses cream as the room.
- No kinetic-slam typography (no Archivo Black, no edge-clipping).
- No mono numerals for stats — use the display serif for the magic of `55 min` etc.
- No drop shadows on cards (use subtle borders + 2% darker cream behind to lift).
- No music with a hard kick beat — ambient warmth only.

## Asset map (for first build)

| Asset | Source | First-pass approach |
|---|---|---|
| Gathered wordmark | Screenshot | Recreate in CSS using Instrument Serif + amber accent dot above the `i` (the visual "spark" in the screenshot) |
| Sprig glyph | Screenshot bottom-corner | Inline SVG, two leaves on a stem, espresso fill |
| Recipe photos (4) | Not yet provided | **Placeholder**: warm gradient cards with serif title + "By Author" sub-line. Replace with real photos later. |
| Pasta photo on dark recipe card | Not yet provided | **Placeholder**: warm gradient mosaic. Replace later. |
| URL-bar messy blog mock | Recreate in CSS | All-CSS: light cream card with a fake URL row, grey "ADVERTISEMENT" rectangle, lorem-ipsum bar list, second ad. Faded `opacity: 0.45`. |
| Recipe Saved toast | Recreate in CSS | White rounded card + sage check icon (inline SVG) + "Recipe Saved! / Added to To Try" two-line text. |
| Amber CTA button | Recreate in CSS | Pill, amber fill, espresso text, slight glow on pulse. |

If/when real food photography arrives, drop into `assets/` and swap the gradient placeholders for `<img>` tags — every card has a `data-photo-slot` we'll target.
