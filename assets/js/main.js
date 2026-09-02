/*
 * Istorii cu Cașcaval — site behaviour.
 * Plain ES2019, no build step, so the same file drops straight into the
 * WordPress theme and gets enqueued as-is.
 */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ------------------------------------------------ Language switcher */

  function initLangSwitcher() {
    var toggle = document.querySelector('[data-lang-toggle]');
    var menu = document.querySelector('[data-lang-menu]');
    if (!toggle || !menu) return;

    function close() {
      menu.setAttribute('data-open', 'false');
      toggle.setAttribute('aria-expanded', 'false');
    }

    toggle.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = toggle.getAttribute('aria-expanded') === 'true';
      menu.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
    });

    document.addEventListener('click', function (e) {
      if (!menu.contains(e.target) && e.target !== toggle) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  }

  /* -------------------------------------------------------- Modal */

  var modalApi = (function () {
    var modal = document.querySelector('[data-modal]');
    if (!modal) return { open: function () {}, close: function () {}, isOpen: function () { return false; } };

    var dialog = modal.querySelector('[data-modal-dialog]');
    var lastFocused = null;

    function focusables() {
      return Array.prototype.slice.call(
        dialog.querySelectorAll('a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])')
      );
    }

    function open() {
      if (isOpen()) return;
      lastFocused = document.activeElement;
      modal.setAttribute('data-open', 'true');
      modal.setAttribute('aria-hidden', 'false');
      document.body.classList.add('is-locked');
      var first = focusables()[0];
      if (first) first.focus();
      document.dispatchEvent(new CustomEvent('modal:open'));
    }

    function close() {
      if (!isOpen()) return;
      modal.setAttribute('data-open', 'false');
      modal.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('is-locked');
      if (lastFocused && lastFocused.focus) lastFocused.focus();
      document.dispatchEvent(new CustomEvent('modal:close'));
    }

    function isOpen() {
      return modal.getAttribute('data-open') === 'true';
    }

    // Trap focus and support Escape / backdrop dismissal.
    modal.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        close();
        return;
      }
      if (e.key !== 'Tab') return;

      var items = focusables();
      if (!items.length) return;
      var first = items[0];
      var last = items[items.length - 1];

      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    });

    modal.addEventListener('mousedown', function (e) {
      if (e.target === modal) close();
    });

    Array.prototype.forEach.call(document.querySelectorAll('[data-close-modal]'), function (btn) {
      btn.addEventListener('click', close);
    });

    Array.prototype.forEach.call(document.querySelectorAll('[data-open-modal]'), function (btn) {
      btn.addEventListener('click', open);
    });

    return { open: open, close: close, isOpen: isOpen };
  })();

  /* ------------------------------------------------- Form validation */

  function initForm() {
    var form = document.querySelector('[data-franchise-form]');
    if (!form) return;

    function showError(field, show) {
      var msg = form.querySelector('[data-error-for="' + field.name + '"]');
      field.setAttribute('aria-invalid', show ? 'true' : 'false');
      if (msg) msg.setAttribute('data-visible', show ? 'true' : 'false');
    }

    function validate(field) {
      var value = field.value.trim();
      var ok = value !== '';
      if (ok && field.type === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
      if (ok && field.type === 'tel') ok = value.replace(/[^\d]/g, '').length >= 8;
      showError(field, !ok);
      return ok;
    }

    Array.prototype.forEach.call(form.querySelectorAll('.field'), function (field) {
      field.addEventListener('blur', function () {
        if (field.value.trim() !== '') validate(field);
      });
      field.addEventListener('input', function () {
        if (field.getAttribute('aria-invalid') === 'true') validate(field);
      });
    });

    form.addEventListener('submit', function (e) {
      var fields = Array.prototype.slice.call(form.querySelectorAll('.field'));
      var valid = fields.map(validate).every(Boolean);

      if (!valid) {
        e.preventDefault();
        var firstBad = fields.filter(function (f) {
          return f.getAttribute('aria-invalid') === 'true';
        })[0];
        if (firstBad) firstBad.focus();
        return;
      }

      // Static build: no endpoint yet, so go straight to the confirmation
      // page. In WordPress this submit is handled by the WPForms entry.
      if (!form.getAttribute('action')) {
        e.preventDefault();
        window.location.href = 'success.html';
      }
    });
  }

  /* ------------------------------------------------------ Bootstrap */

  function init() {
    initLangSwitcher();
    initForm();

    // Expose for the animation layer.
    window.ICC = { modal: modalApi, reduceMotion: reduceMotion };
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
