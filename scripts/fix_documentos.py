# -*- coding: utf-8 -*-
"""Aplica ao livro os dados das certidoes e do livro Storia di Castelcucco."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    s = s.replace(old, new, 1)
    print('ok', label)

# ============================================================== CAPITULO 1
sub(u'''"""Rosa Forner nasceu em 1903, em Monfumo, quatro quilômetros dali.

Fausto Miotto nasceu no ano seguinte, em Castelcucco.

Quatro quilômetros, no Vêneto rural daquela época, não são distância nenhuma e são
distância suficiente. Duas paróquias, dois padres, dois livros de batismo. Mas a
mesma feira, os mesmos santos, as mesmas festas, e famílias que se cruzavam havia
gerações sem precisar de apresentação.

Casaram-se em 1926. Ela com vinte e três anos, ele com vinte e dois.

Não existe registro nenhum de como foi. Não é uma história de amor documentada. É o
que acontecia.""",''',
u'''"""Rosa Forner nasceu às oito e quinze da noite de 24 de junho de 1903, em Monfumo,
quatro quilômetros dali.

Fausto Miotto nasceu às quatro da manhã de 5 de julho de 1904, em Castelcucco.

Esses horários não vêm de memória de família. Vêm dos registros de nascimento dos dois
comuni, atto 31 do ano de 1903 e atto 33 do ano de 1904, que estão hoje em cima da minha
mesa em cópia autenticada.

Quatro quilômetros, no Vêneto rural daquela época, não são distância nenhuma e são
distância suficiente. Duas paróquias, dois padres, dois livros de batismo. Mas a mesma
feira, os mesmos santos, as mesmas festas, e famílias que se cruzavam havia gerações sem
precisar de apresentação.

Casaram-se em 3 de dezembro de 1926, em Castelcucco. Ela com vinte e três anos, ele com
vinte e dois.

O que aconteceu entre esses dois nascimentos e aquele casamento é o assunto de todo o
resto desta parte do livro.""",''', 'cap1 nascimentos exatos')

# ============================================================== CAPITULO 2
sub(u'''"""Luigi Forner nunca foi a lugar nenhum.

Nasceu súdito austríaco em 1817, virou italiano aos quarenta e nove anos sem sair de
casa, e foi enterrado numa terra que trocou de país debaixo dos pés dele. O filho,
Vincenzo, nasceu austríaco em 1862 e virou italiano aos quatro.

Nenhum dos dois atravessou coisa alguma. A fronteira é que atravessou os dois.

Foi a neta de Luigi, filha de Vincenzo, quem finalmente se mexeu. Ela se chamava Rosa,
nasceu em 1903, e para ela a Itália sempre tinha existido.""",''',
u'''"""Luigi Forner nasceu em 14 de agosto de 1817, em Monfumo, súdito austríaco.

Virou italiano aos quarenta e nove anos sem sair de casa. O filho dele, Vincenzo, nascido
em 6 de agosto de 1862, também nasceu austríaco e virou italiano aos quatro.

A fronteira atravessou os dois enquanto os dois estavam parados.

Durante muito tempo eu achei que a história de Luigi terminava aí, e escrevi assim: o
homem que nunca foi a lugar nenhum e a quem o mapa mudou debaixo dos pés.

Estava errado.""",

"""A genealogia impressa em <em>Storia di Castelcucco</em>, o livro de história local que
reconstruiu essas linhagens, traz ao lado do nome dele uma anotação de seis palavras:

<em>emigrato in America dopo il 1891.</em>

Luigi Forner emigrou. Depois de 1891, quando já tinha passado dos setenta e quatro anos.

Morreu em 11 de novembro de 1905, aos oitenta e oito.""",

"""Não sei para onde foi, não sei se sozinho, não sei se voltou, não sei onde está
enterrado. A frase não diz. América, naquele vocabulário, tanto pode ser o Brasil quanto
a Argentina, os Estados Unidos ou o Canadá.

Sei que ele fez alguma coisa que não cabe na versão fácil desta família.

O homem mais velho de que temos notícia, nascido antes de a Itália existir, camponês de
uma encosta de oito quilômetros quadrados, atravessou o Atlântico depois dos setenta.

Trinta e seis anos antes da neta.""",

"""E há mais uma geração atrás dele, que o mesmo livro registra e que ninguém desta
família conhecia.

O pai de Luigi chamava-se <strong>Domenico Forner</strong>, casado com <strong>Maria
Vial</strong>.

Não tenho data de nenhum dos dois. Tenho os nomes, e os nomes empurram esta história para
o século XVIII.

De Domenico e Maria até João Luca, nascido em 2012, são oito gerações documentadas, e
sete delas nunca souberam que a oitava existiria.""",''', 'cap2 Luigi emigrou')

# ============================================================== CAPITULO 4
sub(u'''"""O nome mais antigo é Luigi Forner, nascido em 1817.

Ele se casou com Elisabetta Forner.''',
u'''"""O nome mais antigo com data é Luigi Forner, nascido em 14 de agosto de 1817, em
Monfumo, e morto em 11 de novembro de 1905. Atrás dele há ainda os pais, Domenico Forner
e Maria Vial, sem datas.

Luigi casou-se com Elisabetta Forner.''', 'cap4 Luigi datas')

sub(u'''"""Do casamento de Luigi vieram, entre outros, dois filhos que continuaram a linha:
Domenico Alessandro Forner, de 1853, e Vincenzo Forner, de 1862.

É Vincenzo que interessa aqui, porque é dele que descende esta história.

Vincenzo Forner casou-se com Santa Pandolfo, nascida em 1865.

Segundo o levantamento da família, os dois tiveram dezesseis filhos documentados.""",''',
u'''"""Do casamento de Luigi vieram três filhos documentados: Domenico Alessandro, nascido
em 20 de setembro de 1853 e morto em 25 de janeiro de 1928; Vincenzo, nascido em 6 de
agosto de 1862; e Abele Alessandro, nascido em 16 de agosto de 1865 e morto em 20 de
março de 1954.

Todos os três nasceram em Monfumo.

É Vincenzo que interessa aqui, porque é dele que descende esta história.""",

"""Vincenzo Forner casou-se com Santa Pandolfo, nascida em 1º de novembro de 1865.

O casamento está no índice dos atos de matrimônio do comune: <strong>ano de 1887, ato
número 6</strong>.

Guarde essa data por um instante. Ela vai voltar ao fim deste capítulo, e vai voltar
acompanhada.""",''', 'cap4 filhos de Luigi e casamento 1887')

sub(u'''"""Angela em 1886. Angela outra vez em 1898.''',
u'''"""A primeira coisa que a lista diz, e diz sem querer, é sobre a ordem dos
acontecimentos.

Vincenzo e Santa casaram-se em 1887. A filha Angela nasceu em 1886.

A criança veio primeiro. Um ano antes.""",

"""Angela em 1886. Angela outra vez em 1898.''', 'cap4 Angela antes do casamento')

sub(u'''"""E há uma linha que não precisa de interpretação nenhuma.

Roberto Forner, 1908 a 1908.

Nasceu e morreu no mesmo ano. É o único da lista cuja vida inteira cabe num número
repetido.

No mesmo ano de 1908 nasceu Ausilio Fortunato, que viveu até 1989. Não sei se eram gêmeos
e um não resistiu, ou se Roberto morreu cedo no ano e Ausilio nasceu depois. As duas
coisas são comuns. As duas contam a mesma história.""",''',
u'''"""Duas linhas não precisam de interpretação nenhuma.

<strong>Angela, nascida em 20 de abril de 1898, morta em 17 de abril de 1900.</strong>
Três dias antes de completar dois anos.

<strong>Ausilio Fortunato, nascido em 10 de junho de 1908. Roberto, nascido em 10 de junho
de 1908.</strong>

A mesma data nos dois. Eram gêmeos.

Ausilio viveu até 1989, oitenta e um anos. Roberto morreu ainda em 1908.

Santa Pandolfo teve gêmeos aos quarenta e dois anos, enterrou um deles no mesmo ano, e o
outro atravessou o século inteiro.""",''', 'cap4 gemeos confirmados')

sub(u'''"""E aí chega a linha que mudou o modo como eu entendo esta família inteira.

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

Enquanto não estiver na mão, fica como está aqui: forte, provável e não confirmado.""",''',
u'''"""E aí chega a linha que muda o modo como entendo esta família.

<strong>Santa Pandolfo: 1º de novembro de 1865 a 1914.</strong>

Rosa tinha onze anos quando a mãe morreu. Maria M., a caçula, tinha sete. Francesco,
nascido em 1913, tinha um.

Em 1914 aquela casa perdeu a mulher que a sustentava, e perdeu-a com filho de colo
dentro dela.""",

"""Durante um tempo eu escrevi que o pai tinha morrido no mesmo ano, e montei em cima
disso uma cena de orfandade completa.

Fui verificar. Não se sustenta.

A genealogia impressa em <em>Storia di Castelcucco</em> traz, ao lado de Santa Pandolfo,
a anotação de morte em 1914. Ao lado de Vincenzo, nascido em 6 de agosto de 1862, não traz
data de morte nenhuma.

Ou seja: <strong>não sabemos quando Vincenzo Forner morreu.</strong> Pode ter sido em
1914, pode ter sido vinte anos depois. Pode ter estado vivo, e provavelmente estava,
quando a filha embarcou em 1927.

A cena de orfandade dupla era minha, não dos documentos. Fica registrada aqui como erro
corrigido, porque este livro tem a obrigação de mostrar onde errou.""",

"""O que continua de pé, e é bastante, é isto.

Rosa Forner perdeu a mãe aos onze anos, em 1914, no ano em que a Europa entrou em guerra.
No ano seguinte a Itália entrou junto e levou os irmãos dela.

A irmã mais velha, Maria Luigia, tinha dezoito anos em 1914 e ficou com a casa.

A partida de 1927 não sai de uma casa cheia. Sai de uma casa que já tinha perdido a mãe e
mandado os homens para a montanha.""",

"""E fica uma pergunta que o Comune de Monfumo responde em uma tarde, e que hoje é a mais
importante em aberto deste livro:

<strong>quando morreu Vincenzo Forner?</strong>

Se morreu antes de 1927, Rosa saiu da Itália órfã dos dois.

Se estava vivo, então em algum dia de outubro de 1927 um homem de sessenta e cinco anos
se despediu de duas filhas na porta de casa sabendo que não as veria nunca mais.

São dois livros diferentes, e a diferença cabe numa linha de cartório.""",''',
    'cap4 correcao 1914')

# Miotto: dados oficiais
sub(u'''"""Do outro lado da história estão os Miotto, e deles sabemos menos.

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
Estava repetindo o pai.""",''',
u'''"""Do outro lado da história estão os Miotto.

O tronco documentado começa em Jacobus Miotto, casado com Anna Fidato. Camponeses, sem
mais nada anotado. Dos filhos, quatro deixaram descendência registrada: Luigi, Giovanni,
Antonio e Giuseppe.

O certificado de casamento corrige um nome que a família repetia errado havia décadas.
Luigi Miotto não se casou com Nina Ganeo. Casou-se com <strong>Domenica Ganeo</strong>,
em 24 de junho de 1900, no <strong>Comune di Maser</strong>, ato número 18. Ele tinha
vinte e cinco anos e era nascido em Monfumo. Ela tinha vinte e um e era de Maser.

Repare onde Luigi nasceu: <strong>Monfumo</strong>. A mesma vila dos Forner. Os Miotto
desta história não são de Castelcucco de origem. Chegaram lá depois.""",

"""Fausto nasceu quatro anos depois desse casamento, em Castelcucco, e é o registro dele
que fecha a conta: <em>figlio di Luigi e Ganeo Domenica</em>, 5 de julho de 1904, às
quatro da manhã.

Entre 1900 e 1904 aquele casal saiu de Maser e foi parar em Castelcucco. Quatro
quilômetros, outra vez.

Nesta história inteira, ninguém se muda mais do que quatro quilômetros por vez, até o dia
em que alguém atravessa um oceano.""",

"""E aqui há uma simetria que passou despercebida por décadas.

Luigi Miotto, o pai de Fausto, também emigrou. Não para o Brasil. Para o Canadá.

Existe, no acervo desta família, uma <em>Registration of Death</em> da Província da
Colúmbia Britânica, número 5509-008734. Ela registra a morte de <strong>Louie
Miotto</strong>, em 15 de agosto de 1955, em Vancouver, morto na chegada ao Vancouver
General Hospital.

Nascido em março de 1880, na Itália. Setenta e cinco anos. Quarenta e oito anos no
Canadá, o que põe a chegada dele por volta de 1907. Lenhador aposentado, vinte e cinco
anos na profissão, última vez que trabalhou em 1951. Morava na Prior Street, número 566.

Pai: <strong>Miotto Jack</strong>. Mãe: <strong>Fedato Anna</strong>.

Jack é como um oficial canadense escreve Giacomo. Fedato é como ele escreve Fidato. São
Jacobus Miotto e Anna Fidato, o casal que abre o tronco Miotto deste livro.

Está enterrado no Mountain View Cemetery, em Vancouver. Quem assinou como informante foi
um irmão, John Miotto, que morava no mesmo endereço.""",

"""Só que o documento traz duas linhas que não fecham.

Diz que ele nasceu em <strong>março de 1880</strong>. O certificado de casamento de Maser
diz que Luigi Miotto tinha vinte e cinco anos em junho de 1900, o que o põe nascendo por
volta de 1875.

E diz, no campo de estado civil, uma palavra só: <strong>Single</strong>. Solteiro.

Ou são dois irmãos diferentes, ambos filhos de Jacobus e Anna, e o Luigi que foi para
Vancouver não é o pai de Fausto.

Ou é o mesmo homem, que deixou mulher e um filho de três anos em Castelcucco por volta de
1907, refez a vida do outro lado do mundo, e morreu meio século depois registrado como
solteiro por um irmão que ou não sabia, ou não quis dizer.

Não vou escolher entre as duas. Registro que existe uma sepultura em Vancouver com o
sobrenome desta família, e que ela ainda não foi visitada.""",''', 'cap4 Miotto documentado')

# ============================================================== CAPITULO 7
sub(u'''Naquele mesmo momento, na casa em que ele tinha crescido, havia um detalhe que os
manuais de história não registram: o pai e a mãe tinham morrido no ano anterior, em
1914. Rosa tinha doze anos. O caçula tinha dois.

Ele saiu de uma casa que já estava órfã.""",''',
u'''Naquele mesmo momento, na casa em que ele tinha crescido, havia um detalhe que os
manuais de história não registram: a mãe, Santa Pandolfo, tinha morrido no ano anterior,
em 1914. Rosa tinha doze anos. Francesco, o caçula, tinha dois.

Ele saiu de uma casa que tinha acabado de enterrar a mãe.""",''', 'cap7 orfandade corrigida')

# ============================================================== CAPITULO 8
sub(u'''"""Não existe fotografia do casamento.

Não existe convite, não existe lista de convidados, não existe registro do que se comeu.
O que existe é um ano, 1926, anotado numa árvore genealógica montada quase um século
depois.

Rosa Forner tinha vinte e três anos. Fausto Miotto tinha vinte e dois.

Ela era de Monfumo, ele de Castelcucco, e entre as duas casas havia quatro quilômetros de
estrada que os dois conheciam desde sempre.""",''',
u'''"""Não existe fotografia do casamento. Não existe convite, não existe lista de
convidados, não existe registro do que se comeu.

O que existe é uma linha, escrita à margem da certidão de nascimento dela, no livro do
Comune di Monfumo:

<em>ha contratto matrimonio con Miotto Fausto in data 03/12/1926 a Castelcucco.</em>

E a mesma informação do outro lado, à margem da certidão dele, no livro do Comune di
Castelcucco: ato número 9, parte I, do ano de 1926. Ali ela aparece com o diminutivo,
<strong>Forner Rosina</strong>.

Casaram-se em <strong>3 de dezembro de 1926</strong>, em Castelcucco. Ela com vinte e
três anos, ele com vinte e dois.""",''', 'cap8 data do casamento')

sub(u'''"""Em 10 de outubro de 1926 nasceu Enrico Miotto.

Essa data não vem de memória de família. Vem do Registro de Estrangeiros que ele assinou
em São Paulo em 1949, com nacionalidade italiana, pai Fausto Miotto, mãe Rosa Forner.

Ponha as duas informações lado a lado: casamento em 1926, filho nascido em outubro de
1926.

Se o casamento foi no começo do ano, a criança veio logo depois. Se foi mais tarde, Rosa
já estava grávida quando se casou. As duas coisas eram absolutamente corriqueiras naquele
mundo, e nenhuma das duas é assunto de ninguém.

Registro só porque o livro da paróquia tem a data exata do casamento, e um dia alguém vai
lê-la.""",''',
u'''"""Agora ponha a outra data ao lado.

Enrico Miotto nasceu em <strong>10 de outubro de 1926</strong>. Está no Registro de
Estrangeiros que ele assinou em São Paulo em 1949: nacionalidade italiana, pai Fausto
Miotto, mãe Rosa Forner.

O casamento foi em 3 de dezembro de 1926.

<strong>O filho nasceu cinquenta e quatro dias antes de os pais se casarem.</strong>""",

"""Quando eu tinha só o ano do casamento, escrevi que talvez Rosa estivesse grávida na
cerimônia. Não estava. Ela estava com um bebê de quase dois meses no colo.

Isso não é escândalo e não é fofoca de cartório. É informação sobre como aquela vida
funcionava.

Numa vila católica do Vêneto de 1926, um filho nascido antes do casamento e reconhecido
oito semanas depois quer dizer que houve uma relação estável antes, e que a formalização
esperou alguma coisa. Dinheiro, autorização de família, a vinda de um padre, o fim de uma
colheita, uma papelada. Não dá para saber qual.

E há uma coincidência que o capítulo 4 já mostrou: <strong>trinta e nove anos antes, os
pais de Rosa fizeram exatamente a mesma coisa.</strong> Vincenzo e Santa casaram-se em
1887, e a primeira filha, Angela, nasceu em 1886.

Duas gerações, a mesma sequência.""",''', 'cap8 Enrico antes do casamento')

sub(u'''"""E aí, com o filho recém-nascido, Fausto foi embora.''',
u'''"""E aí, com o casamento feito e o filho de meses, Fausto foi embora.''', 'cap8 fausto parte')

sub(u'''Rosa era órfã de pai e de mãe desde os onze anos. Tinha perdido um irmão na guerra, o
Pietro Luigi, em 1916. Tinha outro irmão, o Sante, que voltou do Monte Grappa com três
medalhas e o silêncio que normalmente vem junto. Tinha sido criada, na prática, pela irmã
mais velha, Maria Luigia.''',
u'''Rosa tinha perdido a mãe aos onze anos. Tinha perdido um irmão, Pietro Luigi, em 1916,
de causa que continua desconhecida. Tinha outro irmão, Sante, que voltou do Monte Grappa
com três medalhas e o silêncio que normalmente vem junto. Tinha sido criada, na prática,
pela irmã mais velha, Maria Luigia.''', 'cap8 perfil da Rosa')

io.open(f, 'w', encoding='utf-8').write(s)
print('\nOK: livro atualizado com os documentos')
