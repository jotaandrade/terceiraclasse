# -*- coding: utf-8 -*-
"""Insere o capitulo 3 e troca a fila de imagens do Livro I por mapa capitulo -> imagens."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

# ---------------------------------------------------------------- capitulo 3
CAP3 = u'''
CAP3 = [
"""No dia 11 de novembro a estrada enchia de carroça.

É o dia de São Martinho, e no campo do norte da Itália era quando venciam os contratos
agrários. Quem tinha sido renovado ficava. Quem não tinha carregava o que cabia,
colchão, panela, imagem de santo, as crianças em cima, e saía procurar outro pedaço de
terra de outro proprietário.

A expressão pegou e sobreviveu à coisa: <em>fare San Martino</em>, em italiano, até hoje
quer dizer mudar de casa.

Uma vez por ano, num único dia, dava para ver na estrada exatamente quantas famílias
tinham perdido o chão.""",

"""Não sei em que condição os Forner e os Miotto trabalhavam a terra.

Podiam ser proprietários de um pedaço, podiam ser meeiros, podiam ser diaristas. Os
documentos que tenho começam tarde demais e não dizem. Vou descrever o sistema, porque o
sistema eu conheço, e deixar claro que não sei em que casa dele essa família morava.

O que dá para afirmar é que ninguém ali era rico. Rico não emigra na terceira classe.""",

"""Havia basicamente três lugares onde se podia estar.

Proprietário de um retalho: dono de faixas espalhadas de encosta, somando às vezes menos
de um hectare, o suficiente para não morrer e não o suficiente para viver.

Meeiro: trabalhava a terra de outro e entregava metade da colheita. Contrato anual,
renovável ou não, com vencimento em São Martinho.

Diarista, o <em>bracciante</em>: não tinha terra nenhuma e vendia o dia. Era o último
degrau, e era para onde os outros dois desciam.

O movimento entre esses três lugares tinha uma direção só.""",

"""A mecânica da queda é sempre a mesma e leva mais ou menos uma década.

Vem um ano ruim: granizo, seca, doença na vinha. A colheita não paga o ano. A família
pede emprestado para atravessar o inverno e comprar semente.

No ano seguinte a colheita paga o ano mas não paga o juro. Pede de novo.

No terceiro ou quarto ano vende uma faixa de terra para quitar. Agora tem menos terra, e
portanto menos colheita, e portanto menos margem para o próximo ano ruim.

Que vem.""",

"""Quem emprestava não era banco. Banco não emprestava a camponês.

Emprestava o proprietário vizinho, o comerciante da vila, o moleiro, o padre às vezes, e
gente que fazia disso profissão. Os juros não estavam em nenhuma tabela. Estavam no que
o credor achasse que dava para cobrar de alguém que não tinha alternativa.

A terra que saía das mãos de uma família ia parar nas mãos de quem já tinha. É assim que
funciona concentração fundiária: não por decreto, por juro.""",

"""E aí, na década de 1880, veio uma pancada que não tinha nada a ver com a Itália.

O trigo americano chegou à Europa.

As pradarias dos Estados Unidos entraram em produção em escala industrial, a ferrovia
levou o grão até os portos e o navio a vapor atravessou o Atlântico em duas semanas em
vez de dois meses. O preço do trigo despencou no continente inteiro.

Para o consumidor urbano foi ótimo. Para o pequeno agricultor europeu, que vendia o
pouco que sobrava para pagar imposto e juro, foi a sentença.""",

"""Repare no que estava acontecendo ao mesmo tempo, porque é uma das ironias mais
perfeitas desta história.

O navio a vapor foi a tecnologia que arruinou o camponês vêneto, porque foi ele que
trouxe o grão barato da América.

E foi a mesma tecnologia, muitas vezes literalmente os mesmos navios, que levou o
camponês vêneto para a América.

O grão vinha de lá para cá. A gente ia daqui para lá. Nos mesmos porões, em direções
opostas.""",

"""O Estado italiano percebeu que havia um problema e fez o que Estados fazem: abriu uma
comissão.

A Inchiesta agraria e sulle condizioni della classe agricola, conduzida por Stefano
Jacini entre 1877 e 1885, foi a maior investigação já feita sobre o campo italiano.
Percorreu o país, ouviu, mediu e publicou.

O que ela concluiu foi desconfortável: a unificação não tinha resolvido as
desigualdades entre as regiões. Tinha acelerado a crise, e cristalizado a desvantagem
de quem já estava atrás.

O relatório é de 1885. A emigração em massa já estava em curso havia dez anos. As
comissões costumam chegar depois.""",

"""Faltava a doença, e a doença tinha nome.

A pelagra começa na pele que pega sol. As costas das mãos ficam vermelhas, depois
escuras, depois rachadas e grossas como couro. É por isso que o nome veio do lombardo
<em>pelle agra</em>, pele áspera.

Depois vem a diarreia, que não passa.

Depois vem a cabeça: confusão, esquecimento, apatia, e em alguns casos alucinação e
delírio. Nos manuais de medicina ela ficou conhecida pelas três palavras que começam com
a mesma letra em inglês: dermatite, diarreia, demência. Havia uma quarta, que os manuais
educados omitem, e que é a morte.""",

"""A causa é falta de niacina, a vitamina B3. E é aqui que a história fica insuportável.

O milho tem niacina. Só que no milho ela vem quimicamente presa, numa forma que o
intestino humano não consegue absorver.

Existe uma solução, e ela é antiga. Os povos da Mesoamérica, que domesticaram o milho ao
longo de milhares de anos, cozinham o grão em água com cal ou com cinza antes de moer. O
processo se chama nixtamalização, e ele quebra a ligação e libera a niacina. Sem isso,
tortilla mataria mexicano. Com isso, alimenta.

Quando os europeus levaram o milho da América para a Europa, no século XVI, levaram a
semente e não levaram a técnica.""",

"""Foi isso que aconteceu com o Vêneto.

Adotaram um cereal do Novo Mundo porque ele rendia mais por hectare do que qualquer
coisa que tivessem, plantaram, moeram e comeram do jeito que se comia trigo. Deu certo
por gerações, enquanto a polenta era uma parte da dieta.

Quando a polenta virou a dieta inteira, porque não sobrava dinheiro para mais nada, a
conta chegou.

As regiões mais atingidas pela pelagra na Itália foram a Lombardia, o Vêneto e a Emilia
Romagna. Em 1878 o governo mandou fazer um levantamento nacional só sobre ela. Chegaram
a existir instituições específicas para internar doentes, os pellagrosari.

Uma população inteira adoeceu de fome comendo, e adoeceu porque tinha atravessado o
Atlântico uma vez, três séculos antes, e trazido metade do conhecimento.""",

"""A pelagra era uma doença de classe, e isso não é figura de linguagem.

Ninguém que comesse carne, ovo, leite ou pão de trigo com alguma regularidade
desenvolvia pelagra. Nenhum proprietário. Nenhum comerciante. Nenhum padre.

Dava em quem comia polenta e mais nada, e quem comia polenta e mais nada era o camponês
que entregava metade da colheita e o diarista que não tinha colheita nenhuma.

Dava para olhar as mãos de uma pessoa na feira e saber em que degrau ela estava.""",

"""Junte as peças e você tem o ano de uma família na encosta do Grappa por volta de 1890.

A terra é pouca porque foi dividida entre irmãos, e é de outro, ou é metade de outro.
Vende-se o excedente por um preço que o trigo americano derrubou. Paga-se imposto sobre
o que se mói e manda-se um filho para o exército. Pega-se emprestado no inverno com juro
que ninguém regula. Come-se polenta três vezes ao dia e por isso as mãos racham.

E em 11 de novembro descobre-se se o contrato foi renovado.""",

"""Não é uma história de vilão. É uma história de engrenagem.

Não houve um decreto expulsando ninguém, não houve exército queimando aldeia, não houve
perseguição. Houve uma soma de coisas razoáveis do ponto de vista de quem as decidia,
que juntas tornaram impossível continuar.

Foi por isso que quando os cartazes começaram a aparecer nas praças, prometendo terra do
outro lado do mar, eles não precisaram convencer ninguém.

Só precisaram avisar que existia saída.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 2: CAP2, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP3.strip() + "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 20: CAP20}", 1)

# ------------------------------------------ imagens: fila -> mapa por capitulo
old_block = s[s.index("IMGS_BY_BOOK = {"):s.index("for bn, btitle, byears, bcolor in BOOKS:")]
new_block = u'''IMG_BY_CAP = {
 1:  [('castellcuco','Os vales de Castelcucco, província de Treviso. Fausto Miotto nasceu aqui em 1904.')],
 2:  [('italia_campo_verde','O campo vêneto. A paisagem que trocou de país duas vezes sem sair do lugar.')],
 3:  [('familia_italiana','Família camponesa italiana no início do século XX.')],
 4:  [('arovore_genealogica','A árvore genealógica reconstruída das famílias Miotto e Forner.')],
 5:  [('cartaz','Cartaz de agenciamento de imigrantes para o Brasil.'),
      ('propaganda_para_italianos_virem_ao_brasil_1024x580','Propaganda para atrair italianos ao Brasil.')],
 6:  [('quadro_guerra_europa','O quadro com as três medalhas de guerra de Sante Forner, concedidas pelo Ministério da Guerra da Itália.'),
      ('sante_militar','Sante Forner, 1893 a 1947, fardado.')],
 9:  [('italianos_no_barco','Imigrantes italianos a bordo, início do século XX.')],
 10: [('imigrantes_italianos_na_hospedaria_dos_imigrantes_em_são_paulo_cerca_de_1890','Imigrantes italianos na Hospedaria dos Imigrantes, São Paulo, por volta de 1890.')],
 16: [('vapor_mafalda','O vapor Principessa Mafalda. Lançado em 1908, afundou em 25 de outubro de 1927.')],
 17: [('princess_mafalda_of_savoy','A princesa Mafalda de Saboia, que deu nome ao navio. Morreu em Buchenwald, em 1944.')],
 21: [('mafalda_naufragando','O naufrágio do Principessa Mafalda em representação de época.')],
 24: [('passageiros_agnoli','Lista de passageiros: a família Agnoli, terceira classe, resgatada pelo navio Alhena.')],
 26: [('rosa_forner','Rosa Forner Miotto, 1903 a 1986. Sobreviveu ao naufrágio aos vinte e quatro anos.'),
      ('rosa_forner_documento','Documento de identificação de Rosa Forner Miotto.')],
 27: [('maria_lugia_forner','Maria Luigia Forner, 1896 a 1992, irmã de Rosa.'),
      ('forner_maria_luigia_col_marito_dei_agnoli_angelo','Maria Luigia Forner e o marido, Angelo dei Agnoli.')],
 29: [('enrico','Enrico Miotto, 1926 a 1998. Tinha um ano e quinze dias na noite do naufrágio.'),
      ('enrico_registro_de_estrangeiro','Registro de Estrangeiros de Enrico Miotto, 29 de dezembro de 1949. Data de nascimento: 10.10.1926.')],
 30: [('mafalda_miotto_forner','Mafalda Miotto Terra, nascida em 1937, dez anos depois do naufrágio, com o nome do navio.')],
 32: [('sante_e_familia','Sante Forner e família, na Itália.'),
      ('giorgio_e_sua_familia','Giorgio Forner e família, o ramo que permaneceu no Vêneto.')],
}

'''
s = s.replace(old_block, new_block, 1)

old_loop = """    imgs = list(IMGS_BY_BOOK.get(bn, []))
    for (num, ctitle, synop) in CAPS[bn]:"""
new_loop = """    for (num, ctitle, synop) in CAPS[bn]:"""
assert old_loop in s, 'loop imgs nao encontrado'
s = s.replace(old_loop, new_loop, 1)

old_tail = """        if imgs and (txt or not txt):
            k, cap = imgs.pop(0)
            P(t='img', key=k, cap=cap, book=bn)
    for k, cap in imgs:
        P(t='img', key=k, cap=cap, book=bn)"""
new_tail = """        for k, cap in IMG_BY_CAP.get(num, []):
            P(t='img', key=k, cap=cap, book=bn)"""
assert old_tail in s, 'tail imgs nao encontrado'
s = s.replace(old_tail, new_tail, 1)

io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 3 inserido; imagens mapeadas por capitulo')
