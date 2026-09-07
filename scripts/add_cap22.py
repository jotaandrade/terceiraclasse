# -*- coding: utf-8 -*-
"""Capitulo 22 — Os botes."""
import io

SRC = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad\build_livro.py"
s = io.open(SRC, encoding='utf-8').read()

CAP22 = u'''CAP22 = [
"""Lendo os vinte depoimentos em sequência, uma coisa aparece que nenhum deles diz sozinho.

<strong>O que matou naquela noite não foi a água.</strong>

Quase ninguém morreu por ter caído no mar e não saber nadar. Morreu por ter entrado num
bote.""",

"""<strong>Ali Hassen</strong>, árabe de quarenta e cinco anos, viajando com três primos,
subiu ao convés e se atirou num bote junto com cerca de cinquenta pessoas. Pelo peso, o
bote afundou.

<strong>Salvador Malone</strong> conseguiu lugar no terceiro bote lançado. A poucos metros
do navio, ele virou.

<strong>Antonio Ponce</strong> entrou num com pelo menos trinta pessoas. A vinte metros do
<em>Alhena</em>, o nervosismo de um dos companheiros fez o bote emborcar.

<strong>Valeriano Galli</strong>, como boa parte da terceira classe, foi dos primeiros a
entrar. O bote cedeu sob o peso e ele foi parar na água.""",

"""<strong>Maria Spinelli</strong> tinha ao lado a amiga Teresa Forggia e o filho dela,
Mario, de três anos.

Um tripulante as obrigou a descer e entrar num bote. Elas entraram.

E então, <strong>a trinta centímetros da água</strong>, as cordas de um dos lados
arrebentaram.

Trinta centímetros. Foi essa a margem.""",

"""<strong>Vincenzo Mandolezzi</strong> esperou uma hora e meia a bordo antes de se jogar.
Nadou até alcançar um dos botes do próprio Mafalda.

Estava furado, ou rachado, ou de alguma forma inservível — ele diz apenas que não estava em
bom estado.

Eram nove pessoas dentro. Remaram com as mãos.""",

"""As razões se acumulam e nenhuma delas é misteriosa.

Botes velhos num navio velho. Superlotação, porque todo mundo queria o mesmo lugar ao mesmo
tempo. Lançamento feito às pressas, no escuro, por gente que nunca tinha feito aquilo de
verdade — o único exercício foi na véspera, ao meio-dia, e era exercício de incêndio.

E o adernamento.

Um navio inclinado tem um lado bom e um lado inútil. De um deles os botes descem raspando o
casco. Do outro, ficam pendurados longe demais para alguém alcançar.

Metade dos botes daquele navio já não servia antes de qualquer pessoa entrar neles.""",

"""E aí a quilha virou o lugar mais seguro do Atlântico.

<strong>Alfio Sanfilippo</strong> se atirou na água às seis da tarde com o irmão e um
oficial do Mafalda. Quase todos os botes já tinham virado. Os três se agarraram ao casco de
um deles, de barriga para cima.

Ficaram ali <strong>oito horas</strong>, até o <em>Empire Star</em> se aproximar.

<strong>Domenico Leo</strong> passou a noite do mesmo jeito, na quilha de outro bote, com
sete ou oito pessoas.""",

"""E agora eu preciso avisar o leitor de uma coisa.

O que vem a seguir são três versões da mesma meia hora, contadas por três pessoas que
estavam naquele navio.

Elas não se completam. Elas se contradizem.

E o que separa uma da outra não é honestidade. É o convés em que cada uma dormia.""",

"""<strong>A família Vacelli viajava na primeira classe.</strong> O casal e três filhos, de
quinze, treze e dez anos. Esperaram a noite inteira na popa e foram recolhidos às nove e
meia.

A versão deles:

<em>Centenas de passageiros da terceira classe foram tomados de tal pânico que se tornaram
animais selvagens, perdendo o juízo. Avançaram desesperadamente como uma massa aterrorizada
sobre os botes, muitos deles portando facas que seguramente, em mais de um caso, foram
usadas contra outros passageiros.</em>

E concluem: aquilo obrigou os passageiros de primeira e segunda classe a permanecerem
paralisados, assistindo à luta terrível que se desenrolava diante deles.""",

"""<strong>Mario Ottaviani, vinte e três anos, viajava na segunda classe</strong>, a
negócios, e sabia nadar.

A versão dele:

<em>Os passageiros da terceira classe e a tripulação foram os responsáveis por transformar a
situação em anarquia. Cometeram atos impróprios de gente civilizada. Empurraram-se para
dentro dos botes e tomaram posse deles pela violência, sem pensar nas mulheres e nas
crianças que clamavam por ajuda.</em>""",

"""<strong>Nicola Lynose, iugoslavo, viajava na terceira classe.</strong>

A versão dele:

Ao primeiro estalo, correram todos ao depósito para pegar os coletes salva-vidas. Quando
voltaram ao convés com os coletes na mão, encontraram <strong>a tripulação em frenesi,
jogando-se dentro dos botes que já se afastavam do navio</strong>.

<em>Só então</em> os imigrantes, cegos de medo, derrubaram três botes no mar e se atiraram
neles de um jeito tão desordenado que os três viraram.

Na versão de Lynose, a terceira classe não começou o pânico. Reagiu a ele.""",

"""Eu não vou escolher entre as três.

E preciso dizer por quê, porque a essa altura já ficou claro de que lado eu venho.

<strong>Sou bisneto de duas mulheres que viajavam na terceira classe daquele navio.</strong>
Se eu arbitrasse essa disputa, estaria arbitrando em causa própria, e o leitor teria todo o
direito de descontar o que eu dissesse.

Então não arbitro. Ponho as três lado a lado e deixo à vista o que elas têm em comum: cada
depoente descreve com precisão o que aconteceu perto dele, e com fúria o que aconteceu do
outro lado do navio, onde não estava.

Um homem da primeira classe viu a terceira invadir os botes. Um homem da terceira viu a
tripulação já dentro deles. As duas coisas provavelmente aconteceram, com meia hora de
diferença, em pontos distintos de um convés no escuro.""",

"""Há uma coisa, porém, em que os três lados concordam.

Parte da tripulação ficou.

Os Vacelli, que são os mais duros com a terceira classe, fazem questão de registrar o
comportamento nobre do <strong>primeiro oficial</strong> e do <strong>primeiro
maquinista</strong>, que segundo eles fizeram esforços inauditos para salvar passageiros.

E <strong>Pedro Volpi</strong> deve a vida a um deles. Depois de se jogar na água, foi
ajudado pelo <strong>terceiro maquinista do Mafalda</strong>, que nadou com ele até um bote.

Volpi acrescenta uma linha que vale o capítulo inteiro: o homem que o salvou, depois de
deixá-lo em segurança, voltou. E salvou outros dois.""",

"""E o herói mais citado daquela noite não era da tripulação.

Era um passageiro: <strong>Juan Santororo</strong>, cadete naval argentino.

Galli, que é o mais crítico de todos em relação aos oficiais do Mafalda, faz questão de
contrastar: enquanto a tripulação fazia o que fazia, havia um passageiro salvando gente na
água.

Santororo só descobriu quem era o homem que ele tinha visto trabalhando no escuro quando
chegou ao porto e viu a multidão carregá-lo nos ombros.""",

"""Na água, o perigo deixou de ser o navio.

<strong>Lynose nadou das sete da noite às dez e meia.</strong> E o que ele conta desse
percurso não é sobre ondas.

<em>A luta mais intensa não foi com as ondas, mas com os passageiros boiando que, não
sabendo nadar, se agarravam a quem estivesse ao lado, soltando gritos desesperados. Ouviam-
se pragas em todas as línguas. Para avançar era preciso se afastar dos outros, que formavam
uma barreira humana.</em>

<strong>Batista Beria</strong> descreve o mesmo mecanismo: quem não sabia nadar direito se
agarrava à roupa de quem estava na frente.

Uma pessoa se afogando não é uma pessoa pedindo ajuda. É uma pessoa que puxa para baixo
quem chega perto.""",

"""E os tubarões.

É a parte mais famosa deste naufrágio, a que aparece em toda reportagem, e é a que menos
resiste a um exame.

<strong>Gabassi</strong> diz que uma mulher e uma criança foram levadas por um tubarão
enorme, na tábua em que ele boiava. <strong>Ponce</strong> viu dois. <strong>Galli</strong>
viu vários, e diz que um feriu um companheiro que morreu depois de içado.
<strong>Malone</strong> não viu tubarão nenhum, mas viu um homem boiando com a perna
destruída.

<strong>Volpi</strong> não viu — e acrescenta: <em>a noite estava muito escura</em>.
<strong>Sanfilippo</strong> não viu, e diz outra coisa no lugar: viu o corpo de uma mulher
boiando agarrada a um bebê. <strong>Beria</strong>, <strong>Uccelli</strong> e
<strong>Solk</strong> também não viram.

E <strong>Domenico Leo</strong> resume a dificuldade toda numa frase: <em>não sei se era um
tubarão, mas era um peixe enorme.</em>""",

"""<strong>Pascual Pecci</strong>, o único cético do grupo, foi mais longe.

Duvidou que houvesse tubarão nenhum. Atribuiu a história a peixes que vinham sendo vistos
seguindo o navio nos dias anteriores, e que ninguém a bordo sabia identificar.

Achava, mais amplamente, que muitos dos relatos dramáticos daquela noite eram invenção de
quem quis criar drama onde não havia. Sobre a própria fuga com a mulher e a filha, disse que
tinha sido tão dramática quanto <em>um dia no Tigre</em>, que é um balneário de fim de
semana perto de Buenos Aires.

Nem ele nem os outros têm como provar o que dizem. Estava escuro, e eles estavam com medo.

O que este livro pode fazer é não decidir por eles.""",

"""De todos os botes que aparecem nestes vinte relatos, quase nenhum chegou inteiro do outro
lado.

Afundaram pelo peso, viraram a poucos metros do casco, cederam, arrebentaram nas cordas,
ficaram pendurados no lado errado do navio, ou chegaram furados e foram remados com as mãos.

<strong>O que segurou foi o dos cozinheiros.</strong>""",
]

'''

anchor = u'CAP19 = ['
assert anchor in s and s.count(anchor) == 1
s = s.replace(anchor, CAP22 + anchor, 1)

old = u'20: CAP20, 21: CAP21}'
new = u'20: CAP20, 21: CAP21, 22: CAP22}'
assert old in s
s = s.replace(old, new, 1)

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('CAP22 inserido')
