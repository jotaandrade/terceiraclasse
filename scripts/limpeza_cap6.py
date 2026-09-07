# -*- coding: utf-8 -*-
"""Limpeza do cap. 6: sai a autocorreção do fecho. Os dois terços iniciais ficam intactos."""
import io

SRC = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad\build_livro.py"
s = io.open(SRC, encoding='utf-8').read()
n = [0]


def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
    s = s.replace(old, new, 1)
    n[0] += 1
    print('  ok  ' + label)


# 1 --------------------------------------------------------------------
sub(u'''Isso é uma afirmação sobre ele, e não sobre o sistema. Como se viu no capítulo anterior,
em 1923 ainda saía de Gênova gente subsidiada, com patrão declarado, neste mesmo navio.
O que se pode dizer do Fausto é que ele não estava entre eles.''',
u'''Como se viu no capítulo anterior, ainda saía de Gênova gente subsidiada em 1923, com
patrão declarado antes do embarque, neste mesmo navio. Fausto não estava entre eles.''',
 '01 sem o enquadramento defensivo')

# 2 --------------------------------------------------------------------
sub(u'''"""E aqui eu preciso desfazer um raciocínio meu.

Durante muito tempo escrevi que Rosa Forner estava no <em>Principessa Mafalda</em> porque
a passagem subvencionada tinha acabado. Que o decreto de 1902 tinha empurrado esta família
para dentro de um transatlântico comercial.

Não foi isso. O documento de 1923 mostra que o transporte subsidiado ainda existia, e
existia neste navio.

O motivo é outro, é mais simples e é melhor: <strong>ela não estava sendo recrutada. Ela
estava indo encontrar o marido.</strong>""",''',
u'''"""E a mulher, quando veio, veio pelo mesmo caminho.

<strong>Rosa Forner não estava sendo recrutada. Estava indo encontrar o marido.</strong>

É uma diferença que parece pequena e que decide tudo o que vem depois.""",''',
 '02 Rosa nao estava sendo recrutada')

# 3 --------------------------------------------------------------------
sub(u'''"""Escrevi, na versão anterior deste capítulo, que uma canetada dada em Roma determinou em
que tipo de embarcação esta família atravessaria o oceano vinte e cinco anos depois.

Era uma boa frase. Não se sustenta.

O decreto de 1902 é fato, e o efeito imediato dele sobre o fluxo é fato. O que eu não posso
dizer é que ele pôs Rosa naquele navio, porque em 1923 aquele navio ainda transportava
gente subsidiada.

O que o decreto fez foi mais modesto e ainda assim grande: mudou quem podia ir sem dinheiro
e quem precisava juntar. Empurrou uma parte da emigração vêneta para o modelo de um por
vez, por conta própria, chamando os outros depois. A família Miotto cabe inteira dentro
desse modelo.

História é feita disso, e também é feita de corrigir a própria frase quando o documento
aparece.""",''',
u'''"""Seria bonito dizer que uma canetada dada em Roma pôs esta família naquele navio, vinte e
cinco anos depois.

Não é verdade, e o documento de 1923 é a prova: aquele navio ainda levava gente subsidiada.

O que o decreto fez foi mais modesto, e ainda assim grande. Mudou quem podia ir sem
dinheiro e quem precisava juntar. Empurrou uma parte da emigração vêneta para o modelo de
um por vez, por conta própria, chamando os outros depois.

<strong>A família Miotto cabe inteira dentro desse modelo.</strong>""",''',
 '03 a canetada em Roma')

# 4 --------------------------------------------------------------------
sub(u'''"""Fica um buraco aberto, e ele é meu.

O Decreto N. 2400, de 13 de julho de 1918, citado no cabeçalho daquela Relação de 1923, é
a base legal <em>brasileira</em> do transporte subsidiado. Do lado italiano, eu não sei até
quando a proibição de 1902 continuou valendo na prática, nem se foi revogada, nem se
simplesmente deixou de ser aplicada.

Sem essa peça, este capítulo não pode afirmar que a proibição durou até 1927, e também não
pode afirmar que caiu antes.

Fica declarado assim até o documento aparecer.""",''',
u'''"""Fica um buraco neste capítulo, e ele é grande.

O Decreto N. 2400, de 13 de julho de 1918, citado no cabeçalho daquela Relação de 1923, é
a base legal <em>brasileira</em> do transporte subsidiado. Do lado italiano, não sei até
quando a proibição de 1902 continuou valendo na prática, nem se foi revogada, nem se
simplesmente deixou de ser aplicada.

Sem essa peça, este capítulo não pode dizer que a proibição durou até 1927, e também não
pode dizer que caiu antes.

Fica assim, declarado, até o documento aparecer.""",''',
 '04 o buraco declarado')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes no cap 6' % n[0])
