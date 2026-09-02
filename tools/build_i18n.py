# -*- coding: utf-8 -*-
"""Generate the Russian and English sites from the Romanian originals.

    python tools/build_i18n.py

The Romanian pages stay the single source of truth for markup. This script only
swaps text, rewrites the paths that change when a page moves down a directory,
and rebuilds the language switcher. Layout changes therefore reach all three
languages by editing one file and re-running this.

It fails loudly rather than silently shipping Romanian: every string it could
not translate is listed at the end, and the exit code is non-zero.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from i18n_lib import (  # noqa: E402
    iter_text_nodes, iter_attr_values, iter_stagger_titles, STAGGER_RE,
    replace_text_nodes, replace_attrs, translate_stagger,
)
from i18n_strings import LOCALES, BASE, PAGES, PASSTHROUGH  # noqa: E402

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = ['index.html', 'termeni-si-conditii.html', '404.html', 'success.html']


# ------------------------------------------------------------------ switcher

def switcher(page, current, wrapper_class):
    """Build the three-language menu for `page` as seen from `current`."""
    order = ['ro', 'ru', 'en']
    meta = {'ro': BASE}
    meta.update(LOCALES)

    options = []
    for code in order:
        target_name = PAGES[page][code]
        target_dir = meta[code]['dir']
        if code == current:
            href = target_name
        elif current == 'ro':
            href = '%s/%s' % (target_dir, target_name)
        elif code == 'ro':
            href = '../%s' % target_name
        else:
            href = '../%s/%s' % (target_dir, target_name)
        options.append(
            '        <a class="lang__option" role="option" hreflang="%s"%s href="%s">%s</a>'
            % (code, ' aria-current="true"' if code == current else '',
               href, meta[code]['name'])
        )

    return '''    <div class="%s">
      <button type="button" class="lang" data-lang-toggle aria-expanded="false" aria-haspopup="listbox">
        <span>%s</span>
        <span class="lang__caret" aria-hidden="true"></span>
      </button>
      <div class="lang__menu" data-lang-menu role="listbox" aria-label="%s">
%s
      </div>
    </div>''' % (wrapper_class, meta[current]['label'], meta[current]['menu_label'],
                 '\n'.join(options))


SWITCHER_RE = re.compile(
    r'[ \t]*<div class="(hero__lang|page__lang)">.*?</div>\s*</div>', re.S)


def replace_switcher(html, page, locale):
    def sub(m):
        return switcher(page, locale, m.group(1))
    new, n = SWITCHER_RE.subn(sub, html)
    if n != 1:
        raise SystemExit('  ! switcher block not found exactly once in %s (%d)'
                         % (page, n))
    return new


# ------------------------------------------------------------------ hreflang

def hreflang(page, current):
    order = ['ro', 'ru', 'en']
    meta = {'ro': BASE}
    meta.update(LOCALES)
    links = []
    for code in order:
        name = PAGES[page][code]
        d = meta[code]['dir']
        if code == current:
            href = name
        elif current == 'ro':
            href = '%s/%s' % (d, name)
        elif code == 'ro':
            href = '../%s' % name
        else:
            href = '../%s/%s' % (d, name)
        links.append('<link rel="alternate" hreflang="%s" href="%s">' % (code, href))
    links.append('<link rel="alternate" hreflang="x-default" href="%s">'
                 % ('%s' % PAGES[page]['ro'] if current == 'ro' else '../%s' % PAGES[page]['ro']))
    return '\n'.join(links)


def inject_hreflang(html, page, locale):
    block = hreflang(page, locale)
    # Sits with the other <head> metadata, right before the icon links.
    marker = '<link rel="icon"'
    if marker not in html:
        raise SystemExit('  ! no icon link to anchor hreflang in %s' % page)
    return html.replace(marker, block + '\n' + marker, 1)


# --------------------------------------------------------------------- paths

def preload_subset(html, lang):
    """Preload the subset the page will actually render in.

    The Romanian original preloads the latin cut. On a Russian page almost
    every glyph comes from the cyrillic file instead, so preloading latin
    warms the wrong cache and leaves the visible text waiting on a font that
    was never requested early.
    """
    if lang != 'ru':
        return html
    return (html
            .replace('kurale-400-latin.woff2', 'kurale-400-cyrillic.woff2')
            .replace('onest-400-latin.woff2', 'onest-400-cyrillic.woff2'))


def rewrite_paths(html):
    """Fix references that break one directory down."""
    html = re.sub(r'(href|src)="(assets/)', r'\1="../\2', html)
    html = html.replace('href="favicon.ico"', href_up('favicon.ico'))
    return html


def href_up(name):
    return 'href="../%s"' % name


def rewrite_links(html, locale):
    """Point internal page links at this locale's filenames."""
    for src, names in PAGES.items():
        target = names[locale]
        if target != src:
            html = html.replace('href="%s"' % src, 'href="%s"' % target)
    return html


# --------------------------------------------------------------------- build

def expected_output(cfg):
    """Everything that may legitimately appear in a translated page.

    Beyond the table's own values this has to include the text nodes *inside*
    translated blocks — a block is swapped as one HTML fragment, so its
    individual sentences never appear as table values — and the language names
    in the switcher, which are the same three words on every page.
    """
    ok = set(cfg['table'].values())
    for dst in cfg['blocks'].values():
        ok.update(iter_text_nodes(dst))
        ok.add(dst.strip())
    ok.update(m['name'] for m in list(LOCALES.values()) + [BASE])
    ok.update(m['menu_label'] for m in list(LOCALES.values()) + [BASE])
    return ok


def translate(html, page, locale, cfg, unmatched):
    table, blocks = cfg['table'], cfg['blocks']
    allowed = expected_output(cfg)
    seen = set()

    # 1. whole HTML fragments whose word order changes between languages
    for src, dst in blocks.items():
        if src in html:
            html = html.replace(src, dst)
            seen.add('<block> ' + src[:40])

    # 2. staggered headings — spans regenerated for the new word count
    html = translate_stagger(html, table, seen)

    # 3. ordinary text nodes and translatable attributes
    html = replace_text_nodes(html, table, seen)
    html = replace_attrs(html, table, seen)

    # 4. anything still Romanian?
    for text in list(iter_stagger_titles(html)) + list(iter_text_nodes(
            STAGGER_RE.sub(lambda m: m.group(1) + m.group(4), html))):
        if text in allowed or text in PASSTHROUGH:
            continue
        unmatched.setdefault((locale, text), set()).add(page)
    for val in iter_attr_values(html):
        if val in allowed or val in PASSTHROUGH:
            continue
        unmatched.setdefault((locale, val), set()).add(page)

    return html


def build():
    unmatched = {}
    written = 0

    for locale, cfg in LOCALES.items():
        outdir = os.path.join(SITE, cfg['dir'])
        if not os.path.isdir(outdir):
            os.makedirs(outdir)

        for page in SOURCES:
            html = io.open(os.path.join(SITE, page), encoding='utf-8').read()

            # Translate first, then build the switcher. The other way round,
            # the translation pass rewrites the menu's own language names —
            # "Română" became "Русский" on the Russian page, so every option
            # read the same. Each language is always named in its own tongue.
            html = translate(html, page, locale, cfg, unmatched)
            html = replace_switcher(html, page, locale)
            html = re.sub(r'<html lang="ro">', '<html lang="%s">' % cfg['lang'],
                          html, count=1)
            html = preload_subset(html, cfg['lang'])
            html = rewrite_links(html, locale)
            html = inject_hreflang(html, page, locale)
            html = rewrite_paths(html)
            # The logo's home link, relative so it survives any subdirectory.
            html = html.replace('<a href="/" aria-label', '<a href="index.html" aria-label')

            out = os.path.join(outdir, PAGES[page][locale])
            io.open(out, 'w', encoding='utf-8').write(html)
            written += 1
            print('  wrote %s/%s' % (cfg['dir'], PAGES[page][locale]))

    # Romanian gets the switcher and hreflang too, in place.
    for page in SOURCES:
        path = os.path.join(SITE, page)
        html = io.open(path, encoding='utf-8').read()
        html = replace_switcher(html, page, 'ro')
        # Must test for the <link> specifically: the switcher's own <a> tags
        # carry hreflang attributes too, so a bare 'hreflang="ru"' check is
        # always true once the menu exists and the alternates never land.
        if 'rel="alternate" hreflang="ru"' not in html:
            html = inject_hreflang(html, page, 'ro')
        html = html.replace('<a href="/" aria-label', '<a href="index.html" aria-label')
        io.open(path, 'w', encoding='utf-8').write(html)
        print('  updated %s (switcher + hreflang)' % page)

    print('\n%d translated pages written.' % written)

    if unmatched:
        print('\nUNTRANSLATED STRINGS (%d):' % len(unmatched))
        for (locale, text), pages in sorted(unmatched.items()):
            print('  [%s] %-24s %s' % (locale, ','.join(sorted(pages))[:24], text[:100]))
        return 1

    print('Every translatable string was covered.')
    return 0


if __name__ == '__main__':
    sys.exit(build())
