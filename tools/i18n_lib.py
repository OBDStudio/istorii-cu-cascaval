# -*- coding: utf-8 -*-
"""Shared machinery for the translated builds.

The Romanian pages are the single source of truth. Rather than maintaining
three hand-edited copies of every page — which drift the moment anyone touches
the layout — the translated pages are generated from the Romanian ones by
swapping text, and nothing else.

Two rules keep that honest:

  * every string is matched as a *whole text node*, never as a substring, so a
    word like "Business" can never be rewritten where it appears inside a class
    name, a URL or another sentence;
  * every key in the translation table must actually be found, and every
    translatable node must actually be covered. Both directions are reported by
    `build_i18n.py`, so a missed string is a build error rather than a patch of
    Romanian nobody notices on a live Russian page.
"""
import re

# Tags whose contents are code, not prose.
OPAQUE = ('script', 'style')

# Attributes that carry human-readable text.
TEXT_ATTRS = ('alt', 'aria-label', 'placeholder', 'content', 'title')

# Text nodes we never translate: pure punctuation, numbers, currency, and the
# handful of proper nouns that stay as they are in every language.
SKIP = re.compile(r'^[\s\d.,:;•\-–—/|()\[\]&+%€$]*$')


def _segments(html):
    """Split into (is_tag, text) parts, marking anything inside <script>/<style>
    as untouchable."""
    parts = re.split(r'(<[^>]*>)', html)
    opaque_depth = 0
    out = []
    for part in parts:
        if part.startswith('<'):
            low = part.lower()
            name = re.match(r'</?\s*([a-z0-9]+)', low)
            if name and name.group(1) in OPAQUE:
                opaque_depth += -1 if low.startswith('</') else 1
                opaque_depth = max(0, opaque_depth)
            out.append((True, part))
        else:
            out.append((False if not opaque_depth else True, part))
    return out


def iter_text_nodes(html):
    """Yield every translatable text node's stripped content."""
    for is_tag, part in _segments(html):
        if is_tag:
            continue
        text = part.strip()
        if text and not SKIP.match(text):
            yield text


def iter_attr_values(html):
    """Yield every translatable attribute value."""
    for is_tag, part in _segments(html):
        if not is_tag or not part.startswith('<'):
            continue
        if part.startswith('<!--'):
            continue
        for attr in TEXT_ATTRS:
            for m in re.finditer(r'\b%s="([^"]*)"' % attr, part):
                val = m.group(1).strip()
                # <meta name="viewport" content="width=..."> and friends are
                # configuration, not prose.
                if attr == 'content' and re.search(r'^(width=|noindex|IE=|\d)', val):
                    continue
                if val and not SKIP.match(val):
                    yield val


def replace_text_nodes(html, table, seen=None):
    """Swap whole text nodes using `table`, preserving surrounding whitespace."""
    out = []
    for is_tag, part in _segments(html):
        if is_tag:
            out.append(part)
            continue
        stripped = part.strip()
        if stripped and stripped in table:
            if seen is not None:
                seen.add(stripped)
            lead = part[:len(part) - len(part.lstrip())]
            tail = part[len(part.rstrip()):]
            out.append(lead + table[stripped] + tail)
        else:
            out.append(part)
    return ''.join(out)


def replace_attrs(html, table, seen=None):
    """Swap translatable attribute values."""
    def fix_tag(m):
        tag = m.group(0)
        if tag.startswith('<!--'):
            return tag
        for attr in TEXT_ATTRS:
            def sub(am):
                val = am.group(1)
                key = val.strip()
                if key in table:
                    if seen is not None:
                        seen.add(key)
                    return '%s="%s"' % (attr, table[key])
                return am.group(0)
            tag = re.sub(r'\b%s="([^"]*)"' % attr, sub, tag)
        return tag

    return re.sub(r'<[^>]*>', fix_tag, html)


# ------------------------------------------------------------------ stagger

STAGGER_RE = re.compile(
    r'(<(h1|h2|p)\b[^>]*\bdata-stagger(?:="[^"]*")?[^>]*>)(.*?)(</\2>)',
    re.S)


def stagger_words(text):
    """Wrap each word in its own span. Mirrors tools/build_pages.py:stagger."""
    words = text.split(' ')
    return ''.join(
        '<span class="stagger__word" style="--i:%d">%s</span>%s'
        % (i, w, ' ' if i < len(words) - 1 else '')
        for i, w in enumerate(words)
    )


def stagger_text(inner):
    """Recover the plain heading text from its per-word spans."""
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', inner)).strip()


def iter_stagger_titles(html):
    for m in STAGGER_RE.finditer(html):
        text = stagger_text(m.group(3))
        if text:
            yield text


def translate_stagger(html, table, seen=None):
    """Translate staggered headings and re-split them.

    Word counts differ between languages, so the spans must be regenerated
    rather than patched — the `--i` index drives the per-word delay.
    """
    def sub(m):
        open_tag, _tag, inner, close = m.groups()
        text = stagger_text(inner)
        if text in table:
            if seen is not None:
                seen.add(text)
            return open_tag + stagger_words(table[text]) + close
        return m.group(0)

    return STAGGER_RE.sub(sub, html)
