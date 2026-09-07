# -*- coding: utf-8 -*-
"""Ultimas tres passagens de autocorrecao: caps. 1 e 2."""
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


# CAP 2 — a reviravolta do Luigi, sem confissao de rascunho
sub(u'''Durante muito tempo eu achei que a história de Luigi terminava aí, e escrevi assim: o
homem que nunca foi a lugar nenhum e a quem o mapa mudou debaixo dos pés.

Estava errado.""",''',
u'''A história de Luigi Forner parecia terminar aí: o homem que nunca foi a lugar nenhum e a
quem o mapa mudou debaixo dos pés.

Não termina.""",''',
 'cap 2 - a reviravolta do Luigi')

# CAP 1 — a primeira precisao
sub(u'''próprias. Durante muito tempo eu escrevi aqui que não sabia o que tinha acontecido lá.

A mesma tabela responde em parte.''',
u'''próprias.

A mesma tabela responde por ela, em parte.''',
 'cap 1 - primeira precisao')

# CAP 1 — a segunda precisao
sub(u'''A segunda é uma correção minha. Quase todo relato geral sobre aquele front repete que
os civis que viviam colados à linha foram retirados em 1917, e eu escrevi isso antes
de verificar. É plausível e é compatível com a documentação, mas a ordem específica,
com a lista de quais localidades e quais casas, ainda não apareceu.''',
u'''A segunda é sobre o que se costuma dizer. Quase todo relato geral sobre aquele front
repete que os civis que viviam colados à linha foram retirados em 1917. É plausível e é
compatível com a documentação, mas a ordem específica, com a lista de quais localidades
e quais casas, ainda não apareceu.''',
 'cap 1 - segunda precisao')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes' % n[0])
