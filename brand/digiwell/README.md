# Digiwell Marketing: Brand Kit (Cedar Night)

The source of truth for any Digiwell video, slide, graphic or overlay made in this workspace.
Hand this folder to a new session and it has everything: tokens, fonts, helpers, textures,
footage, copy rules and a worked reference project.

> **Reference build:** `video-projects/digiwell-sizzle/` (the 42s "How we work" sizzle, 16:9 + 9:16).
> When in doubt, copy what it does.

---

## 1. Positioning (what we say)

| | |
|---|---|
| **Category** | Email strategy, copy and implementation |
| **Who for** | Coaches, consultants, authors and course creators (established, expert-led businesses) |
| **Hero line** | Turn the audience you've already earned *into more business.* |
| **Thesis** | It's not a traffic problem. It's an *email* problem. |
| **Offer shape** | One journey at a time (welcome/nurture, newsletter, or enquiry follow-up), built in the tools they already use, one accountable owner for strategy, copy, build and testing |
| **How we work** | Fit conversation → Scoped build → Test and sign-off → Handover (ongoing help scoped separately) |
| **Commitments** | One owner. Your tools. Your data. Tested before it goes live. |
| **CTA** | Let's talk about *your email.* |
| **URL** | digiwellmarketing.com/contact |
| **Sign-off** | Trevor Davis, Founder, Digiwell Marketing · Toronto |

AI is how the work gets done, never the reason to buy.

### Copy guardrails (hard rules)
- **No em dashes.** Use commas, periods or colons.
- Canadian spelling (colour, behaviour, programme is fine either way, "enquiry").
- No hashtags on LinkedIn; put links in the first comment.
- No AI-agency language: "AI era", "growth engine", "10x", "done-for-you AI", "automate everything".
- No guarantees of leads, revenue, inbox placement, compliance or results.
- No invented stats, case studies, testimonials or screenshots presented as real.
- Placeholders never ship on screen. If a number or quote isn't approved, cut the beat.
- Short plain lines. One idea per beat.

### Approved proof and credits
| Item | Wording | Status |
|---|---|---|
| Testimonial | "Trevor completely gets our *space and messaging.*" Dave, Breakthrough Academy | **Confirm approval before public use** |
| Speaking credit | Toronto Tech Week 2026 workshop, in partnership with StartGBC at George Brown Polytechnic | Confirmed by Trevor |
| On-screen form | Kicker: `Toronto Tech Week 2026` · Line: "Leading a workshop with StartGBC at George Brown Polytechnic." | In use (sizzle) |

---

## 2. Colour

Dark brand. The ground is always near-black cedar, never flat black.

| Token | Hex | Use |
|---|---|---|
| `--cn-bg` | `#0E1714` | Ground |
| `--cn-raise` | `#111C18` | Raised ground |
| `--cn-surf` | `#15231F` | Cards, panels |
| `--cn-surf-2` | `#1A2B26` | Secondary surfaces, chat bubbles |
| `--cn-cedar` | `#2F5D50` | Icon discs, glows |
| `--cn-cedar-deep` | `#1C3A32` | Statement scenes (thesis) |
| `--cn-text` | `#F7F4EE` | Headlines, primary text (warm cream) |
| `--cn-text-2` | `#D3D8D2` | Body |
| `--cn-text-3` | `#A7B5AE` | Muted, metadata |
| `--cn-mint` | `#7FB69E` | Lines, underlines, edges, ticks, focus rings |
| `--cn-mint-2` | `#9CCAB5` | Kickers |
| `--cn-mint-3` | `#C3E2D3` | Italic accent words |
| `--cn-warm` | `#E9DCC6` | Optional accent on dark |
| Lines | `rgba(214,232,223,0.14 / 0.26)` | Hairlines, card borders |

**Grounds:** default `.cn-stage` (lit upper-right, deep pool bottom-left), `.cn-deep` (statements),
`.cn-surf` (lists). For richer scenes use the generated plates in `assets/textures/` (section 7).

A **cream variant** exists on the site (`#F7F4EE` ground, ink `#14201C`, cedar `#2F5D50` accents) for
documents and light UI. Video defaults to dark.

---

## 3. Type

| Role | Face | Spec |
|---|---|---|
| Headlines | **Newsreader** 600 | tracking −0.01em, line-height 1.08 |
| Accent words | Newsreader *italic* 500, `--cn-mint-3` | Wrap in `<span class="acc">`. One accent phrase per line, max |
| Kickers | **Inter** 600 caps | 0.1em tracking, `--cn-mint-2`, ~22–26px at 1080p |
| Body | **Manrope** 500–700 | 34px / 1.45 at 1080p |
| Wordmark | **Fraunces** 600, "Digiwell" | Always Fraunces, never retyped in another face |

Fraunces is also the site's current heading face. Newsreader was chosen for video (cleaner f, calmer).
Swapping headline face = change `.cn-h` in `tokens.css`.

**Sizes at 1920×1080:** hero 116–128px · scene headline 86–104px · step title 96px · body 30–36px.
At 1080×1920 keep the same px; lines just wrap more. Keep accent phrases together (`.cn-grp`).

---

## 4. Wordmark

`Digiwell` in Fraunces 600, cream, with a **hand-drawn mint underline** (SVG path
`M2 12 C 30 3, 60 19, 98 7`, round caps).

- Corner mark on every scene: `<div class="cn-mark cn-corner"></div>` (40px, top-left, 110px gutter).
- End card: large (84px) and the underline **draws on** with `SZ.drawMark()`.
- Never recolour, outline, stretch or add a period. Never put it on a busy photo without a shade.

---

## 5. Motion

Calm and editorial. Confident, not hype.

- **Eases:** `power3.out` for entrances, `power3.inOut` / `expo.inOut` for wipes. No bounces on type.
- **Text:** rises 40–50px with fade, staggered by word (`SZ.words`), 0.04–0.07s.
- **Transitions (one per scene, rotate them):** right-to-left panel wipe with a mint leading edge,
  bottom-up cover with mint edge, centre iris, horizontal split, diagonal wipe with a mint slab,
  slow dissolve for proof. Incoming scene overlaps the outgoing by 0.4s.
- **Underlines and strikes** reveal left to right (clip wipe, not dash animation).
- **Pace:** 3.5–6s per beat; the outro holds 4s+.
- Grain on every scene (`.cn-grain`). No chrome gradients, no perspective grids (those are
  `MOTION_PHILOSOPHY.md` defaults; this brand overrides them, but keep its discipline).

---

## 6. Components (all in the reference project)

| Component | Where | Notes |
|---|---|---|
| UI notification card | `z1-hook` | Icon disc, title, sub, mono chip; desaturate to show "gone cold" |
| Statement + strike | `z2-thesis` | Struck word dims; accent word gets the mint underline |
| Service cards | `z3-services` | Three cards, soft mint focus walks across them |
| Step sequence + rail | `z4-how` | Four steps with progress rail; each step has its own micro-visual |
| Founder / footage | `z4b-founder` | 16:9: framed portrait clip right, name left. 9:16: full-bleed clip, lower third |
| Quote | `z5-proof` | Fraunces quote mark in mint, Newsreader quote, Manrope attribution |
| Stacked lines | `z6-commit` | Four lines landing 0.5s apart, last in accent |
| End card | `z7-cta` | Large wordmark draws on, headline, lede, cream pill URL |

**Lower third spec:** kicker (Inter caps mint) / name (Newsreader 112–128px) / role (Manrope 700,
`--cn-mint-3`) / one plain line. 9:16: anchored bottom with 470px bottom padding (clears platform UI).

---

## 7. Assets

| Path | What |
|---|---|
| `tokens.css` | All tokens, grounds, type classes, wordmark, grain. Import first |
| `brand.js` | `SZ.fmt` (9:16 detection), `SZ.words`, `SZ.marks`, `SZ.drawMark`, `SZ.hold` |
| `fonts/` | Newsreader (roman + italic), Fraunces, Inter, Manrope. Self-hosted woff2 |
| `assets/textures/cedar-plate-16x9.jpg`, `-9x16.jpg` | AI-generated (OpenAI gpt-image-2) atmospheric grounds: cedar with mint glow upper-right, paper grain. No text, safe under type |
| `assets/footage/ttw26-workshop-startgbc-full.mp4` | Trevor teaching, Toronto Tech Week 2026 (25s, 9:16, silent, H.264) |
| `assets/footage/ttw26-workshop-startgbc-4s.mp4` | Graded 4s selects (0–1.9s + 5.3–7.4s of source), used in the sizzle |
| `examples/sizzle-scenes-16x9.jpg`, `lower-third-9x16.jpg` | What on-brand looks like: one frame per sizzle scene, and the 9:16 footage lower third |
| `sfx/synth-reference.py` | Stdlib-only synth for whooshes, thumps, ticks, chimes, pad bed. Retime events per cut |

**iPhone footage is HDR (HLG, bt2020, 10-bit). Always tonemap to Rec.709 SDR before using it.** HDR
sources push HyperFrames into a slow single-worker "HDR layered" composite where the video draws
*over* your text and shades and looks washed out. Convert first:

```bash
TM="zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p"
ffmpeg -i in.MOV -an -vf "$TM,fps=30" -c:v libx264 -crf 18 -g 30 \
  -color_primaries bt709 -color_trc bt709 -colorspace bt709 -movflags +faststart out.mp4
```

Check with `ffprobe ... -show_entries stream=color_transfer` (want `bt709`, not `arib-std-b67`), and in the
render log `"hasHdrContent":false`. The kit's footage is already converted.

**Footage notes:** best moments are 0–1.9s and 5.3–7.4s (facing the room, gesturing). Avoid ~8–12s
(looking down) and 18–20s (drinking). Room audio is unusable. The George Brown podium logo is visible;
fine for the speaking credit, crop it if a piece shouldn't lean on it.

---

## 8. Using OpenAI (key is on the environment)

The proxy injects the key; send `Authorization: Bearer dummy`.

- **Images:** `gpt-image-2` (`/v1/images/generations`). Use for grounds, textures, abstract
  illustrations, device mockups. Always prompt with the hex palette, "no text, no logos, no people".
  Never generate type, logos, data, screenshots or people presented as real.
- **Voiceover:** `gpt-4o-mini-tts`. More natural than Kokoro for narrated cuts.
- **Transcription:** `gpt-4o-transcribe` / `gpt-4o-transcribe-diarize` for captions and speaker labels.

Save generated assets into this kit (with the prompt in the commit message) so they're reused, not
regenerated.

---

## 9. Starting a new piece

```bash
mkdir -p video-projects/<slug>/{compositions,assets/fonts,scripts}
cp brand/digiwell/fonts/*.woff2 video-projects/<slug>/assets/fonts/
cp brand/digiwell/tokens.css video-projects/<slug>/assets/sz.css
cp brand/digiwell/brand.js   video-projects/<slug>/assets/sz.js
cp video-projects/digiwell-sizzle/{hyperframes.json,meta.json} video-projects/<slug>/   # edit meta id/name/size
cp video-projects/digiwell-sizzle/assets/gsap.min.js video-projects/<slug>/assets/
# Start from the sizzle's scripts/_write_scenes.py (shared shell) and scripts/build-roots.mjs (16:9 + 9:16)
```

Then: lint both formats → draft render → pull a frame per scene and look at every one → standard render
→ two-pass loudnorm to −14 LUFS → commit.

**Pre-flight before handing anything over:** every scene has the corner mark and grain · one accent
phrase per line max · no em dashes · no unapproved claims · nothing cropped or overlapping in either format
· text readable over footage (shade it) · outro holds 4s+.
