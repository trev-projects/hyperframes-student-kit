# Digiwell Marketing — "How we work" sizzle

34 seconds, no voiceover, synthesized sound design. One source, two cuts:

| File | Format | Use |
|---|---|---|
| `exports/digiwell-how-we-work-16x9.mp4` | 1920×1080 | Services / how-it-works page, YouTube, LinkedIn feed |
| `exports/digiwell-how-we-work-9x16.mp4` | 1080×1920 | Reels, Shorts, TikTok, LinkedIn/IG stories |
| `exports/poster-16x9.jpg` | still | Poster frame for the web embed |

Copy follows the 2026-09-12 email positioning (same canon as `digiwell-deck/deck-copy-v2.md`):
no stats, no outcome promises, no AI-agency language, no em dashes.

## The cut

| Time | Scene | On screen |
|---|---|---|
| 0–5.8 | Hook | People join your list. (New subscriber / Newsletter still in drafts / Welcome sequence not set up) Day counter: "Nothing sent". Then your email goes quiet. |
| 5.4–9.6 | Thesis | It's not a ~~traffic~~ problem. It's an **email** problem. |
| 9.2–15.6 | What we do | Email strategy and implementation. Email strategy / Newsletters / Welcome and nurture / Implementation. Start with the one that matters most. |
| 15.2–25.6 | How we work | Fit conversation → Scoped build → Test and sign-off (SIGNED OFF) → Handover |
| 25.2–28.8 | Commitments | One owner. Your tools. Your data. Tested before it goes live. |
| 28.4–34 | CTA | Let's talk about your email. digiwellmarketing.com |

## Website embed

Muted autoplay loop. Browsers only autoplay muted video, and the piece reads without sound.

```html
<video src="digiwell-how-we-work-16x9.mp4" poster="poster-16x9.jpg"
       autoplay muted loop playsinline preload="metadata"
       style="width:100%;height:auto;border-radius:16px"></video>
```

## Edit and re-render

```bash
cd video-projects/digiwell-sizzle
# edit compositions/z*.html (copy, timing) or scripts/build-roots.mjs (scene order/timing)
python3 scripts/make-sfx.py          # only if you retime beats: event times live here
node scripts/build-roots.mjs         # writes index.html (16:9) + build/vertical/ (9:16)
npx hyperframes lint && (cd build/vertical && npx hyperframes lint)
npx hyperframes render --quality standard --output renders/h-final.mp4
(cd build/vertical && npx hyperframes render --quality standard --output renders/v-final.mp4)
```

Then loudnorm to -14 LUFS before posting (two-pass; see the trailer projects).

**How the two formats share one source:** HyperFrames allows one root composition per project, so
`build-roots.mjs` generates `build/vertical/` as a sibling project: a copy of `compositions/` and `assets/`
with portrait dimensions stamped into every scene. Each scene adds a `.v` class when its root is portrait,
and its CSS re-lays out under `.v` selectors. **Never edit `build/`** (gitignored, regenerated every build).
