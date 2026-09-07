# -*- coding: utf-8 -*-
"""Limpeza do cap. 4: sai a autocorreção, sai a segunda 'descoberta' do mesmo documento."""
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


# 1 -------------------------------------------------------------------
sub(u'''Durante meses eu li as duas fileiras como uma coisa só: catorze filhos de Vincenzo Forner
e Santa Pandolfo. Fiz contas em cima disso. Escrevi páginas em cima disso.

Estava errado.""",''',
u'''Lida corrida, a lista parece o que não é: catorze filhos de um casal só.""",''',
 '01 o quadro, sem confissao')

# 2 -------------------------------------------------------------------
sub(u'''"""O que me tirou do erro foi ampliar a fotografia.''',
u'''"""Foi preciso ampliar a fotografia para enxergar por quê.''',
 '02 ampliar a fotografia')

# 3 -------------------------------------------------------------------
sub(u'''Antes de enxergar a linha do quadro, eu tinha aqui o que parecia um exemplo perfeito de um
costume real: quando uma criança morria, o nome dela voltava na criança seguinte. O nome
era um bem de família, como a terra, e não se deixava um nome morrer junto com quem o
carregava.

O costume existiu e está documentado na região inteira. Só que estas duas Angelas não são
irmãs. São primas, nascidas em casas diferentes de dois irmãos, e não provam nada disso.

Fica o costume. Sai o exemplo. É uma troca ruim para o parágrafo e boa para o livro.''',
u'''Duas primas com o mesmo nome, nascidas com doze anos de diferença nas casas de dois
irmãos. Não é coincidência nem descuido. O nome era um bem de família, como a terra, e
circulava entre as casas do mesmo sobrenome.

Existia também o costume de devolver o nome de uma criança morta à criança seguinte, e ele
está documentado na região inteira. Não é o caso destas duas, que conviveram.''',
 '03 as duas Angelas')

# 4 -------------------------------------------------------------------
sub(u'''"""Preciso corrigir aqui um segundo erro meu, bem menor que o da fileira, cometido na
primeira vez que li esse quadro numa fotografia ruim.

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

É a mesma tentação da gravidez que nunca existiu, três capítulos atrás.""",

''',
u'''''',
 '04 CORTADO: o bloco do "segundo erro meu"')

# 5 -------------------------------------------------------------------
sub(u'''Índice é ferramenta de busca. Não é prova. Eu tinha me esquecido disso.""",''',
u'''Índice é ferramenta de busca. Não é prova.""",''',
 '05 indice')

# 6 -------------------------------------------------------------------
sub(u'''"""Escrevi tudo isso. E depois achei o documento.

A <em>carta d'identità</em> de Sante Forner, emitida em Asolo em 8 de março de 1940,
registra o nome da mãe dele por extenso:''',
u'''"""O que decidiu a questão não estava em índice nenhum. Estava numa pasta do acervo desta
família.

A <em>carta d'identità</em> de Sante Forner, emitida em Asolo em 8 de março de 1940,
registra o nome da mãe dele por extenso:''',
 '06 a carta d identita entra uma vez')

# 7 -------------------------------------------------------------------
sub(u'''
O que mudou foi o peso. Quando escrevi esta página pela primeira vez, aquelas duas folhas
decidiam se o capítulo 7 era sobre um irmão ou sobre um primo. Não decidem mais. Isso já
foi decidido, e por um documento que estava no acervo desde o começo, guardado numa pasta
que eu tinha aberto sem olhar direito.""",''',
u'''""",''',
 '07 sai "o que mudou foi o peso"')

# 8 -------------------------------------------------------------------
sub(u'''"""E agora o que sobra contra o quadro, que é bem menos do que eu andei dizendo.

<em>Storia di Castelcucco</em> é um livro de história local, feito com cuidado, e é a
melhor fonte que esta família tem sobre as gerações mais antigas. Eu tinha três acusações
contra ele. Duas caíram junto com a minha leitura da segunda fileira.

<strong>Caiu a primeira.</strong> Eu dizia que Alessandro Domenico, de 28 de janeiro de
1903, e Rosa, de junho do mesmo ano, seriam dois partos da mesma mulher em cinco meses.
Não são da mesma mulher. Alessandro Domenico é filho de Cadonà Maria Teresa. Não há
impossibilidade nenhuma.

<strong>Caiu a segunda.</strong> Eu dizia que Angela, de 20 de abril de 1898, e Bonfiglio,
também de 1898, não cabiam no mesmo ano e no mesmo ventre. Angela é de Cadonà, Bonfiglio é
de Santa. Duas casas, dois partos, nenhum problema.

<strong>Fica uma, e essa é sólida.</strong> O quadro diz que Rosa nasceu em 1905. A
certidão do Comune di Monfumo, ato 31 do ano de 1903, diz 24 de junho de 1903. Documento
vence livro.

O livro impresso estava mais certo do que eu. O erro era de leitura, e era meu.""",''',
u'''"""Contra o quadro sobra uma coisa só, e ela é sólida.

<em>Storia di Castelcucco</em> é um livro de história local, feito com cuidado, e é a
melhor fonte que esta família tem sobre as gerações mais antigas. Erra num ponto, e o
ponto é grave para quem escreve este livro: <strong>a data de nascimento da Rosa</strong>.

O quadro diz 1905. A certidão do Comune di Monfumo, ato 31 do ano de 1903, diz
<strong>24 de junho de 1903</strong>.

Documento vence livro.""",''',
 '08 o quadro erra em um ponto')

# 9 -------------------------------------------------------------------
sub(u'''
Corrigi esses números para baixo depois de reler o quadro, e faço questão de dizer que
corrigir para baixo não alivia coisa nenhuma. Dez partos em vinte e um anos, naquela
encosta, com aquela comida, é a mesma vida.
''',
u'''
Dez partos em vinte e um anos, naquela encosta, com aquela comida.
''',
 '09 os numeros da Santa')

# 10 ------------------------------------------------------------------
sub(u'''
Francesco, o de 1913, que eu durante muito tempo pus como caçula dessa casa, é do outro
ramo. A mais nova ali tinha sete anos, e não um.
''',
u'''''',
 '10 CORTADO: Francesco')

# 11 ------------------------------------------------------------------
sub(u'''"""Durante um tempo eu escrevi que o pai tinha morrido no mesmo ano, e montei em cima
disso uma cena de orfandade completa.

Fui verificar. Não se sustenta.

A genealogia impressa em <em>Storia di Castelcucco</em> traz, ao lado de Santa Pandolfo,
a anotação de morte em 1914. Ao lado de Vincenzo, nascido em 6 de agosto de 1862, não traz
data de morte nenhuma.

Ou seja: <strong>não sabemos quando Vincenzo Forner morreu.</strong> Pode ter sido em
1914, pode ter sido vinte anos depois. Pode ter estado vivo, e provavelmente estava,
quando a filha embarcou em 1927.

A cena de orfandade dupla era minha, não dos documentos. Fica registrada aqui como erro
corrigido, porque este livro tem a obrigação de mostrar onde errou.""",''',
u'''"""Sobre o pai, a genealogia impressa é muda.

<em>Storia di Castelcucco</em> traz, ao lado de Santa Pandolfo, a anotação de morte em
1914. Ao lado de Vincenzo, nascido em 6 de agosto de 1862, não traz data nenhuma.

É tentador fechar a cena aí, com os dois enterrados no mesmo ano e Rosa órfã dos dois aos
onze. Fica redondo, e não há uma linha de documento que sustente.""",''',
 '11 a orfandade dupla')

# 12 ------------------------------------------------------------------
sub(u'''"""E depois de escrever isso, achei a linha.

Está na <em>carta d'identità</em> de Sante Forner, emitida pelo Comune di Asolo em 8 de
março de 1940. No campo da filiação, o escrivão escreveu duas linhas, uma embaixo da
outra:''',
u'''"""A resposta estava na mesma carteira de identidade de 1940.

No campo da filiação, o escrivão de Asolo escreveu duas linhas, uma embaixo da outra:''',
 '12 sem a segunda descoberta do mesmo documento')

sub(u'''
Fui conferir na imagem em alta resolução, palavra por palavra, porque uma afirmação dessas
não se faz por cima de um borrão. As duas fórmulas estão lá, na mesma caligrafia, uma
embaixo da outra, sem ambiguidade nenhuma.
''',
u'''''',
 '12b CORTADO: a narracao da conferencia')

sub(u'''O mesmo documento me deu de brinde a data de nascimento exata do Sante, 16 de abril de
1893, e o lugar: Monfumo. Ele é o assunto do capítulo 7, e é lá que essa carteira de
identidade vai ser lida inteira.""",''',
u'''A mesma folha dá a data exata de nascimento do Sante, 16 de abril de 1893, e o lugar:
Monfumo. Ele é o assunto do capítulo 7, e é lá que essa carteira vai ser lida inteira.""",''',
 '12c sem "de brinde"')

# 13 ------------------------------------------------------------------
sub(u'''"""Do outro lado da história estão os Miotto, e aqui eu preciso ser mais honesto do que fui.

Durante muito tempo escrevi que o tronco documentado desta família começa em Jacobus
Miotto, casado com Anna Fidato, camponeses, com quatro filhos que deixaram descendência:
Luigi, Giovanni, Antonio e Giuseppe.

Esse casal existe e esses quatro filhos existem. Só que eles não são, até prova em
contrário, os meus. São a família de Vancouver, e daqui a três páginas eu conto como foi
que entraram nesta árvore.

O que eu tenho documentado da linha Miotto começa e termina em um homem só: <strong>Luigi
Miotto, casado com Domenica Ganeo</strong>. Acima dele, por enquanto, não há papel
nenhum.''',
u'''"""Do outro lado da história estão os Miotto, e deles eu tenho muito menos.

A linha documentada começa e termina num homem só: <strong>Luigi Miotto, casado com
Domenica Ganeo</strong>. Acima dele, por enquanto, não há papel nenhum.

Circula uma versão em que o tronco começa num Jacobus Miotto casado com Anna Fidato, com
quatro filhos: Luigi, Giovanni, Antonio e Giuseppe. Esse casal existe e esses quatro filhos
existem. Só que não são, até prova em contrário, os meus. São a família de Vancouver, e
daqui a três páginas se vê como foi que entraram nesta árvore.''',
 '13 o tronco Miotto')

# 14 ------------------------------------------------------------------
sub(u'''Escrevi isso, e depois fui olhar como a hipótese tinha nascido. Achei a hora exata em que
ela entrou.""",''',
u'''Fui olhar como essa hipótese tinha nascido, e achei a hora exata em que ela entrou.""",''',
 '14 a origem da hipotese')

# 15 ------------------------------------------------------------------
sub(u'''"""E fica a lição, que é a do capítulo inteiro.

Eu abri estas páginas dizendo que não existe uma fonte boa, existem três fontes ruins que
cruzadas chegam perto. Preciso acrescentar uma quarta, e ela é a mais perigosa das quatro,
porque não parece fonte: <strong>a árvore colaborativa</strong>.

Ela não erra por ser velha, nem por ter a tinta apagada, nem por ter tido escrivão
apressado. Erra porque qualquer pessoa, em qualquer lugar do mundo, pode juntar dois homens
num só às onze e vinte e um da manhã e seguir a vida.

E porque o erro, depois de feito, tem exatamente a mesma aparência de tudo o mais que está
ali.""",''',
u'''"""Existe uma quarta fonte nesta história, e é a mais perigosa das quatro, porque não
parece fonte.

A genealogia impressa erra por ser antiga. O índice civil erra por ser resumo. A memória
de família erra por ser memória. <strong>A árvore colaborativa erra porque qualquer pessoa,
em qualquer lugar do mundo, pode juntar dois homens num só às onze e vinte e um da manhã e
seguir a vida.</strong>

E porque o erro, depois de feito, tem exatamente a mesma aparência de tudo o mais que está
ali.""",''',
 '15 a quarta fonte')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d alteracoes no cap 4' % n[0])
