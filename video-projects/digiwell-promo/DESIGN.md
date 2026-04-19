# Digiwell Marketing — Design System

> Source: two mobile screenshots of `digiwellmarketing.com` (hero + Newsletter Growth Engine section). The live site was unreachable from the sandbox capture, so this doc was written from the screenshots directly.

## Overview

Digiwell Marketing positions itself as a **"Growth Partner for the AI Era"** — a done-for-you agency that builds systems (newsletters, CRM automation, segmented nurture flows) to turn cold leads into loyal buyers. The visual identity is **warm-dark premium-tech**: near-black canvas carried by an **amber/gold signature** across headlines, CTAs, product borders, and the hero particle-trail artwork. It reads less "agency services site" and more "AI-era growth platform" — the amber energy does the differentiating work. Motion should lean into that: golden light trails, particle drift, warm halos — never cool-tech blue.

## Colors

- **Canvas / Void** — `#07080c` — near-black backing every scene.
- **Amber Primary** — `#f9a72c` — brand hero color. Headlines' accent word ("AI Era"), CTA button fill, "DONE-FOR-YOU SERVICE" pill, "FREE AUDIT" outline, service-icon strokes, card border-glow.
- **Amber Hot** — `#ff8a2a` — deeper amber for gradient stops and motion trails.
- **Amber Soft** — `#ffd480` — highlight tint on chrome gradient upper stop and card inner-glow.
- **Growth Teal** — `#3de0a6` — positive-stat color (open-rate 47.2%, growth baseline on the chart). Used sparingly, only where a metric is "up".
- **Chrome Headline** — gradient `#fff → #f7d99a → #f9a72c` — warm chrome for hero type. Halo tinted amber, never cool-white.
- **Body Text** — `#d9d9de` at 92% opacity — readable grey on the dark canvas.
- **Grid Ghost** — `rgba(249,167,44,.06)` — perspective grid lines get a faint amber tint instead of neutral white.
- **Vignette** — `#000` at 95% radial edge — always top layer, `pointer-events: none`.

Discipline: amber is the *only* recurring color — it's the brand. Teal appears exactly once (the metrics beat). Everything else is black, chrome, and amber.

## Typography

- **Digiwell wordmark** — "Digiwell" in Inter/Geist 700–800 with warm-chrome gradient fill + amber halo. Small tracked caps "MARKETING" sits one line below in `0.4em` letter-spacing, 40% of the wordmark size, amber at 80% opacity. Wordmark gets a subtle 1px amber underline glow that shimmer-sweeps on hold.
- **Hero headline** — Inter 800, 96–160px depending on scene. Two-tone: opening phrase in warm chrome, final 2–3 words ("AI Era", "GUESSWORK", "CONVERT") in solid Amber Primary. Halo glow `text-shadow: 0 0 24px rgba(249,167,44,.6), 0 0 60px rgba(249,167,44,.25)`.
- **Section label** — Inter 600, uppercase, 28px, `0.18em` tracking, amber at 80% — used for "DONE-FOR-YOU", "AI ERA", "FREE AUDIT".
- **Dashboard numerics** — `JetBrains Mono` 600, 72–120px, color-coded: teal for positive stats, amber for attention stats.
- **Body / caption** — Inter 500, 28px, `#d9d9de` on a 55%-black backdrop-blur pill.
- **URL / CTA text** — Inter 600, 36px, amber `#f9a72c`, `0.04em` tracking. "digiwellmarketing.com" is lowercase.

No italic, no serif, no decorative faces. Mono for numbers, Inter for words.

## Elevation

Depth via **warm light + glass + amber borders**, not drop shadows.

- **Liquid-glass cards** — 4-stop diagonal gradient `rgba(255,255,255,.06 / .02 / .01 / .045)` + `backdrop-filter: blur(14px) saturate(1.12)` + 1px inner highlight `inset 0 1px 0 rgba(255,255,255,.18)` + 1px border `rgba(249,167,44,.22)` — the amber border is the tell.
- **Card outer halo** — `box-shadow: 0 0 60px rgba(249,167,44,.18)` on product-preview cards, mimicking the hero section's glow.
- **Amber halo on hero type** — see typography spec.
- **Perspective grid floor** — on every beat. Crosshair `+` marks at 4 center intersections. Grid lines tinted amber at 6% rather than cool white.
- **Vignette** — radial `transparent 30% → #000 95%` on every beat.
- **Grain overlay** — `npx hyperframes add grain-overlay` on every beat.
- **Particle-trail hero background** — the site's signature visual. Recreate as Canvas 2D procedural: ~80 amber dots orbiting a center in a loose conic swirl, deterministic via seeded PRNG + harmonic-sin positions, slow rotation via GSAP proxy. This is the *brand texture* — use it as the root composition's full-bleed background for the Turn beat (brand reveal) and the CTA outro.

## Components

- **Kinetic-Type Hero** — word-by-word reveal. Opening phrase in warm chrome, key word in solid amber. Hero word scales 1→8, opacity 1→0 in 1.0s `power2.in`.
- **Amber Whip-Streak** — horizontal amber-tinted gradient bar (`transparent → #f9a72c → transparent`), blurred 8px, 0.3–0.4s fire-at-cut. The warm equivalent of Infinite's white streak.
- **Particle-Trail Background** — Canvas 2D, amber dots in a spiral/conic orbit. Root-composition layer; beats sit on top in glass cards.
- **Service-Icon Line Pack** — 6 thin-stroke SVG icons in Amber Primary: envelope (newsletter), pen (content), globe (ESP), magnifier (A/B), bar-chart (analytics), chat-bubble (scheduling). 1.5px stroke, rounded caps. 32px default.
- **Stat Pill** — mono numeric + tiny uppercase label. `"OPEN RATE 47.2%"` pattern from the screenshot. Teal for up-stats, amber for attention.
- **"DONE-FOR-YOU" badge** — pill with amber gradient border, transparent fill, uppercase tracked text. 
- **Dashboard Bento** — 2x2 glass cards with mono numerics + SVG sparklines drawn via `stroke-dashoffset` animation. Amber dashed baseline, teal solid growth line (mirrors the chart in the screenshot).
- **CTA Card** — Digiwell wordmark centered, "digiwellmarketing.com" URL below in amber mono, "FREE AUDIT" pill to the side. Held 5s with shimmer-sweep once mid-hold.

## Do's and Don'ts

### Do's

- Lead every headline with chrome, land every headline on amber. "Your Growth Partner for the **AI Era**" is the template.
- Keep amber as the only recurring color. Teal earns one scene (metrics). Everything else: black + chrome + amber.
- Use the particle-trail background on the brand-reveal and outro beats — it's the site's signature visual.
- Mono for numbers. Inter for words.
- Every transition uses motion (amber streak, particle swirl, color-flip). Zero hard cuts.
- Hold the CTA 5+ seconds. Let "digiwellmarketing.com" breathe.

### Don'ts

- No cool-tech blue, no neon magenta, no rainbow. The warmth is the brand.
- No stock photography, no office shots, no handshake imagery, no founder headshots.
- No drop shadows — use glass + amber-border halo.
- No generic-agency copy ("We're passionate about growth"). Land on specifics: newsletters, CRM, nurture flows, measurable lift.
- No cool-white halos. Halos are always amber-tinted.
- No `Math.random()` / `Date.now()` in render loops. Particle positions via seeded PRNG + harmonic-sin.
