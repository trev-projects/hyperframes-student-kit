# Digiwell Marketing — Standard Deck

A branded, animated slide deck built on HyperFrames. One source gives you:

| Output | How | Use it for |
|---|---|---|
| **Live presentation** | `npx hyperframes present` | Calls, pitches, workshops. Presenter view, speaker notes, audience window |
| **PDF** | `node scripts/export.mjs` | Email, leave-behinds, anywhere slides get attached |
| **Walkthrough MP4** | `node scripts/export.mjs` | LinkedIn, async sends. Every transition plays, then it holds on each slide |

Brand: warm paper, ink, terracotta and sand, set in Sora, Manrope and JetBrains Mono. It's the same system as the AI Operated newsletter; see `DESIGN.md`.

---

## Present it

```bash
cd video-projects/digiwell-deck
npx hyperframes present            # opens the presenter at http://localhost:3004
```

- **→ / Space** next · **← / Backspace** back · **P** opens the audience window · **F** fullscreen
- Speaker notes show in presenter mode (they come from `deck.json`).
- **Google Meet:** share the *audience tab* ("Share screen → A tab"). **Zoom:** drag the audience tab into its own window and share that window.
- Fonts are self-hosted in `assets/fonts/`, so the slides themselves render fully offline.

### Why "next" animates (the motion bridge)

The stock presenter *seeks* between slides, which means slides snap and no transition ever plays.
`scripts/motion-bridge.js` (inlined into `index.html`) upgrades it: a forward step **plays** the
timeline to the next stop, so every wipe, headline rise and card build runs live. Back and
jump-to-slide still snap, which is what you want when you're hunting for a slide.

It only activates inside the presenter. Render and Studio preview are unaffected, and if a future
HyperFrames release changes the presenter internals, it steps aside and you get native
snap navigation instead of a broken deck. To turn it off, set `"motionBridge": false` in `deck.json`
and rebuild.

---

## Edit a deck

**Text** lives in the slide files: `compositions/s01-title.html` … `s09-cta.html`. Open one and change the copy.

**Order, timing and speaker notes** live in `deck.json`:

```json
{ "id": "s06-pillars", "rests": [1.2, 1.8, 2.4], "notes": "Three clicks, one card each…" }
```

- `id` must match the file `compositions/<id>.html` and its `data-composition-id`.
- `rests` are the local times the presenter stops on. **One rest = a normal slide.
  Several = click-by-click builds** (s06 reveals one card per click).
- Put each rest just after that step's animation finishes.

After any `deck.json` change:

```bash
node scripts/build-deck.mjs        # regenerates index.html (timeline + presenter manifest)
npx hyperframes lint
```

The build refuses to run if a slide file is missing, its id doesn't match, or its
`data-duration` isn't `lastRest + 0.6`. It tells you the number to use.

### Add a slide

1. Copy the closest layout, e.g. `cp compositions/s04-statement.html compositions/s10-quote.html`.
2. In the new file, replace **every** `s04-statement` with `s10-quote` (template id, `data-composition-id`, the selector strings).
3. Add `{ "id": "s10-quote", "rests": [1.9], "notes": "…" }` to `deck.json` where you want it.
4. Set the file's `data-duration` (and `SLOT`) to `lastRest + 0.6`, then `node scripts/build-deck.mjs`.
5. Update the `NN / 09` counters in each slide's chrome if the count changed.

### The layout kit

| File | Layout | Notes |
|---|---|---|
| `s01-title` | Title | Wordmark, headline with highlighter, presenter line |
| `s02-agenda` | Agenda | Numbered rows |
| `s03-divider` | Section divider | Terracotta, outlined section number |
| `s04-statement` | Big statement | Two-line reframe, highlighter on the key phrase |
| `s05-stat` | Hero number | Count-up. **Sample stat, so swap in a real client result** |
| `s06-pillars` | Three-up | Builds one card per click |
| `s07-process` | Process | Four nodes on a drawn line |
| `s08-compare` | Before / after | Struck-through vs. checked |
| `s09-cta` | CTA | Terracotta, pill button, URL |

Shared styling lives in `assets/deck.css` (tokens + type scale) and shared motion lives in
`assets/deck.js` (`DW.enter` = the house wipe transition, plus `DW.rise` and `DW.swash`). Restyle or retime the
whole deck there, not in the individual slides.

`scripts/_write_layouts.py` generated the nine starter layouts once. **Re-running it overwrites
`compositions/`**, so edit the HTML files directly from now on.

---

## Export

```bash
npm install                        # once, at the workspace root (installs Playwright for the PDF)
node scripts/export.mjs            # renders standard quality, then writes exports/
node scripts/export.mjs --skip-render   # reuse renders/deck.mp4
```

Writes `exports/digiwell-deck.pdf` (one page per slide, final build state),
`exports/digiwell-deck-walkthrough.mp4`, and `exports/slides/NN.png` (one still per stop).
Set `CHROMIUM_PATH=/path/to/chrome` if Playwright can't find a browser.

## Sounds

`sfx/*.mp3` are the presenter's navigation sounds (advance, build step, back). Mute them with
the speaker icon in the nav cluster, or regenerate with `python3 scripts/make-nav-sfx.py`.
