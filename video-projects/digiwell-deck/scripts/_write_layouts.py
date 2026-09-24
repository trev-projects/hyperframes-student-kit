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
            <div class="dw-eyebrow t-eye">Growth partner for the AI era</div>
            <div class="dw-h-xl t-h1" data-words>Growth systems for</div>
            <div class="dw-h-xl t-h2"><span class="t-the" data-words>the</span> <span class="dw-hl"><span class="dw-hl-bar"></span><span class="dw-hl-text">AI era.</span></span></div>
            <div class="dw-lede t-lede">Newsletters, CRM automation and nurture flows that turn cold leads into loyal buyers.</div>
          </div>
          <div class="t-foot dw-mono"><span>TREVOR DAVIS &middot; TORONTO, ON</span><span class="dw-accent">DIGIWELLMARKETING.COM</span></div>
        </div>''',
f'''      {S.format(c)} .t-grid {{ padding: 90px 120px 90px; justify-content: space-between; }}
      {S.format(c)} .t-word {{ font-weight: 800; font-size: 64px; letter-spacing: -2px; line-height: 1; }}
      {S.format(c)} .t-sub {{ margin-top: 8px; font-size: 18px; letter-spacing: 7px; color: var(--dw-muted); }}
      {S.format(c)} .t-eye {{ margin-bottom: 26px; }}
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
items = [("The problem", "Why good businesses leak growth"),
         ("What we build", "Newsletters, CRM, nurture"),
         ("How it works", "Four steps, done for you"),
         ("Next step", "Your free AI Growth Scorecard")]
rows = "\n".join(
    f'''            <div class="a-row"><div class="a-num dw-mono">0{i + 1}</div><div class="a-title dw-h-s">{t}</div><div class="a-desc dw-body">{d}</div></div>'''
    for i, (t, d) in enumerate(items))
files[c] = shell(c, 2.2, f'''{chrome("AGENDA", 2)}
        <div class="dw-content">
          <div class="dw-eyebrow">Today</div>
          <div class="dw-h-l a-head" data-words>Four things in twenty minutes.</div>
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
            <div class="dw-lede d-sub">Why good businesses leak growth.</div>
          </div>
        </div>''',
f'''      {S.format(c)} .d-grid {{ flex-direction: row; align-items: center; gap: 90px; padding-top: 140px; }}
      {S.format(c)} .d-num {{ font-weight: 800; font-size: 520px; line-height: 0.8; letter-spacing: -30px; color: transparent; -webkit-text-stroke: 4px var(--dw-sand); }}
      {S.format(c)} .d-sub {{ margin-top: 22px; }}''',
'''        DW.rise(tl, q('.d-num'), t0, { y: 0, x: -120, duration: 0.7, ease: 'expo.out' });
        DW.rise(tl, qa('.d-title .dw-w'), t0 + 0.16, { y: 100, stagger: 0.07 });
        DW.rise(tl, q('.d-sub'), t0 + 0.42, { y: 24, ease: 'power2.out' });''',
     terra=True, edge="dw-edge dw-sand")

# 04 — Statement ---------------------------------------------------------------
c = "s04-statement"
files[c] = shell(c, 2.55, f'''{chrome("THE PROBLEM", 4)}
        <div class="dw-content s-grid">
          <div class="dw-h-l s-l1" data-words>Most businesses don&rsquo;t have a traffic problem.</div>
          <div class="dw-h-l s-l2"><span class="s-pre" data-words>They have a</span> <span class="dw-hl"><span class="dw-hl-bar"></span><span class="dw-hl-text">follow-up</span></span> <span class="s-post">problem.</span></div>
          <div class="dw-lede s-note">The leads are already there. Nobody is talking to them.</div>
        </div>''',
f'''      {S.format(c)} .s-grid {{ justify-content: center; padding-top: 150px; }}
      {S.format(c)} .s-l1 {{ max-width: 1560px; }}
      {S.format(c)} .s-l2 {{ margin-top: 30px; color: var(--dw-terra); }}
      {S.format(c)} .s-note {{ margin-top: 56px; }}''',
'''        DW.rise(tl, qa('.s-l1 .dw-w'), t0, { y: 80, stagger: 0.04 });
        DW.rise(tl, [].concat(Array.from(qa('.s-pre .dw-w')), [q('.s-l2 .dw-hl-text'), q('.s-post')]), t0 + 0.5, { y: 80, stagger: 0.06 });
        DW.swash(tl, q('.dw-hl-bar'), t0 + 0.95);
        DW.rise(tl, q('.s-note'), t0 + 1.05, { y: 20, ease: 'power2.out' });''')

# 05 — Big stat ---------------------------------------------------------------
c = "s05-stat"
files[c] = shell(c, 2.1, f'''{chrome("THE PROBLEM", 5)}
        <div class="dw-content st-grid">
          <div class="st-num"><span class="st-val">0</span><span class="st-unit">min</span></div>
          <div class="st-side">
            <div class="dw-eyebrow">Sample stat &middot; swap in a client result</div>
            <div class="dw-h-m st-label" data-words>to see exactly where your growth is leaking.</div>
            <div class="dw-body st-src">The free AI Growth Scorecard returns your score and the three fixes worth doing first.</div>
          </div>
        </div>''',
f'''      {S.format(c)} .st-grid {{ flex-direction: row; align-items: center; gap: 80px; padding-top: 150px; }}
      {S.format(c)} .st-num {{ font-weight: 800; font-size: 420px; line-height: 0.8; letter-spacing: -20px; color: var(--dw-terra); white-space: nowrap; font-variant-numeric: tabular-nums; }}
      {S.format(c)} .st-unit {{ font-size: 110px; letter-spacing: -3px; margin-left: 18px; color: var(--dw-ink); }}
      {S.format(c)} .st-label {{ margin-top: 20px; }}
      {S.format(c)} .st-src {{ margin-top: 30px; max-width: 820px; }}''',
'''        DW.rise(tl, q('.st-num'), t0, { y: 120, duration: 0.6 });
        var v = q('.st-val'), n = { v: 0 };
        tl.to(n, { v: 2, duration: 0.7, ease: 'power3.out', onUpdate: function () { v.textContent = Math.round(n.v); } }, t0 + 0.05);
        DW.rise(tl, q('.dw-eyebrow'), t0 + 0.2, { y: 0, x: -30 });
        DW.rise(tl, qa('.st-label .dw-w'), t0 + 0.26, { y: 60, stagger: 0.035 });
        DW.rise(tl, q('.st-src'), t0 + 0.62, { y: 20, ease: 'power2.out' });''')

# 06 — Three-up (builds one card per click via fragments) --------------------------
c = "s06-pillars"
cards = [("01", "Newsletters", "A weekly letter your list actually opens, written and sent for you."),
         ("02", "CRM automation", "Every lead tagged, scored, routed and followed up. Nothing slips."),
         ("03", "Nurture flows", "Segmented sequences that move cold leads to buyers on their own.")]
cardhtml = "\n".join(
    f'''            <div class="dw-card p-card p{n}{' dw-feature' if n == '02' else ''}"><div class="dw-eyebrow">{n}</div><div class="dw-h-s p-t">{t}</div><div class="dw-body">{d}</div></div>'''
    for n, t, d in cards)
files[c] = shell(c, 3.0, f'''{chrome("WHAT WE BUILD", 6)}
        <div class="dw-content">
          <div class="dw-eyebrow">What we build</div>
          <div class="dw-h-l p-head" data-words>Three systems. One growth engine.</div>
          <div class="p-row">
{cardhtml}
          </div>
        </div>''',
f'''      {S.format(c)} .p-head {{ margin-top: 18px; }}
      {S.format(c)} .p-row {{ margin-top: 70px; display: flex; gap: 40px; }}
      {S.format(c)} .p-card {{ flex: 1 1 0; height: 360px; padding: 46px 44px; display: flex; flex-direction: column; gap: 22px; }}
      {S.format(c)} .p-t {{ margin-top: 6px; }}''',
'''        // Fragments (deck.json): rest at 1.2 / 1.8 / 2.4 — one card lands per click.
        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.p-head .dw-w'), t0 + 0.08, { y: 70 });
        [['.p01', 0.62], ['.p02', 1.25], ['.p03', 1.85]].forEach(function (k) {
          tl.from(q(k[0]), { y: 90, rotation: -2.5, opacity: 0, duration: 0.5, ease: 'back.out(1.5)' }, k[1]);
        });''')

# 07 — Process -----------------------------------------------------------------
c = "s07-process"
steps = [("Audit", "Find the leaks with the Growth Scorecard."),
         ("Build", "We design and wire the systems for you."),
         ("Launch", "Newsletter, CRM and flows go live together."),
         ("Optimise", "Test, measure, and compound what works.")]
stephtml = "\n".join(
    f'''            <div class="pr-step ps{i}"><div class="pr-node"><span>{i}</span></div><div class="dw-h-s pr-t">{t}</div><div class="dw-body pr-d">{d}</div></div>'''
    for i, (t, d) in enumerate(steps, 1))
files[c] = shell(c, 2.9, f'''{chrome("HOW IT WORKS", 7)}
        <div class="dw-content">
          <div class="dw-eyebrow">How it works</div>
          <div class="dw-h-l pr-head" data-words>Four steps. Done for you.</div>
          <div class="pr-track">
            <div class="pr-line"><div class="pr-fill"></div></div>
{stephtml}
          </div>
        </div>''',
f'''      {S.format(c)} .pr-head {{ margin-top: 18px; }}
      {S.format(c)} .pr-track {{ position: relative; margin-top: 100px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px; }}
      {S.format(c)} .pr-line {{ position: absolute; top: 44px; left: 46px; right: 344px; height: 4px; background: var(--dw-rule); }}
      {S.format(c)} .pr-fill {{ width: 100%; height: 100%; background: var(--dw-terra); transform: scaleX(0); transform-origin: left center; }}
      {S.format(c)} .pr-step {{ position: relative; }}
      {S.format(c)} .pr-node {{ width: 92px; height: 92px; border-radius: 50%; background: var(--dw-paper); border: 4px solid var(--dw-terra); display: flex; align-items: center; justify-content: center; font-family: "JetBrains Mono", monospace; font-weight: 700; font-size: 32px; color: var(--dw-terra); }}
      {S.format(c)} .pr-t {{ margin-top: 34px; }}
      {S.format(c)} .pr-d {{ margin-top: 14px; max-width: 360px; }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.pr-head .dw-w'), t0 + 0.08, { y: 70 });
        tl.to(q('.pr-fill'), { scaleX: 1, duration: 1.1, ease: 'power2.inOut' }, t0 + 0.45);
        [1, 2, 3, 4].forEach(function (i) {
          var at = t0 + 0.45 + (i - 1) * 0.3;
          tl.from(q('.ps' + i + ' .pr-node'), { scale: 0, duration: 0.4, ease: 'back.out(2.2)' }, at);
          tl.from(qa('.ps' + i + ' .pr-t, .ps' + i + ' .pr-d'), { y: 30, opacity: 0, duration: 0.4, ease: 'power3.out', stagger: 0.05 }, at + 0.08);
        });''')

# 08 — Before / after ---------------------------------------------------------
c = "s08-compare"
before = ["Leads go cold after one email", "The newsletter goes out when there&rsquo;s time", "Nobody knows what&rsquo;s working"]
after = ["Every lead enters a nurture flow", "A consistent weekly letter, every week", "Dashboards that show what converts"]
li = lambda xs, cls: "\n".join(f'<li class="{cls}">{x}</li>' for x in xs)
files[c] = shell(c, 2.45, f'''{chrome("THE DIFFERENCE", 8)}
        <div class="dw-content">
          <div class="dw-eyebrow">The difference</div>
          <div class="dw-h-l cp-head" data-words>From guesswork to a system.</div>
          <div class="cp-row">
            <div class="cp-col cp-before"><div class="dw-mono cp-label">WITHOUT A SYSTEM</div><ul class="dw-body">
{li(before, "cp-b")}
            </ul></div>
            <div class="cp-col cp-after dw-card dw-feature"><div class="dw-mono cp-label">WITH DIGIWELL</div><ul class="dw-body">
{li(after, "cp-a")}
            </ul></div>
          </div>
        </div>''',
f'''      {S.format(c)} .cp-head {{ margin-top: 18px; }}
      {S.format(c)} .cp-row {{ margin-top: 70px; display: grid; grid-template-columns: 1fr 1fr; gap: 50px; }}
      {S.format(c)} .cp-col {{ padding: 50px 54px; border-radius: 26px; }}
      {S.format(c)} .cp-before {{ border: 1px dashed var(--dw-card-border); }}
      {S.format(c)} .cp-label {{ font-size: 22px; letter-spacing: 3px; color: var(--dw-muted); margin-bottom: 26px; }}
      {S.format(c)} .cp-after .cp-label {{ color: var(--dw-sand); }}
      {S.format(c)} ul {{ list-style: none; display: flex; flex-direction: column; gap: 22px; }}
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

# 09 — CTA (terracotta) ---------------------------------------------------------
c = "s09-cta"
files[c] = shell(c, 2.45, f'''{chrome("NEXT STEP", 9)}
        <div class="dw-content cta-grid">
          <div class="dw-eyebrow">Next step</div>
          <div class="dw-h-xl cta-h" data-words>Find where growth is leaking.</div>
          <div class="dw-lede cta-lede">Take the free 2-minute AI Growth Scorecard. You get your score and the three fixes worth doing first.</div>
          <div class="cta-actions"><div class="dw-pill">Get your free scorecard &rarr;</div><div class="dw-mono cta-url">digiwellmarketing.com/scorecard</div></div>
        </div>''',
f'''      {S.format(c)} .cta-grid {{ justify-content: center; padding-top: 150px; }}
      {S.format(c)} .cta-h {{ margin-top: 24px; max-width: 1500px; }}
      {S.format(c)} .cta-lede {{ margin-top: 36px; max-width: 1200px; }}
      {S.format(c)} .cta-actions {{ margin-top: 60px; display: flex; align-items: center; gap: 44px; }}
      {S.format(c)} .cta-url {{ font-size: 28px; color: var(--dw-sand); }}''',
'''        DW.rise(tl, q('.dw-eyebrow'), t0, { y: 0, x: -30 });
        DW.rise(tl, qa('.cta-h .dw-w'), t0 + 0.08, { y: 100, stagger: 0.06 });
        DW.rise(tl, q('.cta-lede'), t0 + 0.55, { y: 24, ease: 'power2.out' });
        tl.from(q('.dw-pill'), { scale: 0.6, opacity: 0, duration: 0.45, ease: 'back.out(2.2)' }, t0 + 0.8);
        DW.rise(tl, q('.cta-url'), t0 + 0.95, { y: 0, x: -20, ease: 'power2.out' });''',
     terra=True, edge="dw-edge dw-sand")

for cid, html in files.items():
    (OUT / f"{cid}.html").write_text(html)
    print("wrote", cid)
