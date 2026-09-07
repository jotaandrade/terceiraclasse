# -*- coding: utf-8 -*-
"""Corrige o capitulo 4 com a leitura correta do quadro de Storia di Castelcucco."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    s = s.replace(old, new, 1); print('ok', label)

# --------------------------------------------------- a lista dos filhos
sub(u'''"""Os nomes, na ordem em que aparecem:

Angela, 1886. Pietro Luigi, 1889. Martino Giuseppe, 1891. Sante, 1893. Maria Elisabetta,
1895. Maria Luigia, 1896. Bonfiglio Sabino, 1898. Angela, 1898. Giulio Giuseppe, 1900.
Onorato, 1900. Rosa, 1903. Alessandro Domenico, 1903. Maria, 1907. Roberto, 1908. Ausilio
Fortunato, 1908. Francesco, 1913.

E Galliano, sem data.

Lida assim, é uma lista de cartório. Vou lê-la outra vez.""",''',
u'''"""O quadro impresso em <em>Storia di Castelcucco</em> lista catorze filhos, distribuídos
em duas fileiras.

Na primeira: Angela, 1886. Pietro, 27 de outubro de 1889. Martino, 11 de novembro de 1891.
Sante, 1893. Bonfiglio, 1898. Giulio, 1900. Rosa, 1905. Maria M., 1907.

Na segunda: Angela, 20 de abril de 1898. Onorato, 17 de abril de 1900. Alessandro
Domenico, 28 de janeiro de 1903. Ausilio Fortunato, 10 de junho de 1908. Roberto, 10 de
junho de 1908. Francesco L., 28 de maio de 1913.

Lida assim, é uma lista de cartório. Vou lê-la outra vez, e depois vou mostrar por que
ela está errada em pelo menos três pontos.""",''', 'lista dos 14')

# ------------------------------------------- Angela/Onorato: corrigir erro meu
sub(u'''"""Duas linhas não precisam de interpretação nenhuma.

<strong>Angela, nascida em 20 de abril de 1898, morta em 17 de abril de 1900.</strong>
Três dias antes de completar dois anos.

<strong>Ausilio Fortunato, nascido em 10 de junho de 1908. Roberto, nascido em 10 de junho
de 1908.</strong>

A mesma data nos dois. Eram gêmeos.

Ausilio viveu até 1989, oitenta e um anos. Roberto morreu ainda em 1908.

Santa Pandolfo teve gêmeos aos quarenta e dois anos, enterrou um deles no mesmo ano, e o
outro atravessou o século inteiro.""",''',
u'''"""Uma linha não precisa de interpretação nenhuma.

<strong>Ausilio Fortunato, nascido em 10 de junho de 1908. Roberto, nascido em 10 de junho
de 1908.</strong>

A mesma data nos dois. Eram gêmeos.

Roberto morreu em <strong>3 de julho de 1908</strong>, com vinte e três dias.

Ausilio viveu até 21 de janeiro de 1989, oitenta anos.

Santa Pandolfo teve gêmeos aos quarenta e dois anos, enterrou um deles antes do fim do
mês seguinte, e o outro atravessou o século inteiro e morreu depois de Rosa.""",

"""Preciso corrigir aqui um erro meu, cometido na primeira vez que li esse quadro numa
fotografia ruim.

Eu li a segunda fileira como se fosse <em>Angela, 20.4.1898, morta em 17.4.1900</em>, e
escrevi uma frase bonita sobre uma menina que morreu três dias antes de completar dois
anos.

Ela não existiu. Quando a fotografia melhorou, ficou claro que são duas colunas
diferentes: <strong>Angela nasceu em 20 de abril de 1898</strong> e <strong>Onorato nasceu
em 17 de abril de 1900</strong>. Dois filhos, duas datas de nascimento, nenhuma morte.

Deixo o erro registrado porque ele é exemplar. Eu queria que aquela data fosse uma morte,
porque morte de criança confirmava a tese que eu estava construindo sobre nomes
repetidos. A cabeça de quem escreve puxa a evidência para o lado da frase que já está
pronta.

É a mesma tentação da gravidez que nunca existiu, três capítulos atrás.""",''', 'corrigir Angela/Onorato')

# ---------------------------------------- as contradicoes do quadro impresso
sub(u'''"""Agora olhe para Santa Pandolfo.''',
u'''"""E agora o problema maior, que é o próprio quadro.

<em>Storia di Castelcucco</em> é um livro de história local, feito com cuidado, e é a
melhor fonte que esta família tem sobre as gerações mais antigas. Também está errado em
pelo menos três lugares, e dá para provar.

<strong>Um.</strong> O quadro diz que Rosa nasceu em 1905. A certidão do Comune di
Monfumo, ato 31 do ano de 1903, diz 24 de junho de 1903. Documento vence livro.

<strong>Dois.</strong> O quadro põe Alessandro Domenico nascendo em 28 de janeiro de 1903.
Com Rosa nascida em junho do mesmo ano, seriam dois partos da mesma mulher em cinco
meses. Impossível. Uma das duas datas está errada, e sabemos qual não está.

<strong>Três.</strong> O quadro põe Angela em 20 de abril de 1898 e Bonfiglio também em
1898. Mesma coisa: ou são gêmeos e o quadro não diz, ou um dos anos está trocado.""",

"""E há o que o quadro simplesmente não tem.

Não aparecem ali <strong>Maria Elisabetta, de 1895</strong>, nem <strong>Maria Luigia, de
1896</strong>. As duas estão no índice civil de nascimentos do comune, com pai Vincenzo e
mãe Pandolfo Santa, atos 11 e 12 dos respectivos anos.

Maria Luigia é a irmã que atravessou o Atlântico junto com Rosa, com quatro filhos, e que
sobreviveu ao mesmo naufrágio. É metade da história deste livro.

<strong>Ela não está na genealogia impressa da própria família.</strong>

Nem Galliano, que a memória familiar registra e que nenhuma das duas fontes confirma.""",

"""Some tudo e o retrato é este.

A genealogia impressa está certa na estrutura e frouxa nas datas. O índice civil tem
datas melhores e não tem sobrenome do pai. A memória de família tem nomes que nenhuma das
duas registra. E as três discordam entre si.

Não existe uma fonte boa. Existem três fontes ruins que, cruzadas, chegam perto.

É assim que se reconstrói uma família camponesa do século XIX, e quem disser que fez isso
com certeza em algum ponto parou de conferir.""",

"""Agora olhe para Santa Pandolfo.''', 'contradicoes do quadro')

# ------------------------------------------------ irmaos de Vincenzo: casamento de Abele
sub(u'''Todos os três nasceram em Monfumo.''',
u'''Todos os três nasceram em Monfumo. Abele casou-se com Cadonà Maria Teresa, nascida em 7
de maio de 1869, também de Monfumo.''', 'Abele casamento')

io.open(f, 'w', encoding='utf-8').write(s)
print('\nOK: capitulo 4 corrigido pelo quadro em alta resolucao')
