# -*- coding: utf-8 -*-
"""Troca a ordem dos capitulos 6 e 7 (cronologia) e escreve o novo capitulo 6, Prinetti."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

# ---------------------------------------------- 1) troca 6 <-> 7 na estrutura
old = u"""  (6,'Sante nos Alpes','A Grande Guerra, as trincheiras, as três medalhas. O ramo que ficou.'),
  (7,'O Decreto Prinetti','1902: a Itália proíbe a emigração subsidiada para o Brasil.'),"""
new = u"""  (6,'O Decreto Prinetti','1902: a Itália proíbe a emigração subsidiada para o Brasil.'),
  (7,'Sante nos Alpes','A Grande Guerra, as trincheiras, as três medalhas. O ramo que ficou.'),"""
assert old in s, 'CAPS 6/7 nao encontrado'
s = s.replace(old, new, 1)

# imagens do Sante acompanham a mudanca de numero
old_img = u""" 6:  [('quadro_guerra_europa','O quadro com as três medalhas de guerra de Sante Forner, concedidas pelo Ministério da Guerra da Itália.'),
      ('sante_militar','Sante Forner, 1893 a 1947, fardado.')],"""
new_img = u""" 7:  [('quadro_guerra_europa','O quadro com as três medalhas de guerra de Sante Forner, concedidas pelo Ministério da Guerra da Itália.'),
      ('sante_militar','Sante Forner, 1893 a 1947, fardado.')],"""
assert old_img in s, 'IMG_BY_CAP 6 nao encontrado'
s = s.replace(old_img, new_img, 1)

# referencias cruzadas dentro do texto ja escrito
s = s.replace(u'Ele é o assunto do capítulo 6.', u'Ele é o assunto do capítulo 7.')
s = s.replace(u'O capítulo 6 deste livro conta a história do irmão dele, Sante',
              u'O capítulo 7 deste livro conta a história do irmão dele, Sante')

# ------------------------------------------------------- 2) capitulo 6 novo
CAP6 = u'''
CAP6 = [
"""Os relatórios começaram a chegar a Roma no fim do século.

Eram documentos consulares, escritos por funcionários italianos espalhados pelo Brasil,
gente cujo trabalho era cuidar dos interesses de cidadãos italianos em território
estrangeiro. Iam por navio, levavam semanas, e caíam numa mesa em Roma onde alguém tinha
que lê-los.

Durante muito tempo ninguém leu com atenção. A emigração era vista como válvula de
escape: gente demais, terra de menos, e um país vizinho de além-mar disposto a receber.
Se estava indo, ótimo.

Até que o conteúdo daqueles relatórios ficou impossível de ignorar.""",

"""O que os cônsules descreviam era o seguinte.

Que os imigrantes italianos nas fazendas de café tinham se tornado, na prática, servos.
Que não havia assistência médica. Que não havia escola para os filhos. Que as casas eram
pequenas e sem as condições mínimas de higiene.

E que havia violência física, inclusive com uso de chicote.

Essa última linha aparece nos documentos que embasaram a decisão italiana. Catorze anos
depois da abolição, num país que tinha acabado de deixar de escravizar pessoas, o
instrumento continuava em uso, agora contra europeus recém-desembarcados.""",

"""O cônsul italiano no Espírito Santo, onde a colonização era intensa, foi específico no
relatório dele.

Reclamou das condições climáticas para as quais ninguém tinha preparado aquela gente. Da
escassez e da má qualidade da comida. Do tratamento dado aos imigrantes pela polícia. Da
incerteza da justiça, quando um colono tentava reclamar alguma coisa. E das falhas na
medição dos terrenos que deveriam ser entregues a cada família.

Esse último item é o mais revelador dos cinco. A promessa central do cartaz era terra. E
o cônsul está dizendo que nem a medição da terra era confiável.""",

"""Uma coisa tinha mudado na Itália e tornou possível que esses papéis produzissem efeito.

Em 31 de janeiro de 1901 o país aprovou a primeira lei geral sobre emigração e criou o
Commissariato Generale dell'Emigrazione, um órgão de Estado com a atribuição de olhar
para aquilo.

Até então a emigração italiana era um fenômeno sem dono dentro do governo. Havia
agências privadas, havia subagentes pagos por cabeça, havia companhias de navegação, e
não havia ninguém encarregado de perguntar o que acontecia com as pessoas depois que o
navio saía.

A partir de 1901 passou a haver.""",

"""Em 26 de março de 1902, o governo italiano baixou o decreto que ficaria conhecido pelo
nome do ministro das Relações Exteriores, Giulio Prinetti.

O decreto proibia a emigração subsidiada para o Brasil.

Ou seja: ficava proibido a um italiano embarcar para o Brasil com a passagem paga por
outra pessoa. Especificamente, com a passagem paga pelo governo brasileiro.""",

"""É essencial entender o que o decreto não fez, porque é aí que mora a inteligência
dele.

Ele não proibiu italianos de irem para o Brasil.

Quem quisesse ir continuava podendo ir. Só teria que comprar a própria passagem, com o
próprio dinheiro, e chegar do outro lado sem dever nada a ninguém.

A Itália não estava impedindo a saída dos seus cidadãos. Estava cortando o mecanismo
financeiro que transformava a viagem em dívida e a dívida em servidão.""",

"""Vale parar aqui, porque este é o capítulo que desmonta uma frase.

Existe uma versão da história da emigração, confortável e muito repetida, em que a
Itália expulsou os pobres. Um país que se livrou da própria miséria empurrando-a para
dentro de um navio.

O Decreto Prinetti é a prova documental de que não é assim tão simples.

Em 1902 o Estado italiano olhou para o que estava acontecendo com os seus nas fazendas
paulistas e fechou a torneira. Tarde, desajeitado e sem resolver a causa, mas fechou. E
fechou contrariando o interesse imediato de um governo que ficaria muito satisfeito de
continuar exportando bocas.""",

"""O efeito foi imediato e foi grande.

A imigração italiana para o Brasil despencou. O fluxo, que não deixou de existir, mudou
de endereço: passou a ir com mais força para a Argentina e para os Estados Unidos, onde
não havia proibição desse tipo.

Para São Paulo, que tinha construído a lavoura de café sobre passagem subvencionada, foi
um problema sério. Foi preciso buscar mão de obra em outros lugares, e é aí que se
intensificam outras correntes migratórias no estado.

O Brasil reagiu com diplomacia e com irritação. Em 1906 ainda havia gestão em curso para
tentar derrubar as restrições italianas. Não conseguiram.""",

"""E agora a parte que interessa diretamente a esta família.

O decreto não parou a emigração vêneta. Nada parou a emigração vêneta.

O que ele fez foi mudar quem podia ir e em que condição. Sem passagem paga, ir para o
Brasil deixou de ser uma coisa que um miserável absoluto conseguia fazer e virou uma
coisa que exigia dinheiro na mão. Juntar economia, vender o que houvesse, pedir a
parente.

A emigração continuou, mas ficou mais lenta, mais familiar e mais deliberada. Menos
levas organizadas, mais gente indo atrás de gente.""",

"""Vinte e quatro anos depois do decreto, Fausto Miotto embarcou.

Não como colono recrutado, não com passagem paga pelo Estado de São Paulo, não dentro de
um contrato assinado antes de sair. Foi por conta própria, primeiro, sozinho, do jeito
que se fazia depois de 1902: alguém vai, se estabelece, e chama.

Depois chamou a mulher.""",

"""E é por isso que Rosa Forner estava no <em>Principessa Mafalda</em>.

Não num navio fretado de imigrantes, não num transporte contratado por fazendeiro. Num
transatlântico comercial de linha regular, que levava primeira, segunda e terceira classe
na mesma viagem, com passageiros que tinham comprado bilhete.

Ela pagou para estar ali.

Junto com a irmã, com quatro sobrinhos e com um filho de um ano.""",

"""Não estou dizendo que uma lei de 1902 causou um naufrágio em 1927. Não causou.

Estou dizendo uma coisa mais estreita e mais verdadeira: uma decisão tomada em Roma,
escrita para proteger camponeses italianos de fazendeiros brasileiros, determinou em que
tipo de embarcação essa família atravessaria o oceano vinte e cinco anos depois.

Se o sistema de passagem subvencionada ainda existisse, Rosa provavelmente teria feito a
travessia em outro navio, em outra data, sob outro contrato.

História é feita disso. Uma canetada em um continente reorganiza a vida de gente que
nunca ouviu falar de quem assinou.""",

"""Há uma última ironia neste capítulo, e ela é silenciosa.

O decreto foi criado porque cônsules italianos denunciaram que seus compatriotas estavam
sendo tratados como escravizados nas fazendas de café.

Ou seja: a Itália sabia. Em 1902, o governo italiano tinha, por escrito, na própria mesa,
a descrição do que esperava um camponês vêneto que desembarcasse em Santos.

E ainda assim, entre 1902 e 1927, centenas de milhares continuaram vindo.

Porque quando a alternativa é a encosta do Grappa com a terra dividida em três, a
polenta três vezes ao dia e o contrato vencendo em novembro, até o relatório do cônsul
soa como uma proposta.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP6.strip() +
              "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 20: CAP20}", 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulos 6 e 7 trocados; capitulo 6 (Prinetti) escrito')

# --------------------------------------------- 3) caderno de bordo: trocar linhas
cb = os.path.join(SP, 'caderno-de-bordo.html')
c = io.open(cb, encoding='utf-8').read()
row6 = u'<div class="row"><span class="n">06</span><span class="t">Sante nos Alpes</span><span class="d">A Grande Guerra, as trincheiras, as três medalhas. O ramo que ficou.</span><span class="pp">15</span><span class="st"><span class="pill p-pronto">Pronto</span></span></div>'
row7 = u'<div class="row"><span class="n">07</span><span class="t">O Decreto Prinetti</span><span class="d">1902: a Itália proíbe a emigração subsidiada para o Brasil. O capítulo que ninguém conta.</span><span class="pp">14</span><span class="st"><span class="pill p-arquivo">Arquivo</span></span></div>'
new6 = u'<div class="row"><span class="n">06</span><span class="t">O Decreto Prinetti</span><span class="d">1902: a Itália proíbe a emigração subsidiada para o Brasil. O capítulo que ninguém conta.</span><span class="pp">14</span><span class="st"><span class="pill p-pronto">Pronto</span></span></div>'
new7 = u'<div class="row"><span class="n">07</span><span class="t">Sante nos Alpes</span><span class="d">A Grande Guerra, as trincheiras, as três medalhas. O ramo que ficou.</span><span class="pp">15</span><span class="st"><span class="pill p-pronto">Pronto</span></span></div>'
if row6 in c and row7 in c:
    c = c.replace(row6, '@@R6@@', 1).replace(row7, new7, 1).replace('@@R6@@', new6, 1)
    io.open(cb, 'w', encoding='utf-8').write(c)
    print('caderno de bordo atualizado')
else:
    print('AVISO: linhas 6/7 do caderno nao batem, revisar manualmente')
