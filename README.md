# Istorii cu Cașcaval — franchise site

Static build of the Figma design for the *Devină francizor* franchise site,
ahead of integration into the WordPress site at cheesefranchise.com.

**Live preview:** https://obdstudio.github.io/istorii-cu-cascaval/

## Pages

| File | Page |
|---|---|
| `index.html` | Landing page |
| `termeni-si-conditii.html` | Terms & conditions |
| `success.html` | Post-submission confirmation |
| `404.html` | Not found |

## Running it locally

No build step, no dependencies — but it does need to be served over HTTP
rather than opened as a file, or the browser will block the webfonts.

```bash
python -m http.server 8000
# then open http://localhost:8000
```

## Structure

```
assets/
  css/    tokens → base → components → sections → motion  (load in that order)
  js/     main.js      language switcher, modal, form validation
          animations.js motion layer; all timings live in ICC_MOTION at the top
  fonts/  self-hosted woff2, latin + latin-ext (Romanian diacritics)
  img/    photography and exported artwork
  svg/    logo, map, ornaments, cheese-wedge pattern
```

Type is Kurale (display), Onest (body) and Berkshire Swash (the pillar
titles). Fonts are self-hosted rather than pulled from Google, which keeps the
site off a third-party CDN for GDPR purposes.

## Motion

Dependency-free — sticky positioning, `IntersectionObserver` and
`requestAnimationFrame`, no animation library. Behaviours come from the
comments left on the Figma file:

- franchise form opens once per session, after the page glides to rest below the hero
- "De ce investitorii aleg" pins and advances through three stages
- the gold word in "Ce face acest concept diferit?" cycles on a timer
- "Ce primești ca partener" runs as a slow conveyor belt
- location cards and map pins link out to Google Maps
- photography fades and racks into focus as it enters the viewport

Everything degrades: with JavaScript off the page renders complete and static,
and `prefers-reduced-motion` is respected throughout.

## Still to come

- Real photography for the eight "Ce primești ca partener" cards (the Figma
  file uses one placeholder for all of them)
- Company details in `termeni-si-conditii.html` — `[DENUMIREA COMPANIEI]`,
  `[IDNO]`, `[ADRESA]`, `[E-MAIL]`, `[TELEFON]`
- Real social profile URLs (currently platform home pages)
- Privacy and cookie policy pages (linked in the footer, not yet designed)
- Form submission wiring — currently redirects to `success.html`; on WordPress
  this hands off to the existing WPForms setup
