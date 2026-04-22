# RVL — Newsletter Trailer

Evergreen 30s pitch piece for the RVL newsletter. Use on the homepage hero, in paid ads, or as a top-of-feed social post. Updates never — swap once a year if the positioning changes.

**Brand** — identical to `rvl-physical-ai/DESIGN.md` (acid lime `#c3f53b` on `#0a0a0a`, Archivo Black display type, Space Grotesk/JetBrains Mono for secondaries, frame-fit discipline, no decorations, block-wipe transitions). Do NOT fork the brand tokens; if DESIGN changes for RVL, update the Physical AI project and copy here.

## The beat plan (6 beats · 30s · 30fps)

| # | Beat                | Window      | Copy on screen                                              | VO line over it                                     |
|---|---------------------|-------------|-------------------------------------------------------------|-----------------------------------------------------|
| 0 | Cold-open stamp     | 0.0 – 3.0s  | "EVERY SUNDAY."                                             | *(silent — music swells)*                           |
| 1 | Thesis hook         | 3.0 – 8.0s  | "Most newsletters miss the next category."                  | "Most newsletters miss the next category."          |
| 2 | Topic reel          | 8.0 – 14.0s | Cycling pills: BRANDS · STARTUPS · VENTURE CAPITAL · PHYSICAL AI · NEW MEDIA · FRONTIER TECH | "RVL covers the capital flows shaping the next decade." |
| 3 | Issue headlines     | 14.0 – 20.0s| Flash recent headlines (5 items)                            | "From Physical AI to stablecoin commerce — we write the read first." |
| 4 | Audience + delivery | 20.0 – 25.0s| "READ BY OPERATORS. / FOUNDERS. / GPs." + "WEEKLY. FREE."   | "Read by operators, founders, and GPs. Weekly. Free."|
| 5 | CTA outro           | 25.0 – 30.0s| RVL mark + tagline + "Sign up at rvl.tech"                  | "Sign up at R V L dot tech."                        |

## Compositions

```
compositions/
├── 00-rvl-bug.html           persistent corner mark (reused from Physical AI)
├── 01-cold-open.html         "EVERY SUNDAY."
├── 02-thesis.html            "Most newsletters miss the next category."
├── 03-topic-reel.html        Cycling topic pills
├── 04-issue-headlines.html   Recent issue flash-reel
├── 05-audience.html          "READ BY OPERATORS. FOUNDERS. GPs."
└── 06-cta.html               RVL wordmark + URL
```

## Differences from `rvl-physical-ai`

- **No pre-hook teaser** — this IS the teaser.
- **No deal rail** — evergreen, no specific fundraise amounts.
- **Topic cycle** is the signature motion, not a single-issue headline.
- **Issue headlines** reel doubles as social proof (shows the range of content).
- **CTA URL** is root domain: `rvl.tech` not `/p/<issue-slug>`.

## VO

Voice: `af_heart` @ 0.92× (same as Physical AI). Script is ~55 words, 27s natural pace. Starts at t=3.0s so Beat 0 teaser plays clean against music only.

## Music bed

Reusing `assets/music.wav` from Physical AI (34s, 55 Hz sub + A-minor pad + 100 BPM kick, mixed at 18%). Mood matches.
