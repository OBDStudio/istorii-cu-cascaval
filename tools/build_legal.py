# -*- coding: utf-8 -*-
"""Generate the Romanian legal pages: Terms, Privacy Policy, Cookie Policy.

    python tools/build_legal.py

The copy lives in legal_content.py, extracted from the client's Word document.
`doc_body()` is shared with build_i18n.py, which renders the same structure for
the Russian and English pages from their own authored text — these pages are the
one place the translation dictionary is bypassed, because the three versions
were written separately rather than translated from one another.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import shell, SITE, stagger  # noqa: E402
from legal_content import DOCS  # noqa: E402

# doc id -> per-locale filename, and the <head> copy for each language.
PAGES = {
    'terms': {
        'file': {'ro': 'termeni-si-conditii.html', 'en': 'terms.html', 'ru': 'terms.html'},
        'head': {
            'ro': ('Termeni și condiții — Istorii cu Cașcaval',
                   'Termenii și condițiile de utilizare a website-ului de franciză Istorii cu Cașcaval.'),
            'en': ('Terms and conditions — Istorii cu Cașcaval',
                   'The terms and conditions for using the Istorii cu Cașcaval franchise website.'),
            'ru': ('Условия использования — Istorii cu Cașcaval',
                   'Условия использования сайта франшизы Istorii cu Cașcaval.'),
        },
    },
    'privacy': {
        'file': {'ro': 'politica-de-confidentialitate.html', 'en': 'privacy.html', 'ru': 'privacy.html'},
        'head': {
            'ro': ('Politica de confidențialitate — Istorii cu Cașcaval',
                   'Cum colectăm și utilizăm datele personale ale vizitatorilor site-ului de franciză.'),
            'en': ('Privacy policy — Istorii cu Cașcaval',
                   'How we collect and use the personal data of visitors to the franchise website.'),
            'ru': ('Политика конфиденциальности — Istorii cu Cașcaval',
                   'Как мы собираем и используем персональные данные посетителей сайта франшизы.'),
        },
    },
    'cookies': {
        'file': {'ro': 'politica-de-cookies.html', 'en': 'cookies.html', 'ru': 'cookies.html'},
        'head': {
            'ro': ('Politica de cookies — Istorii cu Cașcaval',
                   'Cum utilizează site-ul de franciză Istorii cu Cașcaval fișierele cookies.'),
            'en': ('Cookie policy — Istorii cu Cașcaval',
                   'How the Istorii cu Cașcaval franchise website uses cookies.'),
            'ru': ('Политика использования Cookies — Istorii cu Cașcaval',
                   'Как сайт франшизы Istorii cu Cașcaval использует файлы cookies.'),
        },
    },
}


def doc_body(doc_id, locale):
    """Render one document, in one language, as the page body."""
    doc = DOCS[doc_id][locale]
    out = ['    <div class="doc">',
           '    ' + stagger(doc['title'], 'h1', 'doc__title'),
           '    <p class="doc__updated">%s</p>' % doc['updated'],
           '    <p class="doc__lede">%s</p>' % '<br>'.join(doc['lede'])]

    def render(blocks, indent):
        pad = ' ' * indent
        for kind, val in blocks:
            if kind == 'ul':
                out.append(pad + '<ul>')
                out.extend(pad + '  <li>%s</li>' % i for i in val)
                out.append(pad + '</ul>')
            elif kind == 'h3':
                out.append(pad + '<h3>%s</h3>' % val)
            else:
                out.append(pad + '<p>%s</p>' % val)

    # Anything ahead of the first numbered clause sits outside a <section>.
    out.append('')
    render(doc['intro'], 4)

    open_section = False
    for kind, val in doc['body']:
        if kind == 'h2':
            if open_section:
                out.append('    </section>')
            out.append('')
            out.append('    <section>')
            out.append('      <h2>%s</h2>' % val)
            open_section = True
        else:
            render([(kind, val)], 6)
    if open_section:
        out.append('    </section>')

    out.append('    </div>')
    return '\n'.join(out)


if __name__ == '__main__':
    for doc_id, cfg in PAGES.items():
        title, desc = cfg['head']['ro']
        name = cfg['file']['ro']
        io.open(os.path.join(SITE, name), 'w', encoding='utf-8').write(
            shell(title, desc, doc_body(doc_id, 'ro')))
        print('wrote', name)
