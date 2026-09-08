# -*- coding: utf-8 -*-
"""Exporta o livro para Markdown dentro do proprio repo."""
import io, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import html2md

# tudo relativo ao repo: o export nao depende mais de scratchpad de sessao
HERE = os.path.dirname(os.path.abspath(__file__))          # .../terceiraclasse/livro
REPO = os.path.dirname(HERE)                               # .../terceiraclasse
OLD = HERE                                                 # build_livro.py mora aqui
NEW = HERE
OUT = REPO                                                 # manuscrito/ e docs/ no repo
ART = os.path.join(REPO, "artefatos")                      # os HTML auxiliares

def rd(p):
    return io.open(p, encoding='utf-8').read()

def wr(rel, txt):
    p = os.path.join(OUT, rel)
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(txt)
    print('  %-58s %6d palavras' % (rel, len(txt.split())))

def slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s

def inline(s):
    """HTML inline -> Markdown."""
    s = re.sub(r'<em>(.*?)</em>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '  \n', s)
    s = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = (s.replace('&nbsp;', ' ').replace('&middot;', '·').replace('&amp;', '&')
          .replace('&mdash;', '—').replace('&ndash;', '–')
          .replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"'))
    return re.sub(r'[ \t]+', ' ', s).strip()

# =====================================================================
# 1. MANUSCRITO  (fonte: build_livro.py)
# =====================================================================
src = rd(os.path.join(OLD, 'build_livro.py'))
head = src.split('# ------------------------------------------------------------------ paginas')[0]
ns = {'__file__': os.path.join(OLD, 'build_livro.py'), '__name__': 'blv'}
exec(compile(head, 'build_livro_head', 'exec'), ns)
BOOKS, CAPS, CHAPTERS = ns['BOOKS'], ns['CAPS'], ns['CHAPTERS']

ROMAN = {'I': '1', 'II': '2', 'III': '3', 'IV': '4'}

# apaga o que sobrou de numeracoes anteriores: o export escreve, e agora tambem limpa
_man = os.path.join(OUT, 'manuscrito')
if os.path.isdir(_man):
    for _r, _d, _fs in os.walk(_man):
        for _f in _fs:
            if _f.endswith('.md'):
                os.remove(os.path.join(_r, _f))

print('\nmanuscrito/')
idx = []
total_w = 0
for bn, btitle, byears, bcolor in BOOKS:
    folder = 'manuscrito/livro-%s-%s' % (ROMAN.get(bn, bn), slug(btitle))
    idx.append((bn, btitle, byears, []))
    for (num, ctitle, synop) in CAPS[bn]:
        txt = CHAPTERS.get(num)
        fn = '%s/%02d-%s.md' % (folder, num, slug(ctitle))
        if txt:
            paras = []
            for block in txt:
                block = re.sub(r'\n[ \t]*\n', '\x00', block)
                for para in block.split('\x00'):
                    para = inline(re.sub(r'\s*\n\s*', ' ', para))
                    if para:
                        paras.append(para)
            body = '\n\n'.join(paras)
            w = len(body.split())
            total_w += w
            doc = ('# %d. %s\n\n> Livro %s — %s\n> %s\n\n---\n\n%s\n'
                   % (num, ctitle, bn, btitle, synop, body))
            wr(fn, doc)
            idx[-1][3].append((num, ctitle, synop, w, fn))
        else:
            idx[-1][3].append((num, ctitle, synop, 0, None))

# =====================================================================
# 2. CADERNO DE BORDO  (fonte: caderno-de-bordo.html)
# =====================================================================
cad = rd(os.path.join(ART, 'caderno-de-bordo.html'))
ROW_RE = (r'<div class="row">\s*<span class="n">(.*?)</span>\s*<span class="t">(.*?)</span>'
          r'\s*<span class="d">(.*?)</span>\s*<span class="pp">(.*?)</span>'
          r'\s*<span class="st">(.*?)</span>\s*</div>')
HEAD_RE = (r'<div class="bookhead">\s*<span class="bn">(.*?)</span>\s*<span class="bt">(.*?)</span>'
           r'\s*<span class="bp">(.*?)</span>')
blocks = []
for chunk in cad.split('<div class="book">')[1:]:
    h = re.search(HEAD_RE, chunk, flags=re.S)
    if not h:
        continue
    blocks.append((h.groups(), re.findall(ROW_RE, chunk, flags=re.S)))

STATUS = {1: 'Escrito', 0: ''}
written = set(CHAPTERS.keys())

L = ['# Caderno de Bordo', '',
     '> Plano de escrita de *As Três Mafaldas*. 34 capítulos, ~440 páginas.',
     '> Ordem de escrita ≠ ordem do livro. O capítulo 1 é o último a ser escrito.', '',
     '## Legenda das etiquetas', '',
     '| Etiqueta | Significa |', '|---|---|',
     '| **Pronto** | dá para escrever esta semana com o que já está em casa |',
     '| **Leitura** | precisa do Trento, da Alvim ou da cartilha do Espírito Santo |',
     '| **Arquivo** | precisa de hemeroteca, inquérito italiano ou Treviso |',
     '| **Campo** | precisa das gravações ou da viagem |',
     '| **Escrito** | rascunho existe (ver `manuscrito/`) |', '']

for (bn, bt, bp), rows in blocks:
    L += ['', '## %s — %s' % (inline(bn), inline(bt)), '', '*%s*' % inline(bp), '',
          '| # | Capítulo | O que é | pp | Estado |', '|---:|---|---|---:|---|']
    for r in rows:
        n, t, d, pp, st = [inline(x) for x in r]
        mark = '**Escrito**' if n.strip().isdigit() and int(n) in written else st
        L.append('| %s | %s | %s | %s | %s |' % (n, t, d, pp, mark))

# o resto da pagina (dividas de pesquisa, fases, como escrever um capitulo),
# com as linhas da grade descartadas porque ja viraram as tabelas acima
resto = html2md.convert(cad, drop_classes=('row', 'bookhead', 'legend'))
corte = resto.find('## A ordem de escrita')
if corte == -1:
    corte = resto.find('## Dívidas de pesquisa')
L += ['', '---', '', resto[corte:].rstrip() if corte > -1 else resto]

divs = resto.find('## Dívidas de pesquisa')
if divs > -1 and corte > divs:
    L.insert(len(L) - 1, resto[divs:corte].rstrip())

wr('docs/01-caderno-de-bordo.md', '\n'.join(L) + '\n')

# =====================================================================
# 3. DOSSIE  (fonte: tres-mafaldas.html)
# =====================================================================
def table_to_md(html):
    trs = re.findall(r'<tr\b[^>]*>(.*?)</tr>', html, flags=re.S)
    grid = []
    for tr in trs:
        cells = [inline(c) for c in
                 re.findall(r'<t[hd]\b[^>]*>(.*?)</t[hd]>', tr, flags=re.S)]
        if cells:
            grid.append(cells)
    if not grid:
        return ''
    w = max(len(r) for r in grid)
    grid = [r + [''] * (w - len(r)) for r in grid]
    head = grid[0]
    lines = ['| ' + ' | '.join(head) + ' |',
             '|' + '---|' * w]
    for r in grid[1:]:
        lines.append('| ' + ' | '.join(r) + ' |')
    return '\n'.join(lines)


def html_to_md(path, title):
    h = rd(path)
    h = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', '', h, flags=re.S)
    h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
    tables = []
    def stash(m):
        tables.append(table_to_md(m.group(0)))
        return '<p>@@TBL%d@@</p>' % (len(tables) - 1)
    h = re.sub(r'<table\b[^>]*>.*?</table>', stash, h, flags=re.S)
    out = []
    for m in re.finditer(
            r'<(h1|h2|h3|h4|p|li|blockquote|td|th)\b[^>]*>(.*?)</\1>', h, flags=re.S):
        tag, txt = m.group(1), inline(m.group(2))
        if not txt:
            continue
        if tag == 'h1':
            out.append('\n# ' + txt)
        elif tag == 'h2':
            out.append('\n## ' + txt)
        elif tag == 'h3':
            out.append('\n### ' + txt)
        elif tag == 'h4':
            out.append('\n**' + txt + '**')
        elif tag == 'li':
            out.append('- ' + txt)
        elif tag == 'blockquote':
            out.append('> ' + txt)
        elif tag in ('td', 'th'):
            out.append('- ' + txt)
        else:
            out.append(txt)
    body = '\n\n'.join(out)
    for i, t in enumerate(tables):
        body = body.replace('@@TBL%d@@' % i, t)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    if not body.startswith('#'):
        body = '# ' + title + '\n\n' + body
    return body + '\n'

print('\ndocumentos/')
wr('docs/00-dossie.md', html2md.convert(rd(os.path.join(ART, 'tres-mafaldas.html'))))
wr('docs/03-roteiro-gravacoes.md', html2md.convert(rd(os.path.join(ART, 'gravar-mafalda.html'))))

print('\ntotal escrito: %d palavras' % total_w)

# guarda o indice para o README
io.open(os.path.join(HERE, 'idx.txt'), 'w', encoding='utf-8').write(
    repr([(b, t, y, [(n, c, s, w) for n, c, s, w, f in r]) for b, t, y, r in idx]))
