/* Digiwell sizzle — shared helpers. Each scene works in both formats: SZ.fmt()
   reads the ROOT composition (#root) and tags the scene with .v when it's
   portrait, so scene CSS can re-lay itself out under `.v` selectors. */
(function () {
  if (window.SZ) return;
  var SZ = {};

  SZ.isV = function () {
    var r = document.getElementById('root');
    return !!r && (+r.getAttribute('data-height') > +r.getAttribute('data-width'));
  };
  SZ.fmt = function (scene) { if (SZ.isV()) scene.classList.add('v'); return SZ.isV(); };

  SZ.words = function (scene) {
    Array.prototype.forEach.call(scene.querySelectorAll('[data-words]'), function (el) {
      el.innerHTML = el.textContent.trim().split(/\s+/)
        .map(function (w) { return '<span class="sz-w">' + w + '</span>'; }).join(' ');
    });
  };

  SZ.hold = function (tl, slot) { return tl.to({}, { duration: slot }, 0); };

  window.SZ = SZ;
})();
