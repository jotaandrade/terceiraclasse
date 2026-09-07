# -*- coding: utf-8 -*-
"""Cap. 8: autocorreção, referências quebradas pela reescrita do 4, e a repetição do censo."""
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


# 1 — enquadramento clerical + referência quebrada a Vancouver
sub(u'''"""Vale olhar quem eram essas duas pessoas em 1926, porque a essa altura do livro já
sabemos.

Rosa tinha perdido a mãe aos onze anos.''',
u'''"""Vale olhar quem eram essas duas pessoas em 1926.

Rosa tinha perdido a mãe aos onze anos.''',
 '01 sem "a essa altura do livro"')

sub(u'''Fausto cresceu numa vila em que ir embora era uma das coisas que os homens faziam. Do pai
dele, Luigi Miotto, eu tenho o casamento em Maser em 1900, e o nome repetido duas vezes,
na certidão de nascimento de 1904 e na declaração de óbito de 1979. Entre uma coisa e
outra, nada. Não é dele a sepultura de Vancouver, e é só isso que o capítulo 4 conseguiu
provar.''',
u'''Fausto cresceu numa vila em que ir embora era uma das coisas que os homens faziam. Do pai
dele, Luigi Miotto, existem três aparições em papel ao longo de oitenta anos, e entre elas
nada. Um homem que deixou o nome e não deixou rastro.''',
 '02 referencia quebrada a Vancouver')

# 2 — a gravidez: fato para a frente, sem confissao de rascunho
sub(u'''"""Quando eu tinha só o ano do casamento, escrevi que talvez Rosa estivesse grávida na
cerimônia. Não estava. Ela estava com um bebê de quase dois meses no colo.''',
u'''"""Rosa não estava grávida na cerimônia. Estava com um bebê de quase dois meses no colo.''',
 '03 a gravidez que nao houve')

# 3 — alinhar com o cap. 6 corrigido (a subvencao nao acabou em 1902)
sub(u'''É importante não ler isso com olhos de hoje. Não foi abandono, foi o procedimento. Depois
que o decreto de 1902 acabou com a passagem paga, emigrar virou uma operação em duas
etapas: um homem vai na frente com o dinheiro que a família conseguiu juntar, trabalha,
arruma onde morar, e então manda buscar.

Angelo dei Agnoli, casado com Maria Luigia, foi junto ou por perto. Os dois cunhados
atravessaram, e as duas irmãs ficaram.""",''',
u'''É importante não ler isso com olhos de hoje. Não foi abandono, foi o procedimento. Para
quem não vinha recrutado, emigrar era uma operação em duas etapas: um homem vai na frente
com o dinheiro que a família conseguiu juntar, trabalha, arruma onde morar, e então manda
buscar.

Angelo Dei Agnoli, casado com Maria Luigia, fez o mesmo caminho, e antes dele. As duas
irmãs ficaram para trás nas duas casas.""",''',
 '04 alinhado ao cap 6, e Angelo foi antes')

# 4 — sai a confissão sobre a versão anterior desta página
sub(u'''O pai, ao que tudo indica, estava vivo. Isso eu só fui descobrir depois de ter escrito
esta página de outro jeito, e a versão anterior dizia que não havia adulto nenhum acima
dela naquela casa. Vincenzo tinha sessenta e quatro anos naquele inverno. Não sei o que
ele disse, nem se disse alguma coisa. Sei que ela foi assim mesmo.''',
u'''O pai vivo, a quatro quilômetros, com sessenta e quatro anos.

Não sei o que Vincenzo Forner disse quando soube, nem se disse alguma coisa. Sei que ela
foi assim mesmo.''',
 '05 o pai vivo, sem confissao')

# 5 — o censo mora no cap. 1; aqui fica só o que importa para a cena
sub(u'''Vale lembrar em que lugar ela estava. Maria Luigia casou-se em 1917 e foi morar em Cavaso,
e Cavaso é o comune que, no censo de outubro de 1918, aparece com <strong>2.795 refugiados
numa população de 3.258</strong>. Oitenta e cinco por cento. Enquanto Castelcucco perdia
trinta e nove pessoas, a vila para onde ela tinha acabado de se mudar se esvaziava quase
inteira.

Nove anos depois, ela ia embora de novo. Dessa vez sem volta prevista.''',
u'''Maria Luigia tinha casado em 1917 e ido morar em Cavaso, que é a vila que se esvaziou na
guerra enquanto Castelcucco ficava de pé. Ela chegou lá a tempo de ver quase todo mundo
sair.

Nove anos depois, saía ela. Dessa vez sem volta prevista.''',
 '06 o censo sai daqui, fica no cap 1')

# 6 — a recapitulação final cita material que saiu do cap. 4
sub(u'''parados, o imposto sobre a moagem, a pelagra, os dez filhos, a linha errada num quadro, os''',
u'''parados, o imposto sobre a moagem, a pelagra, os dez filhos de uma mulher só, os''',
 '07 recapitulacao sem a "linha errada num quadro"')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes no cap 8' % n[0])
