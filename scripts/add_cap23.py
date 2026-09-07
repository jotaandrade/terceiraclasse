# -*- coding: utf-8 -*-
"""Cap. 23 — 22h10. E ajusta um desequilibrio no cap. 22."""
import io

SRC = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad\build_livro.py"
s = io.open(SRC, encoding='utf-8').read()

# --- cap 22: so a versao da terceira classe ganhava um resumo favoravel ----
a = u'''<em>Só então</em> os imigrantes, cegos de medo, derrubaram três botes no mar e se atiraram
neles de um jeito tão desordenado que os três viraram.

Na versão de Lynose, a terceira classe não começou o pânico. Reagiu a ele.""",'''
b = u'''<em>Só então</em> os imigrantes, cegos de medo, derrubaram três botes no mar e se atiraram
neles de um jeito tão desordenado que os três viraram.""",'''
assert a in s, 'NAO ACHOU o resumo do Lynose'
s = s.replace(a, b, 1)
print('  ok  cap 22: sai o resumo que favorecia uma das tres versoes')

CAP23 = u'''CAP23 = [
"""Às dez e três da noite, o navio apagou.

Não foi um apagão como o de uma casa. Um transatlântico sem energia perde a luz, perde as
bombas, perde o rádio. Em poucos segundos deixa de ser uma máquina e passa a ser um objeto
grande boiando torto.

A partir daquele minuto, a única luz sobre aquela água veio dos holofotes dos navios que já
tinham chegado.

E holofote ilumina um círculo. O resto continua preto.""",

"""Entre a luz apagar e o navio sumir passaram-se <strong>sete minutos</strong>.""",

"""Pouco antes disso, <strong>Mario Ottaviani</strong> olhou em volta antes de se jogar, e
contou.

Ainda havia nos conveses cerca de <strong>sessenta mulheres e crianças</strong>, e cerca de
<strong>duzentos homens</strong>.

Duzentas e sessenta pessoas, a sete minutos do fim, num navio já deitado.""",

"""<strong>Enrico Nazzeconi</strong> ficou até dez para as dez.

Quando a inclinação a estibordo chegou ao que ele chamou de estado extremo, correu para a
popa. A água já estava pelos joelhos dele, no convés.

Então se jogou.""",

"""E foi da água que ele ouviu.

Três apitos longos, um atrás do outro.

E depois um estrondo que ele não conseguiu descrever de outro jeito senão como estrondo.""",

"""E não viu nada.

Nazzeconi estava a poucas dezenas de metros do casco e diz, com todas as letras, que
<strong>não conseguiu ver o navio afundar</strong>. Estava escuro demais.

A família Vacelli, já a bordo do <em>Empire Star</em>, também não viu. Mal tinham chegado,
olharam para trás, e o Mafalda não estava mais lá.

Um navio de nove mil toneladas desapareceu do Atlântico, e quase ninguém que estava a
duzentos metros dele viu aquilo acontecer.""",

"""O que se sentiu foi a água.

<strong>Andres Scavani del Vicario</strong> tinha se soltado de uma corda pouco antes, junto
com o fotógrafo de bordo, com quem tinha feito amizade durante a viagem. Quando o navio
afundou de vez, o redemoinho da descida arrastou os dois para longe.

Foi o que os salvou. A sucção os empurrou na direção do <em>Formosa</em>, e três horas
depois a tripulação francesa ouviu os gritos deles e os pescou.

O navio, ao afundar, moveu quem estava na água. Alguns para longe da ajuda, outros para
perto dela. Ninguém escolheu.""",

"""E o comandante ficou.

Nisso os vinte depoimentos concordam, e é a única coisa daquela noite sobre a qual eles não
brigam.

Não há um único relato, entre todos os que li, de alguém que tenha visto Simone Gulì tentar
sair daquele navio. Passageiros de primeira, de segunda e de terceira classe; italianos,
árabes e iugoslavos; gente que discorda de tudo o mais, concorda nisso.

Ele estava na ponte quando o navio afundou.""",

"""<strong>Como ele morreu é outra história, e tem duas versões.</strong>

<strong>Salvador Malone</strong>, já içado a bordo do <em>Alhena</em>, diz que assistiu ao
fim de longe e que viu o comandante na ponte, se despedindo com um <em>Viva Italia</em>.

<strong>Eugenio Gabassi</strong>, ainda na água, conta outra coisa: ouviu tiros vindos da
ponte, onde estavam o comandante e o primeiro maquinista, e concluiu que os dois tinham se
matado.""",

"""As duas testemunhas estavam na água, no escuro, a distâncias que nenhuma delas soube
precisar.

Uma interpretou uma silhueta. A outra interpretou um som.

Nenhuma das duas está mentindo, e nenhuma das duas tinha como ter certeza. Aquela noite não
ofereceu certeza a ninguém que estivesse dentro dela.""",

"""Então fica o que dá para dizer.

Simone Gulì levou o <em>Principessa Mafalda</em> de Gênova até quase dezoito graus de
latitude sul. Passou as últimas horas mandando dizer aos passageiros que o navio aguentaria
até o dia seguinte.

Não aguentou. E não há como saber se ele acreditava naquilo, se estava errado nas contas, ou
se estava apenas tentando conter um pânico que veio de qualquer maneira.

O que se sabe é que ele ficou.

<strong>O navio afundou às dez e dez da noite de 25 de outubro de 1927, com o comandante a
bordo.</strong>""",

"""Às dez e onze, aquele ponto do Atlântico era um campo de gente boiando.

Homens agarrados à quilha de botes virados. Mulheres em tábuas. Crianças dentro de coletes
grandes demais para elas. E centenas de pessoas que não sabiam nadar tentando se segurar em
quem sabia.

E, a alguns quilômetros dali, com os holofotes acesos, os navios vindo no escuro.""",
]

'''

anchor = u'CAP19 = ['
assert anchor in s and s.count(anchor) == 1
s = s.replace(anchor, CAP23 + anchor, 1)

old = u'21: CAP21, 22: CAP22}'
new = u'21: CAP21, 22: CAP22, 23: CAP23}'
assert old in s
s = s.replace(old, new, 1)

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('  ok  CAP23 inserido')
