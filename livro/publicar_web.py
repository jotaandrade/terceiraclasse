# -*- coding: utf-8 -*-
"""
Prepara o livro para publicacao em terceiraclasse.com/livroemandamento.

Por que este script existe: `build_livro.py` gera um *fragmento* HTML, sem
<!DOCTYPE>, <html>, <head> nem <body> — e tem de continuar assim, porque esse e
o formato que o publicador de artefatos espera. Servido por nginx, esse fragmento
funciona por tolerancia do navegador, mas fica sem charset declarado e sem como
receber a marca de nao-indexacao.

Este script envolve o fragmento num documento completo e acrescenta:

  - <meta charset="utf-8">          para o acento nao quebrar
  - <meta name="viewport">          para o celular
  - <meta name="robots" noindex>    a marca de nao-indexacao no HTML

A marca do HTML e a *segunda* linha de defesa. A primeira e o cabecalho
`X-Robots-Tag`, mandado pelo nginx, que vale mesmo se o robo nao ler o HTML.
As duas estao ligadas de proposito.

Uso:
    python livro/build_livro.py        # gera o fragmento
    python livro/publicar_web.py       # envolve e escreve o dist
"""
import io
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(AQUI, 'terceira-classe.html')
DESTINO = os.path.join(AQUI, 'dist', 'livroemandamento', 'index.html')

CABECA = u"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<meta name="referrer" content="no-referrer">
"""

RODAPE = u"""
</body>
</html>
"""


def main():
    if not os.path.exists(ORIGEM):
        raise SystemExit('Nao achei %s. Rode antes: python livro/build_livro.py' % ORIGEM)

    frag = io.open(ORIGEM, encoding='utf-8').read()

    # O fragmento abre com <title> e os <link> das fontes: tudo isso e <head>.
    # O <body> comeca onde o primeiro elemento de conteudo comeca.
    marca = frag.find('<body')
    if marca != -1:
        raise SystemExit('O fragmento ja tem <body>. Conferir o build antes de envolver.')

    corte = frag.find('<div')
    if corte == -1:
        raise SystemExit('Nao achei onde o corpo comeca (<div). Conferir o build.')

    cabeca_frag, corpo = frag[:corte], frag[corte:]

    doc = CABECA + cabeca_frag.rstrip() + u'\n</head>\n<body>\n' + corpo.rstrip() + RODAPE

    pasta = os.path.dirname(DESTINO)
    if not os.path.isdir(pasta):
        os.makedirs(pasta)

    dados = doc.encode('utf-8')          # encoda ANTES de abrir para escrita
    with io.open(DESTINO, 'wb') as f:
        f.write(dados)

    # confere no arquivo, nunca na variavel
    lido = io.open(DESTINO, encoding='utf-8').read()
    assert lido.count('<!DOCTYPE html>') == 1
    assert lido.count('name="robots"') == 1
    assert lido.count('<body>') == 1
    print('escrito: %s' % DESTINO)
    print('  %.2f MB' % (len(dados) / 1048576.0))
    print('  noindex no HTML: ok (o X-Robots-Tag vem do nginx)')


if __name__ == '__main__':
    main()
