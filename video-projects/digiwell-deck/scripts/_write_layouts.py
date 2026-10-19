#!/usr/bin/env python3
"""One-time generator for the nine starter layouts in compositions/.

After generation each file is plain, hand-editable HyperFrames HTML; this
script only exists so the shared shell (scripts, stylesheet, fonts, grain,
vignette, timeline registration) is identical everywhere. Re-running it
OVERWRITES compositions/ — edit the HTML files directly once you've customised them.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "compositions"
FONTS = ('https://fonts.googleapis.com/css2?family=Sora:wght@700;800'
         '&family=Manrope:wght@500;700&family=JetBrains+Mono:wght@500;600;700&display=block')


def chrome(section, n, terra=False):
    return f'''<div class="dw-chrome"><div class="dw-brand">Digiwell<span class="dw-dot">.</span></div><div>{section}</div><div>{n:02d}&nbsp;/&nbsp;09</div></div>
          <div class="dw-rule"></div>'''


# deck.css is loaded once by the root index.html. A <link> inside a sub-composition
# template resolves relative to compositions/ in the live player (404), so don't add one.
def shell(cid, dur, body, css, js, terra=False, edge="dw-edge"):
    panel = "dw-panel dw-terra" if terra else "dw-panel"
    return f'''<template id="{cid}-template">
  <script src="assets/gsap.min.js"></script>
  <script src="assets/deck.js"></script>

  <div data-composition-id="{cid}" data-start="0" data-duration="{dur}" data-width="1920" data-height="1080">
    <div class="dw-slide">
      <div class="{panel}">
        {body}
        <div class="dw-vignette"></div>
        <div class="dw-grain"></div>
      </div>
      <div class="{edge}"></div>
    </div>

    <style>
{css}
    </style>

    <script>
      (function () {{
        var SLOT = {dur};
        var root = document.querySelector('[data-composition-id="{cid}"]');
        var q = function (s) {{ return root.querySelector(s); }};
        var qa = function (s) {{ return root.querySelectorAll(s); }};
        DW.words(root);
        var tl = gsap.timeline({{ paused: true }});
        var t0 = DW.enter(tl, root);
{js}
        DW.hold(tl, SLOT);
        window.__timelines = window.__timelines || {{}};
        window.__timelines["{cid}"] = tl;
      }})();
    </script>
  </div>
</template>
'''


S = '[data-composition-id="{}"]'
files = {}

# 01 — Title -----------------------------------------------------------------
c = "s01-title"
files[c] = shell(c, 2.3, f'''<div class="dw-content t-grid">
          <div class="t-mark"><div class="t-word">Digiwell<span class="dw-dot">.</span></div><div class="t-sub dw-mono">MARKETING</div></div>
          <div class="t-main">
            <div class="dw-eyebrow t-eye">Email strategy and implementation</div>
            <div class="dw-h-xl t-h1" data-words>Give interested people</div>
            <div class="dw-h-xl t-h2"><span class="t-the" data-words>a</span> <span class="dw-hl"><span class="dw-hl-bar"></span><span class="dw-hl-text">clear next step.</span></span></div>
            <div class="dw-lede t-lede">For established, expert-led businesses. We turn the interest you already have into consistent email follow-up.</div>
          </div>
          <div class="t-foot dw-mono"><span>TREVOR DAVIS &middot; TORONTO, ON</span><span class="dw-accent">DIGIWELLMARKETING.COM</span></div>
        </div>''',
f'''      {S.format(c)} .t-grid {{ padding: 90px 120px 90px; justify-content: space-between; }}
      {S.format(c)} .t-word {{ font-weight: 800; font-size: 64px; letter-spacing: -2px; line-height: 1; }}
      {S.format(c)} .t-sub {{ margin-top: 8px; font-size: 18px; letter-spacing: 7px; color: var(--dw-muted); }}
      {S.format(c)} .t-eye {{ margin-bottom: 26px; }}
      {S.format(c)} .t-h1, {S.format(c)} .t-h2 {{ font-size: 116px; letter-spacing: -3.6px; }}
      {S.format(c)} .t-lede {{ margin-top: 34px; max-width: 1180px; }}
      {S.format(c)} .t-foot {{ display: flex; justify-content: space-between; font-size: 22px; color: var(--dw-muted); padding-top: 26px; border-top: 1px solid var(--dw-rule); }}''',
'''        DW.rise(tl, q('.t-mark'), t0, { y: -30 });
        DW.rise(tl, q('.t-eye'), t0 + 0.12, { y: 0, x: -30 });
        DW.rise(tl, qa('.t-h1 .dw-w'), t0 + 0.18, { y: 90, stagger: 0.06 });
        DW.rise(tl, [q('.t-the .dw-w'), q('.t-h2 .dw-hl-text')], t0 + 0.38, { y: 90, stagger: 0.06 });
        DW.swash(tl, q('.dw-hl-bar'), t0 + 0.72);
        DW.rise(tl, q('.t-lede'), t0 + 0.62, { y: 24, ease: 'power2.out' });
        DW.rise(tl, q('.t-foot'), t0 + 0.8, { y: 20, ease: 'power2.out' });''')

# 02 — Agenda ----------------------------------------------------------------
c = "s02-agenda"
items = [("The problem", "What happens after someone raises their hand"),
         ("One journey", "Why we start with one, not three"),
         ("How we work", "Fit, scope, test, handover"),
         ("Where to start", "A conversation about your email")]
rows = "\n".join(
    f'''            <div class="a-row"><div class="a-num dw-mono">0{i + 1}</div><div class="a-title dw-h-s">{t}</div><div class="a-desc dw-body">{d}</div></div>'''
    for i, (t, d) in enumerate(items))
files[c] = shell(c, 2.2, f'''{chrome("AGENDA", 2)}
        <div class="dw-content">
          <div class="dw-eyebrow">Today</div>
          <div class="dw-h-l a-head" data-words>What we&rsquo;ll cover.</div>
          <div class="a-list">
{rows}
          </div>
        </div>''',
f'''      {S.format(c)} .a-head {{ margin-top: 18px; }}
      {S.format(c)} .a-list {{ margin-top: 60px; display: flex; flex-direction: column; }}
      {S.format(c)} .a-row {{ display: grid; grid-template-columns: 110px 640px 1fr; align-items: baseline; padding: 26px 0; border-top: 1px solid var(--dw-rule); }}
      {S.format(c)} .a-num {{ font-size: 28px; color: var(--dw-terra); }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.a-head .dw-w'), t0 + 0.08, { y: 70 });
        DW.rise(tl, qa('.a-row'), t0 + 0.42, { y: 0, x: 80, stagger: 0.09, ease: 'power3.out' });''')

# 03 — Section divider (terracotta) -------------------------------------------
c = "s03-divider"
files[c] = shell(c, 1.9, f'''{chrome("SECTION 01", 3)}
        <div class="dw-content d-grid">
          <div class="d-num">01</div>
          <div class="d-text">
            <div class="dw-h-xl d-title" data-words>The problem.</div>
            <div class="dw-lede d-sub">What happens after people show interest.</div>
          </div>
        </div>''',
f'''      {S.format(c)} .d-grid {{ flex-direction: row; align-items: center; gap: 90px; padding-top: 140px; }}
      {S.format(c)} .d-num {{ font-weight: 800; font-size: 520px; line-height: 0.8; letter-spacing: -30px; color: transparent; -webkit-text-stroke: 4px var(--dw-sand); }}
      {S.format(c)} .d-sub {{ margin-top: 22px; }}''',
'''        DW.rise(tl, q('.d-num'), t0, { y: 0, x: -120, duration: 0.7, ease: 'expo.out' });
        DW.rise(tl, qa('.d-title .dw-w'), t0 + 0.16, { y: 100, stagger: 0.07 });
        DW.rise(tl, q('.d-sub'), t0 + 0.42, { y: 24, ease: 'power2.out' });''',
     terra=True, edge="dw-edge dw-sand")

# 04 — Statement (the thesis) -----------------------------------------------------
c = "s04-statement"
files[c] = shell(c, 2.55, f'''{chrome("THE PROBLEM", 4)}
        <div class="dw-content s-grid">
          <div class="dw-h-l s-l1" data-words>Most businesses don&rsquo;t have a traffic problem.</div>
          <div class="dw-h-l s-l2"><span class="s-pre" data-words>They have a</span> <span class="dw-hl"><span class="dw-hl-bar"></span><span class="dw-hl-text">follow-up</span></span> <span class="s-post">problem.</span></div>
          <div class="dw-lede s-note">People subscribe, enquire, then hear nothing useful.</div>
        </div>''',
f'''      {S.format(c)} .s-grid {{ justify-content: center; padding-top: 150px; }}
      {S.format(c)} .s-l1 {{ max-width: 1560px; }}
      {S.format(c)} .s-l2 {{ margin-top: 30px; color: var(--dw-terra); }}
      {S.format(c)} .s-note {{ margin-top: 56px; }}''',
'''        DW.rise(tl, qa('.s-l1 .dw-w'), t0, { y: 80, stagger: 0.04 });
        DW.rise(tl, [].concat(Array.from(qa('.s-pre .dw-w')), [q('.s-l2 .dw-hl-text'), q('.s-post')]), t0 + 0.5, { y: 80, stagger: 0.06 });
        DW.swash(tl, q('.dw-hl-bar'), t0 + 0.95);
        DW.rise(tl, q('.s-note'), t0 + 1.05, { y: 20, ease: 'power2.out' });''')

# 05 — Three questions (one per click) ---------------------------------------------
c = "s05-questions"
qs = ["What happens after someone subscribes?",
      "What happens after someone enquires?",
      "Who owns the newsletter?"]
qhtml = "\n".join(
    f'''            <div class="qn-row qr{i}"><div class="qn-num dw-mono">0{i}</div><div class="qn-q">{t}</div></div>'''
    for i, t in enumerate(qs, 1))
files[c] = shell(c, 3.3, f'''{chrome("THE PROBLEM", 5)}
        <div class="dw-content">
          <div class="dw-eyebrow">Three questions worth asking</div>
          <div class="dw-h-l qn-head" data-words>Where does follow-up break?</div>
          <div class="qn-list">
{qhtml}
          </div>
        </div>''',
f'''      {S.format(c)} .qn-head {{ margin-top: 18px; }}
      {S.format(c)} .qn-list {{ margin-top: 70px; display: flex; flex-direction: column; }}
      {S.format(c)} .qn-row {{ display: grid; grid-template-columns: 110px 1fr; align-items: baseline; padding: 34px 0; border-top: 1px solid var(--dw-rule); }}
      {S.format(c)} .qn-num {{ font-size: 28px; color: var(--dw-terra); }}
      {S.format(c)} .qn-q {{ font-weight: 800; font-size: 64px; line-height: 1.08; letter-spacing: -1.8px; }}''',
'''        // Fragments (deck.json): rest at 1.5 / 2.1 / 2.7, one question per click.
        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.qn-head .dw-w'), t0 + 0.08, { y: 70 });
        [['.qr1', 0.95], ['.qr2', 1.55], ['.qr3', 2.15]].forEach(function (k) {
          tl.from(q(k[0]), { x: 90, opacity: 0, duration: 0.5, ease: 'expo.out' }, k[1]);
        });''')

# 06 — Start with one journey (one card per click; none highlighted) ---------------
c = "s06-journeys"
cards = [("01", "Welcome and nurture", "What new subscribers get, in order, from day one."),
         ("02", "Enquiry follow&#8209;up", "What happens between &ldquo;thanks for reaching out&rdquo; and a real conversation."),
         ("03", "Newsletter loop", "A newsletter with an owner, a rhythm and a way to learn what&rsquo;s working.")]
cardhtml = "\n".join(
    f'''            <div class="dw-card p-card p{n}"><div class="dw-eyebrow">{n}</div><div class="dw-h-s p-t">{t}</div><div class="dw-body">{d}</div></div>'''
    for n, t, d in cards)
files[c] = shell(c, 3.0, f'''{chrome("ONE JOURNEY", 6)}
        <div class="dw-content">
          <div class="dw-eyebrow">Pick the one that matters most</div>
          <div class="dw-h-l p-head" data-words>Start with one journey.</div>
          <div class="p-row">
{cardhtml}
          </div>
        </div>''',
f'''      {S.format(c)} .p-head {{ margin-top: 18px; }}
      {S.format(c)} .p-row {{ margin-top: 70px; display: flex; gap: 40px; }}
      {S.format(c)} .p-card {{ flex: 1 1 0; height: 440px; padding: 46px 44px; display: flex; flex-direction: column; gap: 22px; }}
      {S.format(c)} .p-t {{ margin-top: 6px; }}''',
'''        // Fragments (deck.json): rest at 1.2 / 1.8 / 2.4, one card lands per click.
        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.p-head .dw-w'), t0 + 0.08, { y: 70 });
        [['.p01', 0.62], ['.p02', 1.25], ['.p03', 1.85]].forEach(function (k) {
          tl.from(q(k[0]), { y: 90, rotation: -2.5, opacity: 0, duration: 0.5, ease: 'back.out(1.5)' }, k[1]);
        });''')

# 07 — How we work ---------------------------------------------------------------
c = "s07-process"
steps = [("Fit conversation", "Where things stand, and whether there&rsquo;s a useful first project."),
         ("Scoped build", "One journey, agreed in writing, built in the tools you already use."),
         ("Test and sign-off", "Tested end to end. Nothing goes live without your sign-off."),
         ("Handover", "Documented and handed over. Ongoing help is scoped separately.")]
stephtml = "\n".join(
    f'''            <div class="pr-step ps{i}"><div class="pr-node"><span>{i}</span></div><div class="dw-h-s pr-t">{t}</div><div class="dw-body pr-d">{d}</div></div>'''
    for i, (t, d) in enumerate(steps, 1))
files[c] = shell(c, 2.9, f'''{chrome("HOW WE WORK", 7)}
        <div class="dw-content">
          <div class="dw-eyebrow">How we work</div>
          <div class="dw-h-l pr-head" data-words>How we work together.</div>
          <div class="pr-track">
            <div class="pr-line"><div class="pr-fill"></div></div>
{stephtml}
          </div>
        </div>''',
f'''      {S.format(c)} .pr-head {{ margin-top: 18px; }}
      {S.format(c)} .pr-track {{ position: relative; margin-top: 90px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; }}
      {S.format(c)} .pr-line {{ position: absolute; top: 44px; left: 46px; right: 344px; height: 4px; background: var(--dw-rule); }}
      {S.format(c)} .pr-fill {{ width: 100%; height: 100%; background: var(--dw-terra); transform: scaleX(0); transform-origin: left center; }}
      {S.format(c)} .pr-step {{ position: relative; }}
      {S.format(c)} .pr-node {{ width: 92px; height: 92px; border-radius: 50%; background: var(--dw-paper); border: 4px solid var(--dw-terra); display: flex; align-items: center; justify-content: center; font-family: "JetBrains Mono", monospace; font-weight: 700; font-size: 32px; color: var(--dw-terra); }}
      {S.format(c)} .pr-t {{ margin-top: 34px; font-size: 46px; }}
      {S.format(c)} .pr-d {{ margin-top: 10px; max-width: 370px; }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.pr-head .dw-w'), t0 + 0.08, { y: 70 });
        tl.to(q('.pr-fill'), { scaleX: 1, duration: 1.1, ease: 'power2.inOut' }, t0 + 0.45);
        [1, 2, 3, 4].forEach(function (i) {
          var at = t0 + 0.45 + (i - 1) * 0.3;
          tl.from(q('.ps' + i + ' .pr-node'), { scale: 0, duration: 0.4, ease: 'back.out(2.2)' }, at);
          tl.from(qa('.ps' + i + ' .pr-t, .ps' + i + ' .pr-d'), { y: 30, opacity: 0, duration: 0.4, ease: 'power3.out', stagger: 0.05 }, at + 0.08);
        });''')

# 08 — What you can count on --------------------------------------------------------
c = "s08-compare"
before = ["People subscribe and hear nothing useful",
          "Enquiries wait on whoever has time",
          "The newsletter goes out when someone remembers"]
after = ["One accountable owner, from strategy to testing",
         "Scope agreed in writing",
         "Built in your existing tools, with your data under your control",
         "Tested before anything goes live",
         "A documented handover"]
li = lambda xs, cls: "\n".join(f'<li class="{cls}">{x}</li>' for x in xs)
files[c] = shell(c, 2.6, f'''{chrome("WHAT YOU CAN COUNT ON", 8)}
        <div class="dw-content">
          <div class="dw-eyebrow">What you can count on</div>
          <div class="dw-h-m cp-head" data-words>One owner. One agreed journey.</div>
          <div class="cp-row">
            <div class="cp-col cp-before"><div class="dw-mono cp-label">WITHOUT A CLEAR OWNER</div><ul class="dw-body">
{li(before, "cp-b")}
            </ul></div>
            <div class="cp-col cp-after dw-card dw-feature"><div class="dw-mono cp-label">WITH DIGIWELL</div><ul class="dw-body">
{li(after, "cp-a")}
            </ul></div>
          </div>
        </div>''',
f'''      {S.format(c)} .cp-head {{ margin-top: 18px; }}
      {S.format(c)} .cp-row {{ margin-top: 60px; display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: start; }}
      {S.format(c)} .cp-col {{ padding: 46px 54px; border-radius: 26px; }}
      {S.format(c)} .cp-before {{ border: 1px dashed var(--dw-card-border); }}
      {S.format(c)} .cp-label {{ font-size: 22px; letter-spacing: 3px; color: var(--dw-muted); margin-bottom: 24px; }}
      {S.format(c)} .cp-after .cp-label {{ color: var(--dw-sand); }}
      {S.format(c)} ul {{ list-style: none; display: flex; flex-direction: column; gap: 18px; }}
      {S.format(c)} li {{ position: relative; padding-left: 50px; }}
      {S.format(c)} .cp-b {{ color: var(--dw-muted); text-decoration: line-through; text-decoration-color: rgba(181,83,46,0.6); text-decoration-thickness: 3px; }}
      {S.format(c)} .cp-b::before {{ content: "\\2715"; position: absolute; left: 0; color: var(--dw-muted); }}
      {S.format(c)} .cp-a::before {{ content: "\\2713"; position: absolute; left: 0; color: var(--dw-sand); font-weight: 700; }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.cp-head .dw-w'), t0 + 0.08, { y: 70 });
        DW.rise(tl, q('.cp-before'), t0 + 0.4, { y: 0, x: -60, ease: 'power3.out' });
        DW.rise(tl, qa('.cp-b'), t0 + 0.5, { y: 0, x: -24, stagger: 0.08, ease: 'power2.out' });
        DW.rise(tl, q('.cp-after'), t0 + 0.62, { y: 60, rotation: 1.5, ease: 'back.out(1.4)' });
        DW.rise(tl, qa('.cp-a'), t0 + 0.8, { y: 0, x: 24, stagger: 0.08, ease: 'power2.out' });''')

# 09 — Where to start (terracotta) -------------------------------------------------
c = "s09-cta"
files[c] = shell(c, 2.45, f'''{chrome("WHERE TO START", 9)}
        <div class="dw-content cta-grid">
          <div class="dw-eyebrow">Where to start</div>
          <div class="dw-h-xl cta-h"><span class="cta-a" data-words>Let&rsquo;s talk about</span> <span class="dw-hl"><span class="dw-hl-bar"></span><span class="dw-hl-text">your email.</span></span></div>
          <div class="dw-lede cta-lede">We&rsquo;ll see where things stand and whether there&rsquo;s a useful first project.</div>
          <div class="cta-actions"><div class="dw-pill">digiwellmarketing.com</div><div class="dw-mono cta-sign">TREVOR DAVIS &middot; TORONTO, ON</div></div>
        </div>''',
f'''      {S.format(c)} .cta-grid {{ justify-content: center; padding-top: 150px; }}
      {S.format(c)} .cta-h {{ margin-top: 24px; max-width: 1500px; }}
      {S.format(c)} .cta-lede {{ margin-top: 36px; max-width: 1200px; }}
      {S.format(c)} .cta-actions {{ margin-top: 60px; display: flex; align-items: center; gap: 44px; }}
      {S.format(c)} .cta-sign {{ font-size: 24px; letter-spacing: 3px; color: var(--dw-on-terra-soft); }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.cta-a .dw-w'), t0 + 0.08, { y: 100, stagger: 0.06 });
        DW.rise(tl, q('.cta-h .dw-hl-text'), t0 + 0.3, { y: 100 });
        DW.swash(tl, q('.dw-hl-bar'), t0 + 0.62);
        DW.rise(tl, q('.cta-lede'), t0 + 0.55, { y: 24, ease: 'power2.out' });
        tl.from(q('.dw-pill'), { scale: 0.6, opacity: 0, duration: 0.45, ease: 'back.out(2.2)' }, t0 + 0.8);
        DW.rise(tl, q('.cta-sign'), t0 + 0.95, { y: 0, x: -20, ease: 'power2.out' });''',
     terra=True, edge="dw-edge dw-sand")

for cid, html in files.items():
    (OUT / f"{cid}.html").write_text(html)
    print("wrote", cid)
