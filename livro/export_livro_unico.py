# -*- coding: utf-8 -*-
"""Exporta o livro inteiro num unico Markdown, na ordem das paginas.

Fonte: build_livro.py. Le a lista `pages` ja montada (pre-textuais, partes,
capitulos, imagens, epilogo, agradecimentos e aparato) e converte cada tipo
de pagina para Markdown, sem re-derivar estrutura nenhuma.

    python livro/export_livro_unico.py
"""
import io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'build_livro.py')
OUT = os.path.join(REPO, 'terceira-classe-livro-completo.md')
CORTE = '# ------------------------------------------------------------------- render'


def inline(s):
    """HTML inline -> Markdown. Mesma regra do export_md.py."""
    s = re.sub(r'<em>(.*?)</em>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', '  \n', s)
    s = re.sub(r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S)
    s = re.sub(r'<span class="ix-[pf]">(.*?)</span>', r'\1', s, flags=re.S)
    s = re.sub(r'<[^>]+>', '', s)
    s = (s.replace('&nbsp;', ' ').replace('&middot;', '·').replace('&amp;', '&')
          .replace('&mdash;', '—').replace('&ndash;', '–')
          .replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"'))
    return re.sub(r'[ \t]+', ' ', s).strip()


def paras(txt):
    """Bloco com quebras de linha soltas -> paragrafos Markdown."""
    txt = re.sub(r'\n[ \t]*\n', '\x00', txt)
    saida = []
    for p in txt.split('\x00'):
        p = inline(re.sub(r'\s*\n\s*', ' ', p))
        if p:
            saida.append(p)
    return saida


# ------------------------------------------------------ le a fonte do livro
src = io.open(SRC, encoding='utf-8').read()
if CORTE not in src:
    raise SystemExit('marcador de render nao encontrado em build_livro.py')
ns = {'__file__': SRC, '__name__': 'blv'}
exec(compile(src.split(CORTE)[0], 'build_livro_pages', 'exec'), ns)

pages = ns['pages']
BOOKS, CAPS, CHAPTERS = ns['BOOKS'], ns['CAPS'], ns['CHAPTERS']
NOTA_METODO, AGRADECIMENTOS = ns['NOTA_METODO'], ns['AGRADECIMENTOS']

SUB = 'A travessia italiana para o Brasil e o naufrágio do *Principessa Mafalda*'
TIT_AP = {'fontes': 'Fontes', 'credimg': 'Créditos de imagem',
          'indice': 'Índice onomástico'}

L = []
def add(*linhas):
    L.extend(linhas)

palavras = 0
aparato_aberto = None   # agrupa as varias paginas de fontes/credimg/indice
folio = 0

for p in pages:
    t = p['t']
    if t not in ('fontes', 'credimg', 'indice'):
        aparato_aberto = None
    if t in ('cap', 'texto', 'img', 'audio', 'pendente', 'fontes', 'credimg', 'indice'):
        folio += 1

    if t == 'capa':
        add('# Terceira Classe', '',
            '**' + SUB + '**', '',
            'João Andrade', '',
            '1861 · 1927 · hoje', '', '---', '')

    elif t == 'rosto':
        add('> Edição de trabalho. Este exemplar é um rascunho: os capítulos são',
            '> publicados conforme ficam prontos, e o epílogo ainda não existe.', '')

    elif t == 'creditos':
        add('## Créditos', '',
            '© João José de Andrade Neto', '',
            '*Terceira Classe* — ' + SUB, '',
            'Todos os direitos reservados. Nenhuma parte desta obra pode ser reproduzida '
            'sem autorização escrita do autor.', '',
            '| | |', '|---|---|',
            '| Ano de publicação | a definir |',
            '| Editora | a definir |',
            '| ISBN | a definir |',
            '| Ficha catalográfica (CIP) | a elaborar |',
            '| Preparação, revisão, projeto gráfico e diagramação | a definir |',
            '| Impressão | a definir |', '',
            'As fotografias e os documentos reproduzidos pertencem ao acervo da família '
            'Miotto e Forner, salvo indicação em contrário na relação de créditos de imagem, '
            'ao fim do volume.', '',
            'Foram feitos todos os esforços para identificar e creditar os detentores de '
            'direito sobre as imagens e os textos reproduzidos. Onde a procedência não pôde '
            'ser estabelecida, isso está dito na própria relação de créditos. O autor se '
            'compromete a corrigir, em edições futuras, qualquer omissão ou erro que lhe '
            'seja apontado.', '',
            'As pessoas vivas nomeadas e fotografadas nesta obra autorizaram o uso do nome '
            'e da imagem. Onde um documento particular da família trazia dado pessoal de '
            'terceiro, o dado foi tarjado, e a tarja está declarada na legenda.', '', '---', '')

    elif t == 'dedicatoria':
        add('Para o meu filho', '', '**João Luca Soares de Andrade**', '', '---', '')

    elif t == 'epigrafe':
        add('> A cena é lancinante. Lágrimas, lamúrias, desmaios, invocações devotas, '
            'promessas. Da amurada do navio os lenços sacodem nervosos as despedidas finais. '
            'Addio! Addio! Addio! Os corações se fecham numa saudade funda.', '>',
            '> — Serafim Derenzi, 1974', '', '---', '')

    elif t == 'sumario':
        add('## Sumário', '')
        for bn, btitle, byears, _c in BOOKS:
            add('**Parte %s — %s** · %s' % (bn, btitle, byears), '')
            for (num, ctitle, _s) in CAPS[bn]:
                marca = '' if num in CHAPTERS else '  *(a escrever)*'
                add('%d. %s%s' % (num, ctitle, marca))
            add('')
        add('**Epílogo — As três Mafaldas** *(a escrever)*', '',
            'Agradecimentos · Fontes · Créditos de imagem · Índice onomástico', '', '---', '')

    elif t == 'nota':
        if p['body'] == NOTA_METODO[0]:
            add('## Nota de método', '')
        add(*sum([[x, ''] for x in paras(p['body'])], []))
        if p['body'] == NOTA_METODO[-1]:
            add('---', '')

    elif t == 'parte':
        n = p['n']
        n = ('Parte ' + n) if n in ('I', 'II', 'III', 'IV') else n.capitalize()
        add('# %s — %s' % (n, p['title']), '')
        if p['years']:
            add('*%s*' % p['years'], '')
        add('---', '')

    elif t == 'cap':
        if p.get('book') == 'EP':
            add('## Epílogo — %s' % p['title'], '')
        else:
            add('## %d. %s' % (p['num'], p['title']), '')
        add('> %s' % inline(p['synop']), '')

    elif t == 'texto':
        bloco = paras(p['body'])
        palavras += sum(len(x.split()) for x in bloco)
        add(*sum([[x, ''] for x in bloco], []))

    elif t == 'img':
        leg = inline(p['cap'])
        alt = re.sub(r'[*\[\]]', '', leg)
        alt = re.sub(r'\s+', ' ', alt).strip()
        if len(alt) > 90:
            alt = alt[:90].rsplit(' ', 1)[0] + '…'
        add('![%s](livro/img/%s.webp)' % (alt, p['key']), '',
            '*%s*' % leg, '')

    elif t == 'audio':
        add('### Documento sonoro — %s' % inline(p['tit']), '',
            '*%s*' % inline(p['meta']), '',
            '[Áudio: livro/audio/%s.m4a](livro/audio/%s.m4a)' % (p['key'], p['key']), '',
            inline(p['nota']), '')
        add(*sum([[x, ''] for x in paras(p['tr'])], []))

    elif t == 'pendente':
        add('### %s' % inline(p['title']), '',
            '> **Capítulo pendente.** %s' % inline(p['body']), '')

    elif t == 'agradecimentos':
        add('---', '', '## Agradecimentos', '')
        add(*sum([[x, ''] for x in paras(AGRADECIMENTOS)], []))
        add('João José de Andrade Neto', '')

    elif t in ('fontes', 'credimg', 'indice'):
        if aparato_aberto != t:
            add('## %s' % TIT_AP[t], '')
            aparato_aberto = t
        for k, v in p['itens']:
            if k == 'h':
                add('**%s**' % inline(v), '')
            else:
                add('- %s' % inline(v))
        add('')

    elif t == 'fim':
        add('---', '', '### continua', '',
            'Os vinte e sete capítulos estão escritos. Falta o epílogo, que depende das '
            'gravações com Mafalda Miotto Terra, e a reescrita do capítulo 27 depois da '
            'viagem a Castelcucco.', '',
            'Centenário do naufrágio: 25 de outubro de 2027.', '')

texto = re.sub(r'\n{3,}', '\n\n', '\n'.join(L)).strip() + '\n'
io.open(OUT, 'w', encoding='utf-8', newline='\n').write(texto)

print('%s' % os.path.relpath(OUT, REPO))
print('  %d paginas de origem, %d folios' % (len(pages), folio))
print('  %d palavras de texto corrido, %d palavras no arquivo' % (palavras, len(texto.split())))
print('  %d KB' % (len(texto.encode('utf-8')) // 1024))
