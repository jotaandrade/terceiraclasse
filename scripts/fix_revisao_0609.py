# -*- coding: utf-8 -*-
"""Revisao factual de 06.09.2026. Aplica as correcoes A-G ao manuscrito."""
import io, os

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

# =====================================================================
# A. A segunda fileira do quadro nao e de Vincenzo
# =====================================================================
sub(u'''"""O quadro impresso em <em>Storia di Castelcucco</em> lista catorze filhos, distribuídos
em duas fileiras.

Na primeira: Angela, 1886. Pietro, 27 de outubro de 1889. Martino, 11 de novembro de 1891.
Sante, 1893. Bonfiglio, 1898. Giulio, 1900. Rosa, 1905. Maria M., 1907.

Na segunda: Angela, 20 de abril de 1898. Onorato, 17 de abril de 1900. Alessandro
Domenico, 28 de janeiro de 1903. Ausilio Fortunato, 10 de junho de 1908. Roberto, 10 de
junho de 1908. Francesco L., 28 de maio de 1913.

Lida assim, é uma lista de cartório. Vou lê-la outra vez, e depois vou mostrar por que
ela está errada em pelo menos três pontos.""",''',
u'''"""O quadro impresso em <em>Storia di Castelcucco</em> traz catorze nomes de filhos,
distribuídos em duas fileiras.

Na primeira: Angela, 1886. Pietro, 27 de outubro de 1889. Martino, 11 de novembro de 1891.
Sante, 1893. Bonfiglio, 1898. Giulio, 1900. Rosa, 1905. Maria M., 1907.

Na segunda: Angela, 20 de abril de 1898. Onorato, 17 de abril de 1900. Alessandro
Domenico, 28 de janeiro de 1903. Ausilio Fortunato, 10 de junho de 1908. Roberto, 10 de
junho de 1908. Francesco L., 28 de maio de 1913.

Durante meses eu li as duas fileiras como uma coisa só: catorze filhos de Vincenzo Forner
e Santa Pandolfo. Fiz contas em cima disso. Escrevi páginas em cima disso.

Estava errado.""",

"""O que me tirou do erro foi ampliar a fotografia.

Descendo pela direita do quadro, a partir de <strong>Cadonà Maria Teresa, nascida em 7 de
maio de 1869 em Monfumo</strong>, esposa de Abele Alessandro Forner, há uma linha
vertical. Ela passa ao lado da primeira fileira sem tocar em nada e vai se ligar à barra
horizontal da segunda.

A segunda fileira não é de Vincenzo. É do irmão dele.

<strong>Primeira fileira, oito filhos de Vincenzo e Santa:</strong> Angela, Pietro,
Martino, Sante, Bonfiglio, Giulio, Rosa e Maria M.

<strong>Segunda fileira, seis filhos de Abele Alessandro e Cadonà Maria Teresa:</strong>
Angela, Onorato, Alessandro Domenico, os gêmeos Ausilio Fortunato e Roberto, e Francesco.

Um traço de dois centímetros, num quadro impresso, decidindo quem é irmão de quem.""",''',
 'A · a linha vertical do quadro')

# --- as duas Angelas viram primas ------------------------------------
sub(u'''"""Angela em 1886. Angela outra vez em 1898.

Duas filhas vivas com o mesmo nome, na mesma casa, não acontece. O que acontece, e
acontecia o tempo todo, é que a primeira Angela morreu, e doze anos depois deram o nome
dela para outra menina.

Era costume, e era um costume que tinha uma lógica. O nome era um bem de família, como a
terra. Não se deixava um nome morrer junto com a criança.

Três Marias na mesma lista: Maria Elisabetta em 1895, Maria Luigia em 1896, Maria em
1907. Aqui não dá para afirmar, porque Maria era nome tão comum que vinha composto e
podia conviver. Mas registro a suspeita.""",''',
u'''"""Angela em 1886, na casa de Vincenzo. Angela outra vez em 1898, na casa de Abele.

Antes de enxergar a linha do quadro, eu tinha aqui o que parecia um exemplo perfeito de um
costume real: quando uma criança morria, o nome dela voltava na criança seguinte. O nome
era um bem de família, como a terra, e não se deixava um nome morrer junto com quem o
carregava.

O costume existiu e está documentado na região inteira. Só que estas duas Angelas não são
irmãs. São primas, nascidas em casas diferentes de dois irmãos, e não provam nada disso.

Fica o costume. Sai o exemplo. É uma troca ruim para o parágrafo e boa para o livro.

Três Marias entre os filhos de Vincenzo: Maria Elisabetta em 1895, Maria Luigia em 1896,
Maria M. em 1907. Aqui não dá para afirmar, porque Maria era nome tão comum que vinha
composto e podia conviver. Mas registro a suspeita.""",''',
 'A.2 · as duas Angelas sao primas')

# --- os gemeos sao de Cadona ------------------------------------------
sub(u'''Santa Pandolfo teve gêmeos aos quarenta e dois anos, enterrou um deles antes do fim do
mês seguinte, e o outro atravessou o século inteiro e morreu depois de Rosa.""",''',
u'''Cadonà Maria Teresa teve gêmeos aos trinta e nove anos, enterrou um deles antes do fim do
mês seguinte, e o outro atravessou o século inteiro e morreu em 1989, três anos depois de
Rosa.

São filhos do outro ramo, o do Abele. Estão aqui porque estão no mesmo quadro, e porque
esta família, vista de longe, é uma coisa só.""",''',
 'A.2 · gemeos sao de Cadona')

sub(u'''"""Preciso corrigir aqui um erro meu, cometido na primeira vez que li esse quadro numa
fotografia ruim.''',
u'''"""Preciso corrigir aqui um segundo erro meu, bem menor que o da fileira, cometido na
primeira vez que li esse quadro numa fotografia ruim.''',
 'A.2 · encadeia o segundo erro')

# --- dois dos tres erros do quadro caem -------------------------------
sub(u'''"""E agora o problema maior, que é o próprio quadro.

<em>Storia di Castelcucco</em> é um livro de história local, feito com cuidado, e é a
melhor fonte que esta família tem sobre as gerações mais antigas. Também está errado em
pelo menos três lugares, e dá para provar.

<strong>Um.</strong> O quadro diz que Rosa nasceu em 1905. A certidão do Comune di
Monfumo, ato 31 do ano de 1903, diz 24 de junho de 1903. Documento vence livro.

<strong>Dois.</strong> O quadro põe Alessandro Domenico nascendo em 28 de janeiro de 1903.
Com Rosa nascida em junho do mesmo ano, seriam dois partos da mesma mulher em cinco
meses. Impossível. Uma das duas datas está errada, e sabemos qual não está.

<strong>Três.</strong> O quadro põe Angela em 20 de abril de 1898 e Bonfiglio também em
1898. Mesma coisa: ou são gêmeos e o quadro não diz, ou um dos anos está trocado.""",''',
u'''"""E agora o que sobra contra o quadro, que é bem menos do que eu andei dizendo.

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
 'A.1 · dois dos tres erros caem')

# --- dez filhos + a anotacao Ccucco -----------------------------------
sub(u'''Nem Galliano, que a memória familiar registra e que nenhuma das duas fontes confirma.""",''',
u'''Nem Galliano, que a memória familiar registra e que nenhuma das duas fontes confirma.

Somando o que o quadro traz e o que o índice civil acrescenta: <strong>Vincenzo Forner e
Santa Pandolfo tiveram dez filhos documentados.</strong> Não catorze, não dezesseis.""",

"""E há uma anotação minúscula, de três letras, que fecha uma divergência que estava aberta
havia meses.

Debaixo de <strong>Maria M., 1907</strong>, a caçula, o quadro traz: <em>Ccucco</em>.
Castelcucco.

Rosa nasceu em Monfumo, em 1903. A irmã caçula nasceu em Castelcucco, em 1907. Entre uma
coisa e outra a família mudou de comune. Quatro quilômetros, mais uma vez.

Isso explica, sem precisar recorrer a erro de escrivão, três coisas que não fechavam: por
que Maria Luigia se casou em Castelcucco em 1917, por que Rosa se casou em Castelcucco em
1926, e por que o ato de casamento de 1926 registra Rosina como <em>nata a
Castelcucco</em> quando a certidão de nascimento dela diz Monfumo.

Ela não nasceu lá. Ela era de lá.""",''',
 'A.3 · dez filhos e a anotacao Ccucco')

# --- o corpo de Santa Pandolfo ----------------------------------------
sub(u'''Nasceu em 1865. O primeiro filho documentado é de 1886, quando ela tinha vinte e um anos.
O último é de 1913, quando ela tinha quarenta e oito.

Vinte e sete anos parindo.

Dezesseis gestações documentadas, e é quase certo que houve mais, porque perda de
gravidez e criança morta nos primeiros dias muitas vezes não chegava ao livro da
paróquia. Tudo isso comendo polenta, carregando água, trabalhando a encosta e criando os
que iam ficando.''',
u'''Nasceu em 1865. O primeiro filho documentado é de 1886, quando ela tinha vinte e um anos.
O último é Maria M., de 1907, quando ela tinha quarenta e dois.

Vinte e um anos parindo.

Dez gestações documentadas, e é quase certo que houve mais, porque perda de gravidez e
criança morta nos primeiros dias muitas vezes não chegava ao livro da paróquia. Tudo isso
comendo polenta, carregando água, trabalhando a encosta e criando os que iam ficando.

Corrigi esses números para baixo depois de reler o quadro, e faço questão de dizer que
corrigir para baixo não alivia coisa nenhuma. Dez partos em vinte e um anos, naquela
encosta, com aquela comida, é a mesma vida.''',
 'A.2 · o corpo de Santa Pandolfo')

# =====================================================================
# C. Vincenzo estava vivo em 1940
# =====================================================================
sub(u'''Fica assim: em 1916 aquela casa, que já tinha perdido o pai e a mãe dois anos antes,
perdeu mais um. Do resto, não sei.""",''',
u'''Fica assim: em 1916 aquela casa, que tinha enterrado a mãe dois anos antes, perdeu mais
um. Do resto, não sei.""",''',
 'C · residuo "perdido o pai e a mae"')

sub(u'''Rosa tinha onze anos quando a mãe morreu. Maria M., a caçula, tinha sete. Francesco,
nascido em 1913, tinha um.

Em 1914 aquela casa perdeu a mulher que a sustentava, e perdeu-a com filho de colo
dentro dela.""",''',
u'''Rosa tinha onze anos quando a mãe morreu. Maria M., a caçula, tinha sete.

Francesco, o de 1913, que eu durante muito tempo pus como caçula dessa casa, é do outro
ramo. A mais nova ali tinha sete anos, e não um.

Em 1914 aquela casa perdeu a mulher que a sustentava.""",''',
 'C · idades na morte de Santa (cap 4)')

sub(u'''A cena de orfandade dupla era minha, não dos documentos. Fica registrada aqui como erro
corrigido, porque este livro tem a obrigação de mostrar onde errou.""",''',
u'''A cena de orfandade dupla era minha, não dos documentos. Fica registrada aqui como erro
corrigido, porque este livro tem a obrigação de mostrar onde errou.""",

"""E depois de escrever isso, achei a linha.

Está na <em>carta d'identità</em> de Sante Forner, emitida pelo Comune di Asolo em 8 de
março de 1940. No campo da filiação, o escrivão escreveu duas linhas, uma embaixo da
outra:

<strong>Padre: di Vincenzo.</strong>
<strong>Madre: fu Pandolfo Domenica Santa.</strong>

Em documento italiano, <em>di</em> antes do nome do pai quer dizer pai vivo. <em>fu</em>
quer dizer falecido. São fórmulas fixas, e o mesmo homem usou uma em cada linha, na mesma
caneta, no mesmo minuto.

Se a leitura estiver certa, e ela ainda precisa ser conferida numa digitalização melhor do
que a que tenho, <strong>Vincenzo Forner estava vivo em março de 1940</strong>. Com
setenta e sete anos. Treze anos depois de as duas filhas embarcarem.""",''',
 'C · a carta d identita (di vs fu)')

sub(u'''"""E fica uma pergunta que o Comune de Monfumo responde em uma tarde, e que hoje é a mais
importante em aberto deste livro:

<strong>quando morreu Vincenzo Forner?</strong>

Se morreu antes de 1927, Rosa saiu da Itália órfã dos dois.

Se estava vivo, então em algum dia de outubro de 1927 um homem de sessenta e cinco anos
se despediu de duas filhas na porta de casa sabendo que não as veria nunca mais.

São dois livros diferentes, e a diferença cabe numa linha de cartório.""",''',
u'''"""A pergunta que eu carreguei durante todo este capítulo era esta: <strong>quando morreu
Vincenzo Forner?</strong>

Se tivesse morrido antes de 1927, Rosa teria saído da Itália órfã dos dois.

Duas letras num documento de 1940 dizem que não foi assim. Então a cena é a outra, e ela
tem idade e tem data: em algum dia de outubro de 1927, um homem de sessenta e cinco anos
se despediu de duas filhas na porta de casa e não as viu nunca mais.

Ainda estava vivo treze anos depois, quando o filho que ficou foi tirar carteira de
identidade em Asolo.

Falta o ato de óbito, que deve estar em Castelcucco ou em Monfumo, a partir de 1940. Mas
a pergunta deixou de ser um buraco e virou uma linha de pesquisa.""",''',
 'C · o fecho do capitulo 4')

# =====================================================================
# D. Pandolfo Domenica Santa tem documento
# =====================================================================
sub(u'''Índice é ferramenta de busca. Não é prova. Eu tinha me esquecido disso.""",''',
u'''Índice é ferramenta de busca. Não é prova. Eu tinha me esquecido disso.""",

"""Escrevi tudo isso. E depois achei o documento.

A <em>carta d'identità</em> de Sante Forner, emitida em Asolo em 8 de março de 1940,
registra o nome da mãe dele por extenso:

<strong>Pandolfo Domenica Santa.</strong>

Dois prenomes na mesma mulher, no mesmo documento, escritos pelo mesmo escrivão, que não
tinha motivo nenhum para inventar um nome do meio.

O registro de 1893, o de <em>Sante Domenico</em>, filho de Vincenzo e de <em>Pandolfo
Domenica</em>, não é de outro casal. É dela.

<strong>Sante Forner é irmão de Rosa.</strong> O capítulo 7 deste livro é sobre o irmão
dela, e agora eu posso dizer isso sem me apoiar na genealogia impressa.""",''',
 'D · Pandolfo Domenica Santa confirmada')

sub(u'''Uma tarde de trabalho decide se o capítulo 7 deste livro é sobre um irmão ou sobre um
primo. Enquanto isso não estiver na mão, ele está escrito como irmão, que é o que a
genealogia impressa afirma, e esta página existe para que ninguém tome isso por
certeza.""",''',
u'''O pedido continua de pé e continua valendo a pena, porque o ato inteiro traz o endereço da
casa, a profissão do pai e a idade da mãe, que é material de capítulo e não só de
conferência.

O que mudou foi o peso. Quando escrevi esta página pela primeira vez, aquelas duas folhas
decidiam se o capítulo 7 era sobre um irmão ou sobre um primo. Não decidem mais. Isso já
foi decidido, e por um documento que estava no acervo desde o começo, guardado numa pasta
que eu tinha aberto sem olhar direito.""",''',
 'D · o ato 15 deixa de ser decisivo')

# =====================================================================
# B. Vancouver: alinhar 4, 5 e 8
# =====================================================================
sub(u'''O tronco documentado começa em Jacobus Miotto, casado com Anna Fidato. Camponeses, sem
mais nada anotado. Dos filhos, quatro deixaram descendência registrada: Luigi, Giovanni,
Antonio e Giuseppe.''',
u'''O tronco documentado começa em Jacobus Miotto, casado com Anna Fidato. Camponeses, sem
mais nada anotado. Dos filhos, quatro deixaram descendência registrada: Luigi, Giovanni,
Antonio e Giuseppe.

Registro desde já que a ligação entre esse casal e o Luigi que é pai de Fausto vem da
genealogia impressa, e não de um ato de nascimento. Falta o documento que amarra os dois.
Isso vai importar daqui a três páginas.''',
 'B · ressalva no tronco Miotto')

sub(u'''Não vou escolher entre as duas. Registro que existe uma sepultura em Vancouver com o
sobrenome desta família, e que ela ainda não foi visitada.""",''',
u'''Não vou escolher entre as duas. Registro que existe uma sepultura em Vancouver com o
sobrenome desta família, e que ela ainda não foi visitada.

O que decide é uma folha só: o ato de nascimento de Luigi Miotto, no Comune di Monfumo,
por volta de 1874 ou 1875. Se vier com pai Giacomo e mãe Anna Fidato, o ramo canadense é
família, e Louie passa a ser irmão de Luigi e tio de Fausto, uma geração acima de onde eu
o tinha posto. Se vier outro casal, ele se desprende desta história e vai embora levando
só o sobrenome.""",''',
 'B · o que resolve Vancouver')

sub(u'''Uma esvaziada pela morte dos pais e pela guerra. A outra esvaziada por um pai que foi
para o outro lado do mundo e não voltou.''',
u'''Uma marcada pela morte da mãe e pela guerra. A outra por uma ausência do outro lado do
mundo que eu ainda não consigo nomear com certeza.''',
 'B · fecho do cap 4 sem afirmar Vancouver')

sub(u'''Quando chegou a vez do Fausto, ninguém precisou convencê-lo de nada. Brasil não era
proposta, era uma coisa que se sabia, como se sabe o caminho de Asolo.

E ele tinha um exemplo em casa. O pai dele, Luigi, já tinha atravessado o Atlântico para
o Canadá.""",''',
u'''Quando chegou a vez do Fausto, ninguém precisou convencê-lo de nada. Brasil não era
proposta, era uma coisa que se sabia, como se sabe o caminho de Asolo.

Não foi exemplo de ninguém em particular. Era o que a região inteira já tinha aprendido a
fazer.""",''',
 'B · novo fecho do cap 5')

sub(u'''Fausto era filho de um homem que tinha atravessado o Atlântico para o Canadá e morrido em
Vancouver. Cresceu sabendo que ir embora era uma coisa que os homens da família dele
faziam.''',
u'''Fausto cresceu sem o pai por perto, numa vila em que ir embora era uma das coisas que os
homens faziam. Para onde Luigi Miotto foi, e se é dele a sepultura de Vancouver, o
capítulo 4 deixa em aberto, e eu deixo também.''',
 'B · cap 8 para de afirmar Vancouver')

# =====================================================================
# C (cont). Cap 8: Rosa nao estava sem pai
# =====================================================================
sub(u'''Vinte e três anos. Um filho de meses. Um marido do outro lado do oceano, alcançável
apenas por carta, com semanas de atraso entre a pergunta e a resposta. Sem pai, sem mãe.

A casa em que ela estava não tinha adulto nenhum acima dela.''',
u'''Vinte e três anos. Um filho de meses. Um marido do outro lado do oceano, alcançável
apenas por carta, com semanas de atraso entre a pergunta e a resposta. A mãe morta havia
doze anos.

O pai, ao que tudo indica, estava vivo. Isso eu só fui descobrir depois de ter escrito
esta página de outro jeito, e a versão anterior dizia que não havia adulto nenhum acima
dela naquela casa. Vincenzo tinha sessenta e quatro anos naquele inverno. Não sei o que
ele disse, nem se disse alguma coisa. Sei que ela foi assim mesmo.''',
 'C · cap 8, Rosa nao estava orfa de pai')

# =====================================================================
# E. Nomes e lugares
# =====================================================================
sub(u'''"""Quatro quilômetros dali, em Cavarzo, Maria Luigia estava fazendo a mesma coisa com
quatro crianças.

Dinetta com seis anos. Pulcheria com cinco. Dino com três. Danilo com um.''',
u'''"""Quatro quilômetros dali, em Cavaso del Tomba, Maria Luigia estava fazendo a mesma coisa
com quatro crianças.

Gina com seis anos. Pulcheria com cinco. Rino com três. Danilo com um.''',
 'E · cap 8, Cavaso del Tomba / Gina / Rino')

sub(u'''Filho de Vincenzo Forner e Santa Pandolfo. Quarto na lista dos dezesseis. Irmão mais
velho de Rosa, a que atravessaria o Atlântico dez anos depois de tudo isso terminar.''',
u'''Filho de Vincenzo Forner e Santa Pandolfo. Quarto na lista dos dez. Irmão mais velho de
Rosa, a que atravessaria o Atlântico dez anos depois de tudo isso terminar.''',
 'A · cap 7, quarto de dez')

sub(u'''manuais de história não registram: a mãe, Santa Pandolfo, tinha morrido no ano anterior,
em 1914. Rosa tinha doze anos. Francesco, o caçula, tinha dois.''',
u'''manuais de história não registram: a mãe, Santa Pandolfo, tinha morrido no ano anterior,
em 1914. Rosa tinha onze anos. Maria M., a caçula, tinha sete.''',
 'A · cap 7, idades na morte de Santa')

sub(u'''parados, o imposto sobre a moagem, a pelagra, os dezesseis filhos, as duas Angelas, os''',
u'''parados, o imposto sobre a moagem, a pelagra, os dez filhos, a linha errada num quadro, os''',
 'A · cap 8, recapitulacao final')

sub(u"""  (4,'Forner e Miotto','Luigi Forner, 1817. Jacobus Miotto. Vincenzo, Santa Pandolfo e os dezesseis filhos.'),""",
    u"""  (4,'Forner e Miotto','Luigi Forner, 1817. Jacobus Miotto. Vincenzo, Santa Pandolfo e os dez filhos.'),""",
 'A · subtitulo do cap 4')

# =====================================================================
# F. Capitulo 20
# =====================================================================
sub(u'''Fazia dezenove dias que tinham saído de Gênova.''',
    u'''Fazia catorze dias que tinham saído de Gênova.''',
 'F.1 · catorze dias, nao dezenove')

sub(u'''quatro filhos: Dinetta, de sete anos, Pulcheria, de seis, Dino, de quatro, e
Danilo, de dois.''',
u'''quatro filhos: Gina, de sete anos, Pulcheria, de seis, Rino, de quatro, e
Danilo, de dois.''',
 'E · cap 20, Gina e Rino')

sub(u'''idades, os nomes escritos com a grafia de quem ouviu e anotou, e a última
residência de cada uma: Castelcucco para uma, Cavarzo para a outra. Duas vilas
que hoje se cruzam de carro em quarenta minutos, e que naquela altura já estavam
a um oceano de distância.""",''',
u'''idades, os nomes escritos com a grafia de quem ouviu e anotou, e a última
residência de cada uma: Castelcucco para uma, Cavaso del Tomba para a outra. Duas
vilas que hoje se cruzam de carro em quarenta minutos, e que naquela altura já
estavam a um oceano de distância.

A grafia, aliás, não é detalhe. A menina que o ato de Cavaso registra como <strong>Gina
Oliva</strong>, nascida em 28 de março de 1920, aparece como Dinetta na lista brasileira e
como Ginita na argentina. O nome atravessou dois idiomas e um naufrágio e chegou do outro
lado com outra forma. Vai acontecer com quase todos eles.""",''',
 'E.3 · Gina Oliva e as grafias')

sub(u'''Em Dakar tinha parado por avaria na máquina de bombordo. Consertaram como se
conserta um navio de dezenove anos em porto africano, com o que havia, e
seguiram. Passageiros da primeira classe reclamaram. A companhia registrou. A
viagem continuou.''',
u'''Em algum porto da escala africana ele parou por avaria na máquina de bombordo.
Consertaram como se conserta um navio de dezenove anos longe de casa, com o que
havia, e seguiram. Passageiros da primeira classe reclamaram. A companhia
registrou. A viagem continuou.

Escrevo <em>algum porto</em> de propósito. As descrições da rota habitual do
<em>Principessa Mafalda</em> citam Dakar, mas o que as fontes registram desta
última viagem é a saída de São Vicente, em Cabo Verde, no dia 18 de outubro de
1927, com novecentos e setenta e um passageiros e duzentos e oitenta e oito
tripulantes. Ainda não tenho documento que diga em qual dos dois a máquina abriu.
Quando tiver, nomeio.''',
 'F.2 · Dakar sinalizado')

sub(u'''Na tarde de 25 de outubro de 1927 o <em>Principessa Mafalda</em> navegava a
poucas milhas do arquipélago dos Abrolhos, na costa da Bahia, a cerca de oitenta
quilômetros de Caravelas. Ia atrasado.''',
u'''Na tarde de 25 de outubro de 1927 o <em>Principessa Mafalda</em> navegava a cerca
de setenta quilômetros a leste do arquipélago dos Abrolhos, que já fica a uns
setenta da costa da Bahia. É dessa soma que sai a cifra de cento e trinta
quilômetros de litoral que circula nos relatos. Ia atrasado.''',
 'F.4 · distancia dos Abrolhos')

sub(u'''"""O comandante Simone Gulì tinha sessenta anos e trinta e nove de mar.''',
u'''"""O comandante Simone Gulì era um homem velho com uma vida inteira de mar.

As fontes não concordam sobre a idade. O Museu da Imigração registra cinquenta e
cinco anos. Uma publicação italiana o descreve como sexagenário de sessenta e
dois. Enquanto não aparecer documento, fica assim: entre os cinquenta e cinco e
os sessenta e dois, e quase quatro décadas embarcado.''',
 'F.3 · idade de Guli sinalizada')

sub(u'''"""O sol se pôs por volta das seis e meia.

Esse é o dado mais cruel da noite inteira, e é um dado meteorológico, não
literário: entre o rompimento do eixo e a escuridão completa houve pouco mais de
uma hora. Todo o resgate, todo o embarque nos botes, toda a decisão sobre quem
descia e quem esperava, tudo aconteceu no escuro, num navio inclinado, sem
energia, com lanternas.''',
u'''"""O sol se pôs às seis e vinte e um da tarde.

Esse é o dado mais cruel da noite inteira, e é um dado astronômico, não
literário. Calculado para a posição aproximada do naufrágio, dezessete graus e
cinquenta e quatro minutos de latitude sul, em 25 de outubro de 1927: pôr do sol
às 18h21, fim do crepúsculo civil às 18h48.

Entre o rompimento do eixo e o sol desaparecer houve <strong>uma hora e seis
minutos</strong>. Todo o resgate, todo o embarque nos botes, toda a decisão sobre
quem descia e quem esperava, tudo aconteceu no escuro, num navio inclinado, sem
energia, com lanternas.''',
 'F.5 · por do sol as 18h21')

sub(u'''que ela embarcou, dizem que sobreviveu, dizem que seis dias depois deu entrada
na Hospedaria dos Imigrantes do Brás com um filho de um ano no colo e foi
registrada como chefe de família.''',
u'''que ela embarcou, dizem que sobreviveu, dizem que seis dias depois deu entrada
na Hospedaria dos Imigrantes do Brás com um filho de um ano no colo.

A página em que ela aparece parece registrá-la na condição de chefe da própria
família, o que numa entrada de 1927 não é pouca coisa. Digo <em>parece</em>
porque a digitalização que tenho não me deixa ler a coluna de parentesco com
segurança, e isso é afirmação forte demais para se fazer em cima de uma imagem
ruim.''',
 'J · chefe de familia sinalizado')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d correcoes aplicadas em build_livro.py' % n[0])
