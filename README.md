# Istorii cu Cașcaval — franchise site

Static build of the Figma design for the *Devină francizor* franchise site,
ahead of integration into the WordPress site at cheesefranchise.com.

**Live preview:** https://obdstudio.github.io/istorii-cu-cascaval/

## Pages

Three languages. Romanian sits at the root; Russian and English are generated
into their own directories (see *Translations* below).

| Romanian (root) | Russian | English | Page |
|---|---|---|---|
| `index.html` | `ru/index.html` | `en/index.html` | Landing page |
| `termeni-si-conditii.html` | `ru/terms.html` | `en/terms.html` | Terms & conditions |
| `success.html` | `ru/success.html` | `en/success.html` | Post-submission confirmation |
| `404.html` | `ru/404.html` | `en/404.html` | Not found |

Every page carries `hreflang` alternates for all three locales plus
`x-default`, and the header switcher links to the matching page rather than
dumping the visitor back on the home page.

## Translations

**The Romanian pages are the only ones you edit.** Russian and English are
generated from them, so a layout change reaches all three languages by editing
`index.html` and re-running:

```bash
python tools/build_i18n.py
```

Copy lives in `tools/i18n_strings.py`, keyed by the Romanian original. The
build refuses to finish quietly if anything is missing: every translatable
string it could not place is listed and the exit code is non-zero, so a patch
of untranslated Romanian cannot reach a live Russian page unnoticed.

Conventions, agreed with the client:

- the brand name stays in Latin — *Istorii cu Cașcaval* — in all three
  languages, matching the logo and the social handles
- Russian uses formal «вы»
- Moldovan and Romanian place names take their Russian exonyms (Кишинёв,
  Унгень, Яссы) and street names are transliterated; English keeps the local
  spellings
- personal names, social networks, "ROI" and "break-even" pass through

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
  fonts/  self-hosted woff2 — latin + latin-ext (Romanian diacritics)
          and cyrillic + cyrillic-ext (Russian)
  img/    photography and exported artwork
  svg/    logo, map, ornaments, cheese-wedge pattern
tools/    page generators; build_i18n.py builds the ru/ and en/ sites
```

Type is Kurale (display), Onest (body) and Berkshire Swash (the pillar
titles). Fonts are self-hosted rather than pulled from Google, which keeps the
site off a third-party CDN for GDPR purposes.

Each face is split by `unicode-range`, so a page only downloads the subset it
actually uses — the Romanian and English pages never fetch the Cyrillic files
and the Russian pages never fetch Berkshire Swash.

**Berkshire Swash has no Cyrillic glyphs at all.** The four pillar titles it
sets would fall back to whatever serif the visitor's OS supplies, so on Russian
pages they use Kurale instead — see the `:lang(ru)` rule in `sections.css`. If
that face is ever swapped, check Cyrillic coverage first.

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
- **Native review of the RU and EN copy** before launch — the translations are
  complete and consistent, but marketing copy benefits from a native speaker's
  ear, particularly the CTA ("Стать франчайзи" / "Become a franchisee")
- **Legal review of the translated terms page.** `termeni-si-conditii.html` is
  a legal document; the Russian and English versions carry the same meaning but
  are not certified translations, and the Romanian text remains the governing
  version under Moldovan law
- The footer heading above the legal links reads "Programe și Cursuri"
  (Programmes and Courses) in the Figma file, which does not describe the links
  beneath it. Translated faithfully for now — worth correcting in all three
  languages once the intended wording is confirmed
