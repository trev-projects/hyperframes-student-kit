# RVL Weekly Video — Template & Handoff

> **Canonical template for every weekly RVL issue video.** Each issue is a 30–33s landscape video (1920×1080 @ 30fps) using the RVL brand aesthetic. Humans or agents can produce a new issue in ~10 minutes by cloning this folder, swapping 7 tokens, and running 3 commands.
>
> **Don't edit the template directly.** Clone it for each new issue. The template is a reference.

---

## How to produce next week's issue

```bash
# 1. Clone this template (slug: rvl-week-<number>-<kebab-topic>)
cd video-projects
cp -r rvl-weekly-template rvl-week-18-stablecoins
cd rvl-week-18-stablecoins

# 2. Update meta.json — id + name
sed -i 's/"id": "rvl-weekly-template"/"id": "rvl-week-18-stablecoins"/' meta.json
sed -i 's/"name": "RVL — Weekly Issue Template"/"name": "RVL — W18 Stablecoin Commerce"/' meta.json

# 3. Edit the 7 swap tokens (see checklist below)
# 4. Regenerate the voiceover (main narration only — CTA is already baked)
#    Copy the quoted text from SCRIPT.md's "Main narration" block:
npx hyperframes tts "Paste the edited main-narration block here." \
  --voice af_heart --speed 0.92 --output assets/narration-main.wav

# 5. Lint + draft render
npx hyperframes lint
npx hyperframes render --quality draft --output renders/rvl-week-18-draft.mp4

# 6. Loudnorm post-process for YouTube (-14 LUFS target)
ffmpeg -i renders/rvl-week-18-draft.mp4 \
  -c:v copy -af "loudnorm=I=-14:LRA=11:TP=-1.5" -c:a aac -b:a 192k \
  preview.mp4

# 7. Share assets (mobile-friendly MP4, GIF, contact-sheet)
ffmpeg -i preview.mp4 -vf "scale=1280:720" -c:v libx264 -preset veryfast -crf 30 \
  -c:a aac -b:a 128k -movflags +faststart preview-small.mp4
ffmpeg -i preview.mp4 -vf "fps=10,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=5" \
  -loop 0 preview.gif
ffmpeg -i preview.mp4 -vf "fps=1,scale=480:-1,tile=4x9" -frames:v 1 contact-sheet.png

# 8. Commit + push
cd ../..
git add video-projects/rvl-week-18-stablecoins
git commit -m "rvl-week-18: stablecoin commerce"
git push
```

## Per-Issue Swap Checklist — the 7 tokens

These are the *only* things you change. Palette, fonts, grid, transitions, pacing stay locked.

| #  | Token               | File(s)                                                        | Example (W17 Physical AI)                                |
|----|---------------------|----------------------------------------------------------------|----------------------------------------------------------|
| 1  | `WEEK_LABEL`        | `compositions/00-hook-teaser.html` · `.label-sm`               | `W17 · APR 21`                                           |
| 2  | `ISSUE_HEADLINE`    | `00-hook-teaser.html` (`.slide-b`) + `03-category-land.html` (`.h-physical` + `.h-ai`) | Teaser: `PHYSICAL AI` · Main: `PHYSICAL` / `AI` |
| 3  | `EXAMPLES_3`        | `03-category-land.html` — three `.cyc c1/c2/c3` divs           | `HUMANOIDS` · `FACTORY ROBOTS` · `SELF-DRIVING`          |
| 4  | `DEAL_ROWS_3`       | `04-deal-rail.html` — three `.row` blocks                      | `FIGURE $1.5B` · `PHYSICAL INTELLIGENCE $400M` · `SKILD AI $300M` |
| 5  | `PUNCHLINE_2`       | `05-thesis.html` (`.ln3` + `.ln4`)                             | `PHYSICAL AI` / `THESIS.`                                |
| 6  | `SIGNOFF_PAIR`      | `06-signoff.html` (`.line-1` + `.line-2`)                      | `SOFTWARE ATE THE WORLD.` / `PHYSICAL AI WILL MOVE IT.`  |
| 7  | `SCRIPT_MAIN`       | `SCRIPT.md` — "Main narration" block (re-run TTS)              | See SCRIPT.md                                            |

The CTA ("Read the latest issue and sign up at RVL dot tech") is **fixed** — already in `assets/narration-cta.wav`. Only `narration-main.wav` gets regenerated per issue.

### Token 1 — `WEEK_LABEL`

`compositions/00-hook-teaser.html`, `.label-sm`:
```html
<div class="label-sm">W17 &middot; APR 21</div>
```

### Token 2 — `ISSUE_HEADLINE` (two places)

**Teaser flash** (`00-hook-teaser.html`, `.slide-b`) — one or two words, ≤ 12 chars at 210px:
```html
<div class="slide slide-b" data-split>PHYSICAL AI</div>
```

**Main hero** (`03-category-land.html`) — line 1 sets up, line 2 hits:
```html
<div class="h-physical">PHYSICAL</div>
<div class="h-ai">AI</div>
```
Line 2 is the dominant lime hero at 560px. Keep it ≤ 4 chars so it stays dramatic and fits the frame. For a longer topic, put the subject on `.h-physical` and a short modifier on `.h-ai` (e.g. `STABLECOIN` / `NOW`).

### Token 3 — `EXAMPLES_3`

`03-category-land.html`:
```html
<div class="cyc c1">HUMANOIDS</div>
<div class="cyc c2">FACTORY ROBOTS</div>
<div class="cyc c3">SELF&middot;DRIVING</div>
```
Three short phrases, each on screen ~1.2s. ≤ 16 chars each.

### Token 4 — `DEAL_ROWS_3`

`04-deal-rail.html` — three `.row` blocks:
```html
<div class="row row-1">
  <div class="co">FIGURE</div>
  <div class="arrow">→</div>
  <div class="amt"><span class="amt-num" data-target="1.5">0.0</span><span class="amt-unit">B</span></div>
  <div class="row-underline"></div>
</div>
```
- `data-target` = final number for count-up
- `.amt-unit` = `B` (billions) or `M` (millions)
- Long company names get a smaller font via `.row-2 .co` — reserve row 2 for the long name

### Token 5 — `PUNCHLINE_2`

`05-thesis.html`:
```html
<div class="ln ln3" data-split>PHYSICAL AI</div>
<div class="ln ln4" data-split>THESIS.</div>
```
Two lime hero lines at 220px. Each ≤ 14 chars or they clip.

### Token 6 — `SIGNOFF_PAIR`

`06-signoff.html`:
```html
<div class="line line-1" data-split>SOFTWARE ATE THE WORLD.</div>
<div class="line line-2">
  <span class="prefix" data-split>PHYSICAL AI WILL </span><span class="move">MOVE</span><span class="suffix" data-split> IT.</span>
</div>
```
- Line 1 = white (the callback to history)
- Line 2 = lime (the new thesis). The word inside `.move` gets a scale-burst + rotation wobble — choose a verb you want emphasized.
- Both ≤ 25 chars.

### Token 7 — `SCRIPT_MAIN`

Edit `SCRIPT.md` → "Main narration" block. Keep ~55 words, ~6 short lines delivering *analysis* (not reading the visuals). Then re-run TTS with the command above.

---

## File map

```
rvl-weekly-template/
├── HANDOFF.md                THIS FILE — weekly workflow
├── DESIGN.md                 RVL brand system (locked)
├── SCRIPT.md                 narration template + TTS commands
├── STORYBOARD.md             beat-by-beat direction
├── meta.json                 project metadata (edit id + name per issue)
├── hyperframes.json          CLI config (don't touch)
├── index.html                root — wires all 8 beats + VO + music bed
├── assets/
│   ├── gsap.min.js           bundled GSAP (locked)
│   ├── music.wav             34s synth bed (reuse across issues)
│   ├── narration-main.wav    main VO — REGENERATE per issue
│   └── narration-cta.wav     CTA VO — fixed (baked once)
└── compositions/
    ├── 00-rvl-bug.html       persistent RVL corner mark
    ├── 00-hook-teaser.html   pre-hook teaser (WEEK_LABEL + ISSUE_HEADLINE)
    ├── 01-cold-open.html     "PIXELS ARE OUT." (fixed or swappable pair)
    ├── 02-flip.html          "ATOMS ARE IN." (fixed or swappable pair)
    ├── 03-category-land.html ISSUE_HEADLINE + EXAMPLES_3
    ├── 04-deal-rail.html     DEAL_ROWS_3
    ├── 05-thesis.html        PUNCHLINE_2
    ├── 06-signoff.html       SIGNOFF_PAIR
    └── 07-cta.html           RVL CTA (fixed)
```

### When to deviate

- **Beats 1 + 2** ("PIXELS ARE OUT / ATOMS ARE IN") are *paradigm-shift* openers. For company deep-dives or market-structure pieces, swap in a more neutral pair — e.g. `QUIETLY.` / `ALL AT ONCE.` or `ONE CATEGORY.` / `THREE WINNERS.`
- **Beat 4 (deal rail)** assumes "new category, multiple deals." For a profile piece, replace with the `rvl-trailer/compositions/04-issue-headlines.html` stacked-list layout (a single-subject retrospective).
- **Beat 5 (thesis)** is always 2 lime hero lines. Don't make it prose.

---

## Voice direction

**Default:** `af_heart` @ 0.92× — warm, confident, slightly conspiratorial.

| Voice        | Character                          | Use when                           |
|--------------|-----------------------------------|------------------------------------|
| `af_heart`   | Female, warm, measured *(default)* | Most issues                        |
| `af_sky`     | Female, brighter, higher energy    | Hype issues, launches              |
| `am_michael` | Male, confident, Bloomberg-ish     | Market-structure, macro            |
| `am_adam`    | Male, calm, Apple-keynote          | Deep-dive think pieces             |
| `bm_george`  | British male, dry                  | Retrospectives                     |
| `bf_emma`    | British female, authoritative      | Interview lead-ins                 |

Full list: `npx hyperframes tts --help`.

---

## One-time setup (new machine)

```bash
pip install kokoro-onnx soundfile       # TTS backend
sudo apt install ffmpeg                  # Linux (macOS: brew install ffmpeg)
npx hyperframes doctor                   # verify
```

---

## Render contract — the discipline

- **All hero type fits the 1920 frame.** Existing font sizes are tuned; if a swap token is longer, reduce the font-size in that comp.
- **One symbolic color per beat.** Lime is the brand. White is neutral. Never introduce a third color.
- **Every beat ends with a block-wipe** except Beat 7 (CTA holds).
- **VO is split** into `narration-main.wav` + `narration-cta.wav` so the CTA always lands on Beat 6 regardless of main narration length.
- **Loudnorm to -14 LUFS** before shipping — baseline render is -23 LUFS (broadcast), needs the lift for YouTube/TikTok/LinkedIn.
- **Commit `preview.mp4`, `preview-small.mp4`, `preview.gif`, `contact-sheet.png`** to the branch — `renders/` stays gitignored.

## Worked example — the W17 Physical AI issue

See `../rvl-physical-ai/` for a fully-rendered reference issue. Every swap token has a concrete value; every render step has been executed. Read it side-by-side with this HANDOFF if any part of the workflow is unclear.

## Publishing checklist

- [ ] Pull this week's RVL article (headline, thesis, deals, signoff)
- [ ] Clone template to `rvl-week-<n>-<slug>`
- [ ] Update `meta.json` id + name
- [ ] Fill in the 7 swap tokens
- [ ] Update `SCRIPT.md` Main narration block
- [ ] Regenerate `narration-main.wav`
- [ ] `npx hyperframes lint` → 0 errors
- [ ] Draft render + eyeball the contact-sheet
- [ ] Loudnorm → `preview.mp4` at -14 LUFS
- [ ] Generate share assets (small MP4, GIF, contact-sheet)
- [ ] Commit + push
- [ ] Upload to YouTube / Twitter / LinkedIn / newsletter
