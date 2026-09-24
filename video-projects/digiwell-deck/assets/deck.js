/* Digiwell deck — shared motion helpers.
   Every slide composition calls DW.enter() first, so all slides share one
   transition (a right-to-left panel wipe with a leading edge) and one chrome
   entrance. Change the house motion here, not in 9 files. */
(function () {
  if (window.DW) return;
  var DW = {};

  DW.q = function (root, s) { return root.querySelector(s); };
  DW.qa = function (root, s) { return Array.prototype.slice.call(root.querySelectorAll(s)); };

  // Split [data-words] elements into word spans so lines only break at spaces.
  DW.words = function (root) {
    DW.qa(root, '[data-words]').forEach(function (el) {
      el.innerHTML = el.textContent.trim().split(/\s+/)
        .map(function (w) { return '<span class="dw-w">' + w + '</span>'; }).join(' ');
    });
  };

  // House transition + chrome. Returns the time content may start entering.
  DW.enter = function (tl, root) {
    var panel = DW.q(root, '.dw-panel');
    var edge = DW.q(root, '.dw-edge');
    tl.fromTo(panel, { clipPath: 'inset(0% 0% 0% 100%)' },
      { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.55, ease: 'power3.inOut' }, 0);
    if (edge) tl.fromTo(edge, { x: 1920 }, { x: -16, duration: 0.55, ease: 'power3.inOut' }, 0);

    var rule = DW.q(root, '.dw-rule');
    if (rule) tl.from(rule, { scaleX: 0, transformOrigin: 'left center', duration: 0.6, ease: 'power3.out' }, 0.30);
    var chrome = DW.qa(root, '.dw-chrome > *');
    if (chrome.length) tl.from(chrome, { y: -14, opacity: 0, duration: 0.34, ease: 'power2.out', stagger: 0.05 }, 0.32);
    return 0.36;
  };

  // Standard content rise.
  DW.rise = function (tl, targets, at, opts) {
    var v = { y: 56, opacity: 0, duration: 0.5, ease: 'expo.out', stagger: 0.045 };
    if (opts) for (var k in opts) v[k] = opts[k];
    return tl.from(targets, v, at);
  };

  // Sand highlighter wipe.
  DW.swash = function (tl, bar, at) {
    return tl.fromTo(bar, { scaleX: 0 }, { scaleX: 1, duration: 0.42, ease: 'power3.out' }, at);
  };

  // Law #11: the timeline must fill the whole clip slot.
  DW.hold = function (tl, slot) { return tl.to({}, { duration: slot }, 0); };

  window.DW = DW;
})();
