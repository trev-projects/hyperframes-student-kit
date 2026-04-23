# RVL Weekly — Editorial Template

> **Second canonical template** for weekly RVL issue videos. Same brand (acid lime + black + Archivo Black + JetBrains Mono) as `rvl-weekly-template/`, but a **slower, more designed** rhythm — magazine-style numbered chapters instead of the kinetic-deck pacing of the original.
>
> Use this template for **deeper analysis pieces, profiles, and market-structure issues**. Use the original `rvl-weekly-template/` for **paradigm-shift / new-category issues**.

---

## Style comparison — when to use which

| Dimension       | `rvl-weekly-template/` (Kinetic)            | `rvl-weekly-template-editorial/` (Editorial)            |
|-----------------|---------------------------------------------|---------------------------------------------------------|
| Pacing          | Fast, ~9 beats in 33s                       | Slow, 6 beats in 32s                                    |
| Hero text style | Kinetic per-char bursts, slams, edge-clips  | Numbered chapters, single statement per beat, more hold |
| Structure       | PIXELS/ATOMS opener → category → deals → thesis → signoff → CTA | ISSUE COVER → 4 numbered chapters → CTA |
| Energy          | Punk-VC, "scroll-stop"                      | Magazine cover, "considered" reading                    |
| Best for        | Paradigm-shift issues, new categories       | Profiles, retrospectives, market structure, deep dives  |

Both share the same brand, the same music bed, the same VO voice (`af_heart` @ 0.92×), and the same loudnorm post-process — so you can mix and match week to week without breaking visual continuity.

---

## How to produce next week's issue with this template

```bash
# Same flow as the kinetic template — only the swap tokens change
cd video-projects
cp -r rvl-weekly-template-editorial rvl-week-18-stablecoins
cd rvl-week-18-stablecoins

# Update meta.json
sed -i 's/"id": "rvl-weekly-template-editorial"/"id": "rvl-week-18-stablecoins"/' meta.json
sed -i 's/"name": "RVL — Weekly Issue Template (Editorial)"/"name": "RVL — W18 Stablecoin Commerce"/' meta.json

# Edit the 6 swap tokens in compositions/ (see below)
# Edit SCRIPT.md "Main narration" block, then regenerate VO
npx hyperframes tts "Edited main narration here." \
  --voice af_heart --speed 0.92 --output assets/narration-main.wav

# Lint + draft render + loudnorm + previews + push
npx hyperframes lint
npx hyperframes render --quality draft --output renders/rvl-week-18-draft.mp4
ffmpeg -i renders/rvl-week-18-draft.mp4 \
  -c:v copy -af "loudnorm=I=-14:LRA=11:TP=-1.5" -c:a aac -b:a 192k preview.mp4
ffmpeg -i preview.mp4 -vf "scale=1280:720" -c:v libx264 -preset veryfast -crf 30 \
  -c:a aac -b:a 128k -movflags +faststart preview-small.mp4
ffmpeg -i preview.mp4 -vf "fps=10,scale=640:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=bayer:bayer_scale=5" -loop 0 preview.gif
ffmpeg -i preview.mp4 -vf "fps=1,scale=480:-1,tile=4x8" -frames:v 1 contact-sheet.png
```

## Per-Issue Swap Checklist — 6 tokens

| #  | Token              | File                                       | Example (W17 Physical AI)                                                |
|----|--------------------|--------------------------------------------|--------------------------------------------------------------------------|
| 1  | `ISSUE_NO`         | `00-cover.html` · `.issue-no`              | `ISSUE 17`                                                               |
| 2  | `COVER_TITLE`      | `00-cover.html` · `.cover-title`           | `PHYSICAL AI`                                                            |
| 3  | `CH1_QUOTE`        | `01-chapter-shift.html` · `.chapter-body`  | `Pixels are out. Atoms are in.`                                          |
| 4  | `CH2_STATS`        | `02-chapter-numbers.html` — three rows     | `FIGURE $1.5B` · `PHYS. INTELLIGENCE $400M` · `SKILD AI $300M`           |
| 5  | `CH3_QUOTE`        | `03-chapter-thesis.html` · `.chapter-body` | `Every major fund now has a Physical AI thesis.`                         |
| 6  | `CTA_URL`          | `04-cta.html` · `.cta-url`                 | `rvl.tech/p/physical-ai`                                                 |

Plus `SCRIPT_MAIN` in `SCRIPT.md` (regenerate `narration-main.wav`).

The CTA narration ("Read the latest issue and sign up at RVL dot tech") is fixed in `assets/narration-cta.wav` — never re-record.

---

## File map

```
rvl-weekly-template-editorial/
├── HANDOFF.md                THIS FILE — editorial-template workflow
├── DESIGN.md                 (shared with kinetic template — see ../rvl-weekly-template/DESIGN.md)
├── SCRIPT.md                 narration template (4-line shape, slower)
├── STORYBOARD.md             beat-by-beat direction
├── meta.json                 project metadata
├── hyperframes.json          CLI config
├── index.html                root — wires 6 beats + VO + music bed
├── assets/
│   ├── gsap.min.js
│   ├── music.wav
│   ├── narration-main.wav    REGENERATE per issue
│   └── narration-cta.wav     FIXED
└── compositions/
    ├── 00-cover.html              ISSUE NN + COVER_TITLE
    ├── 01-chapter-shift.html      "01. THE SHIFT" + CH1_QUOTE
    ├── 02-chapter-numbers.html    "02. THE NUMBERS" + CH2_STATS rail
    ├── 03-chapter-thesis.html     "03. THE THESIS" + CH3_QUOTE
    ├── 04-cta.html                "04. READ" + RVL outro
    └── 00-rvl-bug.html            (optional — corner mark; not used by default in editorial)
```

## Worked example

This template ships with the W17 Physical AI content as the placeholder. Render it as-is to see the editorial style applied to a real issue.
