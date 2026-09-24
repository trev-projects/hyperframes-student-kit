# Digiwell deck: copy v2 (aligned to the 2026-09-12 positioning)

**Status: draft for Trevor's approval. Not built yet.** The live deck is still v1.

**Source:** `DECK-REFRESH-PROMPT.md` (its positioning summary, gap analysis and guardrails). The canon
files it cites (`business/positioning.md`, `business/messaging-2026-09.md`, `CLAUDE.md` voice rules) live in
`Digiwell-Master-Skills-Structure`, which this session can't reach. Everything below traces to the
prompt, not to those files directly, and `tools/voice-gate/check.py` has not been run. See the checks at the end.

**The one-breath version this copy serves:** email strategy and implementation for established
expert-led businesses. One important journey, built in the tools they already use, with one accountable
owner. AI is how the work gets done, not the reason to buy. The next step is a fit conversation.

---

## 01 · Title

| | |
|---|---|
| Eyebrow | EMAIL STRATEGY AND IMPLEMENTATION |
| Headline | Give interested people / a **clear next step.** *(sand marker on "clear next step")* |
| Body | For established, expert-led businesses. We turn the interest you already have into consistent email follow-up. |
| Footer | TREVOR DAVIS · TORONTO, ON · DIGIWELLMARKETING.COM |

**Changed:** "Growth systems for the AI era" and "Growth partner for the AI era" are gone (generic AI-agency
language is banned). "Turn cold leads into loyal buyers" was an outcome promise and is gone. The
three-service list is gone. The hero and category lines come from the prompt's messaging direction.

## 02 · Agenda

| | |
|---|---|
| Eyebrow | TODAY |
| Headline | What we'll cover. |
| 01 | **The problem**: What happens after someone raises their hand |
| 02 | **One journey**: Why we start with one, not three |
| 03 | **How we work**: Fit, scope, test, handover |
| 04 | **Where to start**: A conversation about your email |

**Changed:** it ends in "Where to start" (the fit conversation), not the scorecard. "Four things in twenty
minutes" is replaced so the slide makes no time claim. There are still four items because the deck still has
four sections.

## 03 · Section divider

| | |
|---|---|
| Number | 01 |
| Title | The problem. |
| Body | What happens after people show interest. |

**Changed:** only the subline. It moves from "why good businesses leak growth" to where the positioning puts
the problem.

## 04 · Statement *(the thesis)*

| | |
|---|---|
| Line 1 | Most businesses don't have a traffic problem. |
| Line 2 | They have a **follow-up** problem. *(terracotta, marker on "follow-up")* |
| Body | People subscribe, enquire, then hear nothing useful. |

**Changed:** the body only. "Nobody is talking to them" read as a diagnosis of the viewer. This version
describes the gap from the buyer's side, as the prompt directs.

## 05 · Three questions *(new layout; replaces the "2 min" stat)*

| | |
|---|---|
| Eyebrow | THREE QUESTIONS WORTH ASKING |
| Headline | Where does follow-up break? |
| 01 | What happens after someone subscribes? |
| 02 | What happens after someone enquires? |
| 03 | Who owns the newsletter? |

**Changed:** the stat and its visible "SAMPLE STAT · SWAP IN A CLIENT RESULT" placeholder are removed.
No approved proof exists yet, so there's no number. The three questions are the three problem slices, framed
as questions per the messaging rule.

## 06 · Start with one journey *(builds one card per click)*

| | |
|---|---|
| Eyebrow | PICK THE ONE THAT MATTERS MOST |
| Headline | Start with one journey. |
| Card 01 | **Welcome and nurture**: What new subscribers get, in order, from day one. |
| Card 02 | **Enquiry follow-up**: What happens between "thanks for reaching out" and a real conversation. |
| Card 03 | **Newsletter loop**: A newsletter with an owner, a rhythm and a way to learn what's working. |

**Changed:** "Three systems. One growth engine." sold three things at once, and the positioning is ONE journey
per build. "Nothing slips" and "move cold leads to buyers on their own" were overclaims and are gone. The
cards are now a choice. **No card is highlighted terracotta until you confirm a default** (open question 2).

## 07 · How we work

| | |
|---|---|
| Eyebrow | HOW WE WORK |
| Headline | How we work together. |
| 1 | **Fit conversation**: Where things stand, and whether there's a useful first project. |
| 2 | **Scoped build**: One journey, agreed in writing, built in the tools you already use. |
| 3 | **Test and sign-off**: Tested end to end. Nothing goes live without your sign-off. |
| 4 | **Handover**: Documented and handed over. Ongoing help is scoped separately. |

**Changed:** "Audit (scorecard)" is superseded, and "Optimise" implied ongoing work by default. This is the
buying path from the prompt's summary of `offers.md`. "Done for you" is dropped from the headline.

## 08 · What you can count on

| | |
|---|---|
| Eyebrow | WHAT YOU CAN COUNT ON |
| Headline | One owner. One agreed journey. |
| Without (struck) | People subscribe and hear nothing useful · Enquiries wait on whoever has time · The newsletter goes out when someone remembers |
| With Digiwell | One accountable owner, from strategy to testing · Scope agreed in writing · Built in your existing tools, with your data under your control · Tested before anything goes live · A documented handover |

**Changed:** "Dashboards that show what converts" was out of scope and a conversion promise. "A consistent
weekly letter, every week" was only true for the newsletter slice. The With column is now the five commitments
the prompt lists.

## 09 · Where to start

| | |
|---|---|
| Eyebrow | WHERE TO START |
| Headline | Let's talk about **your email.** *(marker on "your email")* |
| Body | We'll see where things stand and whether there's a useful first project. |
| Button | digiwellmarketing.com |
| Sign-off | TREVOR DAVIS · TORONTO, ON |

**Changed:** the scorecard CTA and `/scorecard` URL are superseded. The CTA line and supporting line are the
prompt's own wording, and the sign-off matches slide 1.

---

## Checks I ran (manual, since the voice gate isn't available here)

- No em dashes in any slide text.
- No prices, currencies, timelines, capacity promises, or guarantees of leads, revenue, inbox placement or compliance.
- No stats, testimonials, case studies or placeholders on any slide.
- No "AI era", "growth engine", "10x" or "done-for-you AI". AI doesn't appear on a slide at all.
- Spelling: "enquire" and "enquiries"; no -or/-our words appear, so nothing is at risk there.
- "Handover" is used throughout. The prompt uses both "handed-over" and "handoff", so tell me if canon prefers "handoff".

## Open questions for Trevor

1. **Proof.** There's no approved client result or testimonial, so slide 5 is questions, not a number. Is any proof approved yet?
2. **Default journey.** Should one of the three cards on slide 6 be highlighted as the recommended starting point for a generic pitch? If yes, which one?
3. **First-story slide.** Should there be an optional slide 10 about your earlier business-development role, where you sold more by email than by cold calling? It would be told plainly, with no dollar figure. It's left out until you confirm it's approved.
4. **Voice gate.** Can you run `tools/voice-gate/check.py --surface linkedin` over this copy in the master repo, or give me that repo's owner/repo so I can? I couldn't check against the canon files directly.
