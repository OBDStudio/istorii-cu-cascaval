/*
 * Istorii cu Cașcaval — motion layer.
 *
 * Implements the behaviours annotated in the Figma comments. Deliberately
 * dependency-free: sticky positioning, IntersectionObserver and rAF cover
 * everything here, so the WordPress theme needs no third-party animation CDN.
 *
 * Every timing worth arguing about lives in ICC_MOTION below, so values can be
 * tuned without touching the logic.
 */
var ICC_MOTION_DEFAULTS = {
  // 1 — franchise modal, triggered on leaving the hero
  modal: {
    enabled: true,
    // Fraction of the hero that must have scrolled past before it triggers.
    // 0.2 ≈ "the visitor has started leaving the hero" — the glide below is
    // what makes the arrival feel considered, so the trigger itself no longer
    // has to wait to avoid seeming abrupt.
    afterHero: 0.2,
    // 'session' shows it once per browser session, 'always' every page load.
    frequency: 'session',
    // Rather than cutting in mid-scroll, the page glides to a resting point
    // first and the form opens once it settles. Where it rests: the top of the
    // section after the hero.
    settleTo: '.pillars',
    // How long that glide takes, whatever the distance. Driven here rather
    // than by `behavior: 'smooth'` so the pacing is ours and identical in
    // every browser — see initScrollModal for why the native one was dropped.
    glideMs: 760,
    // Quiet time after the visitor stops scrolling before the glide may start.
    // Nothing moves while a gesture is live, so the page never fights the hand.
    settleMs: 180,
  },

  // 2 — pinned "why" section with three stages
  why: {
    enabled: true,
    // Scroll distance per stage, in viewport heights. Above 1 so each stage
    // has time to be read before the next one takes over.
    stepScroll: 1.75,
    // Desktop always pins.
    minWidth: 1024,
    // Narrower than that it pins only when a stage genuinely fits, measured
    // rather than assumed — see fitsPinned(). Anything that does not fit gets
    // the stacked layout instead, which is the graceful outcome, not a bug.
    // Headroom left below the stage for the counter that runs along the bottom.
    fitMargin: 44,
  },

  // 4 — the gold word cycles on its own
  words: {
    enabled: true,
    // 'timer' cycles on an interval, 'scroll' advances with scroll position.
    mode: 'timer',
    intervalMs: 3600,
  },

  // 5, 6, 7 — reveal on enter
  reveal: {
    enabled: true,
    // Delay between siblings that come into view together.
    stagger: 150,
    // Fires once this much of the item is showing.
    threshold: 0.1,
    // Reveals now run nearly a second, so they have to *start* earlier or the
    // item is still fading while it sits in the middle of the screen — which
    // is the "rushed" feeling from the other direction. Firing close to the
    // viewport edge gives the animation room to finish on arrival.
    rootMargin: '0px 0px -2% 0px',
  },

  // 9 — locations ticker (mobile) and the benefits conveyor (all sizes)
  ticker: {
    enabled: true,
    speed: 26,        // locations, px per second
    maxWidth: 1023,   // locations ticker only runs below this
  },
  conveyor: {
    enabled: true,
    speed: 14,        // benefits belt, px per second — deliberately slow
  },
};

/*
 * Anything already on window.ICC_MOTION wins, group by group, so a page (or
 * the WordPress theme) can override just one value without having to restate
 * the whole config.
 */
window.ICC_MOTION = (function (defaults, overrides) {
  var merged = {};
  Object.keys(defaults).forEach(function (group) {
    merged[group] = {};
    Object.keys(defaults[group]).forEach(function (key) {
      merged[group][key] = defaults[group][key];
    });
    var over = overrides && overrides[group];
    if (over) {
      Object.keys(over).forEach(function (key) {
        merged[group][key] = over[key];
      });
    }
  });
  return merged;
})(ICC_MOTION_DEFAULTS, window.ICC_MOTION);

(function () {
  'use strict';

  var CFG = window.ICC_MOTION;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function onReady(fn) {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  }

  function clamp(v, min, max) {
    return v < min ? min : v > max ? max : v;
  }

  function all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  /* ============================================================ 1. MODAL */

  function initScrollModal() {
    var cfg = CFG.modal;
    var api = window.ICC && window.ICC.modal;
    var hero = document.querySelector('.hero');
    if (!cfg.enabled || !api) return;

    var KEY = 'icc-franchise-modal-seen';
    try {
      if (cfg.frequency === 'session' && sessionStorage.getItem(KEY) === '1') return;
    } catch (e) {
      /* private mode — just show it */
    }

    var fired = false;

    /*
     * Opening the overlay the instant the trigger passes means clamping
     * `overflow: hidden` onto the page while the browser's own scroll momentum
     * is still running — the scroll stops dead under the visitor's finger and
     * reads as a glitch. So: take over, glide to a resting point, and only
     * open once the page has actually stopped.
     */
    function fire() {
      if (fired) return;
      fired = true;
      window.removeEventListener('scroll', check);
      try {
        sessionStorage.setItem(KEY, '1');
      } catch (e) {
        /* ignore */
      }

      var target = document.querySelector(cfg.settleTo);
      if (reduced || !target || typeof window.scrollTo !== 'function') {
        api.open();
        return;
      }

      /*
       * Wait for the visitor to stop scrolling before touching the page.
       *
       * The glide used to start the instant the trigger passed, easing from the
       * scroll position captured at that moment. The visitor's wheel kept
       * adding to the scroll underneath it, and every frame the glide wrote its
       * own curve back over the top — so the page lurched forward with the
       * gesture and was then hauled back against it, measured at six separate
       * jumps of about 110px. That is the "magnet" feeling: the page arguing
       * with the hand moving it.
       *
       * Now nothing moves while a gesture is live. The glide only begins once
       * the scrolling has gone quiet, starts from wherever the visitor actually
       * ended up, and gets out of the way the moment they touch the page again.
       */
      var idle = null;

      function onScroll() {
        window.clearTimeout(idle);
        idle = window.setTimeout(begin, cfg.settleMs);
      }

      window.addEventListener('scroll', onScroll, { passive: true });
      idle = window.setTimeout(begin, cfg.settleMs);

      function begin() {
        window.clearTimeout(idle);
        window.removeEventListener('scroll', onScroll);

        var startY = window.scrollY;
        var destination = Math.round(target.getBoundingClientRect().top + startY);

        // Already there, or scrolled past it while we waited. Never haul the
        // page backwards to make a point — just open where they are.
        if (destination - startY < 4) {
          api.open();
          return;
        }

        var root = document.documentElement;
        // CSS sets `scroll-behavior: smooth` globally, which would make every
        // frame of this loop its own animation. Suspend it for the duration.
        var prevBehavior = root.style.scrollBehavior;
        root.style.scrollBehavior = 'auto';

        var handedBack = false;

        function handBack() {
          handedBack = true;
        }

        // Any fresh input and the glide stops dead: the visitor is steering.
        window.addEventListener('wheel', handBack, { passive: true });
        window.addEventListener('touchstart', handBack, { passive: true });
        window.addEventListener('keydown', handBack);

        function done() {
          window.removeEventListener('wheel', handBack);
          window.removeEventListener('touchstart', handBack);
          window.removeEventListener('keydown', handBack);
          root.style.scrollBehavior = prevBehavior;
          api.open();
        }

        var delta = destination - startY;
        var t0 = null;

        function frame(now) {
          if (handedBack) {
            done();
            return;
          }
          if (t0 === null) t0 = now;
          var p = clamp((now - t0) / cfg.glideMs, 0, 1);
          // easeInOutCubic: leaves and arrives at rest, so the page never
          // appears to be tugged.
          var e = p < 0.5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2;
          window.scrollTo(0, startY + delta * e);
          if (p < 1) {
            window.requestAnimationFrame(frame);
          } else {
            done();
          }
        }

        window.requestAnimationFrame(frame);
      }
    }

    // Tied to the hero rather than a share of total page height, so it lands
    // as the visitor reaches the next section no matter how long the page is.
    function check() {
      if (fired) return;
      if (!hero) return;
      var rect = hero.getBoundingClientRect();
      if (rect.bottom <= rect.height * (1 - cfg.afterHero)) fire();
    }

    window.addEventListener('scroll', check, { passive: true });
    check();
  }

  /* ======================================================== 2. WHY PIN */

  function initWhyPin() {
    var cfg = CFG.why;
    var pin = document.querySelector('[data-why-pin]');
    if (!pin) return;

    var steps = all('[data-why-step]', pin);
    var images = all('[data-why-image]', pin);
    var nums = all('[data-why-nums] span', pin);
    var thumb = pin.querySelector('[data-why-thumb]');
    var section = pin.querySelector('.why');
    if (!steps.length || !section) return;

    var active = -1;
    var pinned = false;
    var unitPx = 0;

    function show(i) {
      if (i === active) return;
      active = i;

      // Toggled with an attribute rather than `hidden` so every step keeps
      // contributing height — the pinned box is then as tall as the tallest
      // stage and nothing below it gets overlapped.
      steps.forEach(function (s, n) {
        var on = n === i;
        s.setAttribute('data-active', String(on));
        s.setAttribute('aria-hidden', String(!on));
        // Where this stage sits relative to the one on screen. The CSS parks
        // passed stages above and unreached ones below, so the movement reads
        // the same way round whichever way the visitor is scrolling.
        s.setAttribute('data-state', on ? 'active' : (n < i ? 'prev' : 'next'));
      });
      nums.forEach(function (s, n) {
        s.setAttribute('data-active', String(n === i));
      });
      // Stage 1 has its own photo; stages 2 and 3 share the second one.
      images.forEach(function (img) {
        var wants = i === 0 ? '1' : '2';
        img.setAttribute('data-active', String(img.getAttribute('data-why-image') === wants));
      });
      if (thumb) {
        thumb.style.transform = 'translateY(' + i * 48 + 'px)';
      }
    }

    function stack() {
      // Fallback layout: every stage visible in sequence, no pinning.
      pinned = false;
      pin.classList.remove('is-pinned');
      pin.style.height = '';
      steps.forEach(function (s) {
        s.setAttribute('data-active', 'true');
        s.removeAttribute('aria-hidden');
        s.removeAttribute('data-state');
      });
      nums.forEach(function (s, n) {
        s.setAttribute('data-active', String(n === 0));
      });
      images.forEach(function (img) {
        img.setAttribute('data-active', String(img.getAttribute('data-why-image') === '1'));
      });
      active = -1;
    }

    function enablePin() {
      pinned = true;
      pin.classList.add('is-pinned');
      // Measure the pinned section rather than trusting innerHeight: on phones
      // the address bar changes innerHeight mid-scroll, but the section is
      // sized in svh and stays put.
      unitPx = section.offsetHeight || window.innerHeight;
      pin.style.height = (unitPx * (1 + cfg.stepScroll * (steps.length - 1))) + 'px';
      // Only claim the first stage on a cold start. Re-running this mid-scroll
      // used to snap the visitor back to stage one for a frame before `update`
      // put it right again.
      if (active < 0) show(0);
    }

    /*
     * Does a pinned stage actually fit this screen?
     *
     * This used to be a guess: pin below 1024px wide only if innerHeight was at
     * least 760. Nearly every phone showing its browser chrome falls under that
     * — an iPhone 14 gives the page 664px — so the section silently stopped
     * animating on real devices while still pinning in a chrome-less emulator.
     * The constant was also wrong in the other direction, refusing phones like
     * the Pixel 7 whose content fits fine at 727px.
     *
     * So measure instead of guessing. The pinned layout is what has to fit, so
     * the class goes on for the measurement and comes straight back off if it
     * is not wanted — same frame, nothing paints in between.
     *
     * Both numbers come from the pinned box: `.why` is sized in svh, the
     * viewport height *with* the toolbar showing, so this is the worst case and
     * the answer cannot change when the bar slides away mid-scroll.
     */
    function fitsPinned() {
      var inner = pin.querySelector('.why__inner');
      if (!inner) return false;

      var had = pin.classList.contains('is-pinned');
      if (!had) pin.classList.add('is-pinned');
      var box = section.offsetHeight;
      var need = inner.scrollHeight;
      if (!had) pin.classList.remove('is-pinned');

      // Room left for the stage counter sitting along the bottom edge.
      return box > 0 && need > 0 && need + cfg.fitMargin <= box;
    }

    function canPin() {
      if (!cfg.enabled || reduced) return false;
      if (window.innerWidth >= cfg.minWidth) return true;
      return fitsPinned();
    }

    function layout() {
      if (!canPin()) {
        if (pinned || active === -1) stack();
        return;
      }
      enablePin();
      update();
    }

    function update() {
      if (!pinned) return;
      var rect = pin.getBoundingClientRect();
      // Against the pinned box's own height, which is sized in svh. Using
      // window.innerHeight here meant a phone's toolbar sliding in or out
      // changed the denominator mid-scroll, so the stage boundaries moved
      // under the visitor and stages could flip back and forth on their own.
      var travel = pin.offsetHeight - unitPx;
      if (travel <= 0) return;
      var progress = clamp(-rect.top / travel, 0, 1);
      // Split the travel evenly across the stages.
      var index = clamp(Math.floor(progress * steps.length), 0, steps.length - 1);
      show(index);
    }

    /*
     * A phone's address bar sliding away fires `resize` with a height change of
     * roughly 10-15% and no width change. Re-laying out on that recomputed the
     * pin's height mid-scroll — measured at a 414px jump on a 393x852 viewport —
     * which yanked everything below it and made the section stutter, most
     * visibly on the way back up, because scrolling up is what brings the bar
     * back. Only a width change, or a height change too large to be chrome, is
     * a real layout change worth re-measuring for.
     */
    var lastW = window.innerWidth;
    var lastH = window.innerHeight;

    function onResize() {
      var w = window.innerWidth;
      var h = window.innerHeight;
      var chromeOnly = w === lastW && Math.abs(h - lastH) / Math.max(lastH, 1) < 0.25;
      lastW = w;
      lastH = h;
      if (chromeOnly) return;
      layout();
    }

    layout();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', onResize);
  }

  /* ====================================================== 4. WORD REEL */

  function initWordReel() {
    var cfg = CFG.words;
    var slot = document.querySelector('[data-word-slot]');
    if (!cfg.enabled || !slot) return;

    var words = all('span', slot);
    if (words.length < 2) return;

    var current = 0;

    /*
     * No width bookkeeping here: the words share one grid cell, so the slot
     * already sizes itself to the longest of them and stays that width as they
     * swap — including after a font swap or a resize, with no JS involved.
     */
    function show(i) {
      if (i === current) return;
      words[current].removeAttribute('data-active');
      words[i].setAttribute('data-active', 'true');
      current = i;
    }

    if (reduced) return;

    if (cfg.mode === 'timer') {
      // Cycles on its own, but only while on screen — an off-screen loop is
      // wasted work and keeps the tab busy for no one.
      var timer = null;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting && !timer) {
            timer = window.setInterval(function () {
              show((current + 1) % words.length);
            }, cfg.intervalMs);
          } else if (!e.isIntersecting && timer) {
            window.clearInterval(timer);
            timer = null;
          }
        });
      }, { threshold: 0.4 });
      io.observe(slot);
      return;
    }

    // Scroll-driven alternative: holds on the first word until the line is on
    // screen, then steps through the rest as it travels up the viewport.
    function onScroll() {
      var rect = slot.getBoundingClientRect();
      var vh = window.innerHeight;
      var progress = clamp((vh * 0.72 - rect.top) / (vh * 0.85), 0, 0.999);
      show(Math.floor(progress * words.length));
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ================================================== PAGE TITLE */

  /*
   * The page's own title comes in a word at a time on load. The words are
   * already split in the markup and the per-word delay is a CSS custom
   * property, so all this does is flip the switch on the next frame — late
   * enough that the transition actually runs rather than being skipped as an
   * initial style.
   *
   * Section titles use the same word-span markup but carry
   * `data-stagger="scroll"` instead, so they're excluded here and handled by
   * initSectionTitleStagger below — the visitor hasn't scrolled to them yet
   * at load time, so firing them immediately would waste the effect.
   */
  function initTitleStagger() {
    var titles = all('[data-stagger]').filter(function (t) {
      return t.getAttribute('data-stagger') !== 'scroll';
    });
    if (!titles.length) return;

    function go() {
      titles.forEach(function (t) {
        t.setAttribute('data-stagger', 'ready');
      });
    }

    if (reduced) {
      go();
      return;
    }

    // Wait for the webfont so words don't reflow mid-animation.
    var start = function () {
      window.requestAnimationFrame(function () {
        window.requestAnimationFrame(go);
      });
    };

    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(start);
      // Never let a stalled font load leave the title invisible.
      window.setTimeout(go, 1200);
    } else {
      start();
    }
  }

  /*
   * Each section's own heading — "Cifrele care contează" and the like —
   * staggers in the first time the visitor scrolls to it. Same markup and
   * CSS as the page title; only the trigger differs.
   */
  function initSectionTitleStagger() {
    var titles = all('[data-stagger="scroll"]');
    if (!titles.length) return;

    if (reduced || !('IntersectionObserver' in window)) {
      titles.forEach(function (t) {
        t.setAttribute('data-stagger', 'ready');
      });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.setAttribute('data-stagger', 'ready');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.4 });

    titles.forEach(function (t) {
      io.observe(t);
    });
  }

  /* ================================================ 5/6/7. REVEALS */

  function initReveals() {
    var cfg = CFG.reveal;
    var items = all('[data-reveal-item]');
    if (!items.length) return;

    function revealAll() {
      items.forEach(function (i) {
        i.setAttribute('data-revealed', 'true');
      });
    }

    if (!cfg.enabled || reduced || !('IntersectionObserver' in window)) {
      revealAll();
      return;
    }

    /*
     * Each item is observed on its own. Observing the container instead — as
     * this used to — means a tall grid needs a large share of its own height
     * on screen before anything moves, so the first cards sit invisible and
     * the rest pop in together. Per item, each one animates as it arrives.
     *
     * Items that arrive in the same frame (a grid row, a pair of cards) are
     * staggered against each other by document order.
     */
    var io = new IntersectionObserver(function (entries) {
      var arriving = entries
        .filter(function (e) {
          return e.isIntersecting;
        })
        .sort(function (a, b) {
          return a.boundingClientRect.top - b.boundingClientRect.top;
        });

      arriving.forEach(function (entry, i) {
        var el = entry.target;
        // The comparison cards were annotated "simultan ... din stânga și
        // dreapta", so that group arrives together rather than staggered.
        var group = el.closest ? el.closest('[data-reveal]') : null;
        var together = group && group.getAttribute('data-reveal') === 'sides';
        el.style.transitionDelay = together ? '0ms' : (i * cfg.stagger) + 'ms';
        el.setAttribute('data-revealed', 'true');
        io.unobserve(el);
      });
    }, { threshold: cfg.threshold, rootMargin: cfg.rootMargin });

    items.forEach(function (item) {
      io.observe(item);
    });
  }

  /* ============================================ 9. TICKER / CONVEYOR */

  /*
   * One continuous-scroll implementation, used by the locations strip and the
   * benefits belt. The track is duplicated so the loop has no visible seam,
   * and the offset wraps at half the track width.
   */
  function createTicker(opts) {
    var wrap = opts.wrap;
    var track = opts.track;
    if (!wrap || !track) return null;

    var originals = all(opts.itemSelector, track);
    if (!originals.length && opts.source) {
      // Locations: the belt is built from the desktop columns' markup.
      originals = opts.source();
      if (!originals.length) return null;
      while (track.firstChild) track.removeChild(track.firstChild);
      originals.forEach(function (node) {
        track.appendChild(node.cloneNode(true));
      });
      originals = all(opts.itemSelector, track);
    }
    if (!originals.length) return null;

    // Clone the run once so scrolling past the end lands back at the start.
    originals.forEach(function (node) {
      var clone = node.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      clone.setAttribute('data-clone', 'true');
      // Clones must never be reachable by keyboard — they are the same links.
      all('a, button', clone).forEach(function (f) {
        f.setAttribute('tabindex', '-1');
      });
      // Reveal observers were bound before this ran, so a clone carrying the
      // attribute would sit at opacity 0 forever with nothing to un-hide it.
      if (clone.hasAttribute('data-reveal-item')) clone.removeAttribute('data-reveal-item');
      all('[data-reveal-item]', clone).forEach(function (n) {
        n.removeAttribute('data-reveal-item');
      });
      track.appendChild(clone);
    });

    var offset = 0;
    var half = 0;
    var running = false;
    var last = 0;
    var raf = null;
    var paused = 0;         // pause requests outstanding (hover, focus, drag)
    var dragging = false;
    var dragStartX = 0;
    var dragStartOffset = 0;
    var moved = 0;

    function measure() {
      half = track.scrollWidth / 2;
    }

    function apply() {
      if (half > 0) offset = ((offset % half) + half) % half;
      track.style.transform = 'translateX(' + -offset + 'px)';
    }

    function tick(now) {
      if (!running) return;
      var dt = last ? Math.min((now - last) / 1000, 0.05) : 0;
      last = now;
      if (!paused && !dragging) {
        offset += opts.speed * dt;
        apply();
      }
      raf = window.requestAnimationFrame(tick);
    }

    function start() {
      if (running || reduced) return;
      running = true;
      last = 0;
      measure();
      raf = window.requestAnimationFrame(tick);
    }

    function stop() {
      running = false;
      if (raf) window.cancelAnimationFrame(raf);
      raf = null;
    }

    function pause() {
      paused++;
    }

    function resume() {
      paused = Math.max(0, paused - 1);
    }

    // Drag to scrub. A drag that barely moves is treated as a click, so the
    // card still opens its link.
    wrap.addEventListener('pointerdown', function (e) {
      dragging = true;
      moved = 0;
      dragStartX = e.clientX;
      dragStartOffset = offset;
      wrap.classList.add('is-dragging');
      try {
        wrap.setPointerCapture(e.pointerId);
      } catch (err) {
        /* capture unavailable — dragging still works */
      }
    });

    wrap.addEventListener('pointermove', function (e) {
      if (!dragging) return;
      var dx = e.clientX - dragStartX;
      moved = Math.max(moved, Math.abs(dx));
      offset = dragStartOffset - dx;
      apply();
    });

    function endDrag(e) {
      if (!dragging) return;
      dragging = false;
      wrap.classList.remove('is-dragging');
      try {
        wrap.releasePointerCapture(e.pointerId);
      } catch (err) {
        /* already released */
      }
    }

    wrap.addEventListener('pointerup', endDrag);
    wrap.addEventListener('pointercancel', endDrag);

    // Swallow the click that follows a real drag.
    track.addEventListener('click', function (e) {
      if (moved > 8) {
        e.preventDefault();
        e.stopPropagation();
      }
    }, true);

    // Hold still while someone is reading or tabbing through it.
    wrap.addEventListener('pointerenter', pause);
    wrap.addEventListener('pointerleave', resume);
    wrap.addEventListener('focusin', pause);
    wrap.addEventListener('focusout', resume);

    // And while the section is off screen, so it isn't burning frames.
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            start();
          } else {
            stop();
          }
        });
      }, { threshold: 0 }).observe(wrap);
    } else {
      start();
    }

    window.addEventListener('resize', measure);

    return {
      start: start,
      stop: stop,
      measure: measure,
      /* Nudge by one item; used by the arrow buttons. */
      nudge: function (dir) {
        var first = track.querySelector(opts.itemSelector);
        if (!first) return;
        var step = first.getBoundingClientRect().width + (opts.gap || 0);
        offset += dir * step;
        apply();
      },
    };
  }

  /* Locations: a ticker only below the layout's column breakpoint. */
  function initLocationsTicker() {
    var cfg = CFG.ticker;
    var wrap = document.querySelector('[data-ticker]');
    var track = document.querySelector('[data-ticker-track]');
    if (!cfg.enabled || !wrap || !track) return;

    var api = createTicker({
      wrap: wrap,
      track: track,
      itemSelector: '.location',
      gap: 12,
      speed: cfg.speed,
      source: function () {
        return all('.locations__col .location');
      },
    });
    if (!api) return;

    function sync() {
      if (window.innerWidth <= cfg.maxWidth) {
        api.measure();
      } else {
        api.stop();
      }
    }
    window.addEventListener('resize', sync);
    sync();
  }

  /*
   * Benefits: a slow conveyor belt. Before this the arrows were never wired to
   * anything, so cards past the fourth could not be reached at all.
   */
  function initBenefitsConveyor() {
    var cfg = CFG.conveyor;
    var wrap = document.querySelector('[data-carousel]');
    var track = document.querySelector('[data-carousel-track]');
    if (!cfg.enabled || !wrap || !track) return;

    var api = createTicker({
      wrap: wrap,
      track: track,
      itemSelector: '.benefit',
      gap: 24,
      speed: cfg.speed,
    });
    if (!api) return;

    var prev = document.querySelector('[data-carousel-prev]');
    var next = document.querySelector('[data-carousel-next]');
    if (prev) {
      prev.addEventListener('click', function () {
        api.nudge(-1);
      });
    }
    if (next) {
      next.addEventListener('click', function () {
        api.nudge(1);
      });
    }
  }

  /* ================================================== HERO VIDEO */

  /*
   * The hero background is a looping video. Two things the `autoplay`
   * attribute cannot express on its own:
   *
   * `autoplay` is declarative and fires regardless of the visitor's motion
   * preference, so reduced-motion has to be honoured here — the poster frame
   * stays up instead, which is a still of the video's own first frame.
   *
   * And once the visitor has scrolled past the hero there is nothing to see,
   * so it pauses off screen rather than decoding frames for no one. Same
   * IntersectionObserver treatment the tickers already get.
   */
  function initHeroVideo() {
    var video = document.querySelector('[data-hero-video]');
    if (!video) return;

    if (reduced) {
      video.removeAttribute('autoplay');
      video.pause();
      return;
    }

    if (!('IntersectionObserver' in window)) return;

    new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          // play() rejects if the browser blocked autoplay; the poster is
          // already showing, so there is nothing to recover from.
          var p = video.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          video.pause();
        }
      });
    }, { threshold: 0 }).observe(video);
  }

  /* ==================================================== Bootstrap */

  onReady(function () {
    initTitleStagger();
    initSectionTitleStagger();
    initScrollModal();
    initWhyPin();
    initWordReel();
    initReveals();
    initLocationsTicker();
    initBenefitsConveyor();
    initHeroVideo();
  });
})();
