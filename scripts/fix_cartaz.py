# -*- coding: utf-8 -*-
"""Cap. 5: o cartaz de verdade. Substitui a imagem e reescreve a abertura."""
import io, os
from PIL import Image

SP = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad"
SRC = os.path.join(SP, 'build_livro.py')
JPG = r"D:\italiaminha\Familia Miotto\Fotos Familiares\Panfleto Oficial da Imigração da Italia para o Brasil.jpg"
OUT = os.path.join(SP, 'img', 'panfleto_in_america.webp')

# --- imagem ----------------------------------------------------------
im = Image.open(JPG).convert('RGB')
w, h = im.size
if h > 1800:
    im = im.resize((int(w * 1800.0 / h), 1800), Image.LANCZOS)
im.save(OUT, 'WEBP', quality=88, method=6)
print('imagem:', OUT, im.size, '%.0f KB' % (os.path.getsize(OUT) / 1024.0))

s = io.open(SRC, encoding='utf-8').read()
n = [0]


def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
    s = s.replace(old, new, 1)
    n[0] += 1
    print('  ok  ' + label)


# --- abertura reescrita ----------------------------------------------
sub(u'''"""O cartaz era colorido, e isso por si só já era um acontecimento.

Numa praça de vila onde tudo era da cor da pedra, da terra e da roupa lavada demais,
alguém pregava um papel com azul, verde e amarelo, um desenho de campo aberto, e letra
grande.

Não adiantava ser letra grande, porque metade das pessoas não lia. Então alguém lia em
voz alta, e a notícia andava do jeito que notícia andava: na feira, na saída da missa, no
moinho enquanto se esperava a vez.

Existe um desses cartazes no acervo desta família. Sobreviveu a um oceano e a cem
anos.""",

"""O que estava escrito neles variava pouco.

Terra para cultivar. Salário. Casa para a família. Passagem paga.

Quatro promessas, e as quatro respondiam exatamente às quatro coisas que faltavam na
encosta do Grappa. Isso não é coincidência. Quem escreveu aquele texto sabia muito bem
com quem estava falando.

O que o cartaz não dizia é quem estava pagando, e por quê.""",''',
u'''"""O cartaz não era colorido.

Tinta preta sobre papel barato, hoje amarelado nas bordas e vincado no lugar onde alguém
o dobrou para guardar. O que chamava atenção não era cor nenhuma. Era a letra do alto:
gótica, cheia de volutas, do tamanho de meia folha, do tipo que se usava em cartaz de
circo e em capa de missal.

Duas palavras, com uma reticência antes, como quem completa uma frase que a pessoa já
vinha pensando sozinha havia meses:

<strong>… In América.</strong>

Existe um desses no acervo desta família. Sobreviveu a um oceano e a cem anos.""",

"""Embaixo do título, numa faixa desenhada como um pergaminho que se desenrola:

<strong>Terre in Brasile per gli Italiani.</strong>

Terras no Brasil para os italianos. E logo abaixo, em letra miúda e reta, a parte
prática:

<em>Navi in partenza tutte le settimane dal Porto di Genova.</em>

Navios partindo toda semana do porto de Gênova.""",

"""No meio da folha, ocupando metade dela, não há campo, não há plantação, não há casa.

Há um navio.

Uma gravura de vapor misto, com mastros, velas e uma chaminé soltando fumaça, saindo do
porto com a bandeira içada e um farol pequeno ao fundo.

Repare no que isso quer dizer. <strong>O cartaz não vende o Brasil. Vende a
travessia.</strong> A imagem que aquela gente levava para casa depois de olhar o papel na
praça não era a de uma terra. Era a de um navio saindo.""",

"""Mais abaixo, duas linhas:

<em>Venite a construire i vostri sogni con la famiglia.</em>

Venham construir os seus sonhos com a família.

E no rodapé, onde ficam as promessas de verdade:

<em>Un paese di opportunità. Clima tropicale, vito in abbondanza. Ricchezze minerali. In
Brasile putete havere il vostro castello. Il governo dá terre ed utensili a tutti.</em>""",

"""Um país de oportunidades. Clima tropical, comida em abundância. Riquezas minerais. No
Brasil vocês podem ter o seu castelo. O governo dá terra e ferramenta a todo mundo.

Cinco promessas, e as cinco respondiam exatamente às cinco coisas que faltavam na encosta
do Grappa.

Isso não é coincidência. Quem escreveu aquele texto sabia muito bem com quem estava
falando.""",

"""E quem escreveu aquele texto não sabia escrever italiano.

<em>Construire</em>, com um <em>n</em> que não existe em <em>costruire</em>.
<em>Putete havere</em>, no lugar de <em>potete avere</em>, com um <em>h</em> que o
italiano tinha largado havia séculos. <em>Vito</em> onde deveria estar <em>vitto</em>, que
é comida.

Não é falha da minha leitura. Está impresso. Alguém compôs aquele tipo letra por letra,
alguém mandou rodar, e ninguém corrigiu.

Não sei quem imprimiu esse cartaz. Sei que não era gente para quem o italiano fosse língua
de trabalho, e que ninguém no caminho achou que valesse a pena revisar — porque o público
alvo, na praça da vila, em boa parte não sabia ler.""",

"""Era por isso que alguém lia em voz alta.

E a notícia andava do jeito que notícia andava: na feira, na saída da missa, no moinho
enquanto se esperava a vez.

O que o cartaz não dizia é quem estava pagando, e por quê.""",''',
 'cap 5 · a abertura com o cartaz verdadeiro')

# --- o castelo do rodape volta no trecho do que o cartaz omitia -------
sub(u'''Não dizia que a casa prometida podia ser um barracão, e que a terra para cultivar podia
ser um pedaço para plantar feijão nas horas em que não se estivesse no cafezal.''',
u'''Não dizia que o castelo do rodapé podia ser um barracão de colônia, e que a terra para
cultivar podia ser um pedaço para plantar feijão nas horas em que não se estivesse no
cafezal.''',
 'cap 5 · o castelo vira barracao')

# --- imagem do capitulo ----------------------------------------------
sub(u""" 5:  [('cartaz','Cartaz de agenciamento de imigrantes para o Brasil.'),""",
    u""" 5:  [('panfleto_in_america','O panfleto, no acervo da família. \u201c…In América. Terre in Brasile per gli Italiani.\u201d Preto sobre papel barato, com o italiano cheio de erros de composição e um navio no lugar onde deveria estar a terra prometida.'),""",
 'cap 5 · imagem correta')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes' % n[0])
