# Digiwell Marketing — "How we work" sizzle

38 seconds, no voiceover, synthesized sound design. One source, two cuts:

| File | Format | Use |
|---|---|---|
| `exports/digiwell-how-we-work-16x9.mp4` | 1920×1080 | Services / how-it-works page, YouTube, LinkedIn feed |
| `exports/digiwell-how-we-work-9x16.mp4` | 1080×1920 | Reels, Shorts, TikTok, LinkedIn/IG stories |
| `exports/poster-16x9.jpg` | still | Poster frame for the web embed |

**Brand: Cedar Night** (the live site's look, from the Digiwell Video Studio). Ground `#0E1714` with cedar
glows, cream `#F7F4EE` type, mint accents (`#7FB69E` lines, `#C3E2D3` italic accent words). Headlines in
**Newsreader** (the studio's suggested heading face; swap the family in `assets/sz.css` and the
`FONTFACE` block of `scripts/_write_scenes.py` to try Fraunces or another), Inter caps kickers, Manrope
body. The wordmark is always **Fraunces "Digiwell" with the hand-drawn mint underline**.

**Positioning:** email strategy, copy and implementation for coaches, consultants, authors and course
creators. No stats, no outcome guarantees, no AI-agency language, no em dashes.

## The cut

| Time | Scene | On screen |
|---|---|---|
| 0–5.8 | Hook | For coaches, consultants, authors and course creators. You've already earned *the audience.* (new subscriber / newsletter in drafts / welcome sequence off, "Day 23, nothing sent") Then the list *goes quiet.* |
| 5.4–9.6 | Thesis | It's not a ~~traffic~~ problem. It's an *email* problem. |
| 9.2–15.6 | Services | Email strategy, copy and implementation. Turn the audience you've already earned *into more business.* Strategy / Copy / Implementation. *Start with the one that matters most.* |
| 15.2–25.6 | How we work | Fit conversation → Scoped build → Test and sign-off → Handover |
| 25.2–29.4 | Proof | "Trevor completely gets our *space and messaging.*" Dave, Breakthrough Academy |
| 29.0–32.6 | Commitments | One owner. Your tools. Your data. Tested before it *goes live.* |
| 32.2–38 | CTA | Digiwell. Let's talk about *your email.* digiwellmarketing.com/contact |

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
python3 scripts/_write_scenes.py     # scenes are generated: edit copy/layout/timing HERE, it overwrites compositions/
# scene order and start times live in scripts/build-roots.mjs
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
