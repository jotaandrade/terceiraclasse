# -*- coding: utf-8 -*-
"""Capitulo 9 — Genova. E corrige o aniversario do Enrico no cap. 20."""
import io

SRC = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad\build_livro.py"
s = io.open(SRC, encoding='utf-8').read()

CAP9 = u'''CAP9 = [
"""Gênova, em 1927, tinha mais gente dentro dela do que todas as vilas do sopé do Grappa
somadas.

Rosa Forner nunca tinha visto uma cidade. Nem a irmã. As duas conheciam Asolo, que tem uma
praça e uma rua principal, conheciam Treviso de passagem, e nada mais.

E não foram a Gênova para conhecer Gênova. Ninguém ia. A cidade não era destino, era
funil: o lugar por onde a Itália vinha escoando a própria gente havia sessenta anos.""",

"""Em algum momento daquela chegada, elas viram o mar.

Não sei em que momento nem de onde. Sei que era a primeira vez, para as duas e para as
cinco crianças.

É uma coisa difícil de imaginar hoje: uma mulher de trinta e um anos vendo o mar pela
primeira vez.

Quem cresce no sopé de uma montanha tem o horizonte a dois quilômetros de distância, e
sempre teve. O horizonte é uma encosta, e atrás dela vem outra.

Gênova é a primeira vez em que aquela gente olha para a frente e não encontra nada.""",

"""E ali, encostado no cais, está o navio.

O <em>Principessa Mafalda</em> tinha dezenove anos e nove mil duzentas e dez toneladas.

Tonelagem não diz nada a ninguém. Isto diz: naquela viagem ele levou mil duzentas e
cinquenta e nove pessoas. Castelcucco inteira, com os seus mil setecentos e vinte e nove
habitantes, quase cabia lá dentro.

Era, com folga, a maior coisa construída que qualquer uma daquelas pessoas tinha visto na
vida.

E não era navio novo, nem bonito, nem orgulho de ninguém. Era um transatlântico velho de
linha regular, no fim da carreira, fazendo o trajeto que sobra para os navios velhos.""",

"""Quem subiu aquela prancha junto com elas?

É uma pergunta que quase nunca tem resposta. Nesta história tem, e por um motivo ruim:
catorze dias depois, cinquenta daquelas pessoas seriam recolhidas do mar e desembarcadas no
Rio de Janeiro, e um funcionário da Intendência de Imigração sentou e escreveu os nomes
numa lista.

Todos com a mesma anotação na coluna do embarque: <strong>Genova, 3ª</strong>.""",

"""<strong>Beck Josef</strong>, iugoslavo, cinquenta e três anos, agricultor, com a mulher
Anna, o filho Ivan de vinte e três e a filha Elizabeth de dezesseis. Iam para São Paulo.

<strong>Bán Sándor</strong>, húngaro, vinte e nove anos, israelita, sozinho.

Os irmãos <strong>Ströbel</strong>, Ernö e Gottfried, vinte e seis e vinte e cinco anos.

<strong>Ruspollo Eugenio</strong>, quarenta e dois, agricultor, com a mulher Maria e quatro
filhos: Giselda de catorze, Serafina de treze, Paulo de onze e Maria-Luisa de dois.

<strong>Zaninni Oliviano</strong>, cinquenta e seis anos, e a mulher <strong>Zaira</strong>,
cinquenta e oito. Os mais velhos da lista.

<strong>Dattoma Cosimo</strong>, dezoito anos, sapateiro.""",

"""E os Pettina.

Ottavio, vinte e cinco anos. A mulher, também chamada Rosa, vinte e cinco. A filha Ottavia,
de dois.

E a segunda filha, Maria, cuja idade a lista registra assim:

<strong>3/12</strong>

Três doze avos de um ano. Três meses.

Alguém subiu aquela prancha em Gênova, em outubro de 1927, carregando no colo um bebê de
três meses de idade.""",

"""E subiram duas mulheres que importam mais do que todas as outras desta lista.

<strong>Luchini Teresa, dezenove anos.</strong>

<strong>De Rosi Emilia, cinquenta e cinco.</strong>

Na relação do Rio de Janeiro elas aparecem uma seguida da outra, sozinhas, sem parentesco
declarado, e as duas com um <em>x</em> marcado à margem.

No pé da mesma folha, escrito à mão pelo funcionário que fechou o documento, está o
motivo:

<em>As passageiras constantes sob Nº 24 e 25 perderam seus maridos, e pedem de ser enviadas
para Italia.</em>""",

"""Em Gênova, em 11 de outubro, elas não eram isso.

Eram duas mulheres casadas subindo uma prancha com os maridos do lado, indo começar outra
vida.

Uma delas tinha dezenove anos.

Dezessete dias depois estava pedindo para voltar para o lugar de onde tinha acabado de
sair.""",

"""Repare na composição daquela lista.

Iugoslavos, húngaros, italianos do norte, italianos do sul, um israelita, um sapateiro de
dezoito anos, um casal de quase sessenta, lavradores, um carpinteiro, um carvoeiro.

<strong>A terceira classe não era um lugar. Era uma tarifa.</strong>

O que aquelas pessoas tinham em comum não era país, nem língua, nem religião, nem ofício.
Era o preço do bilhete.

Quinze anos antes aquele porão teria sido quase todo italiano. Em 1927 já não era. Nas duas
semanas seguintes, aquela gente ia dividir o mesmo espaço sem partilhar uma língua.""",

"""E no meio disso, sete pessoas de uma família só.

<strong>Forner Rosa</strong>, vinte e quatro anos, com <strong>Enrico</strong>, de um.

<strong>Forner Maria</strong>, trinta e um anos, com <strong>Ginneta</strong>, de sete,
<strong>Pulgheria</strong>, de seis, <strong>Rino</strong>, de quatro, e
<strong>Danilo</strong>, de dois.

Duas mulheres e cinco crianças. A mais velha delas tinha sete anos.

Nenhum homem adulto no grupo.""",

"""O navio saiu de Gênova em <strong>11 de outubro de 1927</strong>.

Um dia antes, em 10 de outubro, Enrico Miotto tinha completado um ano de idade.

Fez um ano em Gênova, esperando embarcar, e não existe registro nenhum de que alguém tenha
comemorado.""",

"""O capítulo anterior termina dizendo que a última coisa que aquelas duas mulheres viram do
lugar onde nasceram foi o Monte Grappa.

É verdade, e agora dá para completar.

A última coisa que elas viram da <em>Itália</em> não foi o Grappa. O Grappa fica a
trezentos quilômetros de Gênova.

Foi uma cidade portuária que elas conheciam havia poucos dias, cheia de gente falando um
dialeto que elas não entendiam, vista de longe, do convés de um navio velho.

Ninguém se despede de uma pátria. Despede-se de um lugar. E o lugar delas tinha ficado para
trás dias antes, numa estrada que descia para Asolo.""",

"""Do cais, o que se via era um navio grande saindo devagar.

Mil duzentas e cinquenta e nove pessoas a bordo, a maior parte delas no porão. Catorze dias
de mar até o Rio de Janeiro.

Trezentas e catorze não chegariam.""",
]

'''

anchor = u'CAP19 = ['
assert anchor in s and s.count(anchor) == 1
s = s.replace(anchor, CAP9 + anchor, 1)

old = u'CHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 8: CAP8, 19: CAP19, 20: CAP20}'
new = u'CHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 8: CAP8, 9: CAP9, 19: CAP19, 20: CAP20}'
assert old in s
s = s.replace(old, new, 1)

# --- corrige o aniversario do Enrico no cap. 20 ----------------------
a = u'''Rosa Forner tinha vinte e quatro anos e um filho de um ano. Enrico havia
completado o primeiro aniversário quinze dias antes, ainda em alto-mar, e não
existe registro nenhum de que alguém tenha comemorado.'''
b = u'''Rosa Forner tinha vinte e quatro anos e um filho de um ano. Enrico tinha
feito um ano em Gênova, na véspera do embarque.'''
assert a in s, 'NAO ACHOU o trecho do cap 20'
s = s.replace(a, b, 1)

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('CAP9 inserido; aniversario do Enrico corrigido no cap. 20')
