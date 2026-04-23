# RVL Weekly — Narration Template

**Voice:** `af_heart` @ 0.92× (Kokoro-82M) — warm, confident, slightly conspiratorial
**Length:** 6 short lines (~55 words / ~16–18s of main narration, + a fixed 2s CTA)
**Tone rule:** VO speaks OVER the visuals — it *analyzes*, it doesn't *read*

---

## Main narration — edit per issue, re-run TTS

Edit the six lines below. Keep each line ≤ 18 words, varied rhythm, one idea per line.

```
{HOOK_LINE}

{PARADIGM_SHIFT_LINE}

{CATEGORY_DEFINITION_LINE}

{PROOF_STAT_LINE}

{THESIS_LINE}

{SIGNOFF_CALLBACK_LINE}
```

### Slot meanings

| Slot                          | Purpose                                        | W17 Physical AI example                                                                              |
|-------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------------|
| `{HOOK_LINE}`                 | 1-line tease of this week's topic              | "This week on R V L — the race to the physical world begins."                                       |
| `{PARADIGM_SHIFT_LINE}`       | What's out / what's in                         | "Software's era is ending. Atoms are taking over."                                                  |
| `{CATEGORY_DEFINITION_LINE}`  | Define the category in plain terms + examples  | "Physical A I is robotics meeting frontier models. Humanoids. Factories. Autonomy."                  |
| `{PROOF_STAT_LINE}`           | Data / deal / number that grounds it           | "In the last ninety days, three rounds closed. Two point two billion dollars — just to get started." |
| `{THESIS_LINE}`               | Why everyone should care                       | "Every major fund now has a dedicated pod. If yours doesn't, you're already late."                   |
| `{SIGNOFF_CALLBACK_LINE}`     | A historical callback + new conviction          | "Software redefined value. Physical A I will redefine reality."                                     |

## CTA line — FIXED, do NOT change per issue

```
Read the latest issue and sign up at R V L dot tech.
```

Already baked into `assets/narration-cta.wav`. Only regenerate if the URL or phrasing changes.

---

## Pronunciation / TTS quirks

| Write in script as     | TTS says                 |
|------------------------|--------------------------|
| `A I`                  | A-I (letters)            |
| `R V L`                | R-V-L                    |
| `G P s`                | G-P-s                    |
| `C R M`                | C-R-M                    |
| `one point five billion` | $1.5B                  |
| `ninety`               | 90                       |
| `twenty percent`       | 20%                      |
| `R V L dot tech`       | rvl.tech                 |

## Pre-TTS checks

- [ ] Does each line add ONE thought the visual can't carry alone?
- [ ] Any line that just re-reads the on-screen text? → rewrite or cut
- [ ] Shortest line ≤ 10 words? Longest ≤ 18?
- [ ] Contractions used (reads like a person, not a press release)
- [ ] All numbers spelled out, acronyms letter-spaced

---

## Commands

### Regenerate main narration

Paste your edited Main narration block as the quoted argument:

```bash
npx hyperframes tts "This week on R V L — [your hook]. [your paradigm shift line]. [your category line]. [your proof stat]. [your thesis]. [your callback]." \
  --voice af_heart --speed 0.92 --output assets/narration-main.wav
```

### Regenerate CTA (rarely)

```bash
npx hyperframes tts "Read the latest issue and sign up at R V L dot tech." \
  --voice af_heart --speed 0.92 --output assets/narration-cta.wav
```

### Verify durations

```bash
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 assets/narration-main.wav
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 assets/narration-cta.wav
```

**Targets:**
- `narration-main.wav` — 15–18s (if > 20s, tighten lines or raise `--speed` to 0.96)
- `narration-cta.wav` — 2–3s (fixed, rarely re-generated)
