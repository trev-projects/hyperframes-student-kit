      // Digiwell motion bridge — inlined into index.html by build-deck.mjs.
      //
      // `hyperframes present` navigates by SEEKING, so slides would snap between
      // still frames and no transition would ever play. When this composition runs
      // inside the presenter, this script upgrades the slideshow controller so a
      // forward step PLAYS the timeline up to the next stop instead of jumping.
      // Back / jump-to-slide / audience catch-up still snap, as before.
      //
      // Safe everywhere else: during render or Studio preview there is no
      // <hyperframes-slideshow> in the parent, so it gives up after ~5s. If the
      // presenter's internals ever change shape, it leaves them untouched and the
      // deck falls back to native snap navigation.
      (function () {
        var MAX_HOP = 4.0; // only animate forward steps shorter than this (seconds)
        var host;
        try {
          if (window.parent === window) return;
          host = window.parent;
          host.document; // throws if cross-origin
        } catch (e) { return; }

        var polls = 0;
        var iv = setInterval(function () {
          polls++;
          var ss = host.document.querySelector('hyperframes-slideshow');
          if (!ss) { if (polls > 20) clearInterval(iv); return; }
          var ctrl = ss.controller;
          var player = ss.querySelector('hyperframes-player');
          if (!ctrl || ctrl.__dwMotion || typeof ctrl.playTo !== 'function' || !player ||
              typeof player.play !== 'function' || typeof player.seek !== 'function') return;
          ctrl.__dwMotion = true; // controller can be rebound on re-init; keep polling

          var snap = ctrl.playTo.bind(ctrl);
          var target = null;
          var timer = 0;

          // Park exactly on the stop. The timer is a backstop sized to the hop;
          // timeupdate usually fires first once playback crosses the target.
          function settle() {
            host.clearTimeout(timer); timer = 0;
            if (target === null) return;
            var t = target; target = null;
            player.pause();
            player.seek(t);
          }
          player.addEventListener('timeupdate', function () {
            if (target !== null && player.currentTime >= target - 0.01) settle();
          });

          ctrl.playTo = function (t) {
            var hop = t - player.currentTime;
            if (hop > 0.02 && hop <= MAX_HOP) {
              target = t;
              host.clearTimeout(timer);
              timer = host.setTimeout(settle, hop * 1000 / (player.playbackRate || 1));
              if (player.paused) player.play();
              return;
            }
            host.clearTimeout(timer); timer = 0; target = null;
            player.pause();
            snap(t);
          };
        }, 250);
      })();
