# RVL Weekly — Editorial Template

> **Second canonical template** for weekly RVL issue videos. Same brand (acid lime + black + Archivo Black + JetBrains Mono) as `rvl-weekly-template/`, but a **slower, more designed** rhythm — magazine-style numbered chapters instead of the kinetic-deck pacing of the original.
>
> Use this template for **deeper analysis pieces, profiles, and market-structure issues**. Use the original `rvl-weekly-template/` for **paradigm-shift / new-category issues**.

---

## TL;DR — produce next week's issue

```bash
# From the workspace root, one-shot clone + rename:
./video-projects/rvl-weekly-template-editorial/scripts/new-issue.sh 18 stablecoins "Stablecoin Commerce"

cd video-projects/rvl-week-18-stablecoins

# Edit the remaining content swap points — search for "<!-- SWAP:" in each composition
#   (cover title, chapter labels, chapter quotes, stat rows, summary, attribution)
# Also update the date in compositions/00-cover.html (masthead-date)

# Update SCRIPT.md "Main narration" block, then regenerate VO
npx hyperframes tts "Edited main narration block, 4 lines." \
  --voice af_heart --speed 0.92 --output assets/narration-main.wav

# Lint → draft render → loudnorm → previews → push
npx hyperframes lint
npx hyperframes render --quality draft --output renders/rvl-week-18-draft.mp4

ffmpeg -i renders/rvl-week-18-draft.mp4 \
  -c:v copy -af "loudnorm=I=-14:LRA=11:TP=-1.5" -c:a aac -b:a 192k preview.mp4
ffmpeg -i preview.mp4 -vf "scale=1280:720" -c:v libx264 -preset veryfast -crf 30 \
  -c:a aac -b:a 128k -movflags +faststart preview-small.mp4
ffmpeg -i preview.mp4 -vf "fps=10,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=5" -loop 0 preview.gif
ffmpeg -i preview.mp4 -vf "fps=1,scale=480:-1,tile=4x8" -frames:v 1 contact-sheet.png

cd ../..
git add video-projects/rvl-week-18-stablecoins && git commit -m "rvl-week-18: stablecoin commerce" && git push
```

---

## Style comparison — when to use which template

| Dimension       | `rvl-weekly-template/` (Kinetic)            | `rvl-weekly-template-editorial/` (Editorial)            |
|-----------------|---------------------------------------------|---------------------------------------------------------|
| Pacing          | Fast, ~9 beats in 33s                       | Slow, 5 beats in 32s                                    |
| Hero text style | Kinetic per-char bursts, slams, edge-clips  | Numbered chapters, single statement per beat, more hold |
| Structure       | PIXELS/ATOMS opener → category → deals → thesis → signoff → CTA | ISSUE COVER → 3 numbered chapters → CTA |
| Energy          | Punk-VC, "scroll-stop"                      | Magazine cover, "considered" reading                    |
| Best for        | Paradigm-shift issues, new categories       | Profiles, retrospectives, market structure, deep dives  |

Both share the same brand, the same music bed, the same VO voice (`af_heart` @ 0.92×), and the same loudnorm post-process — so you can mix and match week to week without breaking visual continuity.

---

## Complete swap-token catalog

**13 tokens total.** The helper script `scripts/new-issue.sh` takes care of the 3 global ones (ISSUE_NO, project id, footer). You manually edit the other 10 by opening each composition and searching for `<!-- SWAP: ` comments.

### Global tokens (handled by `scripts/new-issue.sh`)

| #  | Token               | Auto-handled? | Appears in                                             |
|----|---------------------|---------------|--------------------------------------------------------|
| 1  | `PROJECT_ID`        | ✅ script     | `meta.json` (id + name), `index.html` (data-composition-id + __timelines key) |
| 2  | `ISSUE_NO`          | ✅ script     | `00-cover.html` (masthead) + footer on all beats       |
| 3  | `W-ATTRIBUTION`     | ✅ script     | `03-chapter-thesis.html` ("W17" in attribution)        |

### Manual content tokens (edit `<!-- SWAP: ... -->` markers)

| #  | Token                 | File                          | Max chars | Example                                               |
|----|-----------------------|-------------------------------|-----------|-------------------------------------------------------|
| 4  | `ISSUE_DATE`          | `00-cover.html`               | 18        | `APRIL 21, 2026`                                      |
| 5  | `COVER_TITLE`         | `00-cover.html`               | 14 one-line, longer wraps | `PHYSICAL AI` · `STABLECOINS` · `AI-NATIVE BRANDS` |
| 6  | `CH1_LABEL`           | `01-chapter-shift.html`       | 14        | `THE SHIFT` · `THE PLAYER` · `THE MOMENT`             |
| 7  | `CH1_QUOTE`           | `01-chapter-shift.html`       | 50        | `Pixels are out.<br/>Atoms are in.`                   |
| 8  | `CH2_LABEL`           | `02-chapter-numbers.html`     | 14        | `THE NUMBERS` · `THE DEALS` · `THE RAISE`             |
| 9  | `STAT_ROW_1..3`       | `02-chapter-numbers.html`     | co ≤ 20   | `FIGURE $1.5B` · `PHYSICAL INTELLIGENCE $400M`        |
| 10 | `STAT_SUMMARY`        | `02-chapter-numbers.html`     | 60        | `$2.2B in 90 days. New category, fully formed.`       |
| 11 | `CH3_LABEL`           | `03-chapter-thesis.html`      | 14        | `THE THESIS` · `THE TAKE` · `THE READ`                |
| 12 | `CH3_QUOTE`           | `03-chapter-thesis.html`      | 70        | `Every major fund now has a Physical AI thesis.`      |
| 13 | `CH3_ATTRIBUTION`     | `03-chapter-thesis.html`      | 30        | `— RVL ANALYSIS • W17`                                |

**Fixed (almost never change):**
- `CH4_LABEL` in `04-cta.html` — `READ THE ISSUE`
- `RVL_TAGLINE` — the brand tagline
- `CTA_URL` — `rvl.tech`

---

## Stat-row specifics

`02-chapter-numbers.html` has 3 rows. Each `<div class="stat-row">` contains:

```html
<span class="stat-co">COMPANY NAME</span>                   <!-- ≤ 20 chars uppercase -->
<span class="stat-amt">
  <span class="amt-num" data-target="1.5">0.0</span>        <!-- FINAL number (counter counts up) -->
  <span class="amt-unit">B</span>                           <!-- 'B' for billions, 'M' for millions -->
</span>
```

The `$` sign prefix renders automatically. Keep decimal precision sensible: `1.5` becomes `$1.5B`, `400` becomes `$400M`. The counter uses `data-target` as the final value and animates from 0.

If you need fewer than 3 rows (e.g., only 2 deals), delete the extra `<div class="stat-row">` block. The timeline script indexes rows by class name (`.sr1`, `.sr2`, `.sr3`) — delete corresponding entries in the `rows` array in the `<script>` block too.

---

## Variable chapter labels — not just "THE SHIFT / NUMBERS / THESIS"

The defaults work for a paradigm-shift issue. For other issue types, swap in:

| Issue type             | CH1 label        | CH2 label        | CH3 label        |
|------------------------|------------------|------------------|------------------|
| Paradigm shift (W17)   | `THE SHIFT`      | `THE NUMBERS`    | `THE THESIS`     |
| Company profile        | `THE PLAYER`     | `THE RAISE`      | `THE READ`       |
| Market structure       | `THE MOMENT`     | `THE MOVE`       | `THE TAKE`       |
| Retrospective          | `THE ORIGIN`     | `THE ARC`        | `THE LESSON`     |
| Funding roundup        | `THIS WEEK`      | `THE DEALS`      | `THE PATTERN`    |

Pick whichever frame fits the week's content. Keep ≤ 14 chars.

---

## File map

```
rvl-weekly-template-editorial/
├── HANDOFF.md                THIS FILE — workflow + swap-token catalog
├── SCRIPT.md                 narration template (4-line, slower)
├── STORYBOARD.md             beat-by-beat direction (optional reference)
├── meta.json                 project metadata
├── hyperframes.json          CLI config
├── index.html                root — wires 5 beats + VO + music bed
├── scripts/
│   └── new-issue.sh          clone + rename helper
├── assets/
│   ├── gsap.min.js           bundled GSAP (locked)
│   ├── music.wav             34s synth bed (reuse across issues)
│   ├── narration-main.wav    REGENERATE per issue
│   └── narration-cta.wav     FIXED ("Read the latest issue and sign up at RVL dot tech")
└── compositions/
    ├── 00-cover.html              ISSUE_NO + ISSUE_DATE + COVER_TITLE
    ├── 01-chapter-shift.html      CH1_LABEL + CH1_QUOTE
    ├── 02-chapter-numbers.html    CH2_LABEL + STAT_ROW_1..3 + STAT_SUMMARY
    ├── 03-chapter-thesis.html     CH3_LABEL + CH3_QUOTE + CH3_ATTRIBUTION
    └── 04-cta.html                CH4_LABEL + RVL outro
```

## Worked example

This template ships with the W17 Physical AI content as the placeholder state. Render it as-is to see the editorial style applied to a real issue.

---

## QA checklist before shipping

- [ ] Cover title fits the frame (≤ 14 chars one-line; longer wraps naturally)
- [ ] No overflow at chapter labels (≤ 14 chars uppercase)
- [ ] Chapter 1 body ≤ 50 chars per `<br/>`-separated line
- [ ] Chapter 3 body ≤ 70 chars
- [ ] Each `.stat-co` ≤ 20 chars
- [ ] `STAT_SUMMARY` ≤ 60 chars
- [ ] All `ISSUE NN` references match (masthead, 4 footers, W-attribution) — the helper script handles this
- [ ] `narration-main.wav` 13–18s, `narration-cta.wav` 2–3s (fixed)
- [ ] `npx hyperframes lint` → 0 errors
- [ ] Contact-sheet shows no overflow at hero moments
- [ ] Loudnorm applied (preview.mp4 should measure ~-15 LUFS)
