# RVL — Physical AI — 30s Narration Script

**Voice:** mid-age male, fast confident delivery, slightly aggressive. Not the Apple-keynote calm we used on Digiwell — more *Bloomberg cross-talk × Anthropic launch trailer*. Think: a VC who just saw a new fund category open.
**TTS:** Kokoro-82M, voice `am_michael` or `am_puck` (both sharper/more assertive than `am_adam`).
**Target duration:** 28–30s at a slightly faster ~2.8 words/sec pace (~80 words total).

---

## The script (clean, to send to TTS)

Pixels are out.

Atoms are in.

Physical A I — humanoids, factory robots, self driving — just became its own investment category.

Figure — one point five billion. Physical Intelligence — four hundred million. Skild A I — three hundred million.

Every top fund now has a physical A I thesis.

Software ate the world. Physical A I will move it.

Read this week's RVL. Link in bio.

---

## Beat mapping (pre-TTS — refined after timing)

| Beat | Line                                                                       | Approx window |
|------|----------------------------------------------------------------------------|---------------|
| 1 — Cold open       | "Pixels are out."                                                 | 0.0–2.0s  |
| 2 — Flip            | "Atoms are in."                                                   | 2.0–3.8s  |
| 3 — Category land   | "Physical AI — humanoids, factory robots, self-driving — just became its own investment category." | 3.8–11.0s |
| 4 — Deal rail       | "Figure — 1.5 billion. Physical Intelligence — 400 million. Skild AI — 300 million." | 11.0–19.0s |
| 5 — Thesis          | "Every top fund now has a Physical AI thesis."                    | 19.0–22.5s |
| 6 — Signoff         | "Software ate the world. Physical AI will move it."               | 22.5–27.0s |
| 7 — CTA             | "Read this week's RVL. Link in bio."                              | 27.0–30.0s |

## Pronunciation

- **AI** → `A I` (each letter)
- **1.5B / $1.5 billion** → `one point five billion`
- **400M / $400 million** → `four hundred million`
- **300M / $300 million** → `three hundred million`
- **Skild** → `skild` (rhymes with "killed") — one syllable
- **RVL** → `R V L` (spelled out, each letter)
- **rvl.tech** → `R V L dot tech` (used on-screen, not spoken in script v1)

## Tone checks

- Opens with a 4-word claim + a 4-word counter-claim. Punchy. ✓
- Contractions: "ate" (past tense), "week's". Minimal — matches punchier register.
- Proof beat lists 3 specific deals with real numbers. Grounded. ✓
- Closing line is an explicit callback to Marc Andreessen's "software is eating the world" — meta for this audience. ✓
- CTA is deliberately short ("Link in bio" works on Twitter/LinkedIn; the on-screen text gives `rvl.tech/p/physical-ai`).

## Script-swap (future issues)

Structure is parameterized — future weeks fill in:

```
{OLD_PARADIGM} are out.
{NEW_PARADIGM} are in.
{ISSUE_TOPIC} — {EXAMPLES} — just became its own investment category.
{DEAL_1_NAME} — {AMOUNT_1}. {DEAL_2_NAME} — {AMOUNT_2}. {DEAL_3_NAME} — {AMOUNT_3}.
Every top fund now has a {ISSUE_TOPIC} thesis.
{CLOSING_METAPHOR}.
Read this week's RVL. Link in bio.
```

For issues that aren't "new investment category" shaped (e.g., company deep-dives, person profiles, market structure pieces), alternate templates live in `scripts/` — see `HANDOFF.md` when we template them.
