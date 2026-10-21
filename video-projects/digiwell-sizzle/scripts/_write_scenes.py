#!/usr/bin/env python3
"""Generate the seven Cedar Night scenes in compositions/.

One shared shell (self-hosted font faces, cedar ground, corner wordmark,
grain, format detection, timeline registration) so every scene is identical
in structure. After generation the files are plain HyperFrames HTML.
Re-running OVERWRITES compositions/: edit this file, not the output.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "compositions"
OUT.mkdir(exist_ok=True)

FONTFACE = '''      @font-face { font-family: "Newsreader"; src: url("assets/fonts/Newsreader.woff2") format("woff2"); font-weight: 200 800; font-style: normal; font-display: block; }
      @font-face { font-family: "Newsreader"; src: url("assets/fonts/Newsreader-Italic.woff2") format("woff2"); font-weight: 200 800; font-style: italic; font-display: block; }
      @font-face { font-family: "Fraunces"; src: url("assets/fonts/Fraunces.woff2") format("woff2"); font-weight: 100 900; font-display: block; }
      @font-face { font-family: "Inter"; src: url("assets/fonts/Inter.woff2") format("woff2"); font-weight: 100 900; font-display: block; }
      @font-face { font-family: "Manrope"; src: url("assets/fonts/Manrope.woff2") format("woff2"); font-weight: 200 800; font-display: block; }'''


def shell(cid, dur, body, css, js, stage="", corner=True, outside=""):
    S = f'[data-composition-id="{cid}"]'
    corner_html = '<div class="cn-mark cn-corner"></div>' if corner else ''
    return f'''<template id="{cid}-template">
  <script src="assets/gsap.min.js"></script>
  <script src="assets/sz.js"></script>

  <div data-composition-id="{cid}" data-start="0" data-duration="{dur}" data-width="1920" data-height="1080">
    <div class="cn-stage {stage} st">
      {corner_html}
{body}
      <div class="cn-grain"></div>
    </div>
{outside}
    <style>
      /* Self-hosted faces (also in assets/sz.css); declared here so each scene lints standalone. */
{FONTFACE}
      {S} {{ position: absolute; inset: 0; overflow: hidden; }}
      {S}.v .cn-corner {{ top: 120px; left: 80px; }}
{css.replace("$", S)}
    </style>

    <script>
      (function () {{
        var SLOT = {dur};
        var root = document.querySelector('{S}');
        var q = function (s) {{ return root.querySelector(s); }};
        var qa = function (s) {{ return root.querySelectorAll(s); }};
        var V = SZ.fmt(root);
        var W = +root.getAttribute('data-width'), H = +root.getAttribute('data-height');
        SZ.marks(root);
        SZ.words(root);
        var tl = gsap.timeline({{ paused: true }});
{js}
        SZ.hold(tl, SLOT);
        window.__timelines = window.__timelines || {{}};
        window.__timelines["{cid}"] = tl;
      }})();
    </script>
  </div>
</template>
'''


UNDERLINE = '<svg viewBox="0 0 100 20" preserveAspectRatio="none" aria-hidden="true"><path d="M2 12 C 30 3, 60 19, 98 7"/></svg>'
files = {}

# 1 — Hook: the audience is already there; the email around it is idle ----------
files["z1-hook"] = shell("z1-hook", 5.8, '''      <div class="wrap">
        <div class="txt">
          <div class="cn-kick eye">For coaches, consultants, authors and course creators</div>
          <div class="cn-h l1" data-words>You&rsquo;ve already earned <span class="acc">the audience.</span></div>
          <div class="cn-h l2" data-words>Then the list <span class="acc">goes quiet.</span></div>
        </div>
        <div class="ui">
          <div class="cn-card card c1"><div class="ico">&#9993;</div><div class="meta"><div class="t">New subscriber</div><div class="s">Joined your list</div></div><div class="chip">Just now</div></div>
          <div class="cn-card card c2"><div class="ico">&#9636;</div><div class="meta"><div class="t">Newsletter</div><div class="s">Still in drafts</div></div><div class="chip">Draft</div></div>
          <div class="cn-card card c3"><div class="ico">&#8635;</div><div class="meta"><div class="t">Welcome sequence</div><div class="s">Not set up yet</div></div><div class="chip">Off</div></div>
          <div class="days"><span class="d-lab">Day</span><span class="d-num">1</span><span class="d-state">Nothing sent</span></div>
        </div>
      </div>''',
'''      $ .wrap { width: 100%; height: 100%; padding: 60px 110px 0; display: flex; align-items: center; gap: 90px; }
      $ .txt { flex: 1 1 0; }
      $ .eye { margin-bottom: 30px; max-width: 760px; line-height: 1.5; }
      $ .cn-h { font-size: 96px; }
      $ .l2 { margin-top: 44px; }
      $ .ui { flex: 0 0 700px; display: flex; flex-direction: column; gap: 20px; }
      $ .card { display: flex; align-items: center; gap: 24px; padding: 26px 28px; }
      $ .ico { flex: 0 0 64px; height: 64px; border-radius: 50%; background: var(--cn-cedar); color: var(--cn-mint-3); display: flex; align-items: center; justify-content: center; font-size: 30px; font-weight: 800; }
      $ .meta { flex: 1 1 auto; }
      $ .t { font-weight: 700; font-size: 32px; color: var(--cn-text); }
      $ .s { margin-top: 4px; font-weight: 500; font-size: 25px; color: var(--cn-text-3); }
      $ .chip { font-family: "Inter", sans-serif; font-weight: 600; font-size: 15px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cn-mint-2); background: rgba(127,182,158,0.14); border-radius: 999px; padding: 10px 16px; }
      $ .days { align-self: flex-start; display: flex; align-items: baseline; gap: 16px; border: 2px dashed var(--cn-line-2); border-radius: 999px; padding: 16px 28px; font-family: "Inter", sans-serif; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; text-transform: uppercase; }
      $ .d-lab { color: var(--cn-mint-2); }
      $ .d-num { color: var(--cn-mint-3); font-size: 38px; min-width: 2ch; font-variant-numeric: tabular-nums; }
      $ .d-state { color: var(--cn-text-3); }
      $.v .wrap { flex-direction: column; justify-content: center; align-items: stretch; padding: 0 80px; gap: 80px; }
      $.v .txt { flex: 0 0 auto; }
      $.v .ui { flex: 0 0 auto; }''',
'''        tl.from(q('.eye'), { y: 16, opacity: 0, duration: 0.5, ease: 'power3.out' }, 0.15);
        tl.from(qa('.l1 .cn-w'), { y: 50, opacity: 0, duration: 0.6, ease: 'power3.out', stagger: 0.06 }, 0.30);
        // The audience arrives, but nothing around it is running.
        ['.c1', '.c2', '.c3'].forEach(function (c, i) {
          tl.from(q(c), { x: 70, opacity: 0, duration: 0.55, ease: 'power3.out' }, 0.90 + i * 0.30);
        });
        tl.from(q('.days'), { y: 20, opacity: 0, duration: 0.45, ease: 'power3.out' }, 2.05);
        var num = q('.d-num'), d = { v: 1 };
        tl.to(d, { v: 23, duration: 1.3, ease: 'power1.in', onUpdate: function () { num.textContent = Math.round(d.v); } }, 2.15);
        tl.to(qa('.card'), { opacity: 0.45, filter: 'saturate(0)', duration: 0.7, ease: 'power2.out' }, 2.30);
        tl.from(qa('.l2 .cn-w'), { y: 50, opacity: 0, duration: 0.6, ease: 'power3.out', stagger: 0.07 }, 3.20);''')

# 2 — Thesis: not traffic, email -------------------------------------------------
files["z2-thesis"] = shell("z2-thesis", 4.2, f'''      <div class="wrap">
        <div class="cn-h ln ln1"><span class="cn-w">It&rsquo;s</span> <span class="cn-w">not</span> <span class="cn-w">a</span> <span class="cn-w strike">traffic<span class="bar"></span></span> <span class="cn-w">problem.</span></div>
        <div class="cn-h ln ln2"><span class="cn-w">It&rsquo;s</span> <span class="cn-w">an</span> <span class="cn-w acc emw">email{UNDERLINE}</span> <span class="cn-w">problem.</span></div>
      </div>''',
'''      $ .st { clip-path: circle(0px at 50% 50%); }
      $ .wrap { width: 100%; height: 100%; padding: 0 110px; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 36px; text-align: center; }
      $ .ln { font-size: 116px; }
      $ .strike { position: relative; }
      $ .bar { position: absolute; left: -0.04em; right: -0.04em; top: 56%; height: 0.07em; border-radius: 0.04em; background: var(--cn-mint); transform: scaleX(0); transform-origin: left center; }
      $ .emw { position: relative; }
      $ .emw svg { position: absolute; left: 0; width: 100%; bottom: -0.2em; height: 0.3em; overflow: visible; }
      $ .emw svg { clip-path: inset(-50% 100% -50% 0%); }
      $ .emw path { fill: none; stroke: var(--cn-mint); stroke-linecap: round; stroke-width: 0.06em; vector-effect: non-scaling-stroke; }
      $.v .wrap { padding: 0 70px; gap: 70px; }
      $.v .ln { font-size: 104px; line-height: 1.3; }''',
'''        // ENTRY: iris opens from centre in deep cedar.
        tl.fromTo(q('.st'), { clipPath: 'circle(0px at 50% 50%)' }, { clipPath: 'circle(1400px at 50% 50%)', duration: 0.6, ease: 'expo.inOut' }, 0);
        tl.from(qa('.ln1 > .cn-w'), { y: 50, opacity: 0, duration: 0.55, ease: 'power3.out', stagger: 0.06 }, 0.45);
        tl.to(q('.bar'), { scaleX: 1, duration: 0.35, ease: 'power3.out' }, 1.15);
        tl.to(q('.ln1'), { opacity: 0.45, duration: 0.45, ease: 'power2.out' }, 1.45);
        tl.from(qa('.ln2 > .cn-w'), { y: 50, opacity: 0, duration: 0.55, ease: 'power3.out', stagger: 0.07 }, 1.60);
        tl.to(q('.emw svg'), { clipPath: 'inset(-50% 0% -50% 0%)', duration: 0.55, ease: 'power2.inOut' }, 2.15);''',
  stage="cn-deep")

# 3 — Services: strategy, copy, implementation ------------------------------------
cards = [("&#9678;", "Strategy", "What to send, to whom, and when."),
         ("&#9998;", "Copy", "Welcome emails, nurture and newsletters, written for your readers."),
         ("&#10003;", "Implementation", "Built and tested in the tools you already use.")]
cardhtml = "\n".join(f'          <div class="cn-card svc s{i}"><div class="ico">{g}</div><div class="t">{t}</div><div class="d">{d}</div></div>'
                     for i, (g, t, d) in enumerate(cards, 1))
files["z3-services"] = shell("z3-services", 6.4, f'''      <div class="wrap">
        <div class="cn-kick eye">Email strategy, copy and implementation</div>
        <div class="cn-h head" data-words>Turn the audience you&rsquo;ve already earned <span class="acc">into more business.</span></div>
        <div class="cards">
{cardhtml}
        </div>
        <div class="cap">Start with the one that matters most.</div>
      </div>''',
'''      $ .st { clip-path: inset(0% 0% 0% 100%); }
      $ .edge { top: 0; bottom: 0; left: 0; width: 8px; }
      $ .wrap { width: 100%; height: 100%; padding: 80px 110px 0; display: flex; flex-direction: column; justify-content: center; }
      $ .head { margin-top: 20px; font-size: 86px; max-width: 1560px; }
      $ .cards { margin-top: 56px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }
      $ .svc { padding: 34px 36px 38px; display: flex; flex-direction: column; gap: 14px; min-height: 270px; }
      $ .ico { width: 60px; height: 60px; border-radius: 50%; background: var(--cn-cedar); color: var(--cn-mint-3); display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 800; margin-bottom: 6px; }
      $ .t { font-family: "Newsreader", Georgia, serif; font-weight: 600; font-size: 46px; line-height: 1.05; color: var(--cn-text); }
      $ .d { font-weight: 500; font-size: 26px; line-height: 1.45; color: var(--cn-text-2); }
      $ .cap { margin-top: 40px; font-family: "Newsreader", Georgia, serif; font-style: italic; font-weight: 500; font-size: 42px; color: var(--cn-mint-3); }
      $.v .wrap { padding: 0 80px; }
      $.v .head { font-size: 84px; }
      $.v .cards { grid-template-columns: 1fr; gap: 22px; margin-top: 60px; }
      $.v .svc { min-height: 0; padding: 30px 32px; }
      $.v .cap { margin-top: 50px; }''',
'''        // ENTRY: panel wipes in from the right, mint edge on the seam.
        tl.fromTo(q('.st'), { clipPath: 'inset(0% 0% 0% 100%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.fromTo(q('.edge'), { x: W }, { x: -8, duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.from(q('.eye'), { y: 16, opacity: 0, duration: 0.45, ease: 'power3.out' }, 0.40);
        tl.from(qa('.head .cn-w'), { y: 50, opacity: 0, duration: 0.55, ease: 'power3.out', stagger: 0.04 }, 0.50);
        [1, 2, 3].forEach(function (n, i) {
          tl.from(q('.s' + n), { y: 50, opacity: 0, duration: 0.55, ease: 'power3.out' }, 1.00 + i * 0.15);
        });
        // A soft mint focus walks the three services.
        [1, 2, 3].forEach(function (n, i) {
          var at = 1.90 + i * 0.40, el = q('.s' + n);
          tl.to(el, { y: -10, borderColor: '#7FB69E', boxShadow: '0 0 0 2px rgba(127,182,158,0.9), 0 30px 60px -30px rgba(0,0,0,0.6)', duration: 0.2, ease: 'power2.out' }, at);
          tl.to(el, { y: 0, borderColor: 'rgba(214,232,223,0.26)', boxShadow: '0 0 0 0px rgba(127,182,158,0), 0 30px 60px -30px rgba(0,0,0,0.6)', duration: 0.3, ease: 'power2.in' }, at + 0.32);
        });
        tl.from(q('.cap'), { y: 20, opacity: 0, duration: 0.5, ease: 'power3.out' }, 3.20);''',
  outside='    <div class="cn-edge edge"></div>')

# 4 — How we work ----------------------------------------------------------------
files["z4-how"] = shell("z4-how", 10.4, '''      <div class="wrap">
        <div class="top">
          <div class="cn-kick eye">How we work</div>
          <div class="rail">
            <div class="seg"><div class="bar"><div class="fill f1"></div></div><div class="lab">Fit</div></div>
            <div class="seg"><div class="bar"><div class="fill f2"></div></div><div class="lab">Scope</div></div>
            <div class="seg"><div class="bar"><div class="fill f3"></div></div><div class="lab">Test</div></div>
            <div class="seg"><div class="bar"><div class="fill f4"></div></div><div class="lab">Handover</div></div>
          </div>
        </div>
        <div class="area">
          <div class="step st1">
            <div class="tx"><div class="num">Step 01</div><div class="cn-h title" data-words>Fit conversation</div><div class="cn-body desc">Where things stand, and whether there&rsquo;s a useful first project.</div></div>
            <div class="vis cn-card">
              <div class="bb l b1">Where do things stand right now?</div>
              <div class="bb r b2">Here&rsquo;s what we&rsquo;ve got.</div>
              <div class="bb l b3">Is there a useful first project?</div>
            </div>
          </div>
          <div class="step st2">
            <div class="tx"><div class="num">Step 02</div><div class="cn-h title" data-words>Scoped build</div><div class="cn-body desc">One journey, agreed in writing, built in the tools you already use.</div></div>
            <div class="vis cn-card">
              <div class="v-head">Scope &middot; in writing</div>
              <div class="v-title">One journey</div>
              <div class="row"><span class="tick">&#10003;</span>Strategy, copy and build in one place</div>
              <div class="row"><span class="tick">&#10003;</span>One accountable owner</div>
              <div class="row"><span class="tick">&#10003;</span>Agreed before work starts</div>
              <div class="sign"><div class="sig-line"></div><div class="sig-lab">Agreed</div></div>
            </div>
          </div>
          <div class="step st3">
            <div class="tx"><div class="num">Step 03</div><div class="cn-h title" data-words>Test and sign&#8209;off</div><div class="cn-body desc">Tested end to end. Nothing goes live without your sign&#8209;off.</div></div>
            <div class="vis cn-card">
              <div class="v-head">Test run</div>
              <div class="row"><span class="tick">&#10003;</span>Every link</div>
              <div class="row"><span class="tick">&#10003;</span>Every trigger</div>
              <div class="row"><span class="tick">&#10003;</span>Every branch</div>
              <div class="stamp">Signed off</div>
            </div>
          </div>
          <div class="step st4">
            <div class="tx"><div class="num">Step 04</div><div class="cn-h title" data-words>Handover</div><div class="cn-body desc">Documented and handed over. Ongoing help is scoped separately.</div></div>
            <div class="vis cn-card hand">
              <div class="zones"><div class="zone z-a">Digiwell</div><div class="zone z-b">You</div></div>
              <div class="doc"><div class="doc-ico">&#9636;</div><div class="doc-t">Handover doc</div></div>
            </div>
          </div>
        </div>
      </div>''',
'''      $ .st { clip-path: inset(100% 0% 0% 0%); }
      $ .edge { left: 0; right: 0; top: 0; height: 8px; }
      $ .wrap { width: 100%; height: 100%; padding: 150px 110px 90px; display: flex; flex-direction: column; }
      $ .top { display: flex; align-items: center; justify-content: space-between; gap: 60px; }
      $ .rail { display: flex; gap: 16px; }
      $ .seg { width: 170px; }
      $ .bar { height: 6px; border-radius: 3px; background: var(--cn-line); overflow: hidden; }
      $ .fill { width: 100%; height: 100%; background: var(--cn-mint); transform: scaleX(0); transform-origin: left center; }
      $ .lab { margin-top: 12px; font-family: "Inter", sans-serif; font-weight: 600; font-size: 16px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cn-text-3); }
      $ .area { position: relative; flex: 1 1 auto; }
      $ .step { position: absolute; inset: 0; display: grid; grid-template-columns: 1fr 760px; gap: 90px; align-items: center; opacity: 0; }
      $ .num { font-family: "Inter", sans-serif; font-weight: 600; font-size: 22px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cn-mint-2); }
      $ .title { margin-top: 16px; font-size: 96px; }
      $ .desc { margin-top: 26px; max-width: 760px; }
      $ .vis { position: relative; padding: 44px 46px; display: flex; flex-direction: column; gap: 20px; min-height: 440px; justify-content: center; }
      $ .bb { font-weight: 600; font-size: 31px; line-height: 1.35; padding: 22px 30px; border-radius: 28px; max-width: 84%; }
      $ .bb.l { align-self: flex-start; background: var(--cn-surf-2); color: var(--cn-text); border-bottom-left-radius: 8px; }
      $ .bb.r { align-self: flex-end; background: var(--cn-mint); color: var(--cn-bg); border-bottom-right-radius: 8px; }
      $ .v-head { font-family: "Inter", sans-serif; font-weight: 600; font-size: 18px; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cn-text-3); }
      $ .v-title { font-family: "Newsreader", Georgia, serif; font-weight: 600; font-size: 46px; margin-top: -4px; }
      $ .row { display: flex; align-items: center; gap: 20px; font-weight: 600; font-size: 30px; color: var(--cn-text); }
      $ .tick { flex: 0 0 46px; height: 46px; border-radius: 50%; background: var(--cn-mint); color: var(--cn-bg); display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 800; }
      $ .sign { display: flex; align-items: center; gap: 22px; margin-top: 14px; }
      $ .sig-line { flex: 1 1 auto; height: 2px; background: var(--cn-text-2); transform: scaleX(0); transform-origin: left center; }
      $ .sig-lab { font-family: "Inter", sans-serif; font-weight: 600; font-size: 18px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--cn-mint-2); }
      $ .stamp { position: absolute; right: 44px; bottom: 50px; font-family: "Inter", sans-serif; font-weight: 600; font-size: 30px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--cn-mint-3); border: 4px solid var(--cn-mint); border-radius: 12px; padding: 12px 22px; transform: rotate(-8deg); }
      $ .zones { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
      $ .zone { height: 300px; border-radius: 18px; border: 2px dashed var(--cn-line-2); display: flex; align-items: flex-start; justify-content: center; padding-top: 24px; font-family: "Inter", sans-serif; font-weight: 600; font-size: 18px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--cn-text-3); }
      $ .doc { position: absolute; left: 80px; top: 130px; width: 250px; height: 190px; border-radius: 14px; background: var(--cn-mint); color: var(--cn-bg); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; box-shadow: 0 24px 50px -24px rgba(0,0,0,0.7); }
      $ .doc-ico { font-size: 48px; line-height: 1; }
      $ .doc-t { font-weight: 700; font-size: 28px; }
      $.v .wrap { padding: 210px 80px 120px; }
      $.v .top { flex-direction: column; align-items: flex-start; gap: 30px; }
      $.v .seg { width: 215px; }
      $.v .step { grid-template-columns: 1fr; grid-template-rows: auto auto; align-content: center; gap: 70px; }
      $.v .title { font-size: 92px; }
      $.v .doc { left: 120px; }''',
'''        // ENTRY: covers the services scene from the bottom, mint edge on the seam.
        tl.fromTo(q('.st'), { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.fromTo(q('.edge'), { y: H }, { y: -8, duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.from(q('.eye'), { y: 16, opacity: 0, duration: 0.4, ease: 'power3.out' }, 0.30);
        tl.from(qa('.seg'), { y: -12, opacity: 0, duration: 0.35, ease: 'power2.out', stagger: 0.05 }, 0.35);

        var S = [0.45, 2.9, 5.35, 7.8];
        S.forEach(function (s, i) {
          var n = i + 1, st = '.st' + n, next = S[i + 1];
          tl.set(q(st), { opacity: 1 }, s);
          tl.from(q(st + ' .num'), { y: 14, opacity: 0, duration: 0.35, ease: 'power3.out' }, s);
          tl.from(qa(st + ' .title .cn-w'), { y: 50, opacity: 0, duration: 0.5, ease: 'power3.out', stagger: 0.06 }, s + 0.06);
          tl.from(q(st + ' .desc'), { y: 16, opacity: 0, duration: 0.45, ease: 'power2.out' }, s + 0.30);
          tl.from(q(st + ' .vis'), { y: 40, opacity: 0, duration: 0.55, ease: 'power3.out' }, s + 0.18);
          tl.to(q('.f' + n), { scaleX: 1, duration: (next || SLOT - 0.2) - s, ease: 'none' }, s);
          if (next) tl.to(q(st), { y: -40, opacity: 0, duration: 0.28, ease: 'power2.in' }, next - 0.28);
        });

        tl.from(q('.b1'), { x: -30, opacity: 0, duration: 0.4, ease: 'power3.out' }, S[0] + 0.55);
        tl.from(q('.b2'), { x: 30, opacity: 0, duration: 0.4, ease: 'power3.out' }, S[0] + 0.95);
        tl.from(q('.b3'), { x: -30, opacity: 0, duration: 0.4, ease: 'power3.out' }, S[0] + 1.35);
        tl.from(qa('.st2 .row'), { x: 24, opacity: 0, duration: 0.35, ease: 'power3.out', stagger: 0.25 }, S[1] + 0.55);
        tl.from(qa('.st2 .tick'), { scale: 0, duration: 0.3, ease: 'back.out(2)', stagger: 0.25 }, S[1] + 0.62);
        tl.to(q('.sig-line'), { scaleX: 1, duration: 0.5, ease: 'power2.inOut' }, S[1] + 1.35);
        tl.from(q('.sig-lab'), { opacity: 0, x: 16, duration: 0.35, ease: 'power2.out' }, S[1] + 1.65);
        tl.from(qa('.st3 .row'), { x: 24, opacity: 0, duration: 0.35, ease: 'power3.out', stagger: 0.25 }, S[2] + 0.55);
        tl.from(qa('.st3 .tick'), { scale: 0, duration: 0.3, ease: 'back.out(2)', stagger: 0.25 }, S[2] + 0.62);
        tl.from(q('.stamp'), { scale: 1.7, opacity: 0, rotation: -22, duration: 0.32, ease: 'power4.in' }, S[2] + 1.20);
        tl.from(q('.doc'), { scale: 0.7, opacity: 0, duration: 0.4, ease: 'power3.out' }, S[3] + 0.55);
        // Shift = one zone + the 30px gap (vis is 760px wide in 16:9, 920px in 9:16, less 2x46px padding).
        tl.to(q('.doc'), { x: ((V ? 920 : 760) - 92 - 30) / 2 + 30, duration: 0.75, ease: 'power3.inOut' }, S[3] + 1.0);
        tl.to(q('.z-b'), { borderColor: '#7FB69E', color: '#C3E2D3', borderStyle: 'solid', duration: 0.3, ease: 'none' }, S[3] + 1.6);''',
  outside='    <div class="cn-edge edge"></div>')

# 5 — Proof ------------------------------------------------------------------------
files["z5-proof"] = shell("z5-proof", 4.2, '''      <div class="wrap">
        <div class="qm">&ldquo;</div>
        <div class="cn-h quote" data-words>Trevor completely gets our <span class="acc">space and messaging.</span></div>
        <div class="by">Dave, Breakthrough Academy</div>
      </div>''',
'''      $ .wrap { width: 100%; height: 100%; padding: 0 110px; display: flex; flex-direction: column; justify-content: center; }
      $ .qm { font-family: "Fraunces", Georgia, serif; font-weight: 600; font-size: 230px; line-height: 0.75; height: 120px; color: var(--cn-mint); }
      $ .quote { margin-top: 30px; font-size: 104px; max-width: 1500px; }
      $ .by { margin-top: 44px; font-weight: 600; font-size: 32px; color: var(--cn-text-2); }
      $.v .wrap { padding: 0 80px; }
      $.v .quote { font-size: 96px; }''',
'''        // ENTRY: a slow dissolve over the process scene. Calm, the proof should breathe.
        tl.fromTo(q('.st'), { opacity: 0 }, { opacity: 1, duration: 0.6, ease: 'power2.out' }, 0);
        tl.from(q('.qm'), { y: 30, opacity: 0, duration: 0.55, ease: 'power3.out' }, 0.35);
        tl.from(qa('.quote .cn-w'), { y: 40, opacity: 0, duration: 0.55, ease: 'power3.out', stagger: 0.05 }, 0.55);
        tl.from(q('.by'), { y: 14, opacity: 0, duration: 0.5, ease: 'power3.out' }, 1.55);''')

# 6 — Commitments -------------------------------------------------------------------
files["z6-commit"] = shell("z6-commit", 3.6, '''      <div class="wrap">
        <div class="cn-kick eye">What you can count on</div>
        <div class="cn-h ln a">One owner.</div>
        <div class="cn-h ln b">Your tools.</div>
        <div class="cn-h ln c">Your data.</div>
        <div class="cn-h ln d">Tested before it <span class="acc cn-grp">goes live.</span></div>
      </div>''',
'''      $ .st { clip-path: polygon(0% 0%, 0% 0%, -30% 100%, -30% 100%); }
      $ .slab { position: absolute; top: -20%; left: 0; width: 60px; height: 140%; background: var(--cn-mint); transform: translateX(-300px) skewX(-16deg); z-index: 50; }
      $ .wrap { width: 100%; height: 100%; padding: 60px 110px 0; display: flex; flex-direction: column; justify-content: center; gap: 4px; }
      $ .eye { margin-bottom: 26px; }
      $ .ln { font-size: 108px; }
      $.v .wrap { padding: 0 80px; gap: 12px; }
      $.v .ln { font-size: 100px; }''',
'''        tl.fromTo(q('.st'), { clipPath: 'polygon(0% 0%, 0% 0%, -30% 100%, -30% 100%)' },
          { clipPath: 'polygon(0% 0%, 130% 0%, 100% 100%, -30% 100%)', duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.fromTo(q('.slab'), { x: -300 }, { x: W + 700, duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.from(q('.eye'), { y: 16, opacity: 0, duration: 0.4, ease: 'power3.out' }, 0.30);
        [['.a', 0.45], ['.b', 0.95], ['.c', 1.45], ['.d', 1.95]].forEach(function (k) {
          tl.from(q(k[0]), { y: 40, opacity: 0, filter: 'blur(8px)', duration: 0.45, ease: 'power3.out' }, k[1]);
        });''',
  stage="cn-surf", outside='    <div class="slab"></div>')

# 7 — CTA (the studio's end card) -------------------------------------------------
files["z7-cta"] = shell("z7-cta", 5.8, '''      <div class="wrap">
        <div class="cn-mark big"></div>
        <div class="cn-h head" data-words>Let&rsquo;s talk about <span class="acc">your email.</span></div>
        <div class="cn-body lede">We&rsquo;ll see where things stand and whether there&rsquo;s a useful first project.</div>
        <div class="cn-pill pill">digiwellmarketing.com/contact</div>
      </div>''',
'''      $ .st { clip-path: inset(0% 0% 0% 100%); }
      $ .edge { top: 0; bottom: 0; left: 0; width: 8px; }
      $ .wrap { width: 100%; height: 100%; padding: 0 110px; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; }
      $ .big { font-size: 84px; }
      $ .big svg { clip-path: inset(-50% 100% -50% 0%); }
      $ .head { margin-top: 100px; font-size: 128px; max-width: 1500px; }
      $ .lede { margin-top: 34px; max-width: 1100px; }
      $ .pill { margin-top: 54px; padding: 26px 50px; font-size: 36px; }
      $.v .wrap { padding: 0 80px; }
      $.v .head { font-size: 116px; }''',
'''        tl.fromTo(q('.st'), { clipPath: 'inset(0% 0% 0% 100%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.fromTo(q('.edge'), { x: W }, { x: -8, duration: 0.55, ease: 'power3.inOut' }, 0);
        tl.from(q('.big'), { y: 20, opacity: 0, duration: 0.5, ease: 'power3.out' }, 0.45);
        SZ.drawMark(tl, q('.big'), 0.70, 0.7);
        tl.from(qa('.head .cn-w'), { y: 50, opacity: 0, duration: 0.6, ease: 'power3.out', stagger: 0.06 }, 0.80);
        tl.from(q('.lede'), { y: 20, opacity: 0, duration: 0.5, ease: 'power3.out' }, 1.40);
        tl.from(q('.pill'), { y: 20, opacity: 0, duration: 0.5, ease: 'power3.out' }, 1.70);
        tl.to(q('.pill'), { scale: 1.03, duration: 0.7, ease: 'sine.inOut', yoyo: true, repeat: 3 }, 2.70);''',
  corner=False, outside='    <div class="cn-edge edge"></div>')

for old in OUT.glob("z*.html"):
    old.unlink()
for cid, html in files.items():
    (OUT / f"{cid}.html").write_text(html)
    print("wrote", cid)
