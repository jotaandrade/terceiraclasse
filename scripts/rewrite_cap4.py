# -*- coding: utf-8 -*-
"""Cap. 4 reescrito: as duas casas. A crítica de fontes migra para as notas do cap. 33."""
import io, os, re

SP = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad"
SRC = os.path.join(SP, 'build_livro.py')
s = io.open(SRC, encoding='utf-8').read()

# ---------------------------------------------------------------- backup
i0 = s.index(u'CAP4 = [')
i1 = s.index(u'CAP5 = [')
antigo = s[i0:i1]
io.open(os.path.join(SP, 'cap4_antigo.py.bak'), 'w', encoding='utf-8').write(antigo)
print('backup do CAP4 antigo: cap4_antigo.py.bak (%d palavras)' % len(re.sub(r'<[^>]+>', ' ', antigo).split()))

# ---------------------------------------------------------------- novo
NOVO = u'''CAP4 = [
"""Uma certidão de batismo do Vêneto do século XIX cabe em duas linhas.

Data. Nome da criança. Nome do pai. Nome da mãe. Padrinho e madrinha. Assinatura do
pároco, ou a cruz de quem não sabia assinar.

Não tem profissão, não tem endereço, não tem causa de nada. Não diz se a casa era de pedra
ou de pau, se havia comida naquele inverno, se a criança era esperada ou era a oitava.

Levei anos para entender que a informação não está nos nomes. Está no intervalo entre
eles.""",

"""O nome mais antigo com data é <strong>Luigi Forner, nascido em 14 de agosto de
1817</strong>, em Monfumo, e morto em 11 de novembro de 1905.

Oitenta e oito anos. Naquele lugar e naquele século, é quase inverossímil.

Atrás dele estão os pais, Domenico Forner e Maria Vial, sem datas. Dali para trás é
escuro.

Luigi casou-se com Elisabetta Forner.

Leia de novo. Os dois têm o mesmo sobrenome.""",

"""Isso não é escândalo e não é descuido de escrivão. É demografia.

Numa vila de algumas centenas de habitantes, cercada de montanha, onde ninguém se mudava e
o casamento acontecia dentro da paróquia, primos casavam com primos e sobrenomes se
repetiam nos dois lados do altar com uma regularidade que hoje causa espanto e naquela
época não causava nenhum.

O sobrenome Forner ocupa páginas inteiras dos livros daquelas paróquias. Em algum ponto do
século XVIII, quase todo mundo ali era parente de todo mundo.""",

"""Luigi teve três filhos que deixaram rastro: Domenico Alessandro, de 1853, Vincenzo, de
1862, e Abele Alessandro, de 1865. Os três nasceram em Monfumo e os três ficaram por ali.

É o do meio que interessa.

<strong>Vincenzo Forner casou-se com Santa Pandolfo em 1887.</strong> Ele com vinte e cinco
anos, ela com vinte e dois.""",

"""A primeira filha do casal, Angela, nasceu em 1886.

Um ano antes do casamento.

Não há mistério nisso, e faço questão de dizer, porque a mesma coisa vai acontecer de novo
nesta família quarenta anos depois e eu não quero que soe como exceção. Numa vila católica
do Vêneto, um filho antes do papel queria dizer que a relação já era estável e que a
formalização esperava alguma coisa: dinheiro, autorização de família, a vinda de um padre,
o fim de uma colheita.

A criança vinha primeiro. Depois o cartório.""",

"""<strong>Vincenzo e Santa tiveram dez filhos documentados.</strong>

Angela, 1886. Pietro Luigi, 1889. Martino Giuseppe, 1891. Sante, 1893. Maria Elisabetta,
1895. Maria Luigia, 1896. Bonfiglio Sabino, 1898. Giulio Giuseppe, 1900. Rosa, 1903.
Maria, 1907.

Lida como lista de cartório, não diz nada.

Leia os intervalos. Três anos. Dois. Dois. Dois. Um. Dois. Dois. Três. Quatro.""",

"""Agora olhe para a mulher que está atrás desses números.

Santa Pandolfo nasceu em 1º de novembro de 1865. Teve o primeiro filho aos vinte e um anos.
Teve o último aos quarenta e dois.

<strong>Vinte e um anos parindo.</strong>

Dez gestações documentadas, e é quase certo que houve mais, porque perda de gravidez e
criança morta nos primeiros dias muitas vezes não chegava ao livro da paróquia.

Tudo isso comendo polenta, carregando água, trabalhando a encosta e criando os que iam
ficando.

Esta é a bisavó de quem vai atravessar o Atlântico. Convém saber de que corpo ela veio.""",

"""Nem todos ficaram.

Naquelas casas morria-se cedo e morria-se de coisa banal, e o costume era devolver o nome
da criança morta à criança seguinte. O nome era um bem de família, como a terra: não se
deixava um nome morrer junto com quem o carregava.

Na casa do irmão de Vincenzo, a quatro quilômetros dali, nasceram gêmeos em 10 de junho de
1908. Ausilio Fortunato e Roberto.

Roberto morreu em 3 de julho, com vinte e três dias. Ausilio viveu até 1989.

Nasceram no mesmo dia, e entre a morte de um e a do outro passaram oitenta anos.""",

"""Em 1916 morreu <strong>Pietro Luigi Forner</strong>, o segundo filho, com vinte e sete
anos.

A explicação óbvia se escreve sozinha: era idade de convocação, a Itália estava no segundo
ano de guerra, e aquela casa ficava a poucos quilômetros do que viraria a frente do Monte
Grappa.

Fui procurar o nome dele no registro oficial dos militares italianos mortos naquela guerra.
Não está lá.

Pode ter sido a guerra sem constar em lugar nenhum. Pode ter sido tuberculose, acidente,
uma das epidemias que atravessavam aquelas vilas.

Naquele mundo, morrer aos vinte e sete não exigia guerra nenhuma.""",

"""Dois anos antes disso, em 1914, morreu Santa Pandolfo.

Rosa tinha onze anos. A caçula, Maria, tinha sete.

No mesmo ano a Europa entrou em guerra. No ano seguinte a Itália entrou junto e levou os
homens da casa.

Ficou Maria Luigia, de dezoito anos, com a casa nas costas e as irmãs pequenas dentro
dela.""",

"""Guarde essa moça.

Treze anos depois, aos trinta e um, ela vai estar na água escura da costa da Bahia com
quatro filhos pequenos, no mesmo naufrágio da irmã mais nova que ajudou a criar.

Mas isso é dali a dezesseis capítulos.""",

"""E o pai?

O pai estava lá.

<strong>Vincenzo Forner ainda estava vivo em março de 1940</strong>, com setenta e sete
anos. Sei disso por uma carteira de identidade que o filho Sante tirou naquele mês, no
comune de Asolo, em que o escrivão anotou o pai como vivo e a mãe como falecida, com as
duas fórmulas fixas que a burocracia italiana usava para essa diferença.

O que quer dizer que a cena de outubro de 1927 é esta, e não outra:

<strong>um homem de sessenta e cinco anos se despediu de duas filhas na porta de casa e não
as viu nunca mais.</strong>""",

"""Do outro lado desta história estão os Miotto, e deles eu tenho muito menos.

<strong>Luigi Miotto casou-se com Domenica Ganeo em 24 de junho de 1900, no comune di
Maser.</strong> Ele com vinte e cinco anos, ela com vinte e um.

A família repetiu por décadas que ela se chamava Nina. Não se chamava. O certificado de
casamento diz Domenica, e a declaração de óbito do filho dela, setenta e nove anos depois e
do outro lado do oceano, diz Domenica também.

Nina era o apelido. Foi o apelido que atravessou o Atlântico e virou nome.""",

"""Repare onde Luigi Miotto nasceu: <strong>Monfumo</strong>.

A mesma vila dos Forner. Os Miotto desta história não são de Castelcucco de origem.
Chegaram lá depois, como quase todo mundo.

<strong>Fausto nasceu em 5 de julho de 1904, em Castelcucco, às quatro da manhã.</strong>

Entre o casamento em Maser e o nascimento em Castelcucco há quatro anos e quatro
quilômetros.""",

"""E aqui aparece uma coisa que só se enxerga com os dois lados postos lado a lado.

Monfumo. Maser. Castelcucco. Cavaso. Quatro vilas, e entre as duas mais distantes não vão
dez quilômetros.

Os Forner saíram de Monfumo para Castelcucco em algum ponto entre 1903 e 1907: Rosa nasceu
na primeira, a irmã caçula nasceu na segunda. Os Miotto saíram de Monfumo, passaram por
Maser, e de Maser foram para Castelcucco.

<strong>Nesta história inteira, ninguém se muda mais do que quatro quilômetros por
vez.</strong>

Até o dia em que alguém atravessa um oceano.""",

"""De Luigi Miotto, o pai de Fausto, eu tenho três aparições.

O casamento, em 1900. O nome escrito na certidão de nascimento do filho, em 1904. E o nome
outra vez, na declaração de óbito desse mesmo filho, em 1979.

Entre uma coisa e outra, nada. Nenhum documento, nenhuma data, nenhum lugar.

Fausto cresceu numa vila em que ir embora era uma das coisas que os homens faziam. Para
onde foi o pai dele é uma pergunta que me tomou meses e que tem capítulo próprio, mais
adiante neste livro.""",

"""Duas famílias, duas vilas, quatro quilômetros entre elas.

Numa delas, uma mulher pariu dez vezes em vinte e um anos e morreu em 1914, deixando uma
menina de onze anos que um dia atravessaria o Atlântico.

Na outra, um homem deixou o nome em três papéis ao longo de oitenta anos e mais nada.

<strong>Rosa e Fausto casaram-se em 1926.</strong>""",

"""Os sobrenomes que sobreviveram nos livros daquelas paróquias são os dos que ficaram.

Os que ficaram são os que hoje quase ninguém procura.

Este livro existe porque a linha que foi embora é a que teve alguém, cem anos depois, com
tempo e teimosia para voltar atrás.""",
]

'''

s = s[:i0] + NOVO + s[i1:]

# subtitulo do capitulo
a = u"""  (4,'Forner e Miotto','Luigi Forner, 1817. Jacobus Miotto. Vincenzo, Santa Pandolfo e os dez filhos.'),"""
b = u"""  (4,'Forner e Miotto','Luigi Forner, 1817. Vincenzo, Santa Pandolfo e os dez filhos. Duas casas a quatro quilômetros.'),"""
assert a in s
s = s.replace(a, b, 1)

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('CAP4 reescrito: %d palavras' % len(re.sub(r'<[^>]+>', ' ', NOVO).split()))
