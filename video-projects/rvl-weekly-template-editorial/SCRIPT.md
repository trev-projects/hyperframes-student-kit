# RVL Editorial — Narration Template

**Voice:** `af_heart` @ 0.92× (Kokoro-82M) — warm, deliberate, slightly conspiratorial
**Length:** 4 short lines (~45 words / ~14s of main narration, plus the fixed 2s CTA)
**Tone rule:** the editorial style holds longer on each beat, so the VO can breathe — fewer lines, more weight per line. Each line speaks to ONE chapter.

---

## Main narration — 4 lines, one per chapter

```
{CH1_LINE}

{CH2_LINE}

{CH3_LINE}

{CH4_LINE}
```

### Slot meanings

| Slot           | Maps to Beat              | W17 Physical AI example                                                                        |
|----------------|---------------------------|------------------------------------------------------------------------------------------------|
| `{CH1_LINE}`   | 01. THE SHIFT             | "Pixels are out. Atoms are in."                                                                |
| `{CH2_LINE}`   | 02. THE NUMBERS           | "Three rounds, ninety days, two point two billion dollars — just to get started."              |
| `{CH3_LINE}`   | 03. THE THESIS            | "Every major fund now has a Physical A I thesis. If yours doesn't, you're already late."       |
| `{CH4_LINE}`   | 04. THE PAYOFF (CTA lead) | "Software redefined value. Physical A I will redefine reality."                                |

## CTA line — FIXED, never edit per issue

```
Read the latest issue and sign up at R V L dot tech.
```

Pre-baked in `assets/narration-cta.wav`. Plays at t=29s on Beat 04 outro.

---

## Pronunciation notes

| Write as          | TTS says                |
|-------------------|-------------------------|
| `A I`             | A-I (letters)           |
| `R V L`           | R-V-L                   |
| `G P s`           | G-P-s                   |
| `one point five billion` | $1.5B           |
| `R V L dot tech`  | rvl.tech                |

## Pre-TTS checks

- [ ] Each line maps to exactly ONE chapter on screen?
- [ ] Each line ≤ 22 words (longer than kinetic template — editorial allows more breath)?
- [ ] Final line bridges into the CTA naturally?
- [ ] All numbers spelled out, acronyms letter-spaced

## Commands

```bash
# Main narration
npx hyperframes tts "{CH1_LINE} {CH2_LINE} {CH3_LINE} {CH4_LINE}" \
  --voice af_heart --speed 0.92 --output assets/narration-main.wav

# Verify duration (target 13–17s)
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \
  assets/narration-main.wav
```
