# -*- coding: utf-8 -*-
"""Limpeza do cap. 5: tira a autocorreção, mantém a pesquisa como cena."""
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


# 1. A confissão de rascunho vira cena de pesquisa
sub(u'''"""Agora a parte que me obrigou a reescrever este capítulo duas vezes.

Na primeira versão eu escrevi que, quando Fausto Miotto embarcou, em meados dos anos
1920, essa máquina toda já não existia. Era uma frase limpa. Era falsa.

O que é verdade: a imigração subvencionada para o Brasil foi proibida pelo governo
italiano em 1902, pelo decreto que leva o nome do ministro Prinetti, e que é assunto do
próximo capítulo. As agências e os cinco mil subagentes são de 1892. O cartaz colorido na
praça é uma cena do século XIX.

Tudo isso continua de pé. E a máquina continuou funcionando mesmo assim.""",''',
u'''"""Tudo isso é do século XIX. O cartaz colorido na praça, as trinta agências, os cinco mil
subagentes.

Em 1902 o governo italiano proibiu a emigração subvencionada para o Brasil, pelo decreto
que leva o nome do ministro Prinetti e que é assunto do próximo capítulo. Quando Fausto
Miotto embarcou, em meados dos anos 1920, aquela praça já tinha outro aspecto.

Foi com essa ideia na cabeça que passei vinte e cinco listas de desembarque do
<em>Principessa Mafalda</em>, uma por uma, no Arquivo Público de São Paulo, procurando o
nome dele entre 1919 e 1924.

Não achei o Fausto.

Achei outra coisa.""",''',
 'a confissao vira cena de pesquisa')

# 2. "a frase correta" some
sub(u'''"""Então a frase correta não é que a máquina tinha acabado.

É que ela já não era para gente como o Fausto.''',
u'''"""A máquina não tinha acabado.

Tinha mudado de freguês.''',
 'sai "a frase correta"')

# 3. o enquadramento clerical sai; o fato fica
sub(u'''"""Registro aqui uma coisa que muda o modo de ler o resto deste livro.

Os subsidiados de 1923 viajaram na <strong>terceira classe</strong>.''',
u'''"""E há uma coluna nessa folha que muda o modo de ler o resto deste livro.

Os subsidiados de 1923 viajaram na <strong>terceira classe</strong>.''',
 'enquadramento clerical')

# 4. tira a linha do 1904 que virou redundante
sub(u'''Quatro anos depois, Rosa Forner desceu por essa escada.

Fausto nasceu em 1904, quando o cartaz já tinha saído da praça.""",''',
u'''Quatro anos depois, Rosa Forner desceu por essa escada.""",''',
 'linha redundante de 1904')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes no cap 5' % n[0])
