# -*- coding: utf-8 -*-
"""Cap. 7: saem os cartões de tarefa. A lacuna fica; a instrução de trabalho sai."""
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


# 1 — o documento da motivazione deixa de ser tarefa e vira imagem
sub(u'''Essa é a medalha que importa. E é a que tem um documento associado que ainda pode ser
encontrado.''',
u'''Essa é a medalha que importa. E quer dizer que em algum arquivo italiano existe uma folha
de papel que diz o que Sante Forner fez.''',
 '01 a motivazione vira imagem, nao tarefa')

# 2 — as fascette: fica o achado, sai a instrução de fotografia
sub(u'''As barras são a folha de serviço dele, em metal, na parede da casa do Giorgio.

Se a fotografia do quadro tiver resolução suficiente, ou se alguém puder tirar uma nova
de perto, dá para contar as barras e ler os anos. Isso diz, sem precisar de arquivo
nenhum, em quantas campanhas Sante Forner esteve e quais foram.

É a pesquisa mais barata deste livro inteiro e ainda não foi feita.""",''',
u'''As barras são a folha de serviço dele, em metal, na parede da casa do Giorgio. Cada uma
traz o ano gravado, e juntas dizem em quantas campanhas ele esteve e quais foram.

Estão ali desde 1920.

Ninguém nunca as contou.""",''',
 '02 as fascette, sem instrucao de foto')

# 3 — a terceira medalha: fica o nao-saber, sai o "resolve em cinco minutos"
sub(u'''Fica registrado como não identificado, porque inventar aqui seria fácil e seria errado.
Uma foto frontal do quadro, com luz e sem reflexo, resolve em cinco minutos para quem
entende de numismática militar italiana.""",''',
u'''Fica sem nome, porque inventar aqui seria fácil e seria errado.""",''',
 '03 a terceira medalha')

# 4 — o segundo objeto, sem confissão de arquivo mal lido
sub(u'''"""E existe um segundo objeto, que estava na pasta o tempo todo e que eu nunca tinha lido
de verdade.

Em 8 de março de 1940''',
u'''"""E existe um segundo objeto, guardado na mesma pasta.

Em 8 de março de 1940''',
 '04 o segundo objeto')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes no cap 7' % n[0])
