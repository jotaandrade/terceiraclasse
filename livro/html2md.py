# -*- coding: utf-8 -*-
"""Conversor HTML -> Markdown para os artefatos do projeto.

Ao contrario do regex anterior, este percorre a arvore inteira, entao nao perde
o texto que mora em <div class="note">, <span> de card, <dl>, etc.
"""
import re
from html.parser import HTMLParser

SKIP_TAGS = {'script', 'style', 'head', 'title', 'svg', 'noscript'}
# vazias: nunca tem tag de fechamento, entao nao podem abrir um bloco de skip
VOID_TAGS = {'link', 'meta', 'img', 'input', 'hr', 'source', 'col', 'area', 'base'}
BLOCK = {'p', 'div', 'section', 'header', 'footer', 'article', 'ul', 'ol', 'dl',
         'blockquote', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'figure', 'figcaption',
         'table', 'tr', 'main', 'nav', 'aside'}
HEAD = {'h1': '# ', 'h2': '## ', 'h3': '### ', 'h4': '**', 'h5': '**', 'h6': '**'}


class Walker(HTMLParser):
    def __init__(self, drop_classes=()):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.out = []          # blocos ja fechados
        self.buf = []          # texto do bloco corrente
        self.skip = 0
        self.drop = 0
        self.drop_classes = set(drop_classes)
        self.ctx = []          # pilha de (tag, classes)
        self.segs = []         # segmentos (spans) do container corrente
        self.tbl = None
        self.row = None
        self.cell = None

    # ---------------------------------------------------------------- util
    def _txt(self):
        t = ''.join(self.buf)
        self.buf = []
        t = re.sub(r'[ \t\r\n]+', ' ', t).strip()
        return t

    def _flush(self, prefix='', join=' '):
        t = self._txt()
        if t:
            self.segs.append(t)
        if not self.segs:
            return
        body = join.join(self.segs)
        self.segs = []
        body = re.sub(r'\s+([,.;:!?])', r'\1', body).strip()
        if body:
            self.out.append(prefix + body)

    def _classes(self, attrs):
        d = dict(attrs)
        return set((d.get('class') or '').split())

    # ---------------------------------------------------------------- tags
    def handle_starttag(self, tag, attrs):
        if tag in VOID_TAGS:
            return
        if tag in SKIP_TAGS:
            self.skip += 1
            return
        if self.skip or self.drop:
            if self.drop:
                self.ctx.append((tag, set()))
            return

        cls = self._classes(attrs)
        if cls & self.drop_classes:
            self.drop = 1
            self.ctx.append((tag, cls))
            return

        if tag == 'br':
            self.buf.append('\n')
            return
        if tag in ('em', 'i'):
            self.buf.append('*')
            return
        if tag in ('strong', 'b'):
            self.buf.append('**')
            return
        if tag == 'code':
            self.buf.append('`')
            return
        if tag == 'a':
            self.buf.append('[')
            return

        if tag == 'table':
            self._flush()
            self.tbl = []
            self.ctx.append((tag, cls))
            return
        if tag == 'tr' and self.tbl is not None:
            self.row = []
            return
        if tag in ('td', 'th') and self.row is not None:
            self.buf = []
            self.cell = tag
            return

        if tag in BLOCK:
            # um novo bloco fecha o anterior
            t = self._txt()
            if t:
                self.segs.append(t)
            if tag in HEAD:
                self._flush()
            elif 'note' in cls or tag == 'blockquote':
                self._flush()
            elif tag in ('div', 'p', 'section', 'ul', 'ol', 'dl', 'header', 'footer'):
                self._flush()
        elif tag == 'span':
            t = self._txt()
            if t:
                self.segs.append(t)
        elif tag == 'li':
            t = self._txt()
            if t:
                self.segs.append(t)
            self._flush()
        self.ctx.append((tag, cls))

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return

        if self.drop:
            if self.ctx:
                self.ctx.pop()
            if not any(c & self.drop_classes for _, c in self.ctx):
                self.drop = 0
            return

        if tag in ('em', 'i'):
            self.buf.append('*')
            return
        if tag in ('strong', 'b'):
            self.buf.append('**')
            return
        if tag == 'code':
            self.buf.append('`')
            return
        if tag == 'a':
            self.buf.append(']')
            return

        cls = set()
        if self.ctx and self.ctx[-1][0] == tag:
            cls = self.ctx.pop()[1]

        if tag in ('td', 'th') and self.row is not None:
            self.row.append(self._txt())
            self.cell = None
            return
        if tag == 'tr' and self.tbl is not None:
            if self.row:
                self.tbl.append(self.row)
            self.row = None
            return
        if tag == 'table' and self.tbl is not None:
            grid = self.tbl
            self.tbl = None
            if grid:
                w = max(len(r) for r in grid)
                grid = [r + [''] * (w - len(r)) for r in grid]
                lines = ['| ' + ' | '.join(grid[0]) + ' |', '|' + '---|' * w]
                for r in grid[1:]:
                    lines.append('| ' + ' | '.join(r) + ' |')
                self.out.append('\n'.join(lines))
            return

        if tag in HEAD:
            t = self._txt()
            if t:
                self.segs = []
                self.out.append(HEAD[tag] + t + ('**' if tag in ('h4', 'h5', 'h6') else ''))
            return
        if tag == 'li':
            self._flush(prefix='- ', join=' — ')
            return
        if tag == 'blockquote' or 'note' in cls:
            self._flush(prefix='> ', join=' — ')
            return
        if tag in BLOCK:
            self._flush(join=' — ' if cls else ' ')

    def handle_data(self, data):
        if self.skip or self.drop:
            return
        self.buf.append(data)

    def result(self):
        self._flush()
        body = '\n\n'.join(x for x in self.out if x.strip())
        body = re.sub(r'\n{3,}', '\n\n', body)
        # limpa apenas enfase VAZIA, sem tocar em **negrito** de verdade
        body = body.replace('****', '')
        body = re.sub(r'\*\*\s+\*\*', ' ', body)
        body = re.sub(r'(?<!\*)\*\s+\*(?!\*)', ' ', body)
        body = re.sub(r'[ \t]{2,}', ' ', body)
        return body.strip() + '\n'


def convert(html, drop_classes=()):
    w = Walker(drop_classes=drop_classes)
    w.feed(html)
    return w.result()
