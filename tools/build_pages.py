# -*- coding: utf-8 -*-
"""Generate the secondary pages (404, success).

The header bar, footer and modal are lifted straight out of `index.html` so the
shared chrome can never drift out of sync — edit it there, re-run this, done.

    python tools/build_pages.py
"""
import io
import os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_index():
    return io.open(os.path.join(SITE, 'index.html'), encoding='utf-8').read()


def stagger(text, tag='p', cls=''):
    """Wrap each word in its own span so the title can animate in a word at a
    time. Done here rather than at runtime so there is never a frame where the
    heading is unstyled or missing."""
    words = text.split(' ')
    spans = ''.join(
        '<span class="stagger__word" style="--i:%d">%s</span>%s'
        % (i, w, ' ' if i < len(words) - 1 else '')
        for i, w in enumerate(words)
    )
    attrs = ' class="%s stagger" data-stagger' % cls if cls else ' class="stagger" data-stagger'
    return '<%s%s>%s</%s>' % (tag, attrs, spans, tag)


index = read_index()

FOOTER = index[index.index('<!-- =========================================================== FOOTER -->'):
               index.index('</footer>') + len('</footer>')]

MODAL = index[index.index('<!-- ============================================================= MODAL -->'):
              index.index('<script src="assets/js/main.js"')].rstrip()

LANG = '''    <div class="page__lang">
      <button type="button" class="lang" data-lang-toggle aria-expanded="false" aria-haspopup="listbox">
        <span>Ro</span>
        <span class="lang__caret" aria-hidden="true"></span>
      </button>
      <div class="lang__menu" data-lang-menu role="listbox" aria-label="Alege limba">
        <button type="button" class="lang__option" role="option" aria-current="true">Română</button>
      </div>
    </div>'''


def shell(title, description, body, noindex=False):
    robots = '\n<meta name="robots" content="noindex">' if noindex else ''
    return f'''<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">{robots}

<script>document.documentElement.classList.add('has-motion');</script>
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/favicon-180.png">

<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/base.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="stylesheet" href="assets/css/sections.css">
<link rel="stylesheet" href="assets/css/motion.css">
<link rel="stylesheet" href="assets/css/pages.css">
</head>
<body>

<div class="page">
  <div class="pattern" aria-hidden="true"></div>

  <header class="page__bar">
    <a href="index.html" aria-label="Istorii cu Cașcaval — pagina principală">
      <img class="page__logo" src="assets/svg/logo.svg" alt="Istorii cu Cașcaval" width="132" height="167">
    </a>
{LANG}
  </header>

  <main class="page__body">
{body}
  </main>

{FOOTER}
</div>

{MODAL}

<script src="assets/js/main.js" defer></script>
<script src="assets/js/animations.js" defer></script>
</body>
</html>
'''


# --------------------------------------------------------------- 404
body_404 = '''    <div class="container notice">
      <img class="notice__art" src="assets/img/cheese-404.png" alt="" width="406" height="282">
      %s
      %s
      <a class="btn" href="index.html">Pagina principală</a>
    </div>''' % (
    stagger('404', 'p', 'notice__code'),
    stagger('Pagina nu a fost găsită', 'p', 'notice__title'),
)

# ----------------------------------------------------------- success
body_ok = '''    <div class="container notice">
      %s
      <p class="notice__text">În curând veți fi contactat pentru o discuție despre oportunitatea de a deveni partenerul Istorii cu cașcaval.</p>
      <a class="btn" href="index.html">Pagina principală</a>
    </div>''' % stagger('Datele Dvs. au fost recepționate.', 'p', 'notice__title')

pages = [
    ('404.html', 'Pagina nu a fost găsită — Istorii cu Cașcaval',
     'Pagina căutată nu a fost găsită.', body_404, True),
    ('success.html', 'Solicitare trimisă — Istorii cu Cașcaval',
     'Solicitarea ta a fost recepționată. Te vom contacta în curând.', body_ok, True),
]

if __name__ == '__main__':
    for name, title, desc, body, noindex in pages:
        io.open(os.path.join(SITE, name), 'w', encoding='utf-8').write(
            shell(title, desc, body, noindex))
        print('wrote', name)
