# -*- coding: utf-8 -*-
"""Gera terceira-classe.html: o livro folha a folha, navegavel por scroll."""
import os, base64, io, json, html

SP = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(SP, 'img')

def b64(key):
    p = os.path.join(IMG, key + '.webp')
    if not os.path.exists(p):
        raise SystemExit('imagem inexistente: ' + key)
    with open(p, 'rb') as f:
        return 'data:image/webp;base64,' + base64.b64encode(f.read()).decode()

E = html.escape

# ---------------------------------------------------------------- capitulos
BOOKS = [
    ('I',  'A terra que não bastava',   '1861 – 1926', 'ochre'),
    ('II', 'A travessia',             '1874 – 1927', 'sea'),
    ('III','O navio',                 '1908 – 1928', 'verm'),
    ('IV', 'Os que chegaram',         '1927 – hoje', 'terra'),
]

CAPS = {
 'I': [
  (1,'Uma casa em Castelcucco','O mundo antes. A vila, as colinas, o ano agrícola, o sino da igreja.'),
  (2,'A Itália que não existia','O Risorgimento e o mosaico que a unificação não uniu.'),
  (3,'Dívida, imposto, fome','Concentração de terras, impostos, dívida, pelagra.'),
  (4,'Forner e Miotto','Luigi Forner, 1817. Vincenzo, Santa Pandolfo e os dez filhos. Duas casas a quatro quilômetros.'),
  (5,'O cartaz','Agenciadores, promessas, fare l’America. A propaganda e o que ela escondia.'),
  (6,'O Decreto Prinetti','1902: a Itália proíbe a emigração subsidiada para o Brasil.'),
  (7,'Sante nos Alpes','A Grande Guerra, as trincheiras, as três medalhas. O ramo que ficou.'),
  (8,'Rosa e Fausto','Casamento em 1926. Fausto parte. Enrico nasce em 10 de outubro.'),
 ],
 'II': [
  (9,'Gênova','O porto como sistema. A babel de dialetos, a despedida definitiva.'),
  (10,'A terceira classe','O porão por dentro: beliches, comida racionada, os corpos jogados ao mar.'),
  (11,'O negócio da esperança','Companhias de navegação, preço da passagem, dívida, agenciadores.'),
  (12,'Duas irmãs embarcam','Outubro de 1927. Rosa com Enrico de um ano. Maria Luigia com quatro filhos.'),
  (13,'Escala em Dakar','As falhas de máquina, os alertas, a decisão de seguir viagem.'),
  (14,'Os que já estavam lá','Fausto e Angelo no Brasil, a casa preparada, a espera.'),
  (15,'O que o Brasil prometia','Café, contrato de colono, e a fronteira entre trabalho livre e o que veio antes.'),
 ],
 'III': [
  (16,'1908','Construção, o batismo com o nome da princesa, o orgulho da marinha mercante.'),
  (17,'Os anos de glória','Primeira classe, salões, diplomatas e industriais. O navio como vitrine.'),
  (18,'O declínio','Envelhecimento, quebras, a conversão em navio de imigrante.'),
  (19,'A última viagem','Quem estava a bordo. Garovaglio, von Lücken, Bucherer, o comandante Gulì.'),
  (20,'17h15','O eixo da hélice de bombordo se rompe.'),
  (21,'A noite','Hora a hora, do estrondo às 22h10.'),
  (22,'Os botes','Lugares vendidos, botes danificados, os tubarões.'),
  (23,'22h10','O navio afunda. Gulì fica a bordo.'),
  (24,'Alhena, Mosella, Empire Star','O resgate a noite inteira.'),
  (25,'Os 314','Os mortos, o inquérito, a lenda do ouro, e por que o Brasil esqueceu.'),
 ],
 'IV': [
  (26,'31 de outubro','Hospedaria do Brás. Livro 100, página 290.'),
  (27,'O reencontro','Fausto e Angelo recebem as mulheres e as crianças.'),
  (28,'Terra vermelha','O interior paulista, o café, uma vida construída do zero.'),
  (29,'Enrico','1926 a 1998.'),
  (30,'1937','Mafalda nasce em São José do Rio Pardo e recebe o nome do navio.'),
  (31,'Virar brasileiro','Língua, comida, fé, o dialeto que some.'),
  (32,'Os que ficaram, cem anos depois','A linha de Sante: Galliano, Giorgio.'),
  (33,'A busca','A pesquisa como enredo. O dia em que o registro apareceu.'),
  (34,'A casa','Castelcucco hoje. A porta de onde a Rosa saiu.'),
 ],
}

# --------------------------------------------------- capitulos escritos
CAP19 = [
"""O <em>Principessa Mafalda</em> saiu de Gênova em 11 de outubro de 1927, e já saiu
atrasado.

Não muito. Um dia, mais ou menos. O tipo de atraso que ninguém anota e que todo mundo esquece
assim que o navio pega o mar.

Dezoito anos antes, quando ele foi lançado, um atraso desses teria virado assunto de jornal.
Em 1927 já não virava. Era um navio velho fazendo o que navio velho faz.""",

"""A bordo iam <strong>novecentos e setenta e um passageiros e duzentos e oitenta e oito
tripulantes</strong>. Mil duzentas e cinquenta e nove pessoas, e a maior parte delas na
terceira classe.

Só que já não era o porão italiano de vinte anos antes.

Os manifestos de 1923 e 1924, que estão no Arquivo Público de São Paulo, mostram a virada
acontecendo: em agosto de 1923 desembarcaram em Santos sessenta e cinco italianos e vinte e
oito sírios. Em janeiro de 1924, quarenta sírios e trinta e dois italianos.

Cinco meses, e a proporção inverteu.

Quando Rosa embarcou, o porão do Mafalda falava italiano, árabe, servo-croata, húngaro e
alemão. A lista dos náufragos resgatados confirma: dos cinquenta imigrantes desembarcados no
Rio, quarenta e três eram italianos, quatro iugoslavos e três húngaros.""",

"""Sete dessas pessoas interessam a este livro.

Rosa Forner, vinte e quatro anos, com Enrico no colo. A irmã mais velha, Maria Luigia, trinta
e um, com Ginneta, Pulgheria, Rino e Danilo. Terceira classe, embarque em Gênova.

E é tudo o que eu sei delas nesses catorze dias.

Não existe um documento sequer que registre o que aquelas sete pessoas fizeram entre 11 e 25
de outubro de 1927. Elas entram no papel antes, na lista de embarque, e voltam ao papel
depois, na lista dos náufragos. No meio há duas semanas em branco.

O que dá para fazer é reconstruir o navio em volta delas. É o que este capítulo faz.""",

"""E aqui eu preciso dizer de onde vem quase tudo o que vem a seguir.

Nos dias seguintes ao naufrágio, jornais da Argentina e do Brasil entrevistaram dezenas de
sobreviventes. Vinte desses depoimentos chegaram até mim, em tradução, com nome, idade e
procedência de cada depoente.

São a melhor fonte que existe sobre esta travessia. São, na prática, a <em>única</em> fonte
sobre o que se passou dentro daquele navio.

Ainda não localizei o jornal, a data e a página de cada um. Estou atrás. Enquanto não achar,
uso os depoimentos e digo, toda vez, o que eles são: relatos colhidos por repórteres, poucos
dias depois, de gente que tinha acabado de sair da água.

Isso não é pouco. E não é prova.""",

"""O navio quebrou pela primeira vez logo no começo.

Chegou a Barcelona com cerca de um dia de atraso, por problema de máquina. Consertaram e
seguiram.

Pouco depois de Gênova, um passageiro argentino chamado <strong>Patricio de Rosas</strong>
conversou no convés com <strong>Antonio Zanni</strong>, gerente do Hotel Savoia de Capilla del
Monte, na província de Córdoba. Zanni tinha andado perto da casa de máquinas e contou o que
viu: os mecânicos vinham consertando avarias sucessivas.

De Rosas perguntou se o chefe de máquinas tinha dito que estava tudo resolvido.

Zanni respondeu que não. Faltava um pouco de trabalho, e esse pouco podia ser feito no curso
da viagem.""",

"""Havia também as coisas pequenas, que numa travessia de duas semanas deixam de ser pequenas.

Os banheiros funcionavam mal.

A refrigeração funcionava mal, e refrigeração ruim num navio que cruza o Equador em outubro
não é conforto: é comida.

Passageiros da primeira classe reclamaram. A companhia registrou as reclamações, que é o que
companhia faz com reclamação.

Nada disso, sozinho, é catástrofe. Tudo isso junto é um navio que já não deveria estar
naquela linha.""",

"""Em algum porto da escala africana o Mafalda parou outra vez, por avaria na máquina de
bombordo.

Escrevo <em>algum porto</em> pelo mesmo motivo que vou escrever no capítulo seguinte: as
descrições da rota habitual do navio citam Dakar, mas o que as fontes registram desta última
viagem é a saída de <strong>São Vicente, em Cabo Verde, no dia 18 de outubro</strong>, rumo
ao Rio.

Consta como parada emergencial. Consertaram mais uma vez, com o que havia, e seguiram mais
uma vez.

Restavam sete dias.""",

"""Foi por volta desse ponto da viagem que dois passageiros tentaram fazer o navio parar.

De Rosas caminhava pelo convés numa manhã quando encontrou <strong>Antonio Fontana</strong>,
uruguaio, que trazia exatamente o mesmo medo. Os dois conversaram sobre o que estavam vendo e
chegaram à mesma conclusão.

Decidiram redigir um protesto coletivo, assinado pelos passageiros, para entregar ao
comandante.

O pedido era um só: que a viagem fosse suspensa.""",

"""Começaram a falar com outras pessoas a bordo.

Um passageiro chamado <strong>Camilo Rivarola</strong> os desaconselhou. Um abaixo-assinado
desses, disse ele, não pararia navio nenhum. Serviria só para transformá-los em inimigos do
capitão, e ainda faltavam muitos dias de viagem sob a autoridade daquele homem.

O argumento venceu.

O documento não foi escrito. Ninguém assinou nada. A viagem seguiu.

<strong>Antonio Fontana perdeu o irmão, Eduardo, na noite de 25 de outubro.</strong>""",

"""Eu li esse trecho do depoimento umas dez vezes antes de escrever este parágrafo, porque ele
tem uma coisa que a maior parte das histórias de naufrágio não tem.

Normalmente o que se conta é que ninguém sabia.

Aqui, duas pessoas sabiam, escreveram na cabeça o que precisava ser feito, e foram convencidas
por um terceiro de que não valia a pena por causa do incômodo político de encarar a autoridade
do navio.

Rivarola não estava errado sobre o abaixo-assinado. Provavelmente não teria parado nada
mesmo.

Ele estava errado sobre o custo de tentar.""",

"""Havia ainda uma coisa a bordo que não precisava de mecânico para ser percebida.

O navio estava tombado.

<strong>Milhem Solk</strong>, um libanês de trinta e cinco anos que fazia a terceira viagem à
Argentina, foi direto ao ponto: o Principessa Mafalda navegou quase o dia inteiro adernado
para um lado.

De Rosas, no depoimento dele, chama aquilo de <em>o perpétuo adernamento do navio</em>.

Diz-se que a inclinação vinha de falha nas bombas e que chegava a variar entre sete e dez
graus. Esse número eu ainda não confirmei em documento nenhum, e não vou fingir que confirmei.
O que está confirmado, por três depoentes que não se conheciam entre si, é que <strong>dava
para ver a olho nu</strong>.""",

"""E aqui a coisa fica interessante, porque o que se sabia a bordo dependia de onde a pessoa
dormia.

<strong>Nicola Lynose</strong>, iugoslavo, terceira classe, explicou o mecanismo sem querer
explicar nada: os passageiros da terceira estavam muito próximos da tripulação e tinham
consciência dos riscos que o navio corria.

É isso, e é simples. O porão ficava colado à casa de máquinas. Os marinheiros comiam, dormiam
e conversavam ali do lado.

Quem viajava embaixo ouvia o navio, e ouvia quem consertava o navio.

Quem viajava em cima ouvia o comandante.""",

"""O comandante <strong>Simone Gulì</strong> era um homem velho com uma vida inteira de mar, e
o método dele diante do medo alheio era desmenti-lo.

Isso vai pesar muito na noite do dia 25, e é assunto dos capítulos seguintes. Aqui importa por
antecipação, porque atravessou a viagem inteira: a versão oficial a bordo, do primeiro dia ao
último, foi a de que não havia nada de anormal acontecendo.

<strong>Pascual Pecci</strong>, que viajava na segunda classe com a mulher e a filha, disse
depois uma frase que é quase uma acusação. Segundo ele, o conselho do comandante foi decisivo
para embalar os passageiros da primeira classe numa falsa sensação de segurança.

Pecci não acreditou nela. Tirou a família do navio cedo, na noite do naufrágio.

Os três sobreviveram.""",

"""Em <strong>24 de outubro de 1927, uma segunda-feira, à uma da tarde</strong>, os apitos da
sirene tocaram.

Era exercício. Exercício de emergência, do tipo que todo navio de passageiros fazia e que
quase ninguém a bordo levava a sério, porque quase nunca serve para nada.

O Mafalda tinha vinte e oito horas de vida.""",

"""No dia seguinte, à tarde, aconteceu uma coisa que deixou o porão otimista.

O Mafalda ultrapassou o <em>Alhena</em>.

O Alhena era um navio holandês da Zuid Rotterdam, mais lento, indo para o mesmo lado. Ver o
navio velho passar por outro com desenvoltura, depois de duas semanas de pane, avaria e
adernamento, foi o suficiente para o medo baixar alguns graus.

Lynose conta que foi exatamente esse o efeito: os passageiros se encheram de otimismo pela
velocidade com que o Mafalda passou pelo Alhena.""",

"""Pouco depois cruzaram com outro, o <em>Empire Star</em>, britânico.

Gulì o saudou do jeito que se saudava no mar: um apito longo, que atravessa a água e que
qualquer passageiro no convés ouve e entende.

Estavam a dois quilômetros do navio inglês quando Lynose ouviu o primeiro estalo.""",

"""Guarde esses dois nomes, porque os dois voltam.

O <strong>Alhena</strong>, que o Mafalda tinha acabado de ultrapassar por vaidade de máquina,
é o navio que recolheu Rosa Forner, a irmã e as cinco crianças, e que três dias depois as
desembarcou na Ilha das Flores, no Rio de Janeiro.

O <strong>Empire Star</strong>, saudado com apito naquela mesma tarde, tirou da água mais de
uma centena de pessoas.

A coisa que salvou aquela gente já estava à vista quando o eixo partiu.

É o único detalhe bom desta história inteira, e ele é bom por acaso.""",

"""Eram cinco e quinze da tarde de 25 de outubro de 1927.""",
]

CAP20 = [
"""O calor não era o da Itália. Era um calor molhado, que grudava na roupa e não
saía com a sombra, e a bordo diziam que aquilo já era o Brasil chegando antes do
Brasil aparecer.

Fazia catorze dias que tinham saído de Gênova. Na terceira classe do
<em>Principessa Mafalda</em> a rotina já era rotina: a fila da comida, o cheiro
que ninguém mais notava, o corredor de madeira onde as crianças corriam porque
não havia mais nenhum outro lugar para correr.

Rosa Forner tinha vinte e quatro anos e um filho de um ano. Enrico havia
completado o primeiro aniversário quinze dias antes, ainda em alto-mar, e não
existe registro nenhum de que alguém tenha comemorado.""",

"""Duas famílias, na verdade, viajavam juntas sem estar no mesmo grupo.

Numa ponta, Rosa e o menino. Na outra, a irmã mais velha, Maria Luigia, com
quatro filhos: Gina, de sete anos, Pulcheria, de seis, Rino, de quatro, e
Danilo, de dois.

Sete pessoas, cinco delas crianças abaixo dos oito anos, indo encontrar dois
homens que já estavam do outro lado havia meses.

Não sei o que elas conversavam. Ninguém sabe. O que os documentos guardam são as
idades, os nomes escritos com a grafia de quem ouviu e anotou, e a última
residência de cada uma: Castelcucco para uma, Cavaso del Tomba para a outra. Duas
vilas que hoje se cruzam de carro em quarenta minutos, e que naquela altura já
estavam a um oceano de distância.

A grafia, aliás, não é detalhe. A menina que o ato de Cavaso registra como <strong>Gina
Oliva</strong>, nascida em 28 de março de 1920, aparece como <strong>Ginneta</strong> na
lista do Rio, vira <strong>Dinetta</strong> na entrada de São Paulo três dias depois, e sai
<strong>Ginita</strong> nos jornais argentinos.

Quatro grafias para uma menina de sete anos, em duas semanas. O nome atravessou dois
idiomas e um naufrágio e chegou do outro lado com outra forma. Vai acontecer com quase
todos eles.""",

"""O navio ia mal e isso não era segredo de ninguém.

Em algum porto da escala africana ele parou por avaria na máquina de bombordo.
Consertaram como se conserta um navio de dezenove anos longe de casa, com o que
havia, e seguiram. Passageiros da primeira classe reclamaram. A companhia
registrou. A viagem continuou.

Escrevo <em>algum porto</em> de propósito. As descrições da rota habitual do
<em>Principessa Mafalda</em> citam Dakar, mas o que as fontes registram desta
última viagem é a saída de São Vicente, em Cabo Verde, no dia 18 de outubro de
1927, com novecentos e setenta e um passageiros e duzentos e oitenta e oito
tripulantes. Ainda não tenho documento que diga em qual dos dois a máquina abriu.
Quando tiver, nomeio.

Na tarde de 25 de outubro de 1927 o <em>Principessa Mafalda</em> navegava a cerca
de setenta quilômetros a leste do arquipélago dos Abrolhos, que já fica a uns
setenta da costa da Bahia. É dessa soma que sai a cifra de cento e trinta
quilômetros de litoral que circula nos relatos. Ia atrasado. Devia ter chegado ao Rio, e não chegou, e
por isso ainda estava no mar naquele fim de tarde.""",

"""Às cinco e quinze da tarde o eixo da hélice de bombordo se partiu.

Não foi uma explosão, embora muita gente tenha dito depois que foi. Um eixo de
hélice é uma barra de aço que atravessa o casco de dentro para fora. Quando ele
se rompe girando, a ponta solta continua girando, e o que gira fora de eixo
arranca o que estiver por perto.

O que estava por perto era o casco, abaixo da linha d’água.

O aço rasgou. A água entrou. E entrou naquela velocidade que os relatórios
descrevem em metros cúbicos por minuto e que, para quem estava lá dentro,
significou simplesmente que o chão do porão sumiu debaixo de um barulho que
ninguém nunca tinha ouvido.""",

"""Na sala de máquinas os homens souberam primeiro. Sempre sabem.

O compartimento inundou depressa. Os motores pararam. Sem propulsão, um navio
deixa de ser um navio e vira um peso comprido boiando de lado no caminho das
ondas, e o <em>Mafalda</em> começou a adernar para bombordo quase de imediato,
devagar, poucos graus, do jeito que engana.

No convés a maioria dos passageiros ainda não entendia. Um estrondo, o silêncio
esquisito dos motores desligados, e depois nada. Muitos continuaram onde
estavam. Alguns foram ver.

É desse intervalo que quase não sobrou registro: os minutos em que ainda dava
para achar que não era nada.""",

"""O comandante Simone Gulì era um homem velho com uma vida inteira de mar.

As fontes não concordam sobre a idade. O Museu da Imigração registra cinquenta e
cinco anos. Uma publicação italiana o descreve como sexagenário de sessenta e
dois. Enquanto não aparecer documento, fica assim: entre os cinquenta e cinco e
os sessenta e dois, e quase quatro décadas embarcado.

Mandou avaliar a avaria, mandou o rádio pedir socorro e mandou dizer aos
passageiros que se mantivessem calmos, o que é a coisa que todo comandante manda
dizer e que quase nunca funciona.

O rádio funcionava. Isso salvou centenas de vidas e é preciso registrar, porque
quase tudo o mais que se conta daquela noite é sobre o que deu errado. O pedido
de socorro saiu, foi ouvido, e navios mudaram de rota para vir.

O que não havia era tempo suficiente para que chegassem antes do escuro.""",

"""O sol se pôs às seis e vinte e um da tarde.

Esse é o dado mais cruel da noite inteira, e é um dado astronômico, não
literário. Calculado para a posição aproximada do naufrágio, dezessete graus e
cinquenta e quatro minutos de latitude sul, em 25 de outubro de 1927: pôr do sol
às 18h21, fim do crepúsculo civil às 18h48.

Entre o rompimento do eixo e o sol desaparecer houve <strong>uma hora e seis
minutos</strong>. Todo o resgate, todo o embarque nos botes, toda a decisão sobre
quem descia e quem esperava, tudo aconteceu no escuro, num navio inclinado, sem
energia, com lanternas.

Se o eixo tivesse partido às sete da manhã, esta seria a história de uma avaria
grave e de um reboque até Salvador.

Partiu às cinco e quinze da tarde.""",

"""Não sei onde Rosa estava naquele momento.

Passei anos querendo saber e não vou inventar. O que os documentos dizem é o
que vem depois.

Três dias depois do naufrágio, em 28 de outubro de 1927, o vapor holandês
<em>Alhena</em> encostou no porto do Rio de Janeiro e entregou à Intendência de
Imigração uma lista com cinquenta náufragos, todos de terceira classe. Na coluna
onde deveria estar o porto de procedência, o escrivão escreveu uma palavra só:
<strong>Náufragos</strong>.

Linha 26 daquela folha: <strong>Forner Rosa, vinte e quatro anos, casada,
chefe.</strong>

Linha 27: <strong>Enrico, um ano, filho.</strong>""",

"""Chefe.

Ela era casada, e o marido estava vivo, esperando em algum lugar do interior de
São Paulo. Ainda assim, no papel, quem encabeça aquela família é ela. Vinte e
quatro anos, um filho de um ano no colo, e a roupa do corpo.

Dezoito linhas abaixo, na mesma folha, o mesmo registro: <strong>Forner Maria,
trinta e um anos, chefe</strong>, com Ginneta de sete, Pulgheria de seis, Rino de
quatro e Danilo de dois.

Duas irmãs, duas famílias, dois maridos do outro lado do continente, e as duas
anotadas como cabeça da própria casa.

A lista traz ainda, sobre a Rosa, duas coisas que nenhum outro documento desta
família diz. Profissão: <em>doméstica</em>. E, na coluna de instrução, uma
palavra que responde uma pergunta que ficou aberta lá no primeiro capítulo:
<strong>Sim</strong>.

Ela sabia ler.""",

"""Entre o naufrágio e essa folha de papel há uma noite sobre a qual ela falou
pouco, e o pouco que falou chegou até mim pela filha, que ainda está viva e ainda
conta.

O que se sabe com certeza é o horário. Cinco e quinze da tarde, hora de bordo,
25 de outubro de 1927. Depois disso, mais nada foi igual para ninguém que estava
naquele navio.""",
]

CAP1 = [
"""Do ponto em que a estrada entra em Castelcucco dá para ver a montanha inteira.

Ela ocupa o norte do céu e não sobra muito espaço para o resto. Chama-se Monte
Grappa, tem mil setecentos e setenta e cinco metros, e durante séculos foi apenas
isso: a montanha. O lugar de onde descia o frio, o pasto de verão, a linha entre o
mundo conhecido e o que ficava atrás dele.

O vilarejo fica cento e oitenta e nove metros acima do mar, no sopé. Tem oito
quilômetros quadrados e pouco, o que significa que uma pessoa atravessa o município
inteiro a pé numa manhã e ainda sobra manhã.

O nome vem de <em>castello</em> e de <em>cucco</em>, que no dialeto quer dizer
elevação arredondada. Nos documentos medievais aparece como Castrocucho. Um castelo
num morro redondo. O castelo não existe mais.""",

"""Os vizinhos são Asolo, Possagno, Monfumo, Cavaso del Tomba e Pieve del Grappa.

Hoje são nomes de guia turístico. Asolo é a cidade nas colinas onde Robert Browning
escreveu e onde Eleonora Duse quis ser enterrada. Possagno é onde nasceu Canova, e
tem no meio dela um templo branco que o escultor projetou e pagou do próprio bolso.

Nada disso tinha a menor importância para quem morava ali e trabalhava a terra. A
beleza da paisagem do Asolano é uma descoberta do século XX. No século XIX aquilo
era só a distância que separava uma casa da outra.

Em 1695 um terremoto derrubou duas de cada três casas de Castelcucco e arrebentou a
igreja. Reconstruíram. É o tipo de coisa que um lugar pequeno guarda por trezentos
anos e continua contando.""",

"""Rosa Forner nasceu às oito e quinze da noite de 24 de junho de 1903, em Monfumo,
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
resto desta parte do livro.""",

"""A terra ali é boa e é pouca, as duas coisas ao mesmo tempo.

O sopé do Grappa é encosta. Trabalha-se em faixas, com vinha, milho, alguma coisa de
trigo e o que a horta der. Quem tinha terra tinha pedaços de terra, espalhados, e
cada geração dividia os pedaços outra vez entre os filhos, porque era assim que se
fazia.

Faça a conta duas ou três vezes e o pedaço deixa de sustentar uma família.

Essa conta fechou no fim do século XIX. Não houve catástrofe, não houve decreto, não
houve inimigo. Houve aritmética.""",

"""O que se comia era polenta.

Milho de manhã, milho ao meio-dia, milho à noite, variando a consistência. Carne em
dia de festa. Vinho da casa, que não era bom, e que era o que havia.

Uma dieta quase só de milho produz uma doença chamada pelagra, que vem da falta de
niacina. Aparece primeiro na pele que pega sol, nas mãos e no rosto, escura e
rachada. Depois vem a diarreia. Depois a confusão mental. No Vêneto do fim do século
XIX a pelagra era endêmica e não havia família que não conhecesse alguém.

Ninguém chamava aquilo de fome. Chamava de vida.""",

"""O ano tinha uma forma, e a forma se repetia.

Fevereiro e março para podar a vinha. Abril para plantar o milho. O verão inteiro
para carpir, e para subir com o gado quando havia gado para subir. Setembro para a
vindima, e a vindima era a única semana do ano em que o trabalho parecia uma festa.
Outubro para a colheita do milho e para a debulha, feita à noite, em mutirão, com
todo mundo sentado em roda.

Depois o inverno, que era longo e não perdoava, e em que se fazia o que dava para
fazer dentro de casa.

Uma criança aprendia esse calendário antes de aprender a ler. Muitas aprendiam esse
calendário e não aprendiam a ler.""",

"""Miotto e Forner aparecem nos livros daquelas paróquias muito antes de qualquer um
desta história nascer. São sobrenomes de gente que ficou parada por séculos.

Na família se conta que Miotto vem de <em>mio</em> com o diminutivo do dialeto,
alguma coisa como "meu pequeno", e que Forner vem de <em>fornaio</em>, padeiro,
aquele que assava o pão da comunidade.

Etimologia de família é sempre um pouco verdade e um pouco poesia, e eu não consegui
confirmar nenhuma das duas num dicionário sério. Deixo registrado assim mesmo,
porque é o que a família diz de si própria, e o que uma família diz de si própria
também é um dado.""",

"""Em 24 de outubro de 1917 a frente italiana arrebentou em Caporetto.

Em duas semanas o exército recuou mais de cem quilômetros. E parou onde? No rio
Piave, e no Monte Grappa.

Na montanha que se via da janela.

Rosa tinha catorze anos. Fausto tinha treze.""",

"""A partir de novembro de 1917 o Grappa deixou de ser uma montanha e virou uma linha
de frente.

A primeira batalha foi entre 13 e 26 de novembro. A segunda entre 11 e 21 de
dezembro. Os austro-húngaros precisavam tomar aquele maciço para descer na planície
e chegar a Veneza. Não tomaram.

O que isso significa lá embaixo, no sopé, é outra coisa: estrada tomada por comboio
militar, mula, hospital de campanha, tropa aquartelada em casa de gente, e o
barulho. Artilharia de montanha ouvida de baixo não é um estrondo, é um som
contínuo, que muda de tom conforme o vento vira.""",

"""E havia a pergunta que toda aldeia do sopé fez naquele inverno: vamos ter que sair?

Em Castelcucco a resposta foi, nesta ordem: sim, não, talvez, e por fim sim.

Em novembro de 1917 foi emitida uma ordem de evacuação do comune. Ela foi revogada
poucas horas depois.

O vilarejo seguiu habitado e funcionando durante todo o inverno de 1917 para 1918. Há
registros de moradores, de atividade civil e de acontecimentos no próprio território
ao longo daqueles meses, com a frente a poucos quilômetros de subida.""",

"""Em 27 de fevereiro de 1918 Castelcucco reaparece na documentação da Prefettura di
Treviso sobre o <em>sgombero</em>, o esvaziamento.

Só que o procedimento está definido ali com duas palavras que mudam tudo:
<em>facoltativo e parziale</em>.

Facultativo e parcial. Podem sair, quem quiser, em parte.

Pense no que uma frase dessas faz dentro de uma casa. Não houve caminhão, não houve
autoridade batendo na porta e mandando todo mundo embora. Houve uma ordem cancelada
no mesmo dia, um inverno inteiro de incerteza, e depois uma permissão que devolvia a
decisão para cada família.

Ficar era arriscar. Sair era largar a casa, os animais e a terra sem saber se haveria
para onde voltar.""",

"""E existe uma tabela que mede exatamente isso.

Em outubro de 1918, com a guerra ainda em curso, o Ministero per le Terre Liberate fez um
<em>Censimento dei profughi di guerra</em>: contou os refugiados de guerra por comune de
origem. Os números do <em>distretto di Asolo</em>, onde ficam Castelcucco e Monfumo, foram
publicados em Roma no ano seguinte.

Leia a coluna da porcentagem devagar.""",

"""<strong>Borso: 3.700 refugiados numa população de 3.733. Noventa e nove por
cento.</strong>

Paderno d'Asolo, 96,8. Crespano, 87,8. <strong>Cavaso: 2.795 pessoas de 3.258, oitenta e
cinco vírgula oito por cento.</strong> Possagno, 81,7.

Esses são os comuni encostados no maciço. Eles não se esvaziaram um pouco. Eles se
esvaziaram.

E então, na mesma tabela, na mesma guerra, no mesmo distrito:

<strong>Castelcucco: 39 refugiados numa população de 1.729. Dois vírgula três por
cento.</strong>

Trinta e nove pessoas.""",

"""Castelcucco fica a quatro quilômetros de Cavaso.

Oitenta e três pontos percentuais de diferença, em quatro quilômetros. É a distância entre
a montanha e o que fica atrás dela, e é também a distância entre uma casa que se esvazia e
uma casa que fica.

Visto assim, o <em>sgombero facoltativo e parziale</em> de fevereiro de 1918 deixa de ser
nota de rodapé burocrática. Ele é esse número. Deram a escolha, e trinta e nove pessoas
saíram.

A família de Fausto está entre as que ficaram. Não por coragem: por estarem quatro
quilômetros do lado certo de uma montanha.""",

"""Duas ressalvas sobre a tabela, porque quem a publicou também as faz.

O censo conta os refugiados por comune de <em>origem</em> e não diz para onde cada um foi.
E os totais do distretto di Asolo não fecham, por um provável erro de impressão na
publicação ministerial que hoje é impossível corrigir.

Os números por comune, porém, são coerentes entre si: em todos os doze, a divisão entre
refugiados e população bate com a porcentagem impressa ao lado. É material de trabalho, e
eu o uso como tal.""",

"""A evacuação mais ampla só veio na primavera de 1918, e aí sim alcançou Castelcucco e
outros municípios da retaguarda do Grappa.

Fausto Miotto tinha treze anos em novembro de 1917, quando a ordem foi dada e
revogada. Tinha catorze na primavera seguinte, quando ela finalmente veio para valer.

Foi essa a adolescência dele. Não a de quem foge de uma catástrofe num dia, mas a de
quem passa um ano e meio esperando para saber se vai ter que ir embora.""",

"""Duas precisões, porque elas importam.

A primeira: quase tudo isso é sobre Castelcucco, o vilarejo de Fausto. Rosa morava em
Monfumo, quatro quilômetros dali, outro comune, com administração própria e ordens
próprias. Durante muito tempo eu escrevi aqui que não sabia o que tinha acontecido lá.

A mesma tabela responde em parte.

<strong>Monfumo: 307 refugiados numa população de 1.661. Dezoito vírgula cinco por
cento.</strong>

Oito vezes a taxa de Castelcucco. Não é Cavaso e não é catástrofe, mas também não são os
dois por cento do vilarejo do Fausto. Um em cada cinco saiu.

O que a tabela não diz é quem saiu, quando, nem se os Forner estavam entre eles. Diz só que
a vila de Rosa esvaziou bem mais que a vila de Fausto, e que os dois adolescentes desta
história passaram o mesmo inverno em dois lugares que responderam de maneira diferente à
mesma montanha.

A segunda é uma correção minha. Quase todo relato geral sobre aquele front repete que
os civis que viviam colados à linha foram retirados em 1917, e eu escrevi isso antes
de verificar. É plausível e é compatível com a documentação, mas a ordem específica,
com a lista de quais localidades e quais casas, ainda não apareceu.

Então fica assim, e só assim: ordem e revogação em novembro de 1917, sgombero
facultativo e parcial em fevereiro de 1918, evacuação ampla na primavera de 1918. O
resto é provável, e está esperando documento.""",

"""No verão de 1918 os austro-húngaros atacaram o Grappa outra vez e foram parados
outra vez.

Em 24 de outubro de 1918, um ano exato depois de Caporetto, o exército italiano
subiu a montanha para valer, dentro da ofensiva de Vittorio Veneto. No dia 4 de
novembro acabou.

Sante Forner, irmão mais velho de Rosa, nascido em 1893, estava no exército. Voltou
com três medalhas, que a família mandou emoldurar e guarda até hoje, num quadro que
atravessou um século e nunca atravessou o oceano.

Ele é o assunto do capítulo 7. Aqui ele importa por um motivo só: quando a guerra
acabou, Rosa tinha quinze anos e já tinha visto o mundo inteiro subir aquele
morro.""",

"""Depois da guerra, a terra era a mesma terra.

Continuava pouca, continuava dividida, continuava dando milho. A diferença é que
agora havia menos braços para trabalhá-la, mais dívida, e uma geração que tinha
descido da montanha sabendo que o mundo era maior e pior do que parecia da janela.

É nesse lugar e nesses anos que a decisão começa a se formar. Não de uma vez, e não
em ninguém em particular. Do jeito que essas decisões se formam: um primo que
escreveu de longe, um cartaz na praça de Asolo, um vizinho que foi e não voltou e
mandou dinheiro.""",

"""A estrada que sai de Castelcucco desce para Asolo.

De Asolo se chega à estação. Da estação se vai a Treviso. De Treviso a Veneza, de
Veneza a Gênova.

De Gênova se vai embora.

É a mesma estrada que a família fazia para ir à missa.""",
]

CAP2 = [
"""O nome mais antigo que consegui alcançar nesta família é Luigi Forner, nascido em
1817.

Antes dele há gente, obviamente. Há sempre gente antes. Mas antes dele os registros
somem, e o que sobra é a suposição de que eram camponeses no mesmo pedaço de encosta,
fazendo a mesma coisa, com nomes que ninguém anotou.

Luigi nasceu no Vêneto. Só que, em 1817, o lugar onde ele nasceu não era a Itália.

Era o Reino Lombardo-Vêneto, província do Império Austríaco, criado dois anos antes no
Congresso de Viena. Luigi Forner nasceu súdito de Francisco I da Áustria. O documento
que o batizou não dizia italiano em lugar nenhum.""",

"""Em 1817 a palavra Itália descrevia uma península, não um país.

Ali dentro havia o Reino da Sardenha, o Lombardo-Vêneto austríaco, os ducados de Parma,
Módena e Toscana, os Estados Pontifícios com o papa como chefe de governo, e o Reino das
Duas Sicílias no sul. Cada um com sua moeda, seu peso, sua medida, sua alfândega, sua
polícia e suas leis.

Trinta anos depois, em 1847, o chanceler austríaco Metternich escreveria a frase que
resume tudo isso com desprezo perfeito: a Itália é uma expressão geográfica.

Ele estava sendo cruel. Não estava errado.""",

"""Luigi não falava italiano.

Falava vêneto, que não é sotaque nem corruptela. É outra língua, com gramática própria,
e era a única de que ele precisava. O italiano era língua de documento, de padre e de
tribunal.

Quanta gente na península falava italiano no momento da unificação é discussão que os
linguistas ainda não encerraram. A estimativa mais citada, de Tullio De Mauro, fala em
algo perto de dois e meio por cento. Outros trabalhos sobem bastante esse número. O que
ninguém contesta é a ordem de grandeza: a esmagadora maioria das pessoas que viraram
italianas em 1861 não falava italiano.

Fizeram um país com gente que não conseguia conversar entre si.""",

"""Em 1848 a Europa inteira pegou fogo, e Veneza pegou junto.

Daniele Manin proclamou a República de São Marcos em março, e ela durou dezessete meses,
até agosto de 1849, quando os austríacos retomaram a cidade depois de um cerco com
bombardeio, fome e cólera.

Luigi Forner tinha trinta e um anos. Não há registro de que tenha participado de coisa
nenhuma, e é improvável que tenha participado. Camponês de encosta em 1848 não fazia
revolução, fazia colheita.

Mas a notícia chegou. Notícia sempre chega.""",

"""Em 1859 veio a Segunda Guerra de Independência. O Piemonte, com a França do lado,
tirou a Lombardia da Áustria.

O Vêneto ficou.

É um detalhe que quase todo resumo de história pula, e que importa muito para esta
família: quando a Itália foi sendo montada, pedaço por pedaço, o Vêneto foi deixado para
trás duas vezes.

Luigi tinha quarenta e dois anos e continuava austríaco.""",

"""Em 17 de março de 1861 foi proclamado o Reino da Itália.

Sem o Vêneto. E sem Roma.

Ou seja: existia oficialmente um país chamado Itália, com rei, bandeira e parlamento, e
Luigi Forner não morava nele. Continuava do outro lado de uma fronteira, no mesmo lugar
onde tinha nascido, sem ter dado um passo.

No ano seguinte, 1862, nasceu o filho dele, Vincenzo Forner. Também súdito austríaco.
Também sem sair do lugar.""",

"""O Vêneto virou italiano em 1866, e virou de um jeito que ninguém gosta muito de
contar.

Na Terceira Guerra de Independência a Itália perdeu em terra, em Custoza, e perdeu no
mar, em Lissa. Só que a Prússia, aliada dela, arrasou a Áustria em Sadowa, e a Áustria
teve que ceder de qualquer maneira.

Pela paz de Viena, em 3 de outubro de 1866, o Vêneto foi entregue à França, e a França o
repassou à Itália. A província mudou de dono numa mesa, entre três países, e nenhum dos
três era o Vêneto.""",

"""Em 21 e 22 de outubro de 1866 fizeram um plebiscito para confirmar a anexação.

Os números impressionam, e é preciso ler os dois lados deles. De uma população de dois
milhões, quatrocentos e oitenta e cinco mil habitantes, pouco menos de seiscentos e
cinquenta mil tinham direito de voto. Deu sim. As fontes divergem um pouco no total, mas
todas ficam por volta de seiscentos e quarenta e um mil votos a favor contra algo entre
sessenta e nove e setenta contra.

Noventa e nove vírgula noventa e nove por cento.

Também não era voto secreto. A pessoa ia até a mesa e dizia em voz alta, na frente dos
vizinhos e das autoridades, se queria ou não ser italiana.

Luigi Forner tinha quarenta e nove anos. Se votou, não sei. Não existe lista.""",

"""E aí chegou a conta.

Um Estado novo precisa de duas coisas com urgência: dinheiro e soldados. O Reino da
Itália, endividado pelas guerras de unificação, foi buscar as duas no único lugar onde
sempre há: no campo.

O Vêneto entrou na Itália como a região mais pobre do país recém-formado. E a primeira
coisa que o país recém-formado fez foi cobrar.""",

"""Em 7 de julho de 1868 foi promulgada a tassa sul macinato, a taxa sobre a moagem.
Entrou em vigor em 1º de janeiro de 1869.

Era um imposto cobrado sobre a quantidade de cereal moído, com contadores mecânicos
instalados nas mós dos moinhos.

Pense no que isso significa numa região que come polenta três vezes por dia. Taxaram o
ato de transformar milho em comida. Não o lucro, não a venda, não a terra. A moagem. O
gesto.

O país inteiro se revoltou e o norte se revoltou mais. Moinhos fecharam, houve
quebra-quebra e houve morte. Em 26 de janeiro de 1869 o Senado confirmou o imposto e deu
plenos poderes de repressão ao general Raffaele Cadorna.

Guarde esse sobrenome. Ele volta neste livro, em 1917, na pessoa do filho.""",

"""A outra cobrança foi em gente.

A unificação trouxe o serviço militar obrigatório, e serviço militar obrigatório numa
economia camponesa não é questão patriótica, é questão aritmética. Cada filho convocado
é um par de braços que sai da encosta por anos.

Numa terra em que a família só se sustentava porque todos trabalhavam, tirar um filho
era tirar a margem inteira.

O macinato foi abolido em 1884, dezesseis anos depois. Tarde demais para a geração que
ele quebrou.""",

"""Há uma frase que circula sobre esse período, atribuída a Giuseppe Verdi, e que
encontrei citada num catálogo do Arquivo Público do Estado do Espírito Santo:

<em>L&rsquo;Unità sarà la nostra rovina. Moriremo tutti di fame.</em>

A unificação será a nossa ruína. Morreremos todos de fome.

Não consegui rastrear a frase até uma carta ou documento original, e registro isso
porque atribuição de frase célebre é terreno escorregadio. Mas ela sobreviveu cento e
cinquenta anos circulando entre italianos justamente porque descreve com precisão o que
aconteceu com quem estava embaixo.""",

"""O resultado está nos números da emigração, e os números são brutais.

Entre 1876 e 1900, três regiões produziram mais de quarenta e sete por cento de todos os
italianos que deixaram o país. O Vêneto foi a primeira delas, sozinho com dezessete
vírgula nove por cento.

E não foi pico passageiro. Até a década de 1940 o Vêneto continuou liderando a
estatística de emigração italiana, à frente da Sicília, da Campânia e da Calábria.
Somando tudo, calcula-se que três milhões e duzentos mil vênetos foram embora.

A região que mais gente perdeu não foi o sul miserável do imaginário popular. Foi esta,
no norte, a que tinha acabado de entrar na Itália.""",

"""Luigi Forner nasceu em 14 de agosto de 1817, em Monfumo, súdito austríaco.

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
sete delas nunca souberam que a oitava existiria.""",
]

CAP3 = [
"""No dia 11 de novembro a estrada enchia de carroça.

É o dia de São Martinho, e no campo do norte da Itália era quando venciam os contratos
agrários. Quem tinha sido renovado ficava. Quem não tinha carregava o que cabia,
colchão, panela, imagem de santo, as crianças em cima, e saía procurar outro pedaço de
terra de outro proprietário.

A expressão pegou e sobreviveu à coisa: <em>fare San Martino</em>, em italiano, até hoje
quer dizer mudar de casa.

Uma vez por ano, num único dia, dava para ver na estrada exatamente quantas famílias
tinham perdido o chão.""",

"""Não sei em que condição os Forner e os Miotto trabalhavam a terra.

Podiam ser proprietários de um pedaço, podiam ser meeiros, podiam ser diaristas. Os
documentos que tenho começam tarde demais e não dizem. Vou descrever o sistema, porque o
sistema eu conheço, e deixar claro que não sei em que casa dele essa família morava.

O que dá para afirmar é que ninguém ali era rico. Rico não emigra na terceira classe.""",

"""Havia basicamente três lugares onde se podia estar.

Proprietário de um retalho: dono de faixas espalhadas de encosta, somando às vezes menos
de um hectare, o suficiente para não morrer e não o suficiente para viver.

Meeiro: trabalhava a terra de outro e entregava metade da colheita. Contrato anual,
renovável ou não, com vencimento em São Martinho.

Diarista, o <em>bracciante</em>: não tinha terra nenhuma e vendia o dia. Era o último
degrau, e era para onde os outros dois desciam.

O movimento entre esses três lugares tinha uma direção só.""",

"""A mecânica da queda é sempre a mesma e leva mais ou menos uma década.

Vem um ano ruim: granizo, seca, doença na vinha. A colheita não paga o ano. A família
pede emprestado para atravessar o inverno e comprar semente.

No ano seguinte a colheita paga o ano mas não paga o juro. Pede de novo.

No terceiro ou quarto ano vende uma faixa de terra para quitar. Agora tem menos terra, e
portanto menos colheita, e portanto menos margem para o próximo ano ruim.

Que vem.""",

"""Quem emprestava não era banco. Banco não emprestava a camponês.

Emprestava o proprietário vizinho, o comerciante da vila, o moleiro, o padre às vezes, e
gente que fazia disso profissão. Os juros não estavam em nenhuma tabela. Estavam no que
o credor achasse que dava para cobrar de alguém que não tinha alternativa.

A terra que saía das mãos de uma família ia parar nas mãos de quem já tinha. É assim que
funciona concentração fundiária: não por decreto, por juro.""",

"""E aí, na década de 1880, veio uma pancada que não tinha nada a ver com a Itália.

O trigo americano chegou à Europa.

As pradarias dos Estados Unidos entraram em produção em escala industrial, a ferrovia
levou o grão até os portos e o navio a vapor atravessou o Atlântico em duas semanas em
vez de dois meses. O preço do trigo despencou no continente inteiro.

Para o consumidor urbano foi ótimo. Para o pequeno agricultor europeu, que vendia o
pouco que sobrava para pagar imposto e juro, foi a sentença.""",

"""Repare no que estava acontecendo ao mesmo tempo, porque é uma das ironias mais
perfeitas desta história.

O navio a vapor foi a tecnologia que arruinou o camponês vêneto, porque foi ele que
trouxe o grão barato da América.

E foi a mesma tecnologia, muitas vezes literalmente os mesmos navios, que levou o
camponês vêneto para a América.

O grão vinha de lá para cá. A gente ia daqui para lá. Nos mesmos porões, em direções
opostas.""",

"""O Estado italiano percebeu que havia um problema e fez o que Estados fazem: abriu uma
comissão.

A Inchiesta agraria e sulle condizioni della classe agricola, conduzida por Stefano
Jacini entre 1877 e 1885, foi a maior investigação já feita sobre o campo italiano.
Percorreu o país, ouviu, mediu e publicou.

O que ela concluiu foi desconfortável: a unificação não tinha resolvido as
desigualdades entre as regiões. Tinha acelerado a crise, e cristalizado a desvantagem
de quem já estava atrás.

O relatório é de 1885. A emigração em massa já estava em curso havia dez anos. As
comissões costumam chegar depois.""",

"""Faltava a doença, e a doença tinha nome.

A pelagra começa na pele que pega sol. As costas das mãos ficam vermelhas, depois
escuras, depois rachadas e grossas como couro. É por isso que o nome veio do lombardo
<em>pelle agra</em>, pele áspera.

Depois vem a diarreia, que não passa.

Depois vem a cabeça: confusão, esquecimento, apatia, e em alguns casos alucinação e
delírio. Nos manuais de medicina ela ficou conhecida pelas três palavras que começam com
a mesma letra em inglês: dermatite, diarreia, demência. Havia uma quarta, que os manuais
educados omitem, e que é a morte.""",

"""A causa é falta de niacina, a vitamina B3. E é aqui que a história fica insuportável.

O milho tem niacina. Só que no milho ela vem quimicamente presa, numa forma que o
intestino humano não consegue absorver.

Existe uma solução, e ela é antiga. Os povos da Mesoamérica, que domesticaram o milho ao
longo de milhares de anos, cozinham o grão em água com cal ou com cinza antes de moer. O
processo se chama nixtamalização, e ele quebra a ligação e libera a niacina. Sem isso,
tortilla mataria mexicano. Com isso, alimenta.

Quando os europeus levaram o milho da América para a Europa, no século XVI, levaram a
semente e não levaram a técnica.""",

"""Foi isso que aconteceu com o Vêneto.

Adotaram um cereal do Novo Mundo porque ele rendia mais por hectare do que qualquer
coisa que tivessem, plantaram, moeram e comeram do jeito que se comia trigo. Deu certo
por gerações, enquanto a polenta era uma parte da dieta.

Quando a polenta virou a dieta inteira, porque não sobrava dinheiro para mais nada, a
conta chegou.

As regiões mais atingidas pela pelagra na Itália foram a Lombardia, o Vêneto e a Emilia
Romagna. Em 1878 o governo mandou fazer um levantamento nacional só sobre ela. Chegaram
a existir instituições específicas para internar doentes, os pellagrosari.

Uma população inteira adoeceu de fome comendo, e adoeceu porque tinha atravessado o
Atlântico uma vez, três séculos antes, e trazido metade do conhecimento.""",

"""A pelagra era uma doença de classe, e isso não é figura de linguagem.

Ninguém que comesse carne, ovo, leite ou pão de trigo com alguma regularidade
desenvolvia pelagra. Nenhum proprietário. Nenhum comerciante. Nenhum padre.

Dava em quem comia polenta e mais nada, e quem comia polenta e mais nada era o camponês
que entregava metade da colheita e o diarista que não tinha colheita nenhuma.

Dava para olhar as mãos de uma pessoa na feira e saber em que degrau ela estava.""",

"""Junte as peças e você tem o ano de uma família na encosta do Grappa por volta de 1890.

A terra é pouca porque foi dividida entre irmãos, e é de outro, ou é metade de outro.
Vende-se o excedente por um preço que o trigo americano derrubou. Paga-se imposto sobre
o que se mói e manda-se um filho para o exército. Pega-se emprestado no inverno com juro
que ninguém regula. Come-se polenta três vezes ao dia e por isso as mãos racham.

E em 11 de novembro descobre-se se o contrato foi renovado.""",

"""Não é uma história de vilão. É uma história de engrenagem.

Não houve um decreto expulsando ninguém, não houve exército queimando aldeia, não houve
perseguição. Houve uma soma de coisas razoáveis do ponto de vista de quem as decidia,
que juntas tornaram impossível continuar.

Foi por isso que quando os cartazes começaram a aparecer nas praças, prometendo terra do
outro lado do mar, eles não precisaram convencer ninguém.

Só precisaram avisar que existia saída.""",
]

CAP4 = [
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

CAP5 = [
"""O cartaz não era colorido.

Tinta preta sobre papel barato, hoje amarelado nas bordas e vincado no lugar onde alguém
o dobrou para guardar. O que chamava atenção não era cor nenhuma. Era a letra do alto:
gótica, cheia de volutas, do tamanho de meia folha, do tipo que se usava em cartaz de
circo e em capa de missal.

Duas palavras, com uma reticência antes, como quem completa uma frase que a pessoa já
vinha pensando sozinha havia meses:

<strong>… In América.</strong>""",

"""Embaixo do título, numa faixa desenhada como um pergaminho que se desenrola:

<strong>Terre in Brasile per gli Italiani.</strong>

Terras no Brasil para os italianos. E logo abaixo, em letra miúda e reta, a parte
prática:

<em>Navi in partenza tutte le settimane dal Porto di Genova.</em>

Navios partindo toda semana do porto de Gênova.""",

"""No meio da folha, ocupando metade dela, não há campo, não há plantação, não há casa.

Há um navio.

Uma gravura de vapor misto, com mastros, velas e uma chaminé soltando fumaça, saindo do
porto com a bandeira içada e um farol pequeno ao fundo.

Repare no que isso quer dizer. <strong>O cartaz não vende o Brasil. Vende a
travessia.</strong> A imagem que aquela gente levava para casa depois de olhar o papel na
praça não era a de uma terra. Era a de um navio saindo.""",

"""Mais abaixo, duas linhas:

<em>Venite a construire i vostri sogni con la famiglia.</em>

Venham construir os seus sonhos com a família.

E no rodapé, onde ficam as promessas de verdade:

<em>Un paese di opportunità. Clima tropicale, vito in abbondanza. Ricchezze minerali. In
Brasile putete havere il vostro castello. Il governo dá terre ed utensili a tutti.</em>""",

"""Um país de oportunidades. Clima tropical, comida em abundância. Riquezas minerais. No
Brasil vocês podem ter o seu castelo. O governo dá terra e ferramenta a todo mundo.

Cinco promessas, e as cinco respondiam exatamente às cinco coisas que faltavam na encosta
do Grappa.

Isso não é coincidência. Quem escreveu aquele texto sabia muito bem com quem estava
falando.""",

"""E quem escreveu aquele texto não sabia escrever italiano.

<em>Construire</em>, com um <em>n</em> que não existe em <em>costruire</em>.
<em>Putete havere</em>, no lugar de <em>potete avere</em>, com um <em>h</em> que o
italiano tinha largado havia séculos. <em>Vito</em> onde deveria estar <em>vitto</em>, que
é comida.

Não é falha da minha leitura. Está impresso. Alguém compôs aquele tipo letra por letra,
alguém mandou rodar, e ninguém corrigiu.

Não sei quem imprimiu esse cartaz. Sei que não era gente para quem o italiano fosse língua
de trabalho, e que ninguém no caminho achou que valesse a pena revisar — porque o público
alvo, na praça da vila, em boa parte não sabia ler.""",

"""Era por isso que alguém lia em voz alta.

E a notícia andava do jeito que notícia andava: na feira, na saída da missa, no moinho
enquanto se esperava a vez.

O que o cartaz não dizia é quem estava pagando, e por quê.""",

"""Não era a Itália.

Quem pagava a passagem era o Brasil, e mais especificamente o estado de São Paulo, com
dinheiro público, a pedido dos fazendeiros de café.

O número é impressionante: entre 1891 e 1895, oitenta e nove por cento de toda a
imigração que entrou em São Paulo foi imigração subvencionada. Nove em cada dez pessoas
que desembarcaram tiveram a viagem paga pelo Estado brasileiro.

Isso não era caridade e nunca foi apresentado como caridade. Era política de mão de
obra.""",

"""A razão é de 1888.

Com a abolição, a lavoura de café do interior paulista perdeu de uma vez o regime de
trabalho sobre o qual tinha sido construída, e precisava de gente. Muita, barata e
rápida.

Havia um segundo motivo, e ele é feio, e omiti-lo seria desonesto. Parte da elite
brasileira da época defendia abertamente a imigração europeia como projeto de
embranquecimento da população. Está escrito nos jornais e nos discursos do período, sem
eufemismo.

O camponês vêneto que olhava aquele cartaz na praça não fazia ideia de que estava sendo
recrutado para dois projetos ao mesmo tempo, e que só um deles tinha a ver com café.""",

"""Entre o cartaz na praça e o navio em Gênova havia uma indústria inteira.

Em 1892 existiam na Itália trinta agências de emigração registradas e cinco mil cento e
setenta e dois subagentes.

Cinco mil recrutadores. Percorrendo vila por vila, feira por feira, batendo em porta de
casa de camponês.

O subagente típico não vinha de fora. Era alguém da região, às vezes o comerciante, às
vezes o próprio moleiro, alguém que a família conhecia e em quem confiava. Essa era a
eficácia do sistema: a proposta chegava pela boca de um conhecido.""",

"""E os subagentes eram pagos por cabeça.

Guarde isso, porque explica tudo o que veio depois. A remuneração era por pessoa
embarcada, não por pessoa que desse certo do outro lado.

A regra oficial dizia que só deviam ser recrutados agricultores aptos ao trabalho. Na
prática recrutava-se qualquer um. Chegavam ao Brasil, no meio dos jovens camponeses,
velhos que não aguentavam a lavoura, crianças de peito e mulheres em gravidez avançada.

Havia litígio no desembarque por causa disso. O agente já tinha recebido, e estava a um
oceano de distância.""",

"""Sobre o que esperava do outro lado, o cartaz era econômico.

Não dizia que a passagem paga virava dívida, a ser descontada do que a família
produzisse. Não dizia que se comprava no armazém da fazenda, a preço da fazenda,
anotado no caderno da fazenda. Não dizia que o contrato prendia a família por um ano e
que sair antes significava sair devendo.

Não dizia que o castelo do rodapé podia ser um barracão de colônia, e que a terra para
cultivar podia ser um pedaço para plantar feijão nas horas em que não se estivesse no
cafezal.

Nada disso era mentira exatamente. Era a mesma frase, com o resto cortado fora.""",

"""E mesmo assim o cartaz não foi o recrutador mais eficiente.

O recrutador mais eficiente foi o primo.""",

"""Existe uma categoria inteira de documento nos arquivos brasileiros chamada carta de
chamada.

Era o mecanismo formal: quem já estava aqui chamava um parente de lá, assumindo
responsabilidade por ele. Mas por trás do documento havia a coisa real, que era a carta
comum, escrita ou ditada, atravessando o oceano de volta.

Os historiadores que estudam a imigração no Espírito Santo descrevem essas cartas como
propaganda espontânea altamente eficaz. É uma boa definição, e ela esconde uma
crueldade.""",

"""Ninguém escreve para casa dizendo que fracassou.

Quem chegou e se quebrou, quem perdeu filho na travessia, quem descobriu que a dívida
não acabava, quem voltou para a Itália derrotado: essas pessoas ou não escreviam, ou
escreviam pouco, ou escreviam contando outra coisa.

Quem escrevia era quem tinha comprado um pedaço de terra, quem tinha aberto um comércio,
quem podia mandar dinheiro dentro do envelope.

O resultado é que a informação que voltava para o Vêneto era verdadeira e era
sistematicamente enviesada. Não por mentira. Por seleção.

A propaganda mais poderosa daquela emigração não foi escrita por agência nenhuma. Foi
escrita pelos próprios emigrantes, e funcionava por omissão.""",

"""O tamanho do que isso produziu:

Entre 1870 e 1920, os italianos foram quarenta e dois por cento de todos os imigrantes
que entraram no Brasil. De três milhões e trezentas mil pessoas, cerca de um milhão e
quatrocentas mil eram italianas.

Setenta por cento delas foram para São Paulo. Até 1920, os italianos chegaram a
representar nove por cento da população total do estado.

Não é uma nota de rodapé da história do Brasil. É um dos maiores deslocamentos
populacionais do século, e ele foi organizado com cartaz, subagente e comissão.""",

"""Tudo isso é do século XIX. O panfleto na praça, as trinta agências, os cinco mil
subagentes.

Em 1902 o governo italiano proibiu a emigração subvencionada para o Brasil, pelo decreto
que leva o nome do ministro Prinetti e que é assunto do próximo capítulo. Quando Fausto
Miotto embarcou, em meados dos anos 1920, aquela praça já tinha outro aspecto.

Foi com essa ideia na cabeça que passei vinte e cinco listas de desembarque do
<em>Principessa Mafalda</em>, uma por uma, no Arquivo Público de São Paulo, procurando o
nome dele entre 1919 e 1924.

Não achei o Fausto.

Achei outra coisa.""",

"""Está num formulário anexo à lista de chegada de <strong>23 de fevereiro de 1923</strong>,
no porto de Santos. Duas folhas, sessenta e sete pessoas, dez famílias. O cabeçalho vem
impresso:

<em>Relação dos immigrantes ITALIANOS AGRICOLTORES embarcados no Porto de GENOVA c/ o
Vap. "PRINCIPESSA MAFALDA" sahido em 8 de FEVEREIRO de 1923 com destino SANTOS ao Estado
de SÃO PAULO, <strong>em virtude do Decreto N. 2400 de 13 de julho de 1918, por conta da
Companhia Commercial de SÃO PAULO</strong>.</em>

O mesmo navio. Quatro anos antes de Rosa.""",

"""As colunas não deixam dúvida sobre que tipo de transporte era aquele.

<strong>Passagens</strong>, com as frações: 1, 1/2, 1/4, 0. Grau de parentesco com o chefe
da família. Filiação. Última residência. E <strong>Destino declarado</strong>, subdividido
em Estação, Município e <strong>Patrão</strong>.

Patrão. Preenchido antes de o navio sair de Gênova.

Os campos trazem nome de fazenda e de proprietário: Chavantes, Barreiro, Fazenda
Guatapará, S. Simão, e repetidas vezes um mesmo nome, Dr. Ralpho P. Silva.

No pé da folha, a conta: <strong>TESTE N° 67, POSTI N° 57 1/4</strong>. Sessenta e sete
cabeças contra cinquenta e sete passagens e um quarto, porque criança pequena valia
fração de bilhete.

E na lista geral do mesmo dia, na margem esquerda, ao lado de dezenas de nomes, uma
palavra repetida à mão: <strong>Subsidiados</strong>.""",

"""A máquina não tinha acabado.

Tinha mudado de freguês.

Quem ainda vinha subsidiado em 1923 vinha recrutado, com estação, município e patrão
marcados antes do embarque, dentro de um contrato que outra pessoa assinou. Fausto veio
por conta própria, com dinheiro que a família juntou, sem patrão declarado e sem destino
determinado por ninguém.

Duas emigrações diferentes, no mesmo período, saindo do mesmo porto. E, como se vai ver,
dentro do mesmo navio.""",

"""E há uma coluna nessa folha que muda o modo de ler o resto deste livro.

Os subsidiados de 1923 viajaram na <strong>terceira classe</strong>.

Não havia um convés de colono e um convés de passageiro. Havia o porão, e dentro dele
estavam misturados quem tinha comprado o bilhete e quem tinha sido recrutado com fazenda
marcada. As duas populações dormiam no mesmo lugar, comiam da mesma fila e desciam pela
mesma escada.

Quatro anos depois, Rosa Forner desceu por essa escada.""",

"""Então o que levou Fausto Miotto para o Brasil, se o cartaz já não estava lá?

O cartaz já tinha feito o trabalho dele. Cinquenta anos de cartaz, agente e carta de
parente instalaram no Vêneto uma ideia que não precisava mais ser vendida: existe uma
saída, ela fica no Brasil, e gente daqui vai para lá.

Quando chegou a vez do Fausto, ninguém precisou convencê-lo de nada. Brasil não era
proposta, era uma coisa que se sabia, como se sabe o caminho de Asolo.

Não foi exemplo de ninguém em particular. Era o que a região inteira já tinha aprendido a
fazer.""",

"""O produto final daquela indústria de recrutamento não foi um passageiro.

Foi um hábito.

O cartaz convenceu uma geração. Essa geração escreveu cartas. As cartas convenceram a
seguinte. E na terceira, quando o cartaz já tinha desbotado e a agência já tinha fechado,
partir tinha deixado de ser uma decisão extraordinária e virado uma das coisas que uma
pessoa da região simplesmente fazia.

É nesse ponto da história que entra o Estado italiano, tarde, tentando fechar a
porteira.""",
]

CAP6 = [
"""Os relatórios começaram a chegar a Roma no fim do século.

Eram documentos consulares, escritos por funcionários italianos espalhados pelo Brasil,
gente cujo trabalho era cuidar dos interesses de cidadãos italianos em território
estrangeiro. Iam por navio, levavam semanas, e caíam numa mesa em Roma onde alguém tinha
que lê-los.

Durante muito tempo ninguém leu com atenção. A emigração era vista como válvula de
escape: gente demais, terra de menos, e um país vizinho de além-mar disposto a receber.
Se estava indo, ótimo.

Até que o conteúdo daqueles relatórios ficou impossível de ignorar.""",

"""O que os cônsules descreviam era o seguinte.

Que os imigrantes italianos nas fazendas de café tinham se tornado, na prática, servos.
Que não havia assistência médica. Que não havia escola para os filhos. Que as casas eram
pequenas e sem as condições mínimas de higiene.

E que havia violência física, inclusive com uso de chicote.

Essa última linha aparece nos documentos que embasaram a decisão italiana. Catorze anos
depois da abolição, num país que tinha acabado de deixar de escravizar pessoas, o
instrumento continuava em uso, agora contra europeus recém-desembarcados.""",

"""O cônsul italiano no Espírito Santo, onde a colonização era intensa, foi específico no
relatório dele.

Reclamou das condições climáticas para as quais ninguém tinha preparado aquela gente. Da
escassez e da má qualidade da comida. Do tratamento dado aos imigrantes pela polícia. Da
incerteza da justiça, quando um colono tentava reclamar alguma coisa. E das falhas na
medição dos terrenos que deveriam ser entregues a cada família.

Esse último item é o mais revelador dos cinco. A promessa central do cartaz era terra. E
o cônsul está dizendo que nem a medição da terra era confiável.""",

"""Uma coisa tinha mudado na Itália e tornou possível que esses papéis produzissem efeito.

Em 31 de janeiro de 1901 o país aprovou a primeira lei geral sobre emigração e criou o
Commissariato Generale dell'Emigrazione, um órgão de Estado com a atribuição de olhar
para aquilo.

Até então a emigração italiana era um fenômeno sem dono dentro do governo. Havia
agências privadas, havia subagentes pagos por cabeça, havia companhias de navegação, e
não havia ninguém encarregado de perguntar o que acontecia com as pessoas depois que o
navio saía.

A partir de 1901 passou a haver.""",

"""Em 26 de março de 1902, o governo italiano baixou o decreto que ficaria conhecido pelo
nome do ministro das Relações Exteriores, Giulio Prinetti.

O decreto proibia a emigração subsidiada para o Brasil.

Ou seja: ficava proibido a um italiano embarcar para o Brasil com a passagem paga por
outra pessoa. Especificamente, com a passagem paga pelo governo brasileiro.""",

"""É essencial entender o que o decreto não fez, porque é aí que mora a inteligência
dele.

Ele não proibiu italianos de irem para o Brasil.

Quem quisesse ir continuava podendo ir. Só teria que comprar a própria passagem, com o
próprio dinheiro, e chegar do outro lado sem dever nada a ninguém.

A Itália não estava impedindo a saída dos seus cidadãos. Estava cortando o mecanismo
financeiro que transformava a viagem em dívida e a dívida em servidão.""",

"""Vale parar aqui, porque este é o capítulo que desmonta uma frase.

Existe uma versão da história da emigração, confortável e muito repetida, em que a
Itália expulsou os pobres. Um país que se livrou da própria miséria empurrando-a para
dentro de um navio.

O Decreto Prinetti é a prova documental de que não é assim tão simples.

Em 1902 o Estado italiano olhou para o que estava acontecendo com os seus nas fazendas
paulistas e fechou a torneira. Tarde, desajeitado e sem resolver a causa, mas fechou. E
fechou contrariando o interesse imediato de um governo que ficaria muito satisfeito de
continuar exportando bocas.""",

"""O efeito foi imediato e foi grande.

A imigração italiana para o Brasil despencou. O fluxo, que não deixou de existir, mudou
de endereço: passou a ir com mais força para a Argentina e para os Estados Unidos, onde
não havia proibição desse tipo.

Para São Paulo, que tinha construído a lavoura de café sobre passagem subvencionada, foi
um problema sério. Foi preciso buscar mão de obra em outros lugares, e é aí que se
intensificam outras correntes migratórias no estado.

O Brasil reagiu com diplomacia e com irritação. Em 1906 ainda havia gestão em curso para
tentar derrubar as restrições italianas. Não conseguiram.""",

"""E agora a parte que interessa diretamente a esta família.

O decreto não parou a emigração vêneta. Nada parou a emigração vêneta.

O que ele fez foi mudar quem podia ir e em que condição. Sem passagem paga, ir para o
Brasil deixou de ser uma coisa que um miserável absoluto conseguia fazer e virou uma
coisa que exigia dinheiro na mão. Juntar economia, vender o que houvesse, pedir a
parente.

A emigração continuou, mas ficou mais lenta, mais familiar e mais deliberada. Menos
levas organizadas, mais gente indo atrás de gente.""",

"""Vinte e quatro anos depois do decreto, Fausto Miotto embarcou.

Não como colono recrutado, não com passagem paga por ninguém, não dentro de um contrato
assinado antes de sair. Foi por conta própria, primeiro, sozinho, do jeito que boa parte
da emigração vêneta passou a se fazer depois de 1902: alguém vai, se estabelece, e chama.

Como se viu no capítulo anterior, ainda saía de Gênova gente subsidiada em 1923, com
patrão declarado antes do embarque, neste mesmo navio. Fausto não estava entre eles.

Depois chamou a mulher.""",

"""E a mulher, quando veio, veio pelo mesmo caminho.

<strong>Rosa Forner não estava sendo recrutada. Estava indo encontrar o marido.</strong>

É uma diferença que parece pequena e que decide tudo o que vem depois.""",

"""Reunião familiar não é colonização, e o Estado de São Paulo não pagava por ela.

É por isso que Rosa não aparece em nenhuma Relação de subsidiados. É por isso que a
família dela não foi encaminhada a uma fazenda com patrão declarado antes do embarque. E é
por isso que ela viajou num transatlântico de linha regular, que levava primeira, segunda
e terceira classe na mesma viagem, com passageiros que tinham comprado bilhete.

Ela pagou para estar ali.

Junto com a irmã, com quatro sobrinhos e com um filho de um ano.""",

"""Seria bonito dizer que uma canetada dada em Roma pôs esta família naquele navio, vinte e
cinco anos depois.

Não é verdade, e o documento de 1923 é a prova: aquele navio ainda levava gente subsidiada.

O que o decreto fez foi mais modesto, e ainda assim grande. Mudou quem podia ir sem
dinheiro e quem precisava juntar. Empurrou uma parte da emigração vêneta para o modelo de
um por vez, por conta própria, chamando os outros depois.

<strong>A família Miotto cabe inteira dentro desse modelo.</strong>""",

"""Fica um buraco neste capítulo, e ele é grande.

O Decreto N. 2400, de 13 de julho de 1918, citado no cabeçalho daquela Relação de 1923, é
a base legal <em>brasileira</em> do transporte subsidiado. Do lado italiano, não sei até
quando a proibição de 1902 continuou valendo na prática, nem se foi revogada, nem se
simplesmente deixou de ser aplicada.

Sem essa peça, este capítulo não pode dizer que a proibição durou até 1927, e também não
pode dizer que caiu antes.

Fica assim, declarado, até o documento aparecer.""",

"""Há uma última ironia neste capítulo, e ela é silenciosa.

O decreto foi criado porque cônsules italianos denunciaram que seus compatriotas estavam
sendo tratados como escravizados nas fazendas de café.

Ou seja: a Itália sabia. Em 1902, o governo italiano tinha, por escrito, na própria mesa,
a descrição do que esperava um camponês vêneto que desembarcasse em Santos.

E ainda assim, entre 1902 e 1927, centenas de milhares continuaram vindo.

Porque quando a alternativa é a encosta do Grappa com a terra dividida em três, a
polenta três vezes ao dia e o contrato vencendo em novembro, até o relatório do cônsul
soa como uma proposta.""",
]

CAP7 = [
"""O quadro está pendurado numa parede no Vêneto.

Moldura dourada, fundo claro, três medalhas presas com as fitas para cima, e no meio uma
figura alegórica: a Itália vitoriosa, cercada de estandartes.

Ele nunca atravessou o oceano. Ficou onde sempre esteve, passando de mão em mão dentro
do ramo da família que não foi embora, até chegar em Giorgio Forner, que hoje o guarda e
que foi quem mandou a fotografia para o Brasil.

É o objeto mais antigo desta história que ainda existe fisicamente. E ele pertence a um
homem que quase ninguém do lado brasileiro sabia que existiu.""",

"""O homem é Sante Forner, nascido em 1893.

Filho de Vincenzo Forner e Santa Pandolfo. Quarto na lista dos dez. Irmão mais velho de
Rosa, a que atravessaria o Atlântico dez anos depois de tudo isso terminar.

Na Itália daquele tempo você não era apenas nascido em 1893. Você era da <em>classe
1893</em>. O ano de nascimento virava uma categoria administrativa que acompanhava o
homem a vida inteira, e que servia para uma coisa acima de todas as outras: saber quando
chamá-lo.

A classe 1893 foi chamada.""",

"""A Itália entrou na guerra em 24 de maio de 1915, quase um ano depois de o resto da
Europa começar.

Tinha passado esse ano negociando com os dois lados para ver qual pagava mais, e acabou
com a Tríplice Entente pela promessa de receber territórios ao norte, incluindo áreas
ainda sob a Áustria.

Sante tinha vinte e dois anos.

Naquele mesmo momento, na casa em que ele tinha crescido, havia um detalhe que os
manuais de história não registram: a mãe, Santa Pandolfo, tinha morrido no ano anterior,
em 1914. Rosa tinha onze anos. Maria M., a caçula, tinha sete.

Ele saiu de uma casa que tinha acabado de enterrar a mãe.""",

"""A guerra italiana começou no rio Isonzo, e ficou ali por dois anos e meio.

Onze batalhas com o mesmo nome, numeradas de um a onze, entre junho de 1915 e setembro
de 1917. Onze vezes atacando as mesmas posições, no mesmo terreno, contra o mesmo
inimigo entrincheirado em cima.

O terreno era karst: pedra calcária. Não dá para cavar trincheira em pedra. Os soldados
empilhavam pedra solta para se proteger, e quando um obus caía perto, a própria proteção
virava estilhaço.

Não sei em qual dessas batalhas Sante esteve, nem se esteve em alguma. Não tenho o
registro militar dele. Mas um homem da classe 1893, convocado, tinha uma probabilidade
muito alta de estar em pelo menos uma.""",

"""E havia o outro front, o das montanhas, que os italianos chamam até hoje de guerra
branca.

Combate acima dos dois mil metros. Trincheira escavada no gelo. Posições abastecidas por
teleférico e por mula. Homens dormindo em caverna aberta na rocha, a trinta graus
negativos, com o inimigo a cem metros de distância fazendo a mesma coisa.

No inverno de 1916 as avalanches mataram milhares de soldados dos dois lados numa única
semana de dezembro. Não em combate. Soterrados.

A montanha matou tanto quanto o exército austríaco, e matava sem preferência de
uniforme.""",

"""O comandante supremo italiano era Luigi Cadorna.

Sim, o mesmo sobrenome do capítulo 2. Raffaele Cadorna, o general a quem o Senado deu
plenos poderes em 1869 para reprimir as revoltas contra o imposto sobre a moagem, era o
pai dele.

O filho comandou a guerra do mesmo jeito que o pai comandou a repressão: com a convicção
de que o problema era a falta de disciplina de quem estava embaixo.

Cadorna mandou fuzilar soldados italianos por recuo, por indisciplina e por suspeita.
Ressuscitou a decimação, o castigo romano de escolher homens por sorteio e executá-los
como exemplo coletivo. Os números exatos ainda são discutidos por historiadores, e são
altos em qualquer contagem.

Um camponês vêneto de vinte e dois anos, naquele front, tinha dois inimigos, e um deles
usava o mesmo uniforme.""",

"""Em 1916 morreu Pietro Luigi Forner, irmão mais velho de Sante, aos vinte e sete anos.

Durante muito tempo eu completei essa frase com outra, dizendo que ele tinha morrido na
guerra, porque era o que fazia sentido. O nome dele não está no Albo d'Oro. O capítulo 4
conta essa busca e o que ela derrubou.

Então aqui fica só o que se sustenta: em 1916, no meio da guerra, aquela casa perdeu mais
um, e eu não sei de quê.

O que a guerra fez com os Forner, porém, está documentado. E é pior do que um irmão.""",

"""Procurei o sobrenome Forner no Albo d'Oro e apareceram dezesseis homens.

Nove eram de Monfumo. O vilarejo da Rosa.

Angelo di Antonio, classe 1876. Giuseppe di Antonio, 1880. Giovanni di Agostino, 1882.
Giovanni di Giuseppe, 1884. Umberto di Vittore, 1886. Florindo di Antonio, 1887. Pietro
di Fortunato, 1887. Vittorio di Antonio, 1887. Ferruccio di Giovanni, 1891.

Nove homens, um sobrenome, uma vila.

Monfumo hoje tem pouco mais de mil habitantes, e naquela época tinha menos. Não sei o grau
de parentesco de cada um com Rosa, mas o capítulo 4 já mostrou o que um sobrenome
significa numa vila daquele tamanho. É quase certo que houvesse parentesco com quase
todos.""",

"""Vale ler <em>como</em> eles morreram, porque desmonta a imagem de guerra que a gente
carrega.

Florindo morreu no Monte Sabotino em 1915, de ferimentos em combate. Ferruccio no Médio
Isonzo em 1916, de ferimentos. Giovanni di Agostino no Monte Rombon em 1917, em combate.

Os outros seis, não.

Angelo morreu em 1918 num hospital de guerra, de doença. Umberto num hospital de campanha
em 1916, de doença. Vittorio em Mestre, 1917, de doença. Pietro em Bologna, 1917, de
doença. Giuseppe morreu em 1918 na <em>prigionia</em>, cativeiro, de doença.

Mais da metade não caiu atacando trincheira. Adoeceu e morreu longe, numa enfermaria ou
num campo de prisioneiros, às vezes meses depois de ter saído de casa.

Foi assim que a Primeira Guerra matou a maior parte da gente que matou.""",

"""Fiz a mesma busca com o outro sobrenome desta história.

Miotto aparece cinquenta e quatro vezes no Albo d'Oro, espalhado pelo Vêneto e pelo
Friuli: Arba, Vo', Candiana, Adria, Vicenza, Veneza.

Nenhum de Castelcucco. Nenhum de Monfumo, de Possagno, de Cavaso del Tomba, de Asolo ou
de Pieve del Grappa.

Os Miotto do sopé do Grappa não perderam ninguém na guerra. Pelo menos ninguém que tenha
entrado no registro oficial.""",

"""Ponha as duas contas lado a lado, porque elas se encontram num casamento.

Em 1926, uma moça de uma família que enterrou nove homens casou-se com um rapaz de uma
família que não enterrou nenhum.

Moravam a quatro quilômetros um do outro. Eram pobres do mesmo jeito, comiam a mesma
polenta, olhavam a mesma montanha. E saíram da mesma década com contas completamente
diferentes.

Não sei se eles conversavam sobre isso. Desconfio que não. Aquela geração não conversava
sobre isso.""",

"""Em 24 de outubro de 1917 o front arrebentou em Caporetto.

Foi a maior derrota da história militar italiana. Em duas semanas o exército recuou mais
de cem quilômetros, perdeu centenas de milhares de homens entre mortos, feridos e
prisioneiros, e a palavra Caporetto entrou no italiano como sinônimo de desastre
completo. É usada assim até hoje.

Cadorna foi demitido em novembro. Culpou os próprios soldados publicamente.""",

"""E aí a guerra chegou em casa.

O exército recuou até parar em duas linhas: o rio Piave e o Monte Grappa. O Grappa é a
montanha que se vê da janela de Castelcucco e de Monfumo. É a montanha do capítulo 1.

Entre 13 e 26 de novembro de 1917, e outra vez entre 11 e 21 de dezembro, os
austro-húngaros atacaram aquele maciço para descer na planície e chegar a Veneza.

Sante Forner era um soldado italiano de vinte e quatro anos, do exército que defendia
aquela posição, e aquela posição ficava alguns quilômetros acima da casa onde os irmãos
menores dele estavam, órfãos, esperando.

Poucos soldados na história defendem literalmente a vista da própria janela.""",

"""No verão de 1918 os austro-húngaros tentaram o Grappa de novo e falharam de novo.

Em 24 de outubro de 1918, um ano exato depois de Caporetto, os italianos atacaram
subindo, dentro da ofensiva de Vittorio Veneto. O império austro-húngaro se desfez
enquanto a batalha acontecia.

Em 4 de novembro de 1918 acabou.

A Itália terminou a guerra do lado vencedor. As estimativas de mortos militares italianos
variam conforme o critério, mas ficam em torno de seiscentos e cinquenta mil homens. Some
os civis e passa de um milhão.""",

"""Agora as medalhas, e aqui é preciso ser exato, porque exatidão é uma forma de
respeito.

As três não têm o mesmo peso, e a família nunca teve por que saber disso.

A <em>Medaglia al Valor Militare</em> é uma condecoração de bravura, criada em 1833 pela
casa de Saboia, concedida em ouro, prata ou bronze por ato específico. Ela é dada porque
alguém fez alguma coisa, e vem com uma justificativa escrita, uma <em>motivazione</em>,
que descreve o ato.

Essa é a medalha que importa. E quer dizer que em algum arquivo italiano existe uma folha
de papel que diz o que Sante Forner fez.""",

"""A segunda é a <em>Medaglia commemorativa della guerra italo-austriaca 1915-1918</em>, e
ela é de outra natureza.

Foi criada por decreto real de 29 de julho de 1920 e concedida a todos que serviram pelo
menos quatro meses em zona de guerra. Não é prêmio por ato. É registro de presença.

Isso não a torna menos interessante. Torna outra coisa.

No anverso está Vitor Emanuel III de capacete e a inscrição <em>guerra per l'unità
d'Italia 1915-1918</em>. No reverso, uma Vitória alada carregada em triunfo por soldados,
sobre um pedestal feito de escudos de trincheira. O desenho é de Silvio Canevari.

E o metal tem procedência declarada: o decreto determinou que a medalha fosse cunhada
com o bronze fundido de canhões austríacos capturados. Ficou conhecida como a medalha do
<em>bronzo nemico</em>, bronze inimigo.

Sante Forner carregava no peito o metal que tinha atirado nele.""",

"""E há um detalhe nessa medalha que pode responder uma pergunta que ninguém fez.

Ela vinha com fascette, pequenas barras presas à fita. Uma barra para cada ano civil em
que o soldado tivesse servido no mínimo quatro meses, e cada barra traz o ano gravado:
1915, 1916, 1917, 1918.

As barras são a folha de serviço dele, em metal, na parede da casa do Giorgio. Cada uma
traz o ano gravado, e juntas dizem em quantas campanhas ele esteve e quais foram.

Estão ali desde 1920.

Ninguém nunca as contou.""",

"""A terceira medalha eu não consigo identificar pela descrição.

A família a chama de medalha de campanha. Pode ser a Medalha Interaliada da Vitória, que
os países vencedores emitiram em versões nacionais a partir de 1922, pode ser uma
comemorativa da unidade, pode ser outra coisa.

Fica sem nome, porque inventar aqui seria fácil e seria errado.""",

"""Sante Forner voltou.

Casou, teve filhos, e continuou onde sempre esteve. Leo, Delfina e Galliano são dele. De
Galliano veio Giorgio, que hoje mora na mesma região, conhece a história inteira, e é
quem guarda o quadro.

Morreu em 1947, aos cinquenta e quatro anos.

Nunca emigrou. Nunca viu o Brasil. E é quase certo que nunca voltou a ver a irmã Rosa
depois de 1927, porque ninguém naquela condição atravessava o Atlântico duas vezes.""",

"""E existe um segundo objeto, guardado na mesma pasta.

Em 8 de março de 1940 o Comune di Asolo emitiu a <em>carta d'identità</em> de Sante
Forner. Ela está no acervo desta família, gasta nas dobras, com uma marca de vinte e cinco
centavos colada no canto de baixo.

E tem a fotografia dele.

Um homem de quarenta e seis anos, de paletó escuro e camisa clara, encostado numa parede.
Bigode. O queixo um pouco erguido. A cara de quem foi fotografado porque precisava, e não
porque quis.""",

"""O documento informa, campo por campo.

<strong>Nato il 16 aprile 1893, a Monfumo.</strong> A data exata, que a genealogia impressa
não trazia. E o lugar: Monfumo, não Castelcucco. Ele nasceu antes de a família mudar de
comune.

<strong>Stato civile: coniugato. Nazionalità: italiana.</strong>

<strong>Professione: bracciante.</strong>

Bracciante é diarista. Trabalhador de enxada por dia de serviço, sem terra própria.

Vinte e dois anos depois da guerra, com três medalhas emolduradas na parede de casa, a
profissão declarada do homem que ajudou a segurar o Monte Grappa é diarista.""",

"""E vêm os <em>connotati e contrassegni salienti</em>, que é como se descrevia uma pessoa
antes de a fotografia resolver o problema:

<strong>Statura m. 1,62. Occhi castani. Naso regolare. Bocca regolare. Capelli castani.
Barba</strong>, e aqui um traço, que quer dizer nenhuma. <strong>Baffi castani. Segni
particolari: N.N.</strong>

Um metro e sessenta e dois. Castanho de olho, de cabelo e de bigode. Sem barba. Nenhum
sinal particular.

O Estado italiano olhou para esse homem em 1940 e concluiu que não havia nada nele que
merecesse anotação.

Embaixo, a assinatura do titular, firme e inteira: <em>Forner Sante</em>. Ele sabia
escrever o próprio nome.""",

"""Duas coisas mais, nas bordas do papel.

A primeira está no campo da filiação, e é a linha que resolveu o capítulo 4: <em>Padre:
<strong>di</strong> Vincenzo. Madre: <strong>fu</strong> Pandolfo Domenica Santa.</em> Pai
vivo, mãe morta. Em março de 1940 o velho ainda estava lá.

A segunda está na data. <em>Asolo, lì 8-3-1940</em>, e ao lado, <strong>A. XVIII</strong>.
<em>Anno diciottesimo</em>: o ano dezoito da era fascista, contado a partir da Marcha sobre
Roma. Quem assina não é um prefeito eleito. É <strong>il Podestà</strong>.

Três meses depois desse carimbo, a Itália entrou na Segunda Guerra Mundial.

O homem das três medalhas da primeira guerra tirou carteira de identidade a tempo de ver
a segunda começar.""",

"""Repare no que ficou de cada lado.

O ramo que partiu tem fotografias, documentos de imigração, uma certidão de óbito em
Sorocaba e a lembrança de uma senhora de oitenta e nove anos.

O ramo que ficou tem um quadro na parede, com três medalhas e uma Vitória alada de
bronze inimigo. E tem, guardada, uma carteira de identidade de 1940 com o rosto dele
dentro.

Nenhum dos dois lados escapou. Um enfrentou o Atlântico, o outro enfrentou o Grappa. A
diferença é que um dos dois foi obrigado a levar tudo o que tinha numa mala de madeira, e
por isso quase nada sobrou.

Por isso este capítulo existe. Porque o objeto que melhor conta essa família nunca esteve
no Brasil.""",
]

CAP8 = [
"""Não existe fotografia do casamento. Não existe convite, não existe lista de
convidados, não existe registro do que se comeu.

O que existe é uma linha, escrita à margem da certidão de nascimento dela, no livro do
Comune di Monfumo:

<em>ha contratto matrimonio con Miotto Fausto in data 03/12/1926 a Castelcucco.</em>

E a mesma informação do outro lado, à margem da certidão dele, no livro do Comune di
Castelcucco: ato número 9, parte I, do ano de 1926. Ali ela aparece com o diminutivo,
<strong>Forner Rosina</strong>.

Casaram-se em <strong>3 de dezembro de 1926</strong>, em Castelcucco. Ela com vinte e
três anos, ele com vinte e dois.""",

"""Vale olhar quem eram essas duas pessoas em 1926.

Rosa tinha perdido a mãe aos onze anos. Tinha perdido um irmão, Pietro Luigi, em 1916,
de causa que continua desconhecida. Tinha outro irmão, Sante, que voltou do Monte Grappa
com três medalhas e o silêncio que normalmente vem junto. Tinha sido criada, na prática,
pela irmã mais velha, Maria Luigia.

Fausto cresceu numa vila em que ir embora era uma das coisas que os homens faziam. Do pai
dele, Luigi Miotto, existem três aparições em papel ao longo de oitenta anos, e entre elas
nada. Um homem que deixou o nome e não deixou rastro.

Nenhum dos dois tinha herança para receber.""",

"""Agora ponha a outra data ao lado.

Enrico Miotto nasceu em <strong>10 de outubro de 1926</strong>. Está no Registro de
Estrangeiros que ele assinou em São Paulo em 1949: nacionalidade italiana, pai Fausto
Miotto, mãe Rosa Forner.

O casamento foi em 3 de dezembro de 1926.

<strong>O filho nasceu cinquenta e quatro dias antes de os pais se casarem.</strong>""",

"""Rosa não estava grávida na cerimônia. Estava com um bebê de quase dois meses no colo.

Isso não é escândalo e não é fofoca de cartório. É informação sobre como aquela vida
funcionava.

Numa vila católica do Vêneto de 1926, um filho nascido antes do casamento e reconhecido
oito semanas depois quer dizer que houve uma relação estável antes, e que a formalização
esperou alguma coisa. Dinheiro, autorização de família, a vinda de um padre, o fim de uma
colheita, uma papelada. Não dá para saber qual.

E há uma coincidência que o capítulo 4 já mostrou: <strong>trinta e nove anos antes, os
pais de Rosa fizeram exatamente a mesma coisa.</strong> Vincenzo e Santa casaram-se em
1887, e a primeira filha, Angela, nasceu em 1886.

Duas gerações, a mesma sequência.""",

"""E aí, com o casamento feito e o filho de meses, Fausto foi embora.

Não juntos. Não a família toda num navio. Ele primeiro, sozinho.

É importante não ler isso com olhos de hoje. Não foi abandono, foi o procedimento. Para
quem não vinha recrutado, emigrar era uma operação em duas etapas: um homem vai na frente
com o dinheiro que a família conseguiu juntar, trabalha, arruma onde morar, e então manda
buscar.

Angelo Dei Agnoli, casado com Maria Luigia, fez o mesmo caminho, e antes dele. As duas
irmãs ficaram para trás nas duas casas.""",

"""Pense no que sobrou para Rosa Forner naquele ano.

Vinte e três anos. Um filho de meses. Um marido do outro lado do oceano, alcançável
apenas por carta, com semanas de atraso entre a pergunta e a resposta. A mãe morta havia
doze anos.

O pai vivo, a quatro quilômetros, com sessenta e quatro anos.

Não sei o que Vincenzo Forner disse quando soube, nem se disse alguma coisa. Sei que ela
foi assim mesmo.

E o inverno de 1926 para 1927 no sopé do Grappa foi o inverno que sempre foi.""",

"""Quatro quilômetros dali, em Cavaso del Tomba, Maria Luigia estava fazendo a mesma coisa
com quatro crianças.

Gina com seis anos. Pulcheria com cinco. Rino com três. Danilo com um.

Maria Luigia tinha casado em 1917 e ido morar em Cavaso, que é a vila que se esvaziou na
guerra enquanto Castelcucco ficava de pé. Ela chegou lá a tempo de ver quase todo mundo
sair.

Nove anos depois, saía ela. Dessa vez sem volta prevista.

Duas irmãs, duas casas, dois maridos ausentes, cinco crianças pequenas entre elas, e a
mesma correspondência lenta atravessando o Atlântico nos dois sentidos.

Elas já tinham feito isso antes, aliás. Em 1915 os homens tinham ido para a guerra e as
mulheres tinham ficado. A diferença é que agora os homens estavam vivos e o que faltava
não era notícia do front. Era passagem.""",

"""O que chegava era a carta.

Nunca vi essas cartas. É quase certo que não existam mais. Mas sei que existiram, porque
o mecanismo inteiro da emigração italiana dependia delas, e porque em algum momento de
1927 aquelas duas mulheres souberam que era hora.

Uma carta dessas trazia três coisas: a notícia de que dava, o dinheiro ou o bilhete, e a
instrução do que fazer.

E o que fazer, a essa altura, já era mais complicado do que tinha sido para qualquer
geração anterior.""",

"""Porque a Itália de 1927 não era mais a Itália que deixava sair.

Mussolini estava no poder desde 1922, e em 1927 o regime fez uma virada explícita contra
a emigração. A lógica era demográfica e era de potência: um país que quer ser grande
precisa de gente dentro dele, não espalhada pelo mundo. Cada camponês que embarcava era
um soldado a menos e um nascimento a menos em solo italiano.

A emigração deixou de ser válvula de escape e passou a ser sangria.""",

"""Em 28 de abril de 1927, por decreto-lei, o governo fascista extinguiu o Commissariato
Generale dell'Emigrazione.

É o mesmo órgão do capítulo 6 deste livro. Criado em 1901, foi ele que reuniu os
relatórios consulares e sustentou o decreto Prinetti que protegeu os italianos das
fazendas brasileiras em 1902.

Vinte e seis anos depois, foi extinto e substituído pela Direzione Generale degli
Italiani all'Estero.

A mudança de nome não é detalhe burocrático. A palavra emigrante saiu do vocabulário
oficial e entrou italiano no exterior. Não existe mais alguém que sai. Existe um italiano
que por acaso está longe, e que continua pertencendo.""",

"""Junto com a mudança de nome veio a mudança prática.

Ficou mais difícil obter os documentos necessários para deixar o país. As instruções aos
prefeitos mandavam exercer o máximo de severidade e de contenção na liberação de
passaporte, abrindo exceção para emigração temporária e para intelectuais e
profissionais liberais.

Ou seja: quem podia sair era quem ia voltar, e quem tinha diploma.

Uma camponesa de vinte e quatro anos, sem instrução, indo em definitivo, com um filho
pequeno, para reunir a família em outro continente, era exatamente o perfil que o Estado
tinha acabado de decidir segurar.""",

"""Não tenho os passaportes delas. Não sei se houve dificuldade, quanto tempo levou, se
foi preciso pedir favor a alguém, se houve um funcionário compreensivo ou um funcionário
difícil.

O que dá para afirmar é que as duas conseguiram, em algum momento do segundo semestre de
1927, um conjunto de documentos que o próprio governo tinha instruído os prefeitos a
conceder com o máximo de contenção, seis meses antes.

E saíram.

Passaram por uma porta que estava sendo fechada.""",

"""Repare no que estava fechando exatamente naquele ano.

Os Estados Unidos já tinham praticamente encerrado a imigração italiana com o sistema de
cotas de 1921 e 1924. A Itália, em 1927, começava a travar a saída. E o Brasil, que
setenta anos antes pagava a passagem, agora não pagava mais nada.

A janela que a família Forner atravessou em outubro de 1927 é uma das últimas daquele
ciclo. Cinco anos depois teria sido muito mais difícil. Dez anos depois, com a guerra
chegando de novo, seria impossível.

Elas não sabiam disso. Ninguém sabe quando está passando pela última porta.""",

"""Da casa de Castelcucco até Asolo se desce a pé.

De Asolo se pega o trem. De Treviso se muda de trem. De Veneza se atravessa a planície
até Gênova, e em Gênova está o mar, que a maioria daquela gente estava vendo pela
primeira vez na vida.

Rosa Forner tinha vinte e quatro anos e carregava Enrico, que tinha acabado de fazer um.
Maria Luigia tinha trinta e um e carregava quatro.

Não sei o que levaram na bagagem. Sei o que aquela gente costumava levar: roupa,
ferramenta, um retrato, e comida para os primeiros dias.""",

"""Havia um irmão que ficou.

Sante Forner tinha trinta e quatro anos em 1927. Tinha defendido aquela montanha, tinha
voltado, tinha casado e estava criando os filhos dele na mesma encosta em que os pais
morreram.

Ele viu as duas irmãs irem embora.

É quase certo que nunca mais as tenha visto. Morreu em 1947, na Itália. Rosa morreu em
1986, no Brasil. Maria Luigia em 1992. Nenhuma das duas voltou.

A última coisa que aquelas duas mulheres viram do lugar onde nasceram foi a mesma
montanha que o irmão delas tinha passado um ano inteiro defendendo. Para ele, o Grappa
era o que se protege. Para elas, virou o que se deixa.""",

"""Aqui termina a parte que se passa em terra firme.

Tudo o que veio até agora, o terremoto de 1695, a fronteira que atravessou dois homens
parados, o imposto sobre a moagem, a pelagra, os dez filhos de uma mulher só, os
cinco mil subagentes, o cônsul escrevendo de Vitória, o chicote nas fazendas, o bronze
inimigo no peito do Sante, tudo isso existe neste livro por um motivo só.

Para que quando o navio afundar, o leitor saiba exatamente o que aquelas pessoas estavam
tentando alcançar, e o que já tinham atravessado antes de chegar à água.""",
]

CHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 8: CAP8, 19: CAP19, 20: CAP20}

# ------------------------------------------------------------------ paginas
pages = []
def P(**kw): pages.append(kw)

P(t='capa')
P(t='rosto')
P(t='epigrafe')
P(t='sumario')

IMG_BY_CAP = {
 1:  [('castellcuco','Os vales de Castelcucco, província de Treviso. Fausto Miotto nasceu aqui em 1904.')],
 2:  [('italia_campo_verde','O campo vêneto. A paisagem que trocou de país duas vezes sem sair do lugar.')],
 3:  [('familia_italiana','Família camponesa italiana no início do século XX.')],
 4:  [('arovore_genealogica','A árvore genealógica reconstruída das famílias Miotto e Forner.')],
 5:  [('panfleto_in_america','“…In América. Terre in Brasile per gli Italiani.” Preto sobre papel barato, com o italiano cheio de erros de composição e um navio no lugar onde deveria estar a terra prometida.')],
 7:  [('quadro_guerra_europa','O quadro com as três medalhas de guerra de Sante Forner, concedidas pelo Ministério da Guerra da Itália.'),
      ('sante_militar','Sante Forner, 1893 a 1947, fardado.'),
      ('sante_forner_documento','Carta d’identità de Sante Forner, Comune di Asolo, 8 de março de 1940. Nato il 16 aprile 1893 a Monfumo. Professione: bracciante. Statura 1,62. Assinada pelo Podestà e datada A. XVIII, o ano dezoito da era fascista.')],
 8:  [('fausto','Fausto Miotto, nascido em Castelcucco em 1904. Casou-se com Rosa Forner em 1926 e partiu sozinho para o Brasil.')],
 9:  [('italianos_no_barco','Imigrantes italianos a bordo, início do século XX.')],
 10: [('imigrantes_italianos_na_hospedaria_dos_imigrantes_em_são_paulo_cerca_de_1890','Imigrantes italianos na Hospedaria dos Imigrantes, São Paulo, por volta de 1890.')],
 16: [('vapor_mafalda','O vapor Principessa Mafalda. Lançado em 1908, afundou em 25 de outubro de 1927.')],
 17: [('princess_mafalda_of_savoy','A princesa Mafalda de Saboia, que deu nome ao navio. Morreu em Buchenwald, em 1944.')],
 19: [('princessa_mafalda','O Principessa Mafalda. Saiu de Gênova em 11 de outubro de 1927 com 971 passageiros e 288 tripulantes, e já saiu atrasado.')],
 21: [('mafalda_naufragando','O naufrágio do Principessa Mafalda em representação de época.')],
 24: [('passageiros_agnoli','Lista de passageiros: a família Agnoli, terceira classe, resgatada pelo navio Alhena.')],
 26: [('rosa_forner','Rosa Forner Miotto, 1903 a 1986. Sobreviveu ao naufrágio aos vinte e quatro anos.'),
      ('rosa_forner_documento','Documento de identificação de Rosa Forner Miotto.')],
 27: [('maria_lugia_forner','Maria Luigia Forner, 1896 a 1992, irmã de Rosa.'),
      ('forner_maria_luigia_col_marito_dei_agnoli_angelo','Maria Luigia Forner e o marido, Angelo dei Agnoli.')],
 29: [('enrico','Enrico Miotto, 1926 a 1998. Tinha um ano e quinze dias na noite do naufrágio.'),
      ('enrico_registro_de_estrangeiro','Registro de Estrangeiros de Enrico Miotto, 29 de dezembro de 1949. Data de nascimento: 10.10.1926.')],
 30: [('mafalda_miotto_forner','Mafalda Miotto Terra, nascida em 1937, dez anos depois do naufrágio, com o nome do navio.')],
 32: [('sante_e_familia','Sante Forner e família, na Itália.'),
      ('giorgio_e_sua_familia','Giorgio Forner e família, o ramo que permaneceu no Vêneto.')],
}

for bn, btitle, byears, bcolor in BOOKS:
    P(t='parte', n=bn, title=btitle, years=byears, color=bcolor)
    for (num, ctitle, synop) in CAPS[bn]:
        P(t='cap', num=num, title=ctitle, synop=synop, book=bn, color=bcolor)
        txt = CHAPTERS.get(num)
        if txt:
            for body in txt:
                P(t='texto', body=body, book=bn, cap=num, captitle=ctitle)
        for k, cap in IMG_BY_CAP.get(num, []):
            P(t='img', key=k, cap=cap, book=bn)

# ---------------------------------------------------- caderno de imagens
SKIP = {'710doxadqgl__sl1360','716aeqgd2pl__sl1499','71lmjwglzgl__sl1200','71rnbfpskhl__sl1360',
        '52f7878846e1bd9668eb0502126ae9a0','9e1442ad1cef72882ae3ced892b93163','image_4','capa',
        'e01164_afab8415694242ebbd01f48d699c9193_mv2','571_1','571_2','selo','brasao','mattia'}
LEG = {
 'angelo__dei_agnoli':'Passaporte de Angelo dei Agnoli, marido de Maria Luigia Forner.',
 'angelo_dei_agnoli__jpg':'Certidão de registro de Angelo dei Agnoli.',
 'certidao_de_obito':'Declaração de óbito de Enrico Miotto, 6 de outubro de 1998, Sorocaba.',
 'enrico_miotto':'Documento de identificação de Enrico Miotto.',
 'fausto':'Fausto Miotto, nascido em Castelcucco em 1904, marido de Rosa Forner.',
 'forner_galliano':'Galliano Forner, filho de Sante, militar com as tropas alpinas em 1950.',
 'forner_maria_luigia_dei_agnoli_angelo':'Maria Luigia Forner e Angelo dei Agnoli.',
 'forner_martino_fratello_di_mio_nonno_sante':'Martino Forner, irmão de Sante.',
 'galiano':'Galliano Forner.',
 'galliano':'Galliano Forner, retrato emoldurado conservado pela família na Itália.',
 'giorgio':'Giorgio Forner, bisneto de Sante, reencontrado em pesquisa genealógica.',
 'giorgio_seu_pai':'Giorgio Forner e o pai.',
 'giorgio_su_amore':'Giorgio Forner e a esposa.',
 'girgio':'Giorgio Forner.',
 'giovani_bambini':'Crianças no campo vêneto.',
 'mauro_filho_de_giorgio':'Mauro Forner, filho de Giorgio.',
 'miotto_maria_luigia_e_forner_sante':'Maria Luigia Miotto e Sante Forner.',
 'sante':'Sante Forner, 1893 a 1947.',
 'sante_perfil':'Sante Forner, retrato.',
 'sante_forner_documento':'Documento de identificação de Sante Forner.',
 'arovore_genealogica':'Árvore genealógica da família.',
 'familia_forner':'A família Forner.',
 'familia_italiana':'Família italiana no início do século XX.',
 'joao_luca_e_mafalda':'Mafalda Miotto e o bisneto João Luca.',
 'princessa_mafalda':'O Principessa Mafalda.',
 'quadro_de_guerra':'As medalhas de guerra de Sante Forner.',
 'sao_joao_da_boa_vista':'Interior paulista.',
 'stöwer_titanic':'O naufrágio do Titanic em pintura de Willy Stöwer, 1912. Os jornais de 1927 chamaram o Mafalda de "o Titanic italiano".',
 'tio_henrrique':'Enrico Miotto.',
 'imigrantes_italianos_na_hospedaria_dos_imigrantes_em_são_paulo_cerca_de_1890__1':'Hospedaria dos Imigrantes, São Paulo.',
}
_used = {pg['key'] for pg in pages if pg['t'] == 'img'}
_all = sorted(os.path.splitext(f)[0] for f in os.listdir(IMG) if f.endswith('.webp'))
_rest = [k for k in _all if k not in _used and k not in SKIP]
if _rest:
    P(t='parte', n='CADERNO', title='Imagens', years='O acervo da família', color='graf')
    for k in _rest:
        P(t='img', key=k, cap=LEG.get(k, 'Acervo da família Miotto e Forner.'), book='CI')

P(t='parte', n='EPÍLOGO', title='As três Mafaldas', years='', color='graf')
P(t='cap', num=35, title='A princesa, o navio e a menina', synop='As três camadas do livro amarradas num nome. A única que chega viva ao fim.', book='EP', color='graf')
P(t='fim')

# ------------------------------------------------------------------- render
def sheet(inner, cls='', **attrs):
    a = ''.join(' %s="%s"' % (k.replace('_','-'), v) for k, v in attrs.items())
    return '<div class="leaf"%s><div class="sheet %s">%s</div></div>' % (a, cls, inner)

out = []
folio = 0
for p in pages:
    t = p['t']
    if t == 'capa':
        out.append(sheet(
            '<div class="capa">'
            '<p class="cp-au">João Andrade</p>'
            '<h1 class="cp-t">Terceira<br>Classe</h1>'
            '<p class="cp-s">A travessia italiana para o Brasil<br>e o naufrágio do <em>Principessa Mafalda</em></p>'
            '<p class="cp-d">1861 &middot; 1927 &middot; hoje</p>'
            '</div>', 'is-capa', data_nav='Capa'))
    elif t == 'rosto':
        out.append(sheet(
            '<div class="rosto">'
            '<h2>Terceira Classe</h2>'
            '<p class="r-s">A travessia italiana para o Brasil e o naufrágio do <em>Principessa Mafalda</em></p>'
            '<p class="r-a">João Andrade</p>'
            '<p class="r-n">Edição de trabalho<br>Este exemplar é um rascunho navegável. Os capítulos são publicados conforme ficam prontos.</p>'
            '</div>', '', data_nav='Folha de rosto'))
    elif t == 'epigrafe':
        out.append(sheet(
            '<div class="epig">'
            '<blockquote>A cena é lancinante. Lágrimas, lamúrias, desmaios, invocações devotas, promessas. '
            'Da amurada do navio os lenços sacodem nervosos as despedidas finais. Addio! Addio! Addio! '
            'Os corações se fecham numa saudade funda.</blockquote>'
            '<cite>Serafim Derenzi, 1974</cite>'
            '</div>', '', data_nav='Epígrafe'))
    elif t == 'sumario':
        rows = []
        for bn, btitle, byears, bcolor in BOOKS:
            rows.append('<div class="sm-b"><span class="sm-n">Parte %s</span><span class="sm-t">%s</span>'
                        '<span class="sm-y">%s</span></div>' % (bn, E(btitle), byears))
            for (num, ctitle, _s) in CAPS[bn]:
                rows.append('<div class="sm-c"><span class="sm-cn">%02d</span><span>%s</span></div>' % (num, E(ctitle)))
        rows.append('<div class="sm-b"><span class="sm-n">Epílogo</span><span class="sm-t">As três Mafaldas</span><span class="sm-y"></span></div>')
        out.append(sheet('<div class="sumario"><h3>Sumário</h3><div class="sm-list">%s</div></div>' % ''.join(rows),
                         'is-sum', data_nav='Sumário'))
    elif t == 'parte':
        out.append(sheet(
            '<div class="parte">'
            '<p class="pa-n">%s</p><h2 class="pa-t">%s</h2><p class="pa-y">%s</p>'
            '</div>' % (E(p['n']), E(p['title']), E(p['years'])),
            'is-parte c-' + p['color'], data_nav='Parte ' + p['n'] + ' · ' + p['title']))
    elif t == 'cap':
        folio += 1
        out.append(sheet(
            '<div class="capo">'
            '<p class="co-n">Capítulo %02d</p><h2 class="co-t">%s</h2>'
            '<p class="co-s">%s</p><span class="co-r c-%s"></span>'
            '</div><span class="folio">%d</span>' % (p['num'], E(p['title']), E(p['synop']), p['color'], folio),
            'is-cap', data_nav='%02d · %s' % (p['num'], p['title'])))
    elif t == 'texto':
        folio += 1
        paras = ''.join('<p>%s</p>' % b.strip().replace('\n', ' ') for b in p['body'].split('\n\n'))
        out.append(sheet(
            '<span class="run">%s</span><div class="corpo">%s</div><span class="folio">%d</span>'
            % (E(p['captitle']), paras, folio)))
    elif t == 'img':
        folio += 1
        out.append(sheet(
            '<figure class="fig"><div class="fig-i"><img src="%s" alt="%s" loading="lazy"></div>'
            '<figcaption>%s</figcaption></figure><span class="folio">%d</span>'
            % (b64(p['key']), E(p['cap'][:90]), E(p['cap']), folio)))
    elif t == 'fim':
        out.append(sheet(
            '<div class="fim"><p class="fm-1">continua</p>'
            '<p class="fm-2">Os capítulos aparecem aqui conforme são escritos.<br>'
            'Centenário do naufrágio: 25 de outubro de 2027.</p></div>', '', data_nav='Fim'))

BODY = '\n'.join(out)

CSS = """
:root{
 --room:#CFC9BA; --sheet:#F7F4EB; --ink:#1B1E1A; --soft:#5A6158; --faint:#8C9187;
 --rule:#D8D2C2; --accent:#8A6712;
 --ochre:#A67C2E; --sea:#2F5E5C; --verm:#B03923; --terra:#6E4B33; --graf:#2A2E30;
 --zoom:1;
 --fd:"Bodoni Moda",Didot,Georgia,serif; --fb:"EB Garamond",Georgia,serif;
 --fu:"Jost",Futura,"Century Gothic",system-ui,sans-serif;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --room:#08090A; --sheet:#14181A; --ink:#EAE5D9; --soft:#9AA5A2; --faint:#6C7674;
 --rule:#252D30; --accent:#C99B3E;
 --ochre:#8A6626; --sea:#26504E; --verm:#8E2E1C; --terra:#5A3D2A; --graf:#1C2022;
}}
:root[data-theme="dark"]{
 --room:#08090A; --sheet:#14181A; --ink:#EAE5D9; --soft:#9AA5A2; --faint:#6C7674;
 --rule:#252D30; --accent:#C99B3E;
 --ochre:#8A6626; --sea:#26504E; --verm:#8E2E1C; --terra:#5A3D2A; --graf:#1C2022;
}
*{box-sizing:border-box}
body{background:var(--room);color:var(--ink);font-family:var(--fb);margin:0}

.stage{height:100svh;overflow-y:auto;scroll-snap-type:y mandatory;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){.stage{scroll-behavior:auto}}
.stage[data-zoomed="1"]{scroll-snap-type:y proximity}
.leaf{min-height:100svh;display:grid;place-items:center;scroll-snap-align:center;padding:2.2svh 0}

.sheet{
 position:relative;background:var(--sheet);color:var(--ink);
 width:min(93vw,calc(44rem * var(--zoom)),calc(88svh * .707 * var(--zoom)));aspect-ratio:1/1.414;
 padding:3.3em 3.6em 3em;box-shadow:0 1px 2px rgba(0,0,0,.16),0 14px 40px rgba(0,0,0,.22);
 font-size:calc(clamp(10px,2.05svh,15.5px) * var(--zoom));line-height:1.62;
 display:flex;flex-direction:column;justify-content:flex-start;
}
.sheet > *{width:100%;min-width:0;max-width:100%}
.folio{position:absolute;left:0;right:0;bottom:3.4%;text-align:center;font-family:var(--fu);
 font-size:.68em;letter-spacing:.14em;color:var(--faint);font-variant-numeric:tabular-nums}
.run{position:absolute;left:0;right:0;top:4.2%;text-align:center;font-family:var(--fu);
 font-size:.62em;letter-spacing:.2em;text-transform:uppercase;color:var(--faint)}

.corpo{margin:auto 0}
.corpo p{margin:0 0 .95em;font-size:1.06em;line-height:1.66;text-align:justify;hyphens:auto}
.corpo p:first-child::first-letter{font-family:var(--fd);font-size:2.6em;line-height:.82;float:left;
 padding:.06em .12em 0 0;color:var(--accent)}
.corpo em{font-style:italic}

/* capa */
.is-capa{background:var(--graf);color:#F2EDE1;justify-content:space-between}
.capa{display:flex;flex-direction:column;height:100%;justify-content:space-between}
.cp-au{font-family:var(--fu);font-size:.78em;letter-spacing:.24em;text-transform:uppercase;color:#BFB49B;margin:0}
.cp-t{font-family:var(--fd);font-style:italic;font-weight:400;font-size:3.5em;line-height:.95;margin:.35em 0 0;letter-spacing:-.01em}
.cp-s{font-family:var(--fu);font-weight:300;font-size:.95em;line-height:1.5;color:#D8CFBB;margin:1.2em 0 0;max-width:22em}
.cp-d{font-family:var(--fu);font-size:.68em;letter-spacing:.24em;color:#8E8676;margin:0}

.rosto{margin:auto 0;text-align:center}
.rosto h2{font-family:var(--fd);font-style:italic;font-weight:400;font-size:2.5em;margin:0;line-height:1.05}
.r-s{font-size:1em;color:var(--soft);margin:1em auto 0;max-width:20em;line-height:1.5}
.r-a{font-family:var(--fu);font-size:.8em;letter-spacing:.2em;text-transform:uppercase;margin:2.4em 0 0}
.r-n{font-family:var(--fu);font-size:.68em;line-height:1.6;color:var(--faint);margin:3.2em auto 0;max-width:20em}

.epig{margin:auto 0}
.epig blockquote{font-family:var(--fd);font-style:italic;font-size:1.3em;line-height:1.4;margin:0;color:var(--ink)}
.epig cite{display:block;font-family:var(--fu);font-style:normal;font-size:.68em;letter-spacing:.16em;
 text-transform:uppercase;color:var(--faint);margin-top:1.6em}

/* sumario */
.is-sum{padding:2.8em 3.2em}
.sumario{display:flex;flex-direction:column;height:100%;min-height:0}
.sumario h3{font-family:var(--fu);font-size:.68em;letter-spacing:.2em;text-transform:uppercase;
 color:var(--accent);margin:0 0 .9em;flex:none}
.sm-list{overflow:hidden;font-size:.86em}
.sm-b{display:flex;align-items:baseline;gap:.6em;border-bottom:1px solid var(--rule);
 padding:.5em 0 .3em;margin-top:.7em}
.sm-b:first-child{margin-top:0}
.sm-n{font-family:var(--fu);font-size:.72em;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.sm-t{font-family:var(--fd);font-style:italic;font-size:1.12em}
.sm-y{margin-left:auto;font-family:var(--fu);font-size:.66em;color:var(--faint)}
.sm-c{display:flex;gap:.7em;padding:.12em 0;color:var(--soft)}
.sm-cn{font-family:var(--fu);font-size:.78em;color:var(--faint);min-width:1.6em;font-variant-numeric:tabular-nums}

/* parte */
.is-parte{color:#F4EFE3}
.c-ochre{background:var(--ochre)} .c-sea{background:var(--sea)}
.c-verm{background:var(--verm)} .c-terra{background:var(--terra)} .c-graf{background:var(--graf)}
.parte{margin:auto 0}
.pa-n{font-family:var(--fu);font-size:.75em;letter-spacing:.26em;text-transform:uppercase;
 color:rgba(255,255,255,.62);margin:0 0 .8em}
.pa-t{font-family:var(--fd);font-style:italic;font-weight:400;font-size:2.9em;line-height:1;margin:0}
.pa-y{font-family:var(--fu);font-size:.74em;letter-spacing:.2em;color:rgba(255,255,255,.55);margin:1.4em 0 0}

/* capitulo */
.capo{margin:auto 0}
.co-n{font-family:var(--fu);font-size:.7em;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin:0 0 .7em}
.co-t{font-family:var(--fd);font-style:italic;font-weight:400;font-size:2.3em;line-height:1.05;margin:0}
.co-s{font-size:1em;color:var(--soft);margin:1.1em 0 0;max-width:22em;line-height:1.5}
.co-r{display:block;width:2.6em;height:2px;margin-top:1.8em;background:currentColor;opacity:.9}
.co-r.c-ochre{background:var(--ochre)} .co-r.c-sea{background:var(--sea)}
.co-r.c-verm{background:var(--verm)} .co-r.c-terra{background:var(--terra)} .co-r.c-graf{background:var(--graf)}

/* imagem */
.fig{margin:auto 0;display:flex;flex-direction:column;gap:.9em;min-height:0}
.fig-i{display:flex;justify-content:center;min-height:0}
.fig img{max-width:100%;max-height:calc(58svh * var(--zoom));object-fit:contain;display:block;
 filter:saturate(.94)}
.fig figcaption{font-family:var(--fu);font-size:.72em;line-height:1.5;color:var(--soft);
 border-top:1px solid var(--rule);padding-top:.7em}

.fim{margin:auto 0;text-align:center}
.fm-1{font-family:var(--fd);font-style:italic;font-size:2.2em;margin:0;color:var(--accent)}
.fm-2{font-family:var(--fu);font-size:.76em;line-height:1.7;color:var(--faint);margin:1.6em 0 0}

/* chrome */
.bar{position:fixed;left:0;right:0;top:0;height:2px;background:transparent;z-index:40}
.bar i{display:block;height:100%;width:0;background:var(--accent);transition:width .12s linear}
.hud{position:fixed;z-index:41;font-family:var(--fu);font-size:.7rem;letter-spacing:.14em;
 text-transform:uppercase;color:var(--faint)}
.hud.tl{top:.85rem;left:1.1rem}
.hud.tr{top:.85rem;right:1.1rem;font-variant-numeric:tabular-nums}
.tocbtn{position:fixed;z-index:42;bottom:1.1rem;left:1.1rem;font-family:var(--fu);font-size:.7rem;
 letter-spacing:.14em;text-transform:uppercase;color:var(--ink);background:var(--sheet);
 border:1px solid var(--rule);padding:.45rem .8rem;cursor:pointer}
.tocbtn:hover{border-color:var(--accent);color:var(--accent)}
.zoomctl{position:fixed;z-index:42;bottom:1.1rem;right:1.1rem;display:flex;align-items:center;
 background:var(--sheet);border:1px solid var(--rule)}
.zoomctl button{background:none;border:0;color:var(--ink);font-family:var(--fu);font-size:.8rem;
 padding:.42rem .68rem;cursor:pointer;line-height:1}
.zoomctl button:hover,.zoomctl button:focus-visible{color:var(--accent);outline:none}
.zoomctl #zlab{font-family:var(--fu);font-size:.64rem;letter-spacing:.08em;color:var(--faint);
 min-width:2.9rem;text-align:center;font-variant-numeric:tabular-nums}
.toc{position:fixed;inset:0;z-index:60;background:var(--room);overflow-y:auto;padding:4rem 1.5rem 3rem;
 display:none}
.toc[data-open="1"]{display:block}
.toc-in{max-width:34rem;margin:0 auto}
.toc h4{font-family:var(--fu);font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
 color:var(--accent);margin:0 0 1.2rem}
.toc a{display:block;padding:.5rem 0;border-bottom:1px solid var(--rule);color:var(--ink);
 text-decoration:none;font-family:var(--fb);font-size:1rem}
.toc a:hover,.toc a:focus-visible{color:var(--accent);outline:none}
.toc .close{position:fixed;top:1rem;right:1.2rem;background:none;border:0;color:var(--ink);
 font-family:var(--fu);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;cursor:pointer}
@media (max-width:640px){.hud.tl{display:none}}
"""

JS = """
(function(){
 var stage=document.getElementById('stage');
 var leaves=[].slice.call(stage.querySelectorAll('.leaf'));
 var bar=document.getElementById('barfill');
 var lab=document.getElementById('lab'); var pos=document.getElementById('pos');
 var toc=document.getElementById('toc');
 var marks=[];
 leaves.forEach(function(l,i){ var n=l.getAttribute('data-nav'); if(n) marks.push({i:i,n:n}); });

 var ti=document.getElementById('tocin');
 marks.forEach(function(m){
  var a=document.createElement('a'); a.href='#'; a.textContent=m.n;
  a.addEventListener('click',function(e){e.preventDefault();go(m.i);close();});
  ti.appendChild(a);
 });
 function open(){toc.setAttribute('data-open','1');}
 function close(){toc.setAttribute('data-open','0');}
 document.getElementById('tocbtn').addEventListener('click',open);
 document.getElementById('tocclose').addEventListener('click',close);

 function go(i){ i=Math.max(0,Math.min(leaves.length-1,i)); leaves[i].scrollIntoView({block:'center'}); }

 var STEPS=[0.85,1,1.15,1.3,1.5,1.75,2], zi=1, zlab=document.getElementById('zlab');
 function paintZoom(){
  document.documentElement.style.setProperty('--zoom',STEPS[zi]);
  zlab.textContent=Math.round(STEPS[zi]*100)+'%';
  stage.setAttribute('data-zoomed', STEPS[zi]>1?'1':'0');
  document.getElementById('zminus').disabled = (zi===0);
  document.getElementById('zplus').disabled = (zi===STEPS.length-1);
 }
 function setZoom(d){
  var keep=cur(), nz=Math.max(0,Math.min(STEPS.length-1,zi+d));
  if(nz===zi) return;
  zi=nz; paintZoom();
  try{localStorage.setItem('tc_zoom',String(zi));}catch(e){}
  requestAnimationFrame(function(){ go(keep); upd(); });
 }
 document.getElementById('zplus').addEventListener('click',function(){setZoom(1);});
 document.getElementById('zminus').addEventListener('click',function(){setZoom(-1);});
 function cur(){
  var mid=stage.scrollTop+stage.clientHeight/2, best=0, bd=1e9;
  for(var i=0;i<leaves.length;i++){
   var c=leaves[i].offsetTop+leaves[i].offsetHeight/2, d=Math.abs(c-mid);
   if(d<bd){bd=d;best=i;}
  }
  return best;
 }
 var last=-1;
 function upd(){
  var i=cur();
  var pct=leaves.length>1? i/(leaves.length-1)*100 : 100;
  bar.style.width=pct.toFixed(2)+'%';
  pos.textContent=(i+1)+' / '+leaves.length;
  if(i!==last){
   last=i;
   var lb=''; for(var k=0;k<marks.length;k++){ if(marks[k].i<=i) lb=marks[k].n; }
   lab.textContent=lb;
   try{localStorage.setItem('tc_pos',String(i));}catch(e){}
  }
 }
 stage.addEventListener('scroll',function(){ window.requestAnimationFrame(upd); },{passive:true});

 document.addEventListener('keydown',function(e){
  if(toc.getAttribute('data-open')==='1'){ if(e.key==='Escape') close(); return; }
  var k=e.key;
  if(k==='ArrowDown'||k==='PageDown'||k===' '||k==='ArrowRight'){e.preventDefault();go(cur()+1);}
  else if(k==='ArrowUp'||k==='PageUp'||k==='ArrowLeft'){e.preventDefault();go(cur()-1);}
  else if(k==='Home'){e.preventDefault();go(0);}
  else if(k==='End'){e.preventDefault();go(leaves.length-1);}
  else if(k==='s'||k==='S'){open();}
  else if(k==='+'||k==='='){e.preventDefault();setZoom(1);}
  else if(k==='-'||k==='_'){e.preventDefault();setZoom(-1);}
  else if(k==='0'){e.preventDefault();setZoom(1-zi);}
 });

 var zsaved=null; try{zsaved=localStorage.getItem('tc_zoom');}catch(e){}
 if(zsaved!==null && STEPS[+zsaved]!==undefined) zi=+zsaved;
 paintZoom();

 var saved=null; try{saved=localStorage.getItem('tc_pos');}catch(e){}
 if(saved!==null && +saved>0){ setTimeout(function(){ go(+saved); upd(); },60); } else { upd(); }
})();
"""

HTML = """<title>Terceira Classe</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@1,6..96,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@300;400;500&display=swap">
<style>%s</style>

<div class="bar"><i id="barfill"></i></div>
<div class="hud tl" id="lab">Capa</div>
<div class="hud tr" id="pos">1 / 1</div>
<button class="tocbtn" id="tocbtn">Sumário</button>
<div class="zoomctl">
  <button id="zminus" type="button" aria-label="Diminuir a fonte" title="Diminuir (tecla -)">A&#8722;</button>
  <span id="zlab">100%%</span>
  <button id="zplus" type="button" aria-label="Aumentar a fonte" title="Aumentar (tecla +)">A&#43;</button>
</div>

<div class="toc" id="toc" data-open="0">
  <button class="close" id="tocclose">Fechar</button>
  <div class="toc-in"><h4>Terceira Classe &middot; navegação</h4><div id="tocin"></div></div>
</div>

<div class="stage" id="stage">
%s
</div>

<script>%s</script>
""" % (CSS, BODY, JS)

dst = os.path.join(SP, 'terceira-classe.html')
with io.open(dst, 'w', encoding='utf-8') as f:
    f.write(HTML)
print('paginas:', len(pages))
print('tamanho: %.2f MB' % (os.path.getsize(dst) / 1048576.0))
