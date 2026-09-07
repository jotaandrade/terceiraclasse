# -*- coding: utf-8 -*-
"""Lista do vapor Alhena, Rio, 28.10.1927. Fecha a verificacao nº 2."""
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


# --- o hedge da chefia cai, e entra o documento ------------------------
sub(u'''Passei anos querendo saber e não vou inventar. Os documentos que existem dizem
que ela embarcou, dizem que sobreviveu, dizem que seis dias depois deu entrada
na Hospedaria dos Imigrantes do Brás com um filho de um ano no colo.

A página em que ela aparece parece registrá-la na condição de chefe da própria
família, o que numa entrada de 1927 não é pouca coisa. Digo <em>parece</em>
porque a digitalização que tenho não me deixa ler a coluna de parentesco com
segurança, e isso é afirmação forte demais para se fazer em cima de uma imagem
ruim.

Entre uma coisa e outra há uma noite sobre a qual ela falou pouco, e o pouco que
falou chegou até mim pela filha, que ainda está viva e ainda conta.''',
u'''Passei anos querendo saber e não vou inventar. O que os documentos dizem é o
que vem depois.

Três dias depois do naufrágio, em 28 de outubro de 1927, o vapor holandês
<em>Alhena</em> encostou no porto do Rio de Janeiro e entregou à Intendência de
Imigração uma lista com cinquenta náufragos, todos de terceira classe. Na coluna
onde deveria estar o porto de procedência, o escrivão escreveu uma palavra só:
<strong>Náufragos</strong>.

Linha 26 daquela folha: <strong>Forner Rosa, vinte e quatro anos, casada,
chefe.</strong>

Linha 27: <strong>Enrico, um ano, filho.</strong>""",

"""Chefe.

Ela era casada, e o marido estava vivo, esperando em algum lugar do interior de
São Paulo. Ainda assim, no papel, quem encabeça aquela família é ela. Vinte e
quatro anos, um filho de um ano no colo, e a roupa do corpo.

Dezoito linhas abaixo, na mesma folha, o mesmo registro: <strong>Forner Maria,
trinta e um anos, chefe</strong>, com Ginneta de sete, Pulgheria de seis, Rino de
quatro e Danilo de dois.

Duas irmãs, duas famílias, dois maridos do outro lado do continente, e as duas
anotadas como cabeça da própria casa.

A lista traz ainda, sobre a Rosa, duas coisas que nenhum outro documento desta
família diz. Profissão: <em>doméstica</em>. E, na coluna de instrução, uma
palavra que responde uma pergunta que ficou aberta lá no primeiro capítulo:
<strong>Sim</strong>.

Ela sabia ler.""",

"""Entre o naufrágio e essa folha de papel há uma noite sobre a qual ela falou
pouco, e o pouco que falou chegou até mim pela filha, que ainda está viva e ainda
conta.''',
 'cap 20 · a lista do Alhena, chefia confirmada')

# --- quatro grafias, nao duas ------------------------------------------
sub(u'''A grafia, aliás, não é detalhe. A menina que o ato de Cavaso registra como <strong>Gina
Oliva</strong>, nascida em 28 de março de 1920, aparece como Dinetta na lista brasileira e
como Ginita na argentina. O nome atravessou dois idiomas e um naufrágio e chegou do outro
lado com outra forma. Vai acontecer com quase todos eles.''',
u'''A grafia, aliás, não é detalhe. A menina que o ato de Cavaso registra como <strong>Gina
Oliva</strong>, nascida em 28 de março de 1920, aparece como <strong>Ginneta</strong> na
lista do Rio, vira <strong>Dinetta</strong> na entrada de São Paulo três dias depois, e sai
<strong>Ginita</strong> nos jornais argentinos.

Quatro grafias para uma menina de sete anos, em duas semanas. O nome atravessou dois
idiomas e um naufrágio e chegou do outro lado com outra forma. Vai acontecer com quase
todos eles.''',
 'cap 20 · quatro grafias de Gina')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d correcoes' % n[0])
