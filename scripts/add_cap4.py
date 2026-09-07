# -*- coding: utf-8 -*-
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

CAP4 = u'''
CAP4 = [
"""Uma certidão de batismo do Vêneto do século XIX cabe em duas linhas.

Data. Nome da criança. Nome do pai. Nome da mãe. Padrinho e madrinha. Assinatura do
pároco, ou a cruz de quem não sabia assinar.

Não tem profissão, não tem endereço, não tem causa de nada. Não diz se a casa era de
pedra ou de pau, se havia comida naquele inverno, se a criança era esperada ou era a
oitava.

Durante muito tempo eu li essas listas procurando os nomes. Levei anos para entender que
a informação não está nos nomes. Está no intervalo entre eles.""",

"""O nome mais antigo é Luigi Forner, nascido em 1817.

Ele se casou com Elisabetta Forner.

Leia de novo. Os dois têm o mesmo sobrenome.

Isso não é erro de transcrição e não é escândalo. É demografia. Numa vila de algumas
centenas de habitantes, cercada de montanha, onde ninguém se mudava e o casamento
acontecia dentro da paróquia, primos casavam com primos, e sobrenomes se repetiam nos
dois lados do altar com uma regularidade que hoje causa espanto e naquela época não
causava nenhum.

O sobrenome Forner ocupa páginas inteiras dos livros daquelas paróquias. Em algum ponto
do século XVIII, quase todo mundo ali era parente de todo mundo.""",

"""Do casamento de Luigi vieram, entre outros, dois filhos que continuaram a linha:
Domenico Alessandro Forner, de 1853, e Vincenzo Forner, de 1862.

É Vincenzo que interessa aqui, porque é dele que descende esta história.

Vincenzo Forner casou-se com Santa Pandolfo, nascida em 1865.

Segundo o levantamento da família, os dois tiveram dezesseis filhos documentados.""",

"""Os nomes, na ordem em que aparecem:

Angela, 1886. Pietro Luigi, 1889. Martino Giuseppe, 1891. Sante, 1893. Maria Elisabetta,
1895. Maria Luigia, 1896. Bonfiglio Sabino, 1898. Angela, 1898. Giulio Giuseppe, 1900.
Onorato, 1900. Rosa, 1903. Alessandro Domenico, 1903. Maria, 1907. Roberto, 1908. Ausilio
Fortunato, 1908. Francesco, 1913.

E Galliano, sem data.

Lida assim, é uma lista de cartório. Vou lê-la outra vez.""",

"""Angela em 1886. Angela outra vez em 1898.

Duas filhas vivas com o mesmo nome, na mesma casa, não acontece. O que acontece, e
acontecia o tempo todo, é que a primeira Angela morreu, e doze anos depois deram o nome
dela para outra menina.

Era costume, e era um costume que tinha uma lógica. O nome era um bem de família, como a
terra. Não se deixava um nome morrer junto com a criança.

Três Marias na mesma lista: Maria Elisabetta em 1895, Maria Luigia em 1896, Maria em
1907. Aqui não dá para afirmar, porque Maria era nome tão comum que vinha composto e
podia conviver. Mas registro a suspeita.""",

"""E há uma linha que não precisa de interpretação nenhuma.

Roberto Forner, 1908 a 1908.

Nasceu e morreu no mesmo ano. É o único da lista cuja vida inteira cabe num número
repetido.

No mesmo ano de 1908 nasceu Ausilio Fortunato, que viveu até 1989. Não sei se eram gêmeos
e um não resistiu, ou se Roberto morreu cedo no ano e Ausilio nasceu depois. As duas
coisas são comuns. As duas contam a mesma história.""",

"""Agora olhe para Santa Pandolfo.

Nasceu em 1865. O primeiro filho documentado é de 1886, quando ela tinha vinte e um anos.
O último é de 1913, quando ela tinha quarenta e oito.

Vinte e sete anos parindo.

Dezesseis gestações documentadas, e é quase certo que houve mais, porque perda de
gravidez e criança morta nos primeiros dias muitas vezes não chegava ao livro da
paróquia. Tudo isso comendo polenta, carregando água, trabalhando a encosta e criando os
que iam ficando.

Esta é a bisavó de quem vai atravessar o Atlântico. Convém saber de que corpo ela
veio.""",

"""Pietro Luigi Forner: 1889 a 1916.

Vinte e sete anos de idade, morto em 1916.

Não tenho o documento que diz onde nem como, e por isso não vou afirmar. Mas 1916 é o
segundo ano da Itália na Grande Guerra, um homem de vinte e sete anos estava em plena
idade de convocação, e a família morava a poucos quilômetros do que viraria a frente.

A hipótese óbvia é a hipótese óbvia.

O capítulo 6 deste livro conta a história do irmão dele, Sante, que foi para a guerra e
voltou com três medalhas. Vale lembrar que a mesma casa mandou pelo menos dois, e que só
um voltou.""",

"""E aí chega a linha que mudou o modo como eu entendo esta família inteira.

Vincenzo Forner: 1862 a 1914.

Santa Pandolfo: 1865 a 1914.

O pai e a mãe morreram no mesmo ano.

Eu tinha esses dois números na frente dos olhos havia anos, num arquivo de genealogia,
como quem tem uma planilha. Só fui somar quando comecei a escrever este capítulo.""",

"""Faça a conta com as idades dos filhos em 1914.

Sante tinha vinte e um anos. Maria Luigia tinha dezoito. Rosa tinha onze. Francesco, o
caçula, tinha um.

Em algum momento de 1914 aquela casa perdeu o pai e a mãe e ficou com um rapaz de vinte
e um anos como homem mais velho e uma moça de dezoito como mãe de todo mundo.

E então, em maio de 1915, a Itália entrou na guerra e levou os rapazes.""",

"""Isso reescreve a cena da partida.

A história que chegou até hoje, e que está no livro que esta família já tinha escrito, é
a de duas irmãs que deixam a Itália para reencontrar os maridos no Brasil. É verdade e é
insuficiente.

Rosa Forner era órfã desde os onze anos. Maria Luigia tinha criado os irmãos menores.
Quando as duas embarcaram em Gênova, em 1927, não estavam deixando para trás uma casa
cheia. Estavam deixando o que sobrou de uma casa que já tinha sido esvaziada duas vezes,
pela morte dos pais e pela guerra.

Ninguém atravessa um oceano com um filho de um ano no colo porque está entediado.""",

"""Um aviso, e ele é sério.

Tudo o que acabei de ler está apoiado num levantamento genealógico de família, montado a
partir de bases digitais e de memória oral. Datas nesse tipo de fonte erram, e erram de
maneiras previsíveis: ano estimado que vira ano exato, duas pessoas fundidas numa,
transcrição de caligrafia difícil.

A coincidência de 1914 é forte demais para ser aceita sem documento. Pode ser epidemia,
pode ser acidente, pode ser um dos dois anos estar errado.

O lugar onde se confirma isso é o Archivio di Stato di Treviso e os livros das paróquias
de Monfumo e Castelcucco. Registros de óbito de 1914 dizem data, causa e testemunha.

Enquanto não estiver na mão, fica como está aqui: forte, provável e não confirmado.""",

"""Do outro lado da história estão os Miotto, e deles sabemos menos.

O tronco documentado começa em Jacobus Miotto, casado com Anna Fidato. Camponeses, sem
mais nada anotado. Dos filhos, quatro deixaram descendência registrada: Luigi, casado com
Nina Ganeo; Giovanni, casado com Rosa Lazzaro; Antonio, casado com Lugia Maria Genovese;
e Giuseppe, que ficou.

É de Luigi e Nina que nasce Fausto Miotto, em 1904, em Castelcucco.""",

"""E aqui há uma simetria que passou despercebida por muito tempo.

Luigi Miotto, o pai de Fausto, também emigrou.

Não para o Brasil. Para o Canadá. Estabeleceu-se em Vancouver e morreu lá.

Ou seja: o pai atravessou o Atlântico para o noroeste e o filho atravessou para o
sudoeste, e os dois saíram do mesmo vilarejo de oito quilômetros quadrados. Não foi uma
família que emigrou. Foram duas gerações emigrando em direções diferentes, para nunca
mais se verem.

Quando Fausto embarcou para o Brasil, ele não estava fazendo nada de novo na família.
Estava repetindo o pai.""",

"""Duas famílias, duas vilas, quatro quilômetros entre elas.

Uma esvaziada pela morte dos pais e pela guerra. A outra esvaziada por um pai que foi
para o outro lado do mundo e não voltou.

Rosa e Fausto se casaram em 1926.

Os sobrenomes que sobreviveram nos livros daquelas paróquias são os dos que ficaram. Os
que ficaram são os que hoje quase ninguém procura. Este livro existe porque a linha que
foi embora é a que teve alguém, cem anos depois, com tempo e teimosia para voltar
atrás.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP4.strip() + "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 20: CAP20}", 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 4 inserido')
