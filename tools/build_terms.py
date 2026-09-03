# -*- coding: utf-8 -*-
"""Generate the Romanian Terms & Conditions page.

    python tools/build_terms.py

The copy lives in terms_content.py, extracted from the client's Word document.
`doc_body()` is shared with build_i18n.py, which renders the same structure for
the Russian and English pages from their own authored text — that page is the
one place the translation dictionary is bypassed, because the three versions
were written separately rather than translated from one another.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_pages import shell, SITE, stagger  # noqa: E402
from terms_content import TERMS  # noqa: E402


def doc_body(locale):
    """Render one locale's Terms page body."""
    doc = TERMS[locale]
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


META = {
    'ro': ('Termeni și condiții — Istorii cu Cașcaval',
           'Termenii și condițiile de utilizare a website-ului Istorii cu Cașcaval.'),
}

if __name__ == '__main__':
    title, desc = META['ro']
    io.open(os.path.join(SITE, 'termeni-si-conditii.html'), 'w', encoding='utf-8').write(
        shell(title, desc, doc_body('ro')))
    print('wrote termeni-si-conditii.html')
