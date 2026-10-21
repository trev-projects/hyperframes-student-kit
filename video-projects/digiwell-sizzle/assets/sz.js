/* Digiwell sizzle — shared helpers for both formats.
   SZ.fmt():   tags a scene with .v when the ROOT composition is portrait.
   SZ.words(): splits [data-words] into word spans for staggered rises,
               preserving accent spans (<span class="acc">) so italic mint
               accent words keep their style per word.
   SZ.MARK:    the wordmark markup (Fraunces + hand-drawn underline path). */
(function () {
  if (window.SZ) return;
  var SZ = {};

  SZ.isV = function () {
    var r = document.getElementById('root');
    return !!r && (+r.getAttribute('data-height') > +r.getAttribute('data-width'));
  };
  SZ.fmt = function (scene) { if (SZ.isV()) scene.classList.add('v'); return SZ.isV(); };

  function wrap(text, extra) {
    return text.split(/(\s+)/).map(function (tok) {
      if (!tok) return '';
      if (/^\s+$/.test(tok)) return ' ';
      return '<span class="cn-w' + (extra ? ' ' + extra : '') + '">' + tok + '</span>';
    }).join('');
  }
  SZ.words = function (scene) {
    Array.prototype.forEach.call(scene.querySelectorAll('[data-words]'), function (el) {
      var html = '';
      Array.prototype.forEach.call(el.childNodes, function (n) {
        if (n.nodeType === 3) html += wrap(n.textContent);
        // Accent phrases stay together as one unit so they wrap as a whole.
        else if (n.classList && n.classList.contains('acc')) html += '<span class="cn-grp">' + wrap(n.textContent, 'acc') + '</span>';
        else html += n.outerHTML;
      });
      el.innerHTML = html.trim();
    });
  };

  SZ.MARK = 'Digiwell<svg viewBox="0 0 100 20" preserveAspectRatio="none" aria-hidden="true">' +
    '<path d="M2 12 C 30 3, 60 19, 98 7"/></svg>';
  SZ.marks = function (scene) {
    Array.prototype.forEach.call(scene.querySelectorAll('.cn-mark'), function (el) { el.innerHTML = SZ.MARK; });
  };
  // Draw the underline on, left to right. A clip wipe rather than a dash
  // animation: Chromium mis-renders dashes on non-scaling strokes.
  SZ.drawMark = function (tl, el, at, dur) {
    var svg = el.querySelector('svg');
    tl.fromTo(svg, { clipPath: 'inset(-50% 100% -50% 0%)' }, { clipPath: 'inset(-50% 0% -50% 0%)', duration: dur || 0.6, ease: 'power2.inOut' }, at);
  };

  SZ.hold = function (tl, slot) { return tl.to({}, { duration: slot }, 0); };

  window.SZ = SZ;
})();
