# RVL Weekly Video — Template Handoff

> Reusable pipeline for the RVL newsletter's weekly 30s animated video. Swap seven strings + run three commands → new video. Aesthetic (acid lime on black, Archivo Black display type, frame-clipped hero words) stays locked.

## TL;DR — one issue in five steps

```bash
cd video-projects/rvl-physical-ai

# 1. Update the seven swap-tokens in SCRIPT.md + across three compositions
#    (see "Per-Issue Swap Checklist" below)

# 2. Generate voiceover (voices: am_michael, am_adam, am_puck, bm_george, af_bella, af_sarah)
npx hyperframes tts "$(cat SCRIPT.md | grep -v '^#' | tr '\n' ' ')" \
  --voice am_michael --output assets/narration.wav

# 3. Lint
npx hyperframes lint

# 4. Draft render + verify
npx hyperframes render --quality draft --output renders/rvl-weekly-$(date +%Y-%W).mp4

# 5. Final render
npx hyperframes render --quality standard --output renders/rvl-weekly-$(date +%Y-%W)-final.mp4
```

Ship time per issue: ~10 minutes once you know where the swap-tokens live.

---

## Per-Issue Swap Checklist

Seven tokens change week-to-week. Everything else is locked.

| #  | Token               | File(s)                              | Example (Physical AI issue)                   |
|----|---------------------|--------------------------------------|-----------------------------------------------|
| 1  | `WEEK_LABEL`        | `compositions/00-hook-teaser.html`   | `W17 · APR 21`                                |
| 2  | `ISSUE_HEADLINE`    | `compositions/03-category-land.html` · `00-hook-teaser.html` | `PHYSICAL AI`                 |
| 3  | `EXAMPLES_3`        | `compositions/03-category-land.html` (the cycle row) | `HUMANOIDS` · `FACTORY ROBOTS` · `SELF-DRIVING` |
| 4  | `DEAL_ROWS_3`       | `compositions/04-deal-rail.html`     | `FIGURE $1.5B` · `PHYSICAL INTELLIGENCE $400M` · `SKILD AI $300M` |
| 5  | `PUNCHLINE_2`       | `compositions/05-thesis.html` (ln3 + ln4) | `PHYSICAL AI` / `THESIS.`                 |
| 6  | `SIGNOFF_PAIR`      | `compositions/06-signoff.html`       | `SOFTWARE ATE THE WORLD.` / `PHYSICAL AI WILL MOVE IT.` |
| 7  | `SCRIPT_VO`         | `SCRIPT.md` (regenerate narration)   | Full narration block in "The script" section |

Everything else — palette, fonts, grid, transitions, pacing, beat durations — stays locked.

### Where each token lives in code

**1. WEEK_LABEL** — edit `compositions/00-hook-teaser.html`, find `.week-stamp`:
```html
<div class="week-stamp">W17 &middot; APR 21</div>
```

**2. ISSUE_HEADLINE** — two places:
- `compositions/00-hook-teaser.html`: `.headline` text (the big flash word that becomes the teaser) — one or two words max
- `compositions/03-category-land.html`: split across `.h-physical` (line 1) and `.h-ai` (line 2, hero). Keep line 2 to 2–3 chars so it can stay frame-clipped aggressively.

**3. EXAMPLES_3** — `compositions/03-category-land.html`, the three `<div class="cyc c1/c2/c3">…</div>` lines. Each shows for ~0.8s. Keep each under 16 chars.

**4. DEAL_ROWS_3** — `compositions/04-deal-rail.html`, three `<div class="row">` blocks. Each has:
  - `.co` — company name (1–2 lines)
  - `.amt` with `data-target="<number>"` on the `.amt-num` span and a suffix letter `B` or `M` in `.amt-unit`

**5. PUNCHLINE_2** — `compositions/05-thesis.html`, the `.ln3` (first lime line) and `.ln4` (second lime line) content. Both marked `data-split` for per-char animation. Keep each ≤ 14 chars so they fit the frame.

**6. SIGNOFF_PAIR** — `compositions/06-signoff.html`:
  - `.line-1` (`data-split`) — white opener, ≤ 24 chars
  - `.line-2` — prefix + MOVE + suffix. To change the callback-word (the one that wobbles), rename `.move`'s text and adjust prefix/suffix splits.

**7. SCRIPT_VO** — `SCRIPT.md` body text. Use letter-spacing for acronyms (`A I` not `AI`), spell numbers (`one point five billion`). Re-run the `tts` command to regenerate `assets/narration.wav`.

---

## Voice Direction

Default voice: **`am_michael`** — sharp, confident, Bloomberg-cross-talk energy.

Alternative voices (all baked into the CLI, no extra install):

| Voice      | Character                                 | Use when                         |
|------------|-------------------------------------------|----------------------------------|
| `am_michael` | Mid-age male, confident, slightly aggressive | Default — VC/startup newsletter tone |
| `am_adam`    | Mid-age male, calm, Apple-keynote        | Reflective essays / think pieces |
| `am_puck`    | Younger male, energetic                  | Launch-day / hype issues         |
| `bm_george`  | British male, dry                        | Market-structure / analysis pieces |
| `af_bella`   | Female, warm                             | Founder profiles / interview lead-ins |
| `af_sarah`   | Female, professional                     | Report-style issues              |

Full list: `npx hyperframes tts --help` (covers all 40+ Kokoro voices).

---

## First-Time Setup (one-time)

On a fresh machine, install the Kokoro TTS backend:

```bash
pip install kokoro-onnx soundfile
```

FFmpeg is also required for rendering:

```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# macOS
brew install ffmpeg
```

Then verify:

```bash
npx hyperframes doctor
```

---

## Sync Narration Timing to Beats (optional but recommended)

The default beat timings assume the VO fits; if the voice ends up shorter/longer, use Whisper transcription to re-align:

```bash
npx hyperframes transcribe assets/narration.wav --model small.en --json > assets/narration.words.json
```

Then scan the JSON for the word onsets of each beat's opening phrase and shift beat-layer `data-start` values in `index.html`. A rule of thumb: keep beat visuals ~200ms *ahead* of the matching VO word — it reads as inevitable, not chasing.

---

## Weekly Publishing Checklist

- [ ] Pull this week's RVL article (headline, thesis, deals, tagline)
- [ ] Fill in the 7 swap-tokens above
- [ ] Update `SCRIPT.md` to match the article
- [ ] Run `npx hyperframes tts ... --output assets/narration.wav`
- [ ] `npx hyperframes lint` → 0 errors
- [ ] Draft render + eyeball (open `preview.mp4` or use Studio)
- [ ] Final `--quality standard` render
- [ ] Name the file `rvl-weekly-YYYY-WW.mp4` (year + ISO week)
- [ ] Upload to the RVL newsletter / social channels

---

## File Map (what's in this project)

```
rvl-physical-ai/
├── DESIGN.md                 brand (lime + black + display)
├── SCRIPT.md                 narration text (swap per issue)
├── STORYBOARD.md             beat-by-beat creative direction
├── HANDOFF.md                THIS FILE — weekly swap guide
├── assets/
│   ├── gsap.min.js           bundled (sandboxed-render compatible)
│   └── narration.wav         Kokoro TTS output (regenerate per issue)
├── index.html                root: 8 beat layers + VO audio
├── compositions/
│   ├── 00-rvl-bug.html       persistent RVL corner mark
│   ├── 00-hook-teaser.html   pre-hook flash teaser (WEEK_LABEL)
│   ├── 01-cold-open.html     "PIXELS ARE OUT."
│   ├── 02-flip.html          "ATOMS ARE IN."
│   ├── 03-category-land.html ISSUE_HEADLINE + EXAMPLES_3
│   ├── 04-deal-rail.html     DEAL_ROWS_3
│   ├── 05-thesis.html        PUNCHLINE_2
│   ├── 06-signoff.html       SIGNOFF_PAIR
│   └── 07-cta.html           RVL CTA hold
├── preview.mp4               latest draft (1920x1080)
├── preview-small.mp4         720p copy for mobile review
├── preview.gif               animated GIF (inline chat-friendly)
└── contact-sheet.png         4x9 grid of 1-per-second thumbs
```

## Roll Forward to Next Week

```bash
# clone this project as a starting template
cp -r video-projects/rvl-physical-ai video-projects/rvl-weekly-02-<slug>
cd video-projects/rvl-weekly-02-<slug>

# edit meta.json — new `id` + `name`
# edit the 7 swap-tokens
# regenerate narration
# render
```

Or keep one project folder and version the outputs by filename — your call. The project folder is cheap to duplicate (it's all text except `narration.wav` and `gsap.min.js`).
