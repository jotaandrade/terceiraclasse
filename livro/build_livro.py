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

AUD = os.path.join(SP, 'audio')

def b64aud(key):
    p = os.path.join(AUD, key + '.m4a')
    if not os.path.exists(p):
        raise SystemExit('audio inexistente: ' + key)
    with open(p, 'rb') as f:
        return 'data:audio/mp4;base64,' + base64.b64encode(f.read()).decode()

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
  (8,'Rosa e Fausto','Enrico nasce em outubro de 1926, o casamento e em dezembro, e Fausto parte.'),
 ],
 'II': [
  (9,'Gênova','O porto como sistema. A babel de dialetos, a despedida definitiva.'),
  (10,'A terceira classe','O porão por dentro: beliches, comida racionada, os corpos jogados ao mar.'),
  (11,'Duas irmãs embarcam','Sete pessoas sobem a prancha, e nenhuma delas é um homem adulto.'),
  (12,'Os que já estavam lá','Fausto e Angelo no Brasil, a casa preparada, a espera.'),
 ],
 'III': [
  (13,'1908','O navio gêmeo que afundou no próprio lançamento, e o nome que veio depois.'),
  (14,'Os anos de glória','Cento e quarenta pessoas em cima, mil embaixo. A glória era o andar de cima.'),
  (15,'O declínio','Ele não foi aposentado. Foi rebaixado, um degrau por vez, por navios mais novos.'),
  (16,'A última viagem','Quem estava a bordo. Garovaglio, von Lücken, Bucherer, o comandante Gulì.'),
  (17,'17h15','O eixo da hélice de bombordo se rompe.'),
  (18,'A noite','Hora a hora, do estrondo às 22h10.'),
  (19,'Os botes','Lugares vendidos, botes danificados, os tubarões.'),
  (20,'22h10','O navio afunda. Gulì fica a bordo.'),
  (21,'Alhena, Mosella, Empire Star','O resgate a noite inteira.'),
  (22,'Os 314','Os mortos não têm lista, não têm sepultura e não têm nome. E o país nunca guardou a data.'),
 ],
 'IV': [
  (23,'31 de outubro','Hospedaria do Brás. Livro 100, página 290.'),
  (24,'O reencontro','Fausto e Angelo recebem as mulheres e as crianças.'),
  (25,'Terra vermelha','Grama, o café, e a palavra que decidiu tudo: espontâneos.'),
  (26,'Enrico','1926 a 1998. Cinco documentos, e nada além do que eles dizem.'),
  (27,'1937','A menina recebe o nome do navio, e a objeção que essa frase precisa aguentar.'),
  (28,'Virar brasileiro','A língua que some em duas gerações, e os sobrenomes que saem da linha em três.'),
  (29,'Os que ficaram, cem anos depois','O ramo do Sante. Ficar não produz documento — e o site que reencontrou a família.'),
  (30,'A busca','Como o papel mente, como a memória mente, e o que custa começar tarde.'),
  (31,'A casa','Escrito por quem nunca esteve lá. A porta por onde Rosa saiu, vista de longe.'),
 ],
}

# --------------------------------------------------- capitulos escritos
CAP9 = [
"""Gênova, em 1927, tinha mais gente dentro dela do que todas as vilas do sopé do Grappa
somadas.

Rosa Forner nunca tinha visto uma cidade. Nem a irmã. As duas conheciam Asolo, que tem uma
praça e uma rua principal, conheciam Treviso de passagem, e nada mais.

E não foram a Gênova para conhecer Gênova. Ninguém ia. A cidade não era destino, era
funil: o lugar por onde a Itália vinha escoando a própria gente havia sessenta anos.""",

"""Em algum momento daquela chegada, elas viram o mar.

Não sei em que momento nem de onde. Sei que era a primeira vez, para as duas e para as
cinco crianças.

É uma coisa difícil de imaginar hoje: uma mulher de trinta e um anos vendo o mar pela
primeira vez.

Quem cresce no sopé de uma montanha tem o horizonte a dois quilômetros de distância, e
sempre teve. O horizonte é uma encosta, e atrás dela vem outra.

Gênova é a primeira vez em que aquela gente olha para a frente e não encontra nada.""",

"""E ali, encostado no cais, está o navio.

O <em>Principessa Mafalda</em> tinha dezenove anos e nove mil duzentas e dez toneladas.

Tonelagem não diz nada a ninguém. Isto diz: naquela viagem ele levou mil duzentas e
cinquenta e nove pessoas. Castelcucco inteira, com os seus mil setecentos e vinte e nove
habitantes, quase cabia lá dentro.

Era, com folga, a maior coisa construída que qualquer uma daquelas pessoas tinha visto na
vida.

E não era navio novo, nem bonito, nem orgulho de ninguém. Era um transatlântico velho de
linha regular, no fim da carreira, fazendo o trajeto que sobra para os navios velhos.""",

"""Quem subiu aquela prancha junto com elas?

É uma pergunta que quase nunca tem resposta. Nesta história tem, e por um motivo ruim:
catorze dias depois, cinquenta daquelas pessoas seriam recolhidas do mar e desembarcadas no
Rio de Janeiro, e um funcionário da Intendência de Imigração sentou e escreveu os nomes
numa lista.

Todos com a mesma anotação na coluna do embarque: <strong>Genova, 3ª</strong>.""",

"""<strong>Beck Josef</strong>, iugoslavo, cinquenta e três anos, agricultor, com a mulher
Anna, o filho Ivan de vinte e três e a filha Elizabeth de dezesseis. Iam para São Paulo.

<strong>Bán Sándor</strong>, húngaro, vinte e nove anos, israelita, sozinho.

Os irmãos <strong>Ströbel</strong>, Ernö e Gottfried, vinte e seis e vinte e cinco anos.

<strong>Ruspollo Eugenio</strong>, quarenta e dois, agricultor, com a mulher Maria e quatro
filhos: Giselda de catorze, Serafina de treze, Paulo de onze e Maria-Luisa de dois.

<strong>Zaninni Oliviano</strong>, cinquenta e seis anos, e a mulher <strong>Zaira</strong>,
cinquenta e oito. Os mais velhos da lista.

<strong>Dattoma Cosimo</strong>, dezoito anos, sapateiro.""",

"""E os Pettina.

Ottavio, vinte e cinco anos. A mulher, também chamada Rosa, vinte e cinco. A filha Ottavia,
de dois.

E a segunda filha, Maria, cuja idade a lista registra assim:

<strong>3/12</strong>

Três doze avos de um ano. Três meses.

Alguém subiu aquela prancha em Gênova, em outubro de 1927, carregando no colo um bebê de
três meses de idade.""",

"""E subiram duas mulheres que importam mais do que todas as outras desta lista.

<strong>Luchini Teresa, dezenove anos.</strong>

<strong>De Rosi Emilia, cinquenta e cinco.</strong>

Na relação do Rio de Janeiro elas aparecem uma seguida da outra, sozinhas, sem parentesco
declarado, e as duas com um <em>x</em> marcado à margem.

No pé da mesma folha, escrito à mão pelo funcionário que fechou o documento, está o
motivo:

<em>As passageiras constantes sob Nº 24 e 25 perderam seus maridos, e pedem de ser enviadas
para Italia.</em>""",

"""Em Gênova, em 11 de outubro, elas não eram isso.

Eram duas mulheres casadas subindo uma prancha com os maridos do lado, indo começar outra
vida.

Uma delas tinha dezenove anos.

Dezessete dias depois estava pedindo para voltar para o lugar de onde tinha acabado de
sair.""",

"""Repare na composição daquela lista.

Iugoslavos, húngaros, italianos do norte, italianos do sul, um israelita, um sapateiro de
dezoito anos, um casal de quase sessenta, lavradores, um carpinteiro, um carvoeiro.

<strong>A terceira classe não era um lugar. Era uma tarifa.</strong>

O que aquelas pessoas tinham em comum não era país, nem língua, nem religião, nem ofício.
Era o preço do bilhete.

Quinze anos antes aquele porão teria sido quase todo italiano. Em 1927 já não era. Nas duas
semanas seguintes, aquela gente ia dividir o mesmo espaço sem partilhar uma língua.""",

"""E no meio disso, sete pessoas de uma família só.

<strong>Forner Rosa</strong>, vinte e quatro anos, com <strong>Enrico</strong>, de um.

<strong>Forner Maria</strong>, trinta e um anos, com <strong>Ginneta</strong>, de sete,
<strong>Pulgheria</strong>, de seis, <strong>Rino</strong>, de quatro, e
<strong>Danilo</strong>, de dois.

Duas mulheres e cinco crianças. A mais velha delas tinha sete anos.

Nenhum homem adulto no grupo.""",

"""O navio saiu de Gênova em <strong>11 de outubro de 1927</strong>.

Um dia antes, em 10 de outubro, Enrico Miotto tinha completado um ano de idade.

Fez um ano em Gênova, esperando embarcar, e não existe registro nenhum de que alguém tenha
comemorado.""",

"""O capítulo anterior termina dizendo que a última coisa que aquelas duas mulheres viram do
lugar onde nasceram foi o Monte Grappa.

É verdade, e agora dá para completar.

A última coisa que elas viram da <em>Itália</em> não foi o Grappa. O Grappa fica a
trezentos quilômetros de Gênova.

Foi uma cidade portuária que elas conheciam havia poucos dias, cheia de gente falando um
dialeto que elas não entendiam, vista de longe, do convés de um navio velho.

Ninguém se despede de uma pátria. Despede-se de um lugar. E o lugar delas tinha ficado para
trás dias antes, numa estrada que descia para Asolo.""",

"""Do cais, o que se via era um navio grande saindo devagar.

Mil duzentas e cinquenta e nove pessoas a bordo, a maior parte delas no porão. Catorze dias
de mar até o Rio de Janeiro.

Trezentas e catorze não chegariam.""",
]

CAP10 = [
"""Quem viajou na primeira classe daquele navio deixou registro. Deu entrevista aos jornais,
publicou, contou. Sabemos até o nome do fotógrafo de bordo.

Do porão não sobrou memória escrita. Ninguém que atravessou lá embaixo publicou um livro
sobre aquilo, e é quase certo que a maioria não teria como.

Sobraram três coisas: papel de repartição, um punhado de entrevistas dadas em pânico, e a
lembrança de uma menina de seis anos.""",

"""Sobre as entrevistas, uma palavra antes de usá-las, aqui e no resto deste livro.

Nos dias seguintes ao naufrágio, jornais da Argentina e do Brasil ouviram dezenas de
sobreviventes. Vinte desses relatos chegaram até mim, em tradução, com nome, idade e
procedência de cada um.

São a melhor fonte que existe sobre o que se passava dentro daquele navio, e são,
praticamente, a única. Ainda não localizei o jornal, a data e a página de cada um, e estou
atrás disso.

Enquanto não acho, digo toda vez o que eles são: gente que tinha acabado de sair da água,
falando com repórter, poucos dias depois.""",

"""A terceira classe do <em>Principessa Mafalda</em> não era um convés aberto com gente
deitada no chão, como nas fotografias de vinte anos antes.

Era um andar de dormitórios, abaixo da linha d'água, com beliches de ferro em duas ou três
alturas, separados por sexo, e camarotes de quatro ou seis lugares para as famílias.

<strong>Maria Spinelli</strong>, italiana, terceira classe, conta que às cinco da tarde do
dia 25 estava se lavando <em>na cabine</em>. Não era um alojamento coletivo. Era um quarto
apertado, com porta.

Isso importa, e vou voltar a isso: significa que aquelas pessoas estavam separadas em
compartimentos pequenos, embaixo, quando a água entrou.""",

"""O resto era o que sempre foi.

Comida servida em fila, com a marmita que cada um trazia de casa. Ar recirculado por
ventilação forçada, que funcionava quando funcionava. Banheiro coletivo. Piolho e sarna,
que atravessavam o Atlântico com a mesma regularidade dos passageiros.

E a bagagem, que era desinfetada antes do embarque e voltava cheirando a enxofre.

Quem morria durante a travessia era enterrado no mar. Não era brutalidade: era o
procedimento de um navio com duas semanas de viagem pela frente e sem lugar para guardar
um corpo.""",

"""O que me interessa é que <strong>o navio anotava isso</strong>.

Nas folhas de terceira classe de 1923 e 1924, alguém riscou os títulos impressos das
colunas de bagagem e escreveu por cima, à mão, quatro palavras em italiano:

<strong>Bauli · Valigie · Denaro · Indirizzo</strong>

Baús. Valises. Dinheiro. Endereço.""",

"""<em>Denaro</em> é o dinheiro que cada pessoa declarava trazer ao desembarcar.

Está preenchido assim, linha após linha:

<em>1 baú, 1 valise, £ 120, Araraquara.</em>

<em>2 baús, 1 valise, £ 800, São Paulo.</em>

<em>1 baú, 1 valise, £ 1.350, Cuiabá.</em>

E, numa linha que eu li três vezes para ter certeza:

<strong><em>8 baús, 1 valise, £ —, São Paulo.</em></strong>

Um traço. Oito baús e um traço.

Alguém desembarcou em Santos carregando tudo o que possuía no mundo e nenhum dinheiro para
o dia seguinte.""",

"""A coluna do <em>Indirizzo</em> existe porque o Estado brasileiro queria saber onde cada
uma daquelas pessoas ia parar. Traz cidade, e às vezes o nome de uma fazenda.

É uma coluna administrativa e é, ao mesmo tempo, a lista dos lugares para onde a Itália
estava indo morar. Araraquara. São Paulo. Cuiabá.

Ninguém escreveu <em>Gênova</em> em nenhuma delas. Não havia volta prevista.""",

"""E há uma anotação que desfaz uma imagem inteira.

Na folha de 25 de janeiro de 1924, ao lado de três linhas, alguém escreveu à margem:

<em>passato in 2ª cl.</em>

Passou para a segunda classe. No meio da travessia.

Uma das três é <strong>Giannini Giovanni</strong>, cinquenta e três anos, declarado
<em>possidente</em>, viajando com a filha.""",

"""A imagem confortável é a de três mundos lacrados, separados por chapa de aço: os ricos em
cima, os pobres embaixo, e nenhuma passagem entre eles.

Não era assim.

<strong>A terceira classe não era um lugar. Era um preço.</strong> E preço se paga a
qualquer hora, inclusive no quinto dia de mar, quando alguém que podia decidiu que já
tinha dormido embaixo o suficiente.

Quem não podia continuava lá.""",

"""Na mesma folha, linha noventa e dois, há um nome riscado em vermelho.

Ao lado, na margem, uma palavra e uma data. A palavra é de leitura difícil e não vou
forçá-la. A data não é: <strong>19 de janeiro de 1924</strong>.

O navio atracou em Santos no dia 25.

Aquela pessoa embarcou em Gênova, atravessou o Atlântico, morreu seis dias antes de
chegar, e o registro disso é um traço vermelho sobre o nome dela numa lista de
desembarque.

O corpo foi para o mar. O nome ganhou uma linha por cima.""",

"""Outra coisa que o papel revela, e que eu não esperava.

<strong>O porão não esvaziava em Santos.</strong>

Em 17 de dezembro de 1921 o navio trazia oitocentos e vinte pessoas na terceira classe.
Pouco mais de oitenta desembarcaram.

Os outros setecentos continuaram viagem, para Montevidéu e Buenos Aires.

Quem descia em Santos descia sozinho, no meio de um navio que seguia sem ele. E quem
ficava a bordo via a fila diminuir e o Brasil ficar para trás.""",

"""E o navio só ia cheio numa direção.

Descendo da Europa: oitocentas pessoas na terceira classe. Oitocentas e vinte e três numa
viagem, setecentas e oitenta e uma noutra, novecentas e dez em junho de 1923, que é o
recorde do conjunto que examinei.

Subindo de Buenos Aires: <strong>vinte e três</strong>.

Não era um navio de passageiros que também levava imigrantes. Era um navio de imigrantes
que também levava passageiros, e só numa direção.""",

"""Quem estava naquele porão em 1927 já não era só italiano.

As colunas de nacionalidade mostram a virada acontecendo em cinco meses: em agosto de 1923
desembarcaram em Santos sessenta e cinco italianos e vinte e oito sírios; em janeiro de
1924, quarenta sírios e trinta e dois italianos.

<strong>Milhem Solk</strong>, libanês de Beirute, na terceira viagem dele à Argentina,
disse depois uma frase que resume o andar inteiro: a maioria dos companheiros dele não
falava italiano nem espanhol.

Duas semanas dividindo o mesmo ar, a mesma fila e o mesmo cheiro, sem conseguir conversar.""",

"""E havia a cozinha.

Numa terceira classe com quinhentas, oitocentas, novecentas pessoas, a cozinha é o único
lugar do navio que funciona sem parar. É quente, é barulhento, tem gente entrando e saindo
a toda hora, e é o lugar de onde vem a única coisa que todo mundo ali espera três vezes ao
dia.

Crianças não deveriam entrar. Uma entrou.""",

"""<strong>Pulcheria Dei Agnoli tinha seis anos</strong>, era filha de Maria Luigia, e não
saía da cozinha.

Brincava com todo mundo, e havia ali um cozinheiro, um homem de pele escura, que gostava
dela.

Isto não está em documento nenhum. Não está nos manifestos, não está nas listas, não está
em jornal. É lembrança de família, atribuída à própria Pulcheria, e chegou até mim por uma
prima de outro ramo.

E não é lembrança unânime. Outra bisneta de Maria Luigia, que ouviu do avô tudo o que sabe
desta história, não conhece este cozinheiro.""",

"""Guarde esse cozinheiro.

Daqui a oito capítulos, quando o navio estiver inclinado e cheio de água e as duas irmãs
tiverem se escondido no fundo de um porão, é ele que vai descer atrás delas.

O papel de repartição registrou o dinheiro, a bagagem, o destino e a morte daquela gente.

Não registrou isso.""",
]

CAP14 = [
"""Enquanto o navio atravessava, dois homens esperavam em algum lugar do interior de São
Paulo.

Angelo Dei Agnoli, casado com Maria Luigia. Fausto Miotto, casado com Rosa.

Dos dois, um deixou rastro. O outro não deixou nenhum.""",

"""Angelo foi primeiro, e foi muito antes do que a família conta.

Em 14 de fevereiro de 1925, no Comune di Cavaso del Tomba, registrou-se o nascimento de
Danilo Angelo Dei Agnoli.

Quem foi declarar não foi o pai. Foi a parteira, Celli Maria. E o escrivão anotou o motivo,
em italiano de cartório:

<em>in luogo del marito, perché residente all'estero a scopo di lavoro.</em>

Em lugar do marido, por estar residindo no exterior a trabalho.""",

"""Leia outra vez o que esse documento é.

<strong>É uma certidão de nascimento que registra a ausência de um pai.</strong>

E o Estado italiano tinha fórmula pronta para isso. A situação era tão corriqueira que não
exigia explicação nenhuma: bastava a frase feita, e o escrivão seguia para a linha
seguinte.

Não era exceção. Era categoria.""",

"""Isso desfaz uma coisa que a família conta.

A versão que chegou até mim é a de que os dois cunhados atravessaram juntos. Os dois
maridos vão na frente, as duas irmãs ficam para trás, e depois mandam buscar.

Não foi assim.

Em fevereiro de 1925, quando Angelo já estava fora trabalhando, Fausto Miotto tinha vinte
anos e ainda não tinha casado. Faltavam vinte e dois meses para o casamento dele com a
Rosa.

Angelo saiu antes, e por uma margem larga.""",

"""E em algum momento Angelo voltou à Itália, porque em 1927 ele fez a travessia outra vez,
no sentido de vir.

Existe uma certidão do Serviço de Registro de Estrangeiros, número 61, que registra o
desembarque:

<strong>Santos, 30 de abril de 1927. Vindo do vapor Principessa Mafalda.</strong>""",

"""Pare um segundo nessa linha.

Angelo Dei Agnoli conheceu aquele navio. Atravessou nele. Dormiu naquele porão, comeu
naquela fila, subiu e desceu aquelas escadas.

E seis meses depois embarcou nele a mulher, com Gina, Pulcheria, Rino e Danilo.

<strong>Ele mandou buscar a família no navio que ele mesmo tinha usado, e do qual não teve
o que reclamar.</strong>""",

"""E o Fausto?

Nada.

Não está no Registro de Matrícula da Hospedaria do Brás: a busca pelo nome dele retorna
zero. Não está em nenhum dos vinte e cinco manifestos do <em>Principessa Mafalda</em> que
examinei, embora esses parem em 1924. Não há ficha de estrangeiro localizada.

O homem que fez esta família atravessar o Atlântico não deixou registro nenhum de ter
atravessado ele mesmo.""",

"""O que dá para dizer é onde ele cabe.

Casou-se em Castelcucco em <strong>3 de dezembro de 1926</strong>, o que prova que estava na
Itália naquele dia. Rosa embarcou em Gênova em <strong>11 de outubro de 1927</strong>, o
que prova que ele já estava do outro lado, e estabelecido o bastante para mandar buscá-la.

Dez meses.

É toda a precisão que eu tenho sobre a travessia do meu bisavô.""",

"""E a ausência dele não é mistério. É coerência.

O capítulo 6 mostrou que Fausto não veio recrutado. Não tinha patrão declarado, não tinha
fazenda marcada, não estava em Relação de subsidiados nenhuma.

Quem chegava assim, com dinheiro próprio e destino próprio, não passava pela Hospedaria. A
Hospedaria era para quem precisava ser encaminhado, e ele não precisava.

A falta dele naquele livro não é buraco do arquivo. É o retrato de um homem que veio por
conta própria.""",

"""O destino, esse eu sei.

<strong>Grama</strong>, hoje São Sebastião da Grama, município da comarca de São José do Rio
Pardo, no nordeste do estado de São Paulo. Terra de café.

Dois documentos põem a família ali: o carimbo da Delegacia de Polícia de Grama na ficha de
estrangeiro do Angelo, e o assento de casamento número 660 do cartório de Grama, de 1947,
que registra o casamento de uma filha de Fausto e Rosa nascida naquele município.

Era para lá que aquelas sete pessoas estavam indo.""",

"""E o que ele foi fazer lá foi o que sabia fazer.

<strong>Agricultor.</strong>

O mesmo ofício que a família tinha na encosta do Grappa. A mesma enxada, o mesmo corpo, a
mesma terra de outro homem.

Atravessaram um oceano para fazer exatamente a mesma coisa.""",

"""O cartaz da praça, vinte anos antes, prometia <em>terre in Brasile per gli Italiani</em>.
Terras no Brasil para os italianos. Prometia que o governo dava terra e ferramenta a todos,
e que no Brasil se podia ter o próprio castelo.

O que havia era café, e trabalho de agricultor, e nenhuma escolha.

Não porque tivessem sido enganados na hora de embarcar. Fausto veio em 1927, quando o
cartaz já tinha desbotado havia duas décadas e ninguém precisava mais vender nada a
ninguém.

Veio porque era isso ou a encosta. E do outro lado era isso também, com café no lugar do
milho.""",

"""Era com esse trabalho que se pagavam as passagens.

Sete bilhetes de terceira classe, Gênova a Santos. Dois homens no interior paulista
guardando o que a lavoura deixava guardar, durante meses, até dar.

Não sei quanto custava um bilhete daqueles em 1927. Ainda não achei o número.

Sei o intervalo: Angelo desembarcou de volta em abril, e elas embarcaram em outubro. Seis
meses entre uma coisa e outra.""",

"""E há um mecanismo por trás desses seis meses, que tem nome e era o mais comum de todos.

Chamava-se <strong>chamada</strong>.

O homem que já estava do outro lado juntava dinheiro, comprava a passagem aqui, e mandava —
em remessa, ou como bilhete pré-pago para ser retirado numa agência do porto de Gênova.

Não era gesto isolado de ninguém. Era uma das maiores movimentações de dinheiro da Itália
daquele tempo: emigrante mandando moeda estrangeira para casa, mês após mês, por décadas.""",

"""E se foi assim com esta família — e é de longe o mais provável — então há uma consequência
que eu levei muito tempo para enxergar.

<strong>A data da viagem de Rosa não foi decidida por Rosa.</strong>

Foi decidida pelo tempo que Fausto levou para juntar o dinheiro numa lavoura de café no
interior de São Paulo.

Se ele tivesse juntado dois meses antes, ela teria pegado outro navio. Se tivesse demorado
dois meses a mais, teria pegado outro navio.""",

"""É a coisa mais fria deste livro, e eu ainda não sei o que fazer com ela.

Um homem de vinte e três anos, sem português, trabalhando terra que não era dele, mandou
buscar a mulher e o filho assim que pôde. Fez a única coisa certa que havia para fazer, e fez
o mais rápido que conseguiu.

<strong>E foi isso que escolheu o navio.</strong>""",

"""Em outubro de 1927 os dois sabiam a data.

Sabiam o nome do navio, sabiam quando tinha saído de Gênova e sabiam mais ou menos quando
encostaria. Uma carta tinha atravessado o oceano com essa informação, semanas antes.

O que aconteceu depois é assunto da parte seguinte deste livro, e eu não vou antecipar.""",

"""Só uma coisa, que pertence a este capítulo e não àquele.

Os dois foram esperar. Estavam lá, procurando.

Isso não está em documento nenhum. É lembrança de família, atribuída a uma menina de seis
anos que estava naquele navio, e chegou até mim por duas primas de outro ramo.

<strong>Fausto Miotto não aparece em nenhuma lista de 1927.</strong>

Aparece na memória de uma criança que nem filha dele era.""",
]

CAP21 = [
"""A primeira coisa que aconteceu depois do estrondo foi alguém subir à ponte para
perguntar.

<strong>Eugenio Gabassi</strong>, vice-cônsul italiano na cidade argentina de Paraná,
cinquenta e seis anos, foi falar com o comandante assim que sentiu o navio parar.

Voltou tranquilizado. Disseram a ele que não havia com que se preocupar e que, no pior dos
casos, o navio seria rebocado até o Rio de Janeiro.""",

"""Essa frase circulou pelo navio a noite inteira, e matou gente.

<strong>Pedro Volpi</strong>, trabalhador agrícola italiano de trinta e três anos, ficou a
bordo até o último instante possível. Explicou depois por quê, sem nenhum rancor: o capitão
tinha dito que o navio ficaria à tona até o dia seguinte.

Ele não estava sendo ingênuo. Estava obedecendo a autoridade do lugar onde estava.""",

"""E quem não acreditou saiu cedo.

<strong>Pascual Pecci</strong> viajava na segunda classe com a mulher e a filha. Achou que
o comandante estava enganado sobre o tempo que o navio aguentaria, e agiu por conta
própria: tirou a família dali logo no começo.

Os três sobreviveram.

Pecci disse depois, com todas as letras, que a palavra do comandante tinha embalado os
passageiros da primeira classe numa falsa sensação de segurança.""",

"""Enquanto isso, no porão, ninguém sabia de nada.

<strong>Milhem Solk</strong>, libanês de trinta e cinco anos, ouviu o estrondo e foi
perguntar. Procurou marinheiro, perguntou a vários, um atrás do outro.

Nenhum deles soube dizer o que tinha acontecido.

Não é que estivessem escondendo. É que não sabiam. A informação levava tempo para descer, e
a essa altura já havia mais gente perguntando do que gente com resposta.""",

"""E o navio ia deitando.

Ele já vinha adernado desde antes do acidente, como se viu dois capítulos atrás. Depois do
eixo, a inclinação deixou de ser desconforto e virou geometria.

<strong>Enrico Nazzeconi</strong> descreve a certa altura da noite uma inclinação a
estibordo em estado extremo. <strong>Ali Hassen</strong> fala da popa afundando.

Uma coisa que quem nunca esteve num navio não imagina: quando o casco inclina, o chão deixa
de ser chão. Corredor vira ladeira. Escada vira parede. E cada grau a mais torna mais
difícil sair de onde se está.""",

"""O pedido de socorro saiu, e é sobre a hora dele que as fontes brigam.

Uma diz <strong>17h35</strong>, vinte minutos depois do eixo partir. Outra diz
<strong>19h15</strong>, quase duas horas depois.

São duas noites diferentes. Numa, o navio pediu ajuda quase imediatamente. Na outra,
esperou.

Não tenho como decidir entre as duas, e não vou fingir que tenho. O que é certo é o
resultado: o pedido foi ouvido, e navios mudaram de rota para vir.""",

"""Às seis e vinte e um da tarde o sol se pôs, como o capítulo anterior mostrou.

A partir daí, tudo o que se conta desta história aconteceu no escuro.

Não é detalhe atmosférico. É a condição de tudo o que vem: cada decisão, cada bote, cada
salto na água, cada pessoa procurando outra, tudo isso foi feito sem enxergar.""",

"""Os depoimentos voltam a esse ponto o tempo todo, e sempre da mesma maneira.

Volpi, perguntado se tinha visto tubarões, respondeu que não, e emendou: <em>a noite estava
muito escura</em>.

Nazzeconi, que ficou a bordo até quase o fim, disse que se jogou na água, ouviu três apitos
longos e um estrondo, e <strong>não conseguiu ver o navio afundar</strong>. Estava a poucas
dezenas de metros dele.

<strong>Batista Beria</strong>, nadando, só via o que os holofotes dos navios de resgate
alcançavam. Nos intervalos, ouvia gritos sem conseguir localizar de onde vinham.""",

"""E a informação continuou distribuída como sempre tinha estado a bordo: por classe.

<strong>Nicola Lynose</strong>, iugoslavo da terceira classe, explicou o mecanismo sem
querer. Quem viajava embaixo estava colado à tripulação e enxergava o que a tripulação
fazia.

Quem viajava em cima tinha a palavra do comandante.

No dia a dia isso é uma diferença de conforto. Naquela noite virou uma diferença de tempo
de reação, e tempo de reação, ali, era a distância entre estar num bote e estar na água.""",

"""Havia também quem simplesmente esperasse.

A <strong>família Vacelli</strong> — o casal e três filhos de quinze, treze e dez anos —
passou a noite inteira na popa, junto à escada, aguardando a vez. O pai repetia que havia
tempo.

Às <strong>nove e meia da noite</strong> um bote do <em>Empire Star</em> encostou naquela
escada e levou os cinco.

Eles acham que foram dos últimos a sair. Mal chegaram ao navio inglês e o Mafalda já não
estava lá.""",

"""<strong>Mario Ottaviani</strong>, que ficou a bordo até quase o fim porque sabia nadar,
deixou um número.

Quando entendeu que o navio ia mesmo afundar e se jogou, ainda havia nos conveses
<strong>cerca de sessenta mulheres e crianças</strong>, e cerca de <strong>duzentos
homens</strong>.

Guarde esse número. Ele volta no capítulo dos 314.""",

"""Meia hora antes do fim, o navio começou a fazer um barulho novo.

Lynose descreve: móveis, louça e cristais se quebrando dentro dos salões.

Era a inclinação chegando ao ponto em que nada mais fica parado. Tudo o que estava sobre uma
superfície horizontal deixou de estar, ao mesmo tempo, em todos os cômodos do navio.

Quem estava no porão ouviu aquilo por cima da cabeça e entendeu.""",

"""E as sete pessoas desta história?

Duas mulheres. Cinco crianças, a mais velha com sete anos, a mais nova com dois. Um bebê de
um ano no colo de uma delas.

Nenhuma das duas sabia nadar. Nenhuma delas falava a língua da tripulação. Estavam num
andar abaixo da linha d'água, num navio inclinando, no escuro.

O que os documentos dizem sobre elas nessa noite é nada. Elas entram no papel de novo só
três dias depois, no Rio de Janeiro.""",

"""O que existe é uma lembrança.

<strong>Rosa e Maria Luigia desceram e se esconderam no fundo de um porão.</strong>

Não subiram para o convés. Não foram para os botes. Foram para baixo, para o lugar mais
fundo que conheciam, e ficaram lá com as cinco crianças.

Pode parecer a pior decisão possível. Não é difícil de entender.

Lá em cima havia empurrão, grito, gente correndo em quatro línguas e botes virando. Elas
não sabiam nadar. Duas mulheres com cinco crianças pequenas, num convés inclinado no
escuro, não têm chance nenhuma de manter as cinco juntas.

Então fizeram o que se faz quando não há como avançar: se enfiaram num canto e seguraram as
crianças.""",

"""E alguém foi buscá-las.

Havia na cozinha daquele navio um cozinheiro, um homem de pele escura, que tinha se afeiçoado
a <strong>Pulcheria</strong> nas duas semanas de travessia. A menina de seis anos que não
saía de lá.

Quando o navio estava se enchendo de água, ele desceu ao porão, achou as duas mulheres e as
cinco crianças, e tirou todos de lá.

Levou-os para o <strong>bote dos cozinheiros</strong>.""",

"""Preciso dizer exatamente o que isto é.

Não está em documento nenhum. Não está nos manifestos, não está na lista do Rio, não está
em jornal, não está no inquérito. Nenhum papel deste livro registra esse homem.

É lembrança de família, e eu preciso ser exato sobre de quem.

Ela é atribuída à própria Pulcheria, que tinha seis anos e estava lá, e chegou até mim por uma
prima de outro ramo — bisneta de Maria Luigia, como eu sou bisneto de Rosa.

E <strong>a outra linha desta família não tem essa história.</strong> A Patrícia Betti, também
bisneta de Maria Luigia e neta da Pulcheria, ouviu tudo o que sabe do avô, João Betti, que era
o marido da Pulcheria. Do cozinheiro ele nunca falou.

Então não são duas testemunhas. É uma lembrança que desceu por um galho desta família e não
desceu pelo outro.

E é a única explicação que existe para sete pessoas terem saído de dentro de um porão
alagado.

<strong>Sem esse homem, este livro não teria autor.</strong>""",

"""O <em>Principessa Mafalda</em> perdeu energia às <strong>dez e três da noite</strong>.

Sete minutos depois, às <strong>dez e dez</strong>, afundou.

Nazzeconi, na água, ouviu três apitos longos e, logo em seguida, um estrondo que ele não
soube descrever de outro jeito.

E não viu nada, porque estava escuro.""",
]

CAP22 = [
"""Lendo os vinte depoimentos em sequência, uma coisa aparece que nenhum deles diz sozinho.

<strong>O que matou naquela noite não foi a água.</strong>

Quase ninguém morreu por ter caído no mar e não saber nadar. Morreu por ter entrado num
bote.""",

"""<strong>Ali Hassen</strong>, árabe de quarenta e cinco anos, viajando com três primos,
subiu ao convés e se atirou num bote junto com cerca de cinquenta pessoas. Pelo peso, o
bote afundou.

<strong>Salvador Malone</strong> conseguiu lugar no terceiro bote lançado. A poucos metros
do navio, ele virou.

<strong>Antonio Ponce</strong> entrou num com pelo menos trinta pessoas. A vinte metros do
<em>Alhena</em>, o nervosismo de um dos companheiros fez o bote emborcar.

<strong>Valeriano Galli</strong>, como boa parte da terceira classe, foi dos primeiros a
entrar. O bote cedeu sob o peso e ele foi parar na água.""",

"""<strong>Maria Spinelli</strong> tinha ao lado a amiga Teresa Forggia e o filho dela,
Mario, de três anos.

Um tripulante as obrigou a descer e entrar num bote. Elas entraram.

E então, <strong>a trinta centímetros da água</strong>, as cordas de um dos lados
arrebentaram.

Trinta centímetros. Foi essa a margem.""",

"""<strong>Vincenzo Mandolezzi</strong> esperou uma hora e meia a bordo antes de se jogar.
Nadou até alcançar um dos botes do próprio Mafalda.

Estava furado, ou rachado, ou de alguma forma inservível — ele diz apenas que não estava em
bom estado.

Eram nove pessoas dentro. Remaram com as mãos.""",

"""As razões se acumulam e nenhuma delas é misteriosa.

Botes velhos num navio velho. Superlotação, porque todo mundo queria o mesmo lugar ao mesmo
tempo. Lançamento feito às pressas, no escuro, por gente que nunca tinha feito aquilo de
verdade — o único exercício foi na véspera, ao meio-dia, e era exercício de incêndio.

E o adernamento.

Um navio inclinado tem um lado bom e um lado inútil. De um deles os botes descem raspando o
casco. Do outro, ficam pendurados longe demais para alguém alcançar.

Metade dos botes daquele navio já não servia antes de qualquer pessoa entrar neles.""",

"""E aí a quilha virou o lugar mais seguro do Atlântico.

<strong>Alfio Sanfilippo</strong> se atirou na água às seis da tarde com o irmão e um
oficial do Mafalda. Quase todos os botes já tinham virado. Os três se agarraram ao casco de
um deles, de barriga para cima.

Ficaram ali <strong>oito horas</strong>, até o <em>Empire Star</em> se aproximar.

<strong>Domenico Leo</strong> passou a noite do mesmo jeito, na quilha de outro bote, com
sete ou oito pessoas.""",

"""E agora eu preciso avisar o leitor de uma coisa.

O que vem a seguir são três versões da mesma meia hora, contadas por três pessoas que
estavam naquele navio.

Elas não se completam. Elas se contradizem.

E o que separa uma da outra não é honestidade. É o convés em que cada uma dormia.""",

"""<strong>A família Vacelli viajava na primeira classe.</strong> O casal e três filhos, de
quinze, treze e dez anos. Esperaram a noite inteira na popa e foram recolhidos às nove e
meia.

A versão deles:

<em>Centenas de passageiros da terceira classe foram tomados de tal pânico que se tornaram
animais selvagens, perdendo o juízo. Avançaram desesperadamente como uma massa aterrorizada
sobre os botes, muitos deles portando facas que seguramente, em mais de um caso, foram
usadas contra outros passageiros.</em>

E concluem: aquilo obrigou os passageiros de primeira e segunda classe a permanecerem
paralisados, assistindo à luta terrível que se desenrolava diante deles.""",

"""<strong>Mario Ottaviani, vinte e três anos, viajava na segunda classe</strong>, a
negócios, e sabia nadar.

A versão dele:

<em>Os passageiros da terceira classe e a tripulação foram os responsáveis por transformar a
situação em anarquia. Cometeram atos impróprios de gente civilizada. Empurraram-se para
dentro dos botes e tomaram posse deles pela violência, sem pensar nas mulheres e nas
crianças que clamavam por ajuda.</em>""",

"""<strong>Nicola Lynose, iugoslavo, viajava na terceira classe.</strong>

A versão dele:

Ao primeiro estalo, correram todos ao depósito para pegar os coletes salva-vidas. Quando
voltaram ao convés com os coletes na mão, encontraram <strong>a tripulação em frenesi,
jogando-se dentro dos botes que já se afastavam do navio</strong>.

<em>Só então</em> os imigrantes, cegos de medo, derrubaram três botes no mar e se atiraram
neles de um jeito tão desordenado que os três viraram.""",

"""Eu não vou escolher entre as três.

E preciso dizer por quê, porque a essa altura já ficou claro de que lado eu venho.

<strong>Sou bisneto de duas mulheres que viajavam na terceira classe daquele navio.</strong>
Se eu arbitrasse essa disputa, estaria arbitrando em causa própria, e o leitor teria todo o
direito de descontar o que eu dissesse.

Então não arbitro. Ponho as três lado a lado e deixo à vista o que elas têm em comum: cada
depoente descreve com precisão o que aconteceu perto dele, e com fúria o que aconteceu do
outro lado do navio, onde não estava.

Um homem da primeira classe viu a terceira invadir os botes. Um homem da terceira viu a
tripulação já dentro deles. As duas coisas provavelmente aconteceram, com meia hora de
diferença, em pontos distintos de um convés no escuro.""",

"""Há uma coisa, porém, em que os três lados concordam.

Parte da tripulação ficou.

Os Vacelli, que são os mais duros com a terceira classe, fazem questão de registrar o
comportamento nobre do <strong>primeiro oficial</strong> e do <strong>primeiro
maquinista</strong>, que segundo eles fizeram esforços inauditos para salvar passageiros.

E <strong>Pedro Volpi</strong> deve a vida a um deles. Depois de se jogar na água, foi
ajudado pelo <strong>terceiro maquinista do Mafalda</strong>, que nadou com ele até um bote.

Volpi acrescenta uma linha que vale o capítulo inteiro: o homem que o salvou, depois de
deixá-lo em segurança, voltou. E salvou outros dois.""",

"""E o herói mais citado daquela noite não era da tripulação.

Era um passageiro: <strong>Juan Santororo</strong>, cadete naval argentino.

Galli, que é o mais crítico de todos em relação aos oficiais do Mafalda, faz questão de
contrastar: enquanto a tripulação fazia o que fazia, havia um passageiro salvando gente na
água.

Santororo só descobriu quem era o homem que ele tinha visto trabalhando no escuro quando
chegou ao porto e viu a multidão carregá-lo nos ombros.""",

"""Na água, o perigo deixou de ser o navio.

<strong>Lynose nadou das sete da noite às dez e meia.</strong> E o que ele conta desse
percurso não é sobre ondas.

<em>A luta mais intensa não foi com as ondas, mas com os passageiros boiando que, não
sabendo nadar, se agarravam a quem estivesse ao lado, soltando gritos desesperados. Ouviam-
se pragas em todas as línguas. Para avançar era preciso se afastar dos outros, que formavam
uma barreira humana.</em>

<strong>Batista Beria</strong> descreve o mesmo mecanismo: quem não sabia nadar direito se
agarrava à roupa de quem estava na frente.

Uma pessoa se afogando não é uma pessoa pedindo ajuda. É uma pessoa que puxa para baixo
quem chega perto.""",

"""E os tubarões.

É a parte mais famosa deste naufrágio, a que aparece em toda reportagem, e é a que menos
resiste a um exame.

<strong>Gabassi</strong> diz que uma mulher e uma criança foram levadas por um tubarão
enorme, na tábua em que ele boiava. <strong>Ponce</strong> viu dois. <strong>Galli</strong>
viu vários, e diz que um feriu um companheiro que morreu depois de içado.
<strong>Malone</strong> não viu tubarão nenhum, mas viu um homem boiando com a perna
destruída.

<strong>Volpi</strong> não viu — e acrescenta: <em>a noite estava muito escura</em>.
<strong>Sanfilippo</strong> não viu, e diz outra coisa no lugar: viu o corpo de uma mulher
boiando agarrada a um bebê. <strong>Beria</strong>, <strong>Uccelli</strong> e
<strong>Solk</strong> também não viram.

E <strong>Domenico Leo</strong> resume a dificuldade toda numa frase: <em>não sei se era um
tubarão, mas era um peixe enorme.</em>""",

"""<strong>Pascual Pecci</strong>, o único cético do grupo, foi mais longe.

Duvidou que houvesse tubarão nenhum. Atribuiu a história a peixes que vinham sendo vistos
seguindo o navio nos dias anteriores, e que ninguém a bordo sabia identificar.

Achava, mais amplamente, que muitos dos relatos dramáticos daquela noite eram invenção de
quem quis criar drama onde não havia. Sobre a própria fuga com a mulher e a filha, disse que
tinha sido tão dramática quanto <em>um dia no Tigre</em>, que é um balneário de fim de
semana perto de Buenos Aires.

Nem ele nem os outros têm como provar o que dizem. Estava escuro, e eles estavam com medo.

O que este livro pode fazer é não decidir por eles.""",

"""De todos os botes que aparecem nestes vinte relatos, quase nenhum chegou inteiro do outro
lado.

Afundaram pelo peso, viraram a poucos metros do casco, cederam, arrebentaram nas cordas,
ficaram pendurados no lado errado do navio, ou chegaram furados e foram remados com as mãos.

<strong>O que segurou foi o dos cozinheiros.</strong>""",
]

CAP23 = [
"""Às dez e três da noite, o navio apagou.

Não foi um apagão como o de uma casa. Um transatlântico sem energia perde a luz, perde as
bombas, perde o rádio. Em poucos segundos deixa de ser uma máquina e passa a ser um objeto
grande boiando torto.

A partir daquele minuto, a única luz sobre aquela água veio dos holofotes dos navios que já
tinham chegado.

E holofote ilumina um círculo. O resto continua preto.""",

"""Entre a luz apagar e o navio sumir passaram-se <strong>sete minutos</strong>.""",

"""Pouco antes disso, <strong>Mario Ottaviani</strong> olhou em volta antes de se jogar, e
contou.

Ainda havia nos conveses cerca de <strong>sessenta mulheres e crianças</strong>, e cerca de
<strong>duzentos homens</strong>.

Duzentas e sessenta pessoas, a sete minutos do fim, num navio já deitado.""",

"""<strong>Enrico Nazzeconi</strong> ficou até dez para as dez.

Quando a inclinação a estibordo chegou ao que ele chamou de estado extremo, correu para a
popa. A água já estava pelos joelhos dele, no convés.

Então se jogou.""",

"""E foi da água que ele ouviu.

Três apitos longos, um atrás do outro.

E depois um estrondo que ele não conseguiu descrever de outro jeito senão como estrondo.""",

"""E não viu nada.

Nazzeconi estava a poucas dezenas de metros do casco e diz, com todas as letras, que
<strong>não conseguiu ver o navio afundar</strong>. Estava escuro demais.

A família Vacelli, já a bordo do <em>Empire Star</em>, também não viu. Mal tinham chegado,
olharam para trás, e o Mafalda não estava mais lá.

Um navio de nove mil toneladas desapareceu do Atlântico, e quase ninguém que estava a
duzentos metros dele viu aquilo acontecer.""",

"""O que se sentiu foi a água.

<strong>Andres Scavani del Vicario</strong> tinha se soltado de uma corda pouco antes, junto
com o fotógrafo de bordo, com quem tinha feito amizade durante a viagem. Quando o navio
afundou de vez, o redemoinho da descida arrastou os dois para longe.

Foi o que os salvou. A sucção os empurrou na direção do <em>Formosa</em>, e três horas
depois a tripulação francesa ouviu os gritos deles e os pescou.

O navio, ao afundar, moveu quem estava na água. Alguns para longe da ajuda, outros para
perto dela. Ninguém escolheu.""",

"""E o comandante ficou.

Nisso os vinte depoimentos concordam, e é a única coisa daquela noite sobre a qual eles não
brigam.

Não há um único relato, entre todos os que li, de alguém que tenha visto Simone Gulì tentar
sair daquele navio. Passageiros de primeira, de segunda e de terceira classe; italianos,
árabes e iugoslavos; gente que discorda de tudo o mais, concorda nisso.

Ele estava na ponte quando o navio afundou.""",

"""<strong>Como ele morreu é outra história, e tem duas versões.</strong>

<strong>Salvador Malone</strong>, já içado a bordo do <em>Alhena</em>, diz que assistiu ao
fim de longe e que viu o comandante na ponte, se despedindo com um <em>Viva Italia</em>.

<strong>Eugenio Gabassi</strong>, ainda na água, conta outra coisa: ouviu tiros vindos da
ponte, onde estavam o comandante e o primeiro maquinista, e concluiu que os dois tinham se
matado.""",

"""As duas testemunhas estavam na água, no escuro, a distâncias que nenhuma delas soube
precisar.

Uma interpretou uma silhueta. A outra interpretou um som.

Nenhuma das duas está mentindo, e nenhuma das duas tinha como ter certeza. Aquela noite não
ofereceu certeza a ninguém que estivesse dentro dela.""",

"""Então fica o que dá para dizer.

Simone Gulì levou o <em>Principessa Mafalda</em> de Gênova até quase dezoito graus de
latitude sul. Passou as últimas horas mandando dizer aos passageiros que o navio aguentaria
até o dia seguinte.

Não aguentou. E não há como saber se ele acreditava naquilo, se estava errado nas contas, ou
se estava apenas tentando conter um pânico que veio de qualquer maneira.

O que se sabe é que ele ficou.

<strong>O navio afundou às dez e dez da noite de 25 de outubro de 1927, com o comandante a
bordo.</strong>""",

"""Às dez e onze, aquele ponto do Atlântico era um campo de gente boiando.

Homens agarrados à quilha de botes virados. Mulheres em tábuas. Crianças dentro de coletes
grandes demais para elas. E centenas de pessoas que não sabiam nadar tentando se segurar em
quem sabia.

E, a alguns quilômetros dali, com os holofotes acesos, os navios vindo no escuro.""",
]

CAP24 = [
"""A única coisa boa desta história inteira é que os navios já estavam perto.

Naquela mesma tarde o Mafalda tinha cruzado com o <em>Empire Star</em> e o comandante o
saudara com um apito longo. Quando o eixo partiu, poucas horas depois, o navio inglês estava
a cerca de dois quilômetros.

Não foi previdência de ninguém. Foi rota comercial. Aquele trecho do Atlântico, em outubro
de 1927, tinha tráfego.""",

"""O pedido de socorro alcançou mais navios do que se costuma contar.

Os telegramas daquela noite registram <strong>Alhena</strong>, <strong>Empire Star</strong>,
<strong>Formosa</strong>, <strong>Mosella</strong>, <strong>Avelona</strong>,
<strong>Rosetti</strong>, e ainda <em>Salem</em>, <em>Forthmouth</em>, <em>Frederik</em> e
<em>Piauhy</em>.

Dez nomes. Holandês, inglês, francês, italiano, brasileiro. Nenhum deles tinha qualquer
obrigação com aquela gente além da que existe entre navios.""",

"""E alguém, a bordo do <em>Alhena</em>, teve uma ideia que salvou vidas.

Esticaram <strong>uma corda ao longo do casco</strong>, da popa à proa, à altura da água.

Quem chegasse nadando, chegasse onde chegasse, encontrava corda.

Três sobreviventes que não se conheciam descrevem a mesma corda.
<strong>Nazzeconi</strong> diz que foi ela que o deixou aguentar até alguém puxá-lo.
<strong>Beria</strong> diz que ela permitiu que ele subisse com facilidade.
<strong>Solk</strong> conta que nadou até levar uma pancada forte na nuca, ergueu os braços
por instinto, e havia corda ali.""",

"""Nem todo mundo teve essa sorte.

<strong>Ali Hassen</strong>, quarenta e cinco anos, viajava com três primos. O bote em que
entrou afundou pelo peso. Voltou à superfície, achou um pedaço de madeira e ficou boiando
<strong>quatro horas</strong>.

Nesse tempo ele bateu <strong>várias vezes contra o casco de um dos navios de resgate</strong>
sem que ninguém o notasse.

Já tinha perdido a esperança quando encontrou uma corda, se agarrou, e sentiu que estava
sendo içado.

Os três primos dele morreram.""",

"""Os tempos na água, como os próprios sobreviventes contaram:

Uccelli, uma hora e meia. Beria, duas. Milano, duas. Galli, duas. Scavani, três. Hassen,
quatro.

Lynose nadou das sete da noite às dez e meia.

<strong>Alfio Sanfilippo passou oito horas</strong> agarrado à quilha de um bote virado, com
o irmão e um oficial do navio.

E <strong>Eugenio Gabassi</strong> passou a noite inteira sobre uma tábua, com quatro
mulheres e três crianças, até ser recolhido pelo <em>Rosetti</em> na manhã seguinte.""",

"""<strong>Domingo Milano tinha catorze anos e viajava sozinho.</strong>

O pai e os irmãos estavam na Argentina esperando por ele.

Era bom nadador. Quando viu que o navio ia mesmo afundar, mergulhou da proa e começou a
nadar na direção do <em>Alhena</em>, que estava longe.

Ficou duas horas na água. Estava a ponto de desistir quando passou perto um bote carregado
de náufragos. Num último esforço, agarrou um remo.

Foi assim que ele chegou.""",

"""Agora a parte que eu não consigo resolver, e que precisa ser dita.

<strong>A conta do resgate não fecha em nenhuma fonte.</strong>

Uma delas soma os salvos assim: Alhena 450, Avelona 300, Empire Star 202, Formosa 151,
Rosetti 122, Mosella 49. Total: mil duzentos e setenta e quatro pessoas resgatadas.

Só que a bordo iam mil duzentas e cinquenta e nove. Somando os trezentos e catorze mortos,
dá <strong>mil quinhentas e oitenta e oito pessoas</strong> num navio que levava mil
duzentas e cinquenta e nove.

Outra fonte, com números diferentes, comete o mesmo excesso. E lista dois navios,
<em>Athenas</em> e <em>Alhena</em>, com exatamente o mesmo número de salvos — quase
certamente o mesmo navio, contado duas vezes.""",

"""Isso não é desleixo de quem contou.

<strong>É o que a noite era.</strong>

Um homem entrava num bote, o bote virava, ele nadava até outro bote, esse bote encostava num
navio, e horas depois aquele navio transferia parte dos recolhidos para outro. Cada vez que
alguém trocava de casco, havia a chance de ser contado outra vez.

A soma que não fecha é a única prova aritmética que existe do que aconteceu com aquelas
pessoas depois que o Mafalda sumiu: <strong>elas foram passadas de mão em mão, no escuro,
por gente que não sabia quem já tinha contado quem.</strong>""",

"""E é exatamente aqui que a minha família reaparece.

O que a memória guarda é isto: o cozinheiro tirou as duas irmãs e as cinco crianças do
porão e as levou para o <strong>bote dos cozinheiros</strong>.

Desse bote, foram levadas para outro navio. E esse navio, no relato que chegou até mim,
<strong>não era um navio de passageiros. Era um navio que carregava carvão.</strong>""",

"""Não sei qual era.

O documento que existe põe as sete no <em>Alhena</em>, holandês, três dias depois. Entre o
bote e o Alhena pode ter havido um navio, ou dois, e a memória da família guardou o que a
pele guardou.

Porque o que ficou dessa passagem, e ficou por cem anos, foi o carvão.

<strong>Elas chegaram pretas.</strong> As duas mulheres e as cinco crianças, cobertas de pó
de carvão da cabeça aos pés.""",

"""Em <strong>28 de outubro de 1927</strong>, o vapor holandês <em>Alhena</em> entrou no
porto do Rio de Janeiro.

O intérprete Thomas Filipovich subiu a bordo e recebeu uma lista. Na coluna de procedência,
onde deveria estar o nome de um porto, o funcionário escreveu uma palavra só:
<strong>Náufragos</strong>.

Cinquenta imigrantes, todos de terceira classe, todos desembarcados na
<strong>Ilha das Flores</strong>. Quarenta e três italianos, quatro iugoslavos, três
húngaros.

Nas linhas 26 e 27, e depois nas linhas 44 a 48, estão as sete pessoas deste livro.""",

"""<strong>Maria Spinelli</strong> desceu naquele mesmo desembarque.

É a mulher que recebeu no colo, por cima da amurada, o filho de três anos da amiga Teresa
Forggia, quando parecia que a mãe ia ficar no navio. Terceira classe, italiana, salva pelo
<em>Alhena</em>.

Ela já tinha atravessado o Atlântico três vezes antes daquela. Não era uma emigrante. Era
uma viajante.

E fecha o depoimento assim: <em>depois de três viagens à América do Sul, resolvi ficar aqui
para sempre e nunca mais voltar à Itália</em>.

O naufrágio não a impediu de chegar. Impediu-a de voltar.""",

"""E naquela folha estão as duas mulheres do capítulo 9.

<strong>Luchini Teresa, dezenove anos. De Rosi Emilia, cinquenta e cinco.</strong> Números 24
e 25, uma seguida da outra, cada uma com um <em>x</em> marcado à margem.

Subiram a prancha em Gênova ao lado dos maridos. Desceram aqui sem eles.""",

"""Aquela folha de papel é o momento em que esta família volta a existir para o mundo.

Entre o estrondo das cinco e quinze do dia 25 e a assinatura do intérprete no dia 28, não há
uma linha sequer sobre elas em documento nenhum. Três dias inteiros de nada.

E então, de repente, sete nomes, sete idades, uma profissão, uma coluna de instrução e um
destino.

<strong>Forner Rosa, vinte e quatro anos, chefe. Enrico, um ano, filho.</strong>

Vivos.""",
]

CAP25 = [
"""Eu não tenho os nomes deles.

Tenho vinte depoimentos de sobreviventes, com nome, idade, classe, cidade de origem e a
profissão de alguns. Tenho cinquenta nomes datilografados na lista do <em>Alhena</em>, com
idade e grau de parentesco. Tenho uma família inteira reconstruída em cartório, geração por
geração, até 1861.

<strong>Dos trezentos e catorze, não tenho lista nenhuma.</strong>""",

"""O próprio número não é pacífico. Há fonte que fala em duzentos e setenta e dois.
Trezentos e catorze é o que o cruzamento sustenta, e é o que este livro usa.

A bordo iam mil duzentas e cinquenta e nove pessoas.

<strong>Um em cada quatro não chegou.</strong>""",

"""E o que se sabe sobre como aquelas pessoas morreram não vem de laudo, de perícia nem de
inquérito.

<strong>Vem de olho de sobrevivente.</strong>

Não houve autópsia, não houve corpo, não houve investigação no local. O que existe é o que
gente apavorada, no escuro, dentro da água, disse ter visto — e disse dias depois, num porto,
para jornalistas.""",

"""Então é isto o que ficou.

<strong>Valeriano Galli</strong> tinha um companheiro ao lado. O homem foi ferido na água e
morreu depois de içado, já em segurança.

<strong>Salvador Malone</strong> viu um homem boiando com uma perna destruída.

<strong>Alfio Sanfilippo</strong>, agarrado à quilha havia horas, viu passar o corpo de uma
mulher boiando com um bebê nos braços.

<strong>Eugenio Gabassi</strong> passou a noite numa tábua com quatro mulheres e três
crianças. Quando amanheceu e o <em>Rosetti</em> o recolheu, uma das mulheres e uma das
crianças não estavam mais ali.""",

"""<strong>Ali Hassen</strong> tinha quarenta e cinco anos e embarcou em Gênova com três
primos.

Chegou ao Rio de Janeiro sozinho.

Não sei o nome de nenhum dos três. Não sei a idade, não sei de onde vieram, não sei para onde
iam. Sei que eram três, que eram primos dele, e que morreram os três — porque ele contou, e
porque quem conta uma coisa dessas não erra a conta.""",

"""Há um número que não é a lista dos mortos, mas chega perto.

Sete minutos antes do fim, <strong>Mario Ottaviani</strong> olhou o convés antes de se jogar
e contou cerca de sessenta mulheres e crianças e cerca de duzentos homens.

Duzentas e sessenta pessoas.

Não é a lista dos que morreram: parte daquela gente se atirou depois dele e foi recolhida.
Mas é <strong>a última vez que alguém, naquele navio, parou para contar quem ainda estava
vivo</strong>.""",

"""Dois dos trezentos e catorze estão num documento que está em cima da minha mesa. E estão
nele como ausência.

Na lista do <em>Alhena</em>, os números 24 e 25 são <strong>Luchini Teresa, dezenove
anos</strong>, e <strong>De Rosi Emilia, cinquenta e cinco</strong>. Aparecem sozinhas, uma
seguida da outra, sem parentesco declarado, cada uma com um <em>x</em> marcado à margem.

E no pé da folha, escrito à mão:

<em>As passageiras constantes sob Nº 24 e 25 perderam seus maridos, e pedem de ser enviadas
para Italia.</em>

Os dois homens não têm nome em documento nenhum que eu tenha encontrado. Existem ali como
aquilo que faltou ao lado do nome de duas mulheres.""",

"""E a última coisa daquela folha é o que elas pedem.

Dezessete dias antes tinham subido a prancha em Gênova ao lado dos maridos, indo embora para
sempre. Atravessaram o Atlântico inteiro. Chegaram.

<strong>E o que pedem, na primeira repartição brasileira em que puderam falar, é para
voltar.</strong>""",

"""Não houve recolhimento de corpos.

Os navios que chegaram naquela noite estavam apanhando gente viva no escuro, e foram embora
ao amanhecer, cada um para o porto que já era o seu destino. Ninguém voltou àquele ponto do
mar.

Quem morreu ali ficou ali. <strong>Não existe sepultura de nenhum dos trezentos e catorze, em
lugar nenhum, com nome nenhum.</strong>""",

"""E aqui eu preciso admitir uma coisa sobre este livro.

Ele é feito de depoimento. E depoimento é coisa de vivo.

Este livro chegou até aqui, e quase todos os capítulos são sobre gente que chegou. Não porque
quem chegou importe mais. Porque foram eles que puderam falar.

As duas mulheres desta família estão neste livro pelo mesmo motivo pelo qual quase todo mundo
está: <strong>não morreram</strong>.""",

"""E a minha família fica devendo.

Rosa e Maria Luigia estiveram na água daquela noite com cinco crianças. Estiveram num bote.
Foram passadas de navio em navio, no escuro. É quase impossível que não tenham visto alguém
morrer.

Nada disso atravessou.

O que chegou até mim, por três gerações e pela boca, foi o cozinheiro, o porão, o carvão, e um
pai procurando as filhas entre gente preta de fuligem.

<strong>Sobre os mortos, silêncio.</strong>""",

"""Eu acho que sei por quê, e é a coisa menos documentada que eu vou escrever neste livro.

Uma família que atravessou uma noite dessas conta a parte que salva. Conta o cozinheiro.
Conta o carvão. Conta o reencontro.

A outra parte ela não conta, e não conta porque contar seria entregar aos filhos e aos netos
alguma coisa que ela mesma não conseguiu carregar direito.

Dez anos depois daquela noite, Rosa teve uma filha e botou nela <strong>o nome do
navio</strong>.

Isso não é esquecimento. Quem esquece não faz uma coisa dessas.""",

"""E eu cheguei aos quarenta e poucos anos sabendo apenas que tinha havido um navio.

Não aprendi na escola. Não vi em livro didático, não passei por nenhuma placa. Nenhum 25 de
outubro da minha vida foi aniversário de coisa alguma.

Um transatlântico afundou diante da costa da Bahia levando mil duzentas e cinquenta e nove
pessoas, e a maior parte delas estava vindo para cá. Para ser brasileira. Muitas já tinham
parente esperando numa estação do interior de São Paulo.

<strong>Foi memória de família, não memória de país.</strong>

É por causa dessa diferença que este livro existe.""",
]

CAP26 = [
"""Entre a Ilha das Flores e a Hospedaria do Brás existem três dias que ninguém registrou.

O intérprete Thomas Filipovich assinou a parte dele no Rio de Janeiro em 28 de outubro. A
entrada na Hospedaria do Brás, em São Paulo, é de 31.

O que aconteceu no meio, eu não sei. Não sei se foram de trem ou de navio costeiro, não sei
onde dormiram, não sei o que comeram, não sei quem pagou.""",

"""O que dá para dizer é o que elas não tinham.

Tudo o que aquelas duas famílias carregavam da Itália estava dentro do <em>Principessa
Mafalda</em>, e o <em>Principessa Mafalda</em> estava no fundo do Atlântico.

A roupa de cama, as ferramentas, as fotografias, os documentos, a roupa de domingo, o dinheiro
que tivesse sobrado da passagem. Uma família que emigra leva o que consegue, e o que consegue
é tudo o que tem.

Chegaram com o corpo e com as crianças.""",

"""Em <strong>31 de outubro de 1927</strong>, seis dias depois do naufrágio, alguém abriu o
Livro 100 da Hospedaria de Imigrantes do Brás na página 290 e começou a escrever.

Aquele livro era o funil por onde passava a imigração de São Paulo. Nome, idade, residência,
número de família, destino. Milhares de páginas iguais, uma atrás da outra, por décadas.""",

"""E há uma coluna naquela página que eu não consigo passar sem olhar duas vezes.

A coluna do vapor.

Ela diz <strong>P. Mafalda</strong>.

O navio estava no fundo do mar havia seis dias. Trezentas e catorze pessoas tinham morrido
dentro dele. E o formulário pedia o nome do vapor de procedência, então o funcionário escreveu
o nome do vapor de procedência.

Não é frieza. É o procedimento fazendo a única coisa que sabe fazer. Mas o efeito, lido cem
anos depois, é que aquela página registra sete pessoas chegando a São Paulo num navio que já
não existia.""",

"""Família número 19270:

<strong>FORNER ROSA, 24 anos, Castelcucco.</strong><br>
<strong>ENRICO, 1 ano.</strong>

Família número 19260:

<strong>FORNER MARIA, 31 anos, Cavaso del Tomba.</strong><br>
Gina, 7. Pulcheria, 6. Rino, 4. Danilo, 2.""",

"""Maria Luigia entra ali como <strong>Forner</strong>.

Ela era casada com Angelo Dei Agnoli desde 25 de fevereiro de 1917. Dez anos e quatro filhos.

Não é erro do escrivão. No registro civil italiano a mulher não troca de sobrenome ao casar:
continua sendo quem nasceu, em todos os papéis, a vida inteira.

As duas se apresentaram como as duas irmãs Forner que eram, e o funcionário escreveu o que
ouviu.""",

"""E as duas entram como <strong>CHEFE</strong>.

Não é leitura minha. Está escrito na coluna de parentesco da lista do <em>Alhena</em>, no Rio,
em 28 de outubro. E o registro do Brás, três dias depois, em outra cidade e em outro órgão,
faz o mesmo.

Duas mulheres casadas, com os maridos vivos e esperando no interior de São Paulo, registradas
como chefes das próprias famílias em dois documentos independentes do Estado brasileiro.""",

"""Chefe, ali, não é uma opinião sobre o casamento delas.

É uma função. Chefe é quem responde pelo grupo diante da autoridade: quem dá o nome, a idade
e o destino de todo mundo, quem assina o que houver para assinar, quem é chamada se faltar
alguém.

Rosa Forner tinha vinte e quatro anos, um filho de um ano no colo, nenhum documento, nenhuma
bagagem e nenhuma palavra de português.

E foi ela quem respondeu.""",

"""A lista do <em>Alhena</em> traz uma coluna a mais que a do Brás, e é a que mais me
interessa.

<strong>Instrução: sim.</strong>

Rosa Forner sabia ler.

No primeiro capítulo deste livro eu escrevi que muitas crianças daquele lugar aprendiam o
calendário agrícola e não aprendiam a ler. Ela aprendeu as duas coisas.

Profissão: doméstica. Destino declarado: S. Paulo.""",

"""A mesma página do Brás traz outros sobrenomes: De Rossi, Strufaldi, Lovato, Panarotto,
Puldeghinio, Beck.

São os mesmos que estão na lista do <em>Alhena</em>, três dias antes, no Rio.

É a mesma leva de gente, documentada duas vezes, em duas cidades, por dois órgãos que não
conversavam entre si.

Cinquenta pessoas desembarcaram na Ilha das Flores. <strong>Quarenta e duas deram entrada no
Brás em 31 de outubro, e mais uma no dia seguinte.</strong>

Sete ficaram no Rio. Quem foram, eu não sei.""",

"""Há uma coisa nessa sobreposição que eu queria saber e não sei.

Na lista do <em>Alhena</em>, a passageira número 25 é <strong>De Rosi Emilia</strong>,
cinquenta e cinco anos, que perdeu o marido no naufrágio e pediu para ser mandada de volta à
Itália.

Na página do Brás há um <strong>De Rossi</strong>.

Na digitalização que eu tenho, não consigo dizer se é ela. Se for, quer dizer que o pedido não
foi atendido, ou que ela desistiu dele, e que a mulher que queria voltar pegou o mesmo trem
que todo mundo.""",

"""E é aqui que esta história faz uma curva que eu não esperava quando comecei.

Em 25 de outubro, aquelas sete pessoas foram notícia no mundo inteiro. O naufrágio do
<em>Principessa Mafalda</em> saiu em jornal de Buenos Aires, de Roma, de Londres e de Nova
York. Sobrevivente de terceira classe deu entrevista no cais.

Em 31 de outubro, seis dias depois, elas viraram <strong>família 19270 e família
19260</strong>.""",

"""E era exatamente isso que elas tinham vindo fazer.

Ninguém atravessa o Atlântico na terceira classe para virar notícia. Atravessa para virar
número de família num livro de hospedaria, para pegar um trem para o interior e para começar a
trabalhar numa terra que não é sua.

O naufrágio foi um acidente no meio de uma coisa muito mais comum.

<strong>A página 290 é o momento em que a viagem volta a ser o que sempre foi.</strong>""",
]

CAP27 = [
"""Este é o único capítulo deste livro em que o arquivo não tem nada e a memória tem tudo.

Todos os documentos que eu juntei até aqui registram <em>que</em> aquelas sete pessoas
sobreviveram. As listas, os manifestos, as folhas de desembarque. Nenhum deles registra
<em>como</em>, e nenhum deles registra o que aconteceu quando elas desceram.

O que vem agora não tem papel nenhum. Tem cadeia oral, e eu vou dizer qual é antes de
contar.""",

"""<strong>Pulcheria Pasqua Dei Agnoli</strong>, filha de Maria Luigia, tinha seis anos na
noite do naufrágio. Nasceu em 1921 e morreu em 2013, aos noventa e dois anos.

Ela casou com <strong>João Betti</strong>, nascido em 1920, que não estava naquele navio.

E foi <em>ele</em>, não ela, quem passou a vida contando esta história dentro de casa.

A neta dos dois, <strong>Patrícia Betti</strong>, é categórica: <em>quem me contou todas as
histórias foi meu avô, que era o marido da Pulcheria. Eu só sei da fonte dele.</em>""",

"""Vale parar um segundo nisso, porque é estranho e é importante.

A mulher que viu aquele navio afundar aos seis anos de idade viveu até 2013, e não é ela a
narradora desta história na própria casa.

Quem narrava era o marido. Um homem que ouviu de outra pessoa e recontou por décadas — dela, e
talvez também da sogra, Maria Luigia, que morreu em 1992, aos noventa e seis anos.

<strong>Entre a menina que viu e eu, que escrevo, há um homem que não estava lá.</strong>""",

"""Os dois homens estavam esperando.

<strong>Angelo Dei Agnoli</strong>, marido de Maria Luigia, tinha desembarcado em Santos em
30 de abril de 1927. Seis meses antes.

Ele veio no <em>Principessa Mafalda</em>.

O mesmo navio, o mesmo casco, provavelmente o mesmo porão. Trouxe o marido em segurança em
abril e quase matou a mulher e os quatro filhos em outubro.""",

"""<strong>Fausto Miotto</strong> também já estava aqui.

Veio antes de Rosa, e é por isso que ela atravessou como chefe da própria família, com um
filho de um ano, e não ao lado do marido.

Em que mês e em que navio, eu ainda não sei. É uma das coisas que continuo procurando.""",

"""E os dois foram esperar.

<strong>Foi em São Paulo.</strong>

Não no cais do Rio, quando o <em>Alhena</em> atracou em 28 de outubro. Três dias depois, na
Hospedaria de Imigrantes do Brás.

Quem localiza a cena é a Patrícia, repetindo o avô: <em>quando o meu avô contou que o meu
bisavô foi encontrar a família lá em São Paulo, ele não reconheceu… na frente da hospedaria
ali…</em>

Bate com o papel. A entrada no Livro 100 é de 31 de outubro.""",

"""E o que desceu foram duas mulheres e cinco crianças <strong>cobertas de pó de carvão da
cabeça aos pés</strong>.

O navio que as recolheu, depois do bote dos cozinheiros, carregava carvão. Elas passaram
horas, ou dias, dentro dele.

Não havia como se lavar. Não havia roupa para trocar, porque a roupa tinha afundado junto com
todo o resto.""",

"""<strong>Angelo e Fausto passaram os olhos por elas e não as reconheceram.</strong>

Essa é a frase que atravessou cem anos, e ela vem inteira na voz da Patrícia repetindo o
avô: <em>ele não reconheceu porque disse que ela estava toda suja de carvão. Então, tem uma
história, sim.</em>

Não é que estivessem distraídos. Estavam procurando a cara da mulher deles no meio de uma
multidão, e a cara da mulher deles estava preta.""",

"""<strong>Quem achou foi uma das meninas.</strong>

Uma criança pequena viu o pai no meio daquela gente toda, e foi ela quem resolveu.

Não sei qual. Gina tinha sete anos, Pulcheria tinha seis. O relato diz apenas <em>uma das
filhas pequenas dele</em>, e as duas cabem na frase.

E este pedaço vem do outro galho. Na versão do João Betti, o carvão está lá e o
não-reconhecimento está lá; a menina que resolve, não.

<strong>Uma linha desta família guardou como a cena começou. A outra guardou como ela
terminou.</strong>""",

"""Vale parar um segundo no que isso significa.

Durante seis dias, homens adultos com autoridade e formulário contaram aquela gente.
Contaram nos botes, contaram nos navios de resgate, contaram no telegrama, contaram no Rio,
contaram no Brás.

<strong>A conta não fechou em fonte nenhuma.</strong> Sobrou gente em toda soma que alguém
tentou fazer daquela noite.

E o reencontro que importava foi resolvido por uma menina de seis ou sete anos que reconheceu
um rosto.""",

"""O relato não diz uma palavra sobre Rosa e Fausto.

É uma história contada do lado Dei Agnoli, por quem estava com os Dei Agnoli. Pulcheria era
filha de Maria Luigia, e o pai que ela viu era o pai dela.

O que se passou entre Rosa e Fausto quando finalmente se acharam, ninguém contou a ninguém que
contasse a mim.

Eu poderia escrever. Seria fácil, seria bonito, e seria mentira. <strong>Fica em
branco.</strong>""",

"""Fica também o que a família escolheu guardar.

Aquela noite tinha o estrondo, o convés inclinado, o navio apagando, os gritos na água, os
mortos. Nada disso passou.

O que atravessou os dois galhos desta família, três gerações e cem anos de Brasil foi
<strong>o carvão</strong>.

A sujeira. A imagem física de duas mulheres e cinco crianças pretas de fuligem, de pé diante de
uma hospedaria de imigrantes, sem serem reconhecidas.""",

"""Talvez seja porque o carvão é a única parte da história que termina bem.

Quem conta o carvão tem que contar que uma menina achou o pai. A cena vem inteira, e a cena
inteira é o reencontro.

Contar o resto seria ter que contar a água.

<strong>Elas escolheram contar a parte em que a família se acha.</strong>""",
]

CAP28 = [
"""O destino era Grama.

Hoje se chama São Sebastião da Grama. É um município pequeno no nordeste do estado de São
Paulo, na região que se chamava Mogiana, e naquela época pertencia à comarca de São José do
Rio Pardo.

Eu sei disso por dois papéis: um carimbo da <strong>Delegacia de Polícia de Grama</strong> no
registro de estrangeiro de Angelo Dei Agnoli, e um assento de casamento, o número 660 do
cartório de Grama, lavrado vinte anos depois.""",

"""É terra de café.

O solo daquela região é vermelho, quase alaranjado quando seco e quase roxo quando molhado.
Vem de basalto decomposto, é fundo, é fértil, e foi ele que fez a riqueza do café paulista.

Chamam de <em>terra roxa</em>. Conta-se que o nome veio dos próprios italianos, que diziam
<em>rossa</em>, e que o ouvido brasileiro transformou em roxa. Não sei se é verdade. É o tipo
de história que um lugar conta de si mesmo, e eu registro como tal.""",

"""Na folha do <em>Alhena</em> há uma palavra que aparece duas vezes.

<strong>Espontâneos.</strong>

Está na parte do intérprete — <em>entregou 1 lista com 50 immigrantes sendo todos em terceira
classe, espontaneos</em> — e está outra vez no resumo do desembarque.

É a palavra mais importante daquele documento para entender o que aconteceu com esta família
depois.""",

"""Para dizer o que ela significa, eu preciso mostrar o que aquelas sete pessoas
<em>não</em> foram.

Quatro anos antes, o mesmo navio fez a mesma rota com outro tipo de gente a bordo. Está
anexado à lista de fevereiro de 1923, num formulário diferente de todos os outros:

<em>RELAÇÃO dos immigrantes ITALIANOS AGRICOLTORES embarcados no Porto de GENOVA c/ o Vap.
"PRINCIPESSA MAFALDA"… em virtude do Decreto N. 2400 de 13 de julho de 1918, por conta da
Companhia Commercial de SÃO PAULO.</em>""",

"""Sessenta e sete pessoas, dez famílias. E aquele formulário tem uma coluna que a lista
comum não tem.

<strong>Patrão.</strong>

Preenchida antes do embarque, com o destino já resolvido: Chavantes. Barreiro. Fazenda
Guatapará. S. Simão. E o mesmo nome repetido linha após linha, <em>Dr. Ralpho P. Silva</em>.

Aquelas pessoas atravessaram o Atlântico com o nome do dono do trabalho delas já escrito no
papel, antes de terem pisado no Brasil.""",

"""E iam na terceira classe, no mesmo porão, ao lado de quem tinha comprado a passagem.

Do lado de fora não havia diferença nenhuma. A mesma comida, o mesmo beliche, a mesma água,
o mesmo cheiro.

A diferença estava no formulário.

<strong>E Rosa não estava nesse formulário.</strong>""",

"""Ela não foi recrutada. Não teve passagem paga pelo Estado de São Paulo, não tinha patrão
declarado, não seguiu para fazenda nenhuma.

Ela veio encontrar o marido.

<strong>Reunião familiar, não colonização.</strong> É uma distinção que parece burocrática e
que decide uma vida inteira.""",

"""Quem vinha pelo sistema de colonato chegava devendo.

Devia a passagem, ou o adiantamento, ou as duas coisas. Cuidava de um número contratado de
pés de café, comprava no armazém da própria fazenda, e levava anos para saber se a conta
andava para a frente ou para trás.

Quem vinha por conta própria chegava sem nada. Sem casa, sem ferramenta, sem adiantamento,
sem promessa.

<strong>Mas chegava sem dono.</strong>""",

"""Fausto Miotto era agricultor na Itália e foi agricultor aqui.

Não por escolha. Um homem de vinte e três anos, sem uma palavra de português, sem terra, sem
instrução formal e sem ofício urbano faz no Brasil a única coisa que sabe fazer.

A diferença é que na Itália ele trabalhava numa encosta pequena, de onde uma família tirava
polenta, e aqui foi trabalhar numa terra vasta, fértil e de outra pessoa.""",

"""Angelo Dei Agnoli já estava em Grama havia seis meses quando as duas irmãs chegaram.

Tinha onde dormir e tinha trabalho. É por isso que o destino declarado das duas famílias, no
Rio e depois em São Paulo, era o mesmo lugar.

A cadeia é simples e é a de sempre: um homem vem primeiro, se estabelece e chama. Angelo
chamou Maria Luigia e os quatro filhos. Fausto chamou Rosa e o Enrico.

As duas irmãs vieram no mesmo navio porque foram chamadas para o mesmo lugar.""",

"""<strong>Em 10 de novembro de 1928, em Grama, nasceu Erminda Miotto.</strong>

Treze meses depois do naufrágio.

A primeira brasileira desta família.""",

"""Vale parar nessa conta.

Em pouco mais de um ano, aquelas pessoas caíram no Atlântico, perderam tudo o que traziam,
foram recolhidas por navios estrangeiros, desembarcaram no Rio, atravessaram para São Paulo,
deram entrada numa hospedaria de imigrantes, pegaram um trem para o interior, arrumaram
trabalho, montaram uma casa e tiveram um filho.

Não houve luto público. Não houve indenização. Não houve pausa.

Ninguém deu a eles um ano para se recuperar, e eu desconfio que nem lhes tenha ocorrido
pedir.""",

"""Depois de Erminda vieram Nair, Maria Therezinha, Izaira, Fermino, Mafalda, Rosalia, Luiz,
Dionísio, e mais uma.

<strong>Onze filhos ao todo</strong>, contando o Enrico. Dez nascidos no Brasil.

Nem todos chegaram à idade adulta. Rosalia nasceu em 1940 e morreu em 1941, e naquele lugar e
naquela época isso não era exceção.""",

"""A Parte I deste livro se chama <em>A terra que não bastava</em>.

Rosa e Fausto atravessaram um oceano, sobreviveram a um naufrágio e foram parar numa terra
que bastava e que não era deles.

<strong>Chegaram pretas de carvão e foram trabalhar em terra vermelha.</strong>""",
]

CAP29 = [
"""Enrico Miotto nasceu em 10 de outubro de 1926, na Itália.

Morreu em 6 de outubro de 1998, no Conjunto Hospitalar de Sorocaba.

Entre uma data e a outra há setenta e um anos e cinco documentos. Este capítulo é feito com
eles, e não vai ter aqui nada que eles não digam.""",

"""Ele tinha um ano e quinze dias quando o navio afundou.

Estava no colo da mãe, na terceira classe, no porão. Não escolheu nada, não entendeu nada e
não se lembrou de nada.

É o passageiro deste livro que menos participou da própria história.""",

"""Em 31 de outubro de 1927 ele entrou na Hospedaria do Brás como segunda linha da família
19270.

<strong>ENRICO, 1 ano.</strong>

Sem sobrenome. Nas listas de imigração o sobrenome se escreve uma vez, na linha do chefe, e
vale para todos os que vêm embaixo.""",

"""Depois disso ele some dos meus papéis por vinte e dois anos.

Cresceu em Grama, entre os irmãos que foram nascendo. Não achei registro escolar, não achei
certidão de nada, não achei fotografia com data.

O que aconteceu com ele entre 1927 e 1949, eu não sei.""",

"""E aí ele reaparece, numa repartição de São Paulo, em 29 de dezembro de 1949.

<strong>Registro de Estrangeiros.</strong>

Vinte e três anos. Solteiro. Profissão: <strong>pedreiro</strong>. Endereço: Parque São
Jorge, sem número, Penha, São Paulo, capital. RG 1.335.902, carteira 308.460.

Nacionalidade: <strong>italiana</strong>.""",

"""Vinte e dois anos depois de chegar, ele ainda era italiano.

Se chegou a se naturalizar em algum momento, eu não achei o papel.""",

"""E aquele documento prova uma coisa que nenhum outro prova sozinho.

Criança nascida no Brasil não precisa de registro de estrangeiro.

Se Enrico teve que tirar um, aos vinte e três anos, é porque sabia que tinha nascido do outro
lado. E alguém contou isso a ele.

<strong>Enrico sabia que tinha estado naquele navio.</strong> Rosa contou a mesma história aos
dois filhos: a ele, o primeiro, e à Mafalda, que nasceria dez anos depois com o nome do
navio.""",

"""E ele saiu da terra.

O pai era agricultor. Os irmãos ficaram no interior. Enrico foi para a capital e virou
pedreiro, na Penha, do outro lado da cidade.

Era pedreiro em São Paulo na década de 1950, que é quando São Paulo cresceu mais depressa.""",

"""Solteiro em 1949, aos vinte e três.

Solteiro em 1998, aos setenta e um.

Nunca se casou e não teve filhos. Os dois documentos que eu tenho, separados por quase
cinquenta anos, dizem a mesma coisa nessa linha.""",

"""Morreu de câncer.

A certidão registra insuficiência respiratória como causa direta, e desnutrição. Declaração de
Óbito nº 5501831.

Setenta e um anos, aposentado, morador da Rua Cervantes, 607, Vila Assis, Sorocaba.""",

"""Foi em 6 de outubro.

Ele faria setenta e dois no dia 10.""",

"""Enrico Miotto atravessou o Atlântico antes de aprender a andar.

Sobreviveu a um naufrágio antes de aprender a falar.

Não se lembrava de nada daquilo, e sabia de tudo aquilo, porque a mãe contou.

<strong>Foi o primeiro dos onze filhos de Rosa. Foi o único que esteve no navio.</strong>""",
]

CAP30 = [
"""Em 2 de janeiro de 1937, Rosa Forner teve o sétimo filho. Uma menina.

E botou nela o nome do navio.""",

"""Essa é a frase que fez este livro existir.

Eu a ouvi pela primeira vez sem entender direito o que ela queria dizer, e depois passei a não
conseguir pensar em outra coisa. Uma mulher que quase morreu num naufrágio com um bebê de um
ano no colo dá a uma filha, dez anos depois, o nome do navio que afundou.

É uma frase perfeita.

E é exatamente por isso que ela precisa apanhar um pouco antes de eu deixar que fique de
pé.""",

"""A primeira objeção é a mais óbvia, e é a mais forte.

<strong>Mafalda não era um nome esquisito na Itália.</strong>

Mafalda di Savoia nasceu em 1902, filha de Vittorio Emanuele III, rei da Itália. Era princesa
de sangue, casou com um príncipe alemão em 1925, saía em jornal e em revista, e em 1937 estava
viva e tinha trinta e quatro anos.

O navio não deu o nome a ela. <strong>Ela deu o nome ao navio.</strong> Quando o casco foi
batizado, em 1908, escolheram o nome da filha do rei.""",

"""Então uma italiana batizando uma filha de Mafalda em 1937 pode simplesmente estar fazendo o
que muitas italianas da geração dela fizeram.

Pode ser nome da moda. Pode ser devoção monárquica. Pode ser porque achava bonito.

Se for isso, este livro perde a pergunta que o organiza. E eu prefiro admitir a possibilidade
agora a deixar que um leitor a admita por mim no meio do capítulo.""",

"""A segunda objeção é de tempo.

Em janeiro de 1937 o naufrágio tinha <strong>dez anos</strong>.

Não era ferida aberta. Era coisa de uma década antes, em outro oceano, numa vida que já tinha
virado completamente outra. Rosa tinha trinta e três anos, seis filhos vivos, uma casa no
interior de São Paulo e uma língua nova mais ou menos na boca.

Quem passa por uma coisa dessas costuma querer distância. Botar o nome do navio numa filha é o
contrário de distância.""",

"""E há uma terceira objeção, que ninguém levanta e que eu levanto porque seria desonesto não
levantar.

<strong>Eu quero que a história seja verdadeira.</strong>

Sou bisneto de Rosa. Cresci ouvindo isso. De todos os capítulos deste livro, este é o que eu
mais queria escrever.

Um autor nessa posição é a pessoa menos confiável do mundo para julgar a própria tese.""",

"""Então eu fui procurar alguma coisa que não dependesse de mim.

Achei numa lista de nomes.""",

"""Rosa e Fausto tiveram onze filhos.

<strong>Enrico</strong>, nascido na Itália em 1926. <strong>Erminda</strong>, 1928.
<strong>Nair</strong>, 1931. <strong>Maria Therezinha</strong>, 1932.
<strong>Izaira</strong>, 1932. <strong>Fermino</strong>, 1934.
<strong>MAFALDA</strong>, 1937. <strong>Rosalia</strong>, 1940. <strong>Luiz</strong>, 1942.
<strong>Dionísio</strong>, 1949. E mais uma.""",

"""Leia a série de novo e olhe o que ela faz.

O primeiro filho nasceu na Itália e tem nome italiano. Depois dele, a casa começa a batizar em
português: Nair, Izaira, Luiz, Maria Therezinha. São nomes brasileiros de menino e de menina
dos anos 1930, e não são nomes que se dão em Castelcucco.

Aquela família estava fazendo o que toda família de imigrante faz a partir da segunda leva de
filhos: virando daqui.""",

"""E aí, no sétimo, <strong>Mafalda</strong>.

Não Maria, não Ana, não Teresa. Não um nome italiano corriqueiro. Um nome da Casa de Savoia,
no meio de uma sequência de nomes brasileiros, numa casa de agricultor no interior paulista,
dez anos depois de a mãe ter sido tirada da água de um navio que se chamava assim.

<strong>Não é prova. É um padrão com um furo, e o furo tem nome.</strong>""",

"""E não é um furo qualquer. É o único.

De onze filhos, dez foram batizados dentro de uma lógica: o primeiro italiano porque nasceu
lá, os outros brasileiros porque nasceram aqui.

Uma só escapa da regra. E a que escapa carrega exatamente as sete letras que estavam pintadas
na proa.""",

"""Falta dizer onde ela nasceu, e aí aparece uma coincidência que eu não esperava.

A certidão de casamento de Mafalda, de 1954, reemitida em 1981 na cidade de Nova Fátima, diz
que ela nasceu em <strong>São José do Rio Pardo</strong>.

Só que a família morava em <strong>Grama</strong>. E Grama, naquela época, era município da
comarca de São José do Rio Pardo.

O escrivão quase certamente escreveu a jurisdição no lugar do lugar.""",

"""E isso já tinha acontecido antes, do outro lado do oceano, com a mãe dela.

Em 1926, o oficial de Castelcucco fez a mesma coisa com a naturalidade de Rosa.

Dois cartórios, dois países, onze anos de distância, e o mesmo hábito de funcionário.
<strong>Mãe e filha têm o próprio lugar de nascimento levemente errado no papel, pelo mesmo
motivo.</strong>

É a coisa mais parecida com herança que eu encontrei em documento neste projeto inteiro.""",

"""E a pergunta continua de pé, e continua sem resposta.

Eu tenho a data, tenho a lista de nomes, tenho o padrão e tenho o furo. Não tenho a única
coisa que resolveria isso: alguém que estivesse naquela casa e que tivesse perguntado à Rosa
por que aquele nome.

Só que essa pessoa existe.""",

"""Ela nasceu em 2 de janeiro de 1937.

Está viva. Tem oitenta e nove anos, e faz noventa em 2 de janeiro de 2027.

E se chama Mafalda.

<strong>Este livro tem uma pergunta central e tem uma testemunha viva, e as duas são a mesma
pessoa.</strong>""",
]

CAP31 = [
"""Ninguém vira brasileiro num dia.

Vira devagar, ao longo de uma vida inteira. E depois vira de repente, por decreto, sem ter
sido consultado.""",

"""A parte devagar já apareceu neste livro sem que eu percebesse que era ela.

Está na lista dos filhos.

Enrico nasceu na Itália e tem nome italiano. Erminda, Nair, Maria Therezinha, Izaira, Fermino,
Rosalia, Luiz e Dionísio nasceram aqui e têm nome daqui.

Uma família não decide num dia parar de ser italiana. Ela vai batizando os filhos e, sem
anunciar nada a ninguém, <strong>muda de língua no meio da própria descendência</strong>.""",

"""A parte de repente começou dez meses depois de Mafalda nascer.

Em novembro de 1937, Getúlio Vargas fechou o Congresso e instaurou o Estado Novo. Com ele veio
a <strong>campanha de nacionalização</strong>.

Escolas em língua estrangeira, fechadas. Jornal em língua estrangeira, proibido. Associações de
imigrantes, sob controle. E, em vários lugares, proibido falar a língua em público.""",

"""É preciso entender o que uma lei dessas quer dizer dentro de uma casa.

Não é uma lei sobre bandeira e sobre hino.

<strong>É uma lei sobre a boca.</strong>

Um homem e uma mulher que chegaram adultos, que falavam dialeto vêneto entre si e português
tropeçado na rua, passaram a viver num país onde a língua em que eles pensavam tinha virado
problema.""",

"""Em agosto de 1942, o Brasil declarou guerra à Itália.

Rosa Forner e Fausto Miotto moravam aqui havia quinze anos, tinham sete filhos brasileiros e
trabalhavam a terra de outra pessoa no interior de São Paulo.

De um dia para o outro, viraram <strong>súditos do Eixo</strong>.

Carteira de estrangeiro obrigatória. Restrição de circulação. Registro em delegacia.""",

"""E é aqui que um papel deste acervo deixa de ser curiosidade de arquivo.

O <strong>registro de estrangeiro de Angelo Dei Agnoli</strong>, com o carimbo da Delegacia de
Polícia de Grama, foi o documento que me provou para onde a família tinha ido. Eu o usei como
pista de geografia.

Ele não foi feito para isso. <strong>Foi feito para vigiar.</strong>

Aquele carimbo era a prova de que o Estado sabia onde ele morava. E não tê-lo era um problema
muito maior do que tê-lo.""",

"""Eu não sei o que aconteceu com esta família naqueles anos.

Não achei processo, não achei multa, não achei denúncia, não achei apreensão. É perfeitamente
possível que não tenha acontecido nada: eram agricultores no interior, longe de porto e de
colônia grande, e a máquina da guerra apertou muito mais em Santa Catarina e no Rio Grande do
Sul do que numa cidade de café da Mogiana.

O que dá para dizer é que a lei valia para eles.""",

"""E há uma coisa que o documento diz sozinho.

Em 29 de dezembro de 1949 — quatro anos depois do fim da guerra, vinte e dois anos depois de
ter atravessado o Atlântico com um ano de idade e de ter sido pescado de um naufrágio —
<strong>Enrico Miotto ainda era italiano</strong>.

Não é descuido. Naturalizar custava dinheiro, tempo e papel, e para um pedreiro de vinte e três
anos não resolvia nada de prático.

Ninguém vira brasileiro porque quer. Vira porque nasceu, ou porque compensa.""",

"""O que eu não tenho é o dentro da casa.

O que se falava à mesa. O que se cozinhava no domingo. Em que língua se rezava, se é que se
rezava. Se o dialeto servia para conversar, ou só para brigar e para contar segredo na frente
das crianças. Se alguém ensinou uma palavra de italiano a alguém de propósito, ou se todos
deixaram cair.

Nenhum arquivo guarda isso. Não existe cartório de cozinha.

É a parte da história que só existe na cabeça de quem estava lá — e a única pessoa que estava
lá e ainda pode contar nasceu em 2 de janeiro de 1937.""",

"""O que dá para medir é a velocidade.

Na lista do <em>Alhena</em>, em 1927, a coluna Instrução diz <strong>Sim</strong> para Rosa
Forner. Ela sabia ler, em italiano, num tempo e num lugar em que muita gente não sabia ler em
língua nenhuma.

Os netos dela não falam italiano.

<strong>Duas gerações.</strong> É esse o prazo.""",

"""E existe um marcador ainda mais frio, que eu só enxerguei quando montei a árvore inteira
numa página só.

Rosa <strong>Forner</strong> casou com Fausto Miotto, e teve Mafalda <strong>Miotto</strong>.

Mafalda Miotto casou com José Mariano Terra, e teve Marta <strong>Terra</strong>.

Marta Terra casou com Carlos de Andrade, e teve João de <strong>Andrade</strong>.""",

"""Em três gerações, por três casamentos, os dois sobrenomes que atravessaram o Atlântico
saíram da linha.

Forner durou uma geração. Miotto durou duas.

O bisneto que está escrevendo este livro não se chama nem Forner nem Miotto.""",

"""E não houve perda nenhuma nisso, no sentido em que se costuma falar de perda.

Ninguém foi apagado, ninguém foi obrigado a trocar de nome, nenhuma dessas três mulheres foi
coagida a coisa alguma. Casaram com quem quiseram e adotaram o sobrenome do marido, que era o
que se fazia.

<strong>Virar brasileiro, nesta família, foi isso: uma sequência de mulheres trocando de nome,
e cada troca afastando um pouco mais a linha do porto de onde ela saiu.</strong>""",

"""E talvez seja por isso que a memória desta família passou por mulher.

O sobrenome foi embora pelo lado dos homens. A história ficou do outro.

Rosa contou ao Enrico e contou à Mafalda. Maria Luigia teve a Pulcheria, e o que a Pulcheria
viu chegou a mim pela Patrícia. Mafalda contou à Marta. E chegou a mim.

<strong>Quatro gerações de gente que não se chama Forner carregando o que aconteceu com uma
mulher chamada Forner.</strong>""",
]

CAP32 = [
"""Vincenzo Forner e Santa Pandolfo tiveram dez filhos.

Este livro seguiu dois deles através de um oceano: Rosa, a nona, e Maria Luigia, a sexta.

Este capítulo é sobre o quarto.""",

"""<strong>Sante Forner</strong> nasceu em 16 de abril de 1893, em Monfumo.

Foi para a Grande Guerra, esteve nos Alpes, e voltou com três medalhas que a família mandou
emoldurar.

Aquele quadro existe até hoje. Nunca atravessou o oceano.""",

"""E ele ficou.

Não por coragem, não por apego, não por nenhuma razão que alguém tenha escrito num papel.
Ficou porque ficar também é uma decisão, e é a única das duas que não deixa rastro.""",

"""Aqui é preciso admitir uma assimetria que atravessa este livro inteiro.

<strong>Este livro existe porque uma parte da família foi embora.</strong>

Ir embora produz documento. Produz lista de embarque, manifesto, folha de desembarque,
registro de estrangeiro, livro de hospedaria, carimbo de delegacia. Cada fronteira que uma
pessoa cruza gera um papel, porque alguém do outro lado quer saber quem entrou.

<strong>Ficar não produz quase nada.</strong>""",

"""O resultado é constrangedor, e eu vou dizer com todas as letras:

Eu sei mais sobre quatro dias da vida de Rosa Forner em outubro de 1927 do que sobre os
cinquenta e quatro anos inteiros de vida do irmão dela.

Tenho a hora em que ela nasceu. Tenho a cabine em que ela viajou, o número da família dela numa
hospedaria, a profissão que ela declarou, o destino que ela deu e o fato de que sabia ler.

Do Sante eu tenho uma data de nascimento, três medalhas, uma carteira de identidade e um ano
de morte.""",

"""E aquela carteira de identidade é o exemplo perfeito do problema.

Ele a tirou no comune de Asolo, em março de 1940. Ela existe neste projeto não pelo que diz
sobre ele, mas pelo que diz sobre o pai dele: foi a linha <em>Padre: di Vincenzo</em> que me
provou que o velho ainda estava vivo naquele mês.

<strong>O homem que ficou aparece no meu arquivo como testemunha da vida de outra pessoa.</strong>""",

"""Sante morreu em 1947, aos cinquenta e quatro anos.

Rosa morreu em 1986, aos oitenta e três, no Brasil.

<strong>Depois de outubro de 1927, os dois nunca mais se viram.</strong> Ela sobreviveu a ele
por trinta e nove anos, em outro continente.

Se escreveram cartas, eu não sei. Nenhuma sobreviveu deste lado.""",

"""Maria Luigia durou ainda mais.

Nasceu em 1896, sobreviveu ao naufrágio aos trinta e um anos com quatro filhos, e morreu em
1992, aos noventa e seis.

<strong>Sessenta e cinco anos depois daquela noite.</strong> Ela ainda estava viva quando eu
nasci.""",

"""E do lado de lá a linha continuou.

Sante teve <strong>Galliano</strong>. Galliano teve <strong>Giorgio</strong>.

Três gerações no mesmo canto do Vêneto, enquanto quatro gerações aconteciam aqui.""",

"""Ponha as duas colunas lado a lado e olhe o que elas fazem.

Deste lado: Rosa, 1903. Mafalda, 1937. Marta, 1960. João, 1984. João Luca, 2012. Cinco
gerações, e o sobrenome sumiu na terceira.

Do lado de lá: Sante, 1893. Galliano. Giorgio.

<strong>A linha que ficou seguiu por homens. A linha que foi seguiu por mulheres.</strong>

É por isso que lá o nome está inteiro e aqui ele acabou. Não foi o oceano que comeu o
sobrenome. Foi a sequência de quem teve filha.""",

"""Cem anos de separação não são uma história dramática.

Não houve briga, não houve rompimento, não houve carta rasgada. Duas famílias tocaram a
própria vida, cada uma no seu lugar, e a distância fez o que a distância faz: primeiro vira
notícia rara, depois vira nome numa história antiga, depois vira nada.

Em algum ponto entre 1927 e hoje, os dois lados desta família pararam de saber que o outro
existia.""",

"""E aí a coisa se desfez de um jeito que ninguém teria imaginado.

Eu estava montando a árvore da minha família num site de genealogia. Botando nome, data,
lugar, um por um.

Do outro lado do Brasil, <strong>Patrícia Betti</strong> estava fazendo exatamente a mesma
coisa, ao mesmo tempo, sem me conhecer.

Ela é neta da Pulcheria — a menina de seis anos da cozinha — e bisneta de Maria Luigia.""",

"""E então nós dois chegamos nos nossos avós.

<strong>As duas árvores se tocaram.</strong>

Não fui eu que a achei, e não foi ela que me achou. Foi o banco de dados que percebeu, porque
duas pessoas tinham digitado o mesmo casal do século XIX em duas cidades diferentes.

Vincenzo Forner e Santa Pandolfo, mortos havia mais de um século, apresentaram um ao outro
dois bisnetos que não sabiam da existência um do outro.""",

"""Depois disso a gente conversou muito, e continua conversando.

Unificamos as raízes, juntamos o que cada um tinha, e boa parte do que este livro conta veio
dessas conversas. A cena do cozinheiro veio daí. O bote dos cozinheiros veio daí. O navio de
carvão veio daí. A menina que achou o pai veio daí.

<strong>Sem a Patrícia, o capítulo mais importante deste livro seria uma lista de nomes numa
folha holandesa.</strong>""",

"""E foi por elas, pelas primas que apareceram do outro lado do Brasil, que eu cheguei ao
<strong>Giorgio</strong>.

O bisneto do irmão que ficou.

Cem anos, um oceano e uma guerra depois, a família que se dividiu em Monfumo voltou a se falar
porque quatro ou cinco pessoas resolveram, mais ou menos ao mesmo tempo, escrever os nomes dos
próprios avós num formulário na internet.""",

"""O quadro com as três medalhas continua na Itália.

A casa de onde Rosa saiu, se ainda estiver de pé, continua na Itália.

E agora existe alguém do lado de lá que atende quando eu chamo.""",
]

CAP12 = [
"""Este capítulo é sobre sete pessoas subindo uma prancha, e sobre uma coisa que quase ninguém
aponta quando conta esta história.

<strong>Não havia um homem adulto entre elas.</strong>""",

"""Rosa Forner, vinte e quatro anos, com Enrico, de um ano.

Maria Luigia Forner, trinta e um, com Gina de sete, Pulcheria de seis, Rino de quatro e Danilo
de dois.

Duas mulheres e cinco crianças. A mais velha das crianças tinha sete anos. E um bebê que tinha
completado um ano na véspera.""",

"""Os dois maridos já estavam do outro lado do oceano.

Angelo Dei Agnoli tinha desembarcado em Santos em abril. Fausto Miotto tinha ido antes, num
mês que eu ainda não sei.

Foi assim que se fez a maior parte da emigração italiana, e é assim até hoje em qualquer
emigração do mundo: o homem vai primeiro, aguenta um tempo sozinho, junta o que dá, e manda
buscar.

O que quase nunca se conta é o que sobra para quem é buscado.""",

"""O que sobrou para elas foi isto.

Sair de Monfumo e de Castelcucco com cinco crianças. A estrada até Asolo, o trem até Treviso,
outro trem até Gênova. Atravessar uma cidade que nenhuma das duas conhecia, com bagagem e com
criança de colo.

Achar o navio, achar a fila certa, passar pela inspeção sanitária, responder ao funcionário,
entregar o nome e a idade de cada uma das sete pessoas.

E depois catorze dias de mar.

<strong>Sem um único adulto para dividir isso.</strong>""",

"""Há uma palavra num documento deste livro que só faz sentido depois de se ler essa cena
inteira.

Quando as duas foram anotadas numa lista, três dias depois do naufrágio, o funcionário
escreveu na coluna de parentesco a mesma coisa para as duas: <strong>CHEFE</strong>.

Aquilo não foi um erro de leitura do escrivão, nem uma delicadeza com duas náufragas.

Foi uma descrição correta do que tinha acontecido durante catorze dias no mar.""",

"""E as duas eram irmãs, mas não eram irmãs de qualquer jeito.

Maria Luigia nasceu em 1896. Rosa, em 1903. Sete anos entre uma e outra.

Em 1914 a mãe delas, <strong>Santa Pandolfo</strong>, morreu. Rosa tinha onze anos. Maria
Luigia tinha dezoito.

Numa casa de dez filhos, no Vêneto rural, quando a mãe morre e existe uma filha de dezoito
anos, não se contrata ninguém.

<strong>A filha de dezoito vira a mãe.</strong>""",

"""Treze anos depois, as duas estão na mesma prancha em Gênova.

A que criou e a que foi criada, cada uma carregando os próprios filhos, indo para o mesmo
lugar.

Não é coincidência de irmãs que combinaram viajar juntas: foram chamadas para o mesmo destino
porque os maridos estavam no mesmo lugar. Mas o efeito é o que é.

Numa noite de outubro, no meio do Atlântico, a mulher que tinha criado Rosa estava a poucos
metros dela, na água, com quatro filhos.""",

"""E ficou gente para trás.

<strong>Vincenzo Forner ainda estava vivo.</strong> O pai delas tinha sessenta e cinco anos em
1927, e continuaria vivo por pelo menos mais treze — eu sei disso pela carteira de identidade
que o filho Sante tirou em Asolo, em 1940, com o pai anotado como vivo.

Sante ficou. Os outros irmãos ficaram.

Rosa e Maria Luigia se despediram do pai em 1927 e, até onde eu consegui apurar, nenhuma das
duas o viu outra vez.""",

"""Eu não sei o que elas levavam.

As listas de passageiros daqueles anos têm colunas para isso. Bagagem, com marca e número de
volume. E o dinheiro declarado, por pessoa — em algumas listas o campo traz só um traço, que
quer dizer chegada sem recurso nenhum.

A lista de embarque de Gênova de outubro de 1927 é um dos papéis que eu ainda não achei.

Se ela aparecer, vai dizer quantos volumes aquelas duas mulheres subiram carregando. Que é a
mesma coisa que dizer quantos volumes foram para o fundo do Atlântico catorze dias depois.""",

"""A partir daqui a história já está decidida, e elas não sabem.

Subiram a prancha num dia de outubro achando que estavam começando uma vida nova. E estavam.
Só que entre a prancha e a vida nova havia uma coisa que ninguém tinha posto na conta.

Rosa Forner tinha vinte e quatro anos e não conhecia o mar até aquela semana.

Catorze dias depois ela ia passar horas dentro dele.""",

"""O <em>Principessa Mafalda</em> largou de Gênova em <strong>11 de outubro de 1927</strong>.

A viagem completa, da Itália até a Argentina, levava catorze dias em condições normais.

Ele afundou em <strong>25 de outubro</strong>.

<strong>O navio durou exatamente o tempo de uma travessia.</strong>""",
]

CAP16 = [
"""Para entender o que aquele navio era em 1927, é preciso saber o que ele foi em 1908.

E para saber isso, é preciso começar pelo irmão dele, que nunca navegou.""",

"""<strong>22 de setembro de 1907.</strong> Estaleiro em Riva Trigoso, no litoral perto de
Gênova.

A Navigazione Generale Italiana ia lançar o primeiro de dois transatlânticos gêmeos
encomendados para a rota da América do Sul. O primeiro se chamava
<strong><em>Principessa Jolanda</em></strong>.

Havia autoridade, havia imprensa, havia madrinha, havia multidão. Lançamento de navio grande
era espetáculo público, e este tinha sido anunciado.""",

"""O casco desceu a rampa e entrou na água.

E <strong>tombou</strong>.

Adernou para um lado, deitou, e afundou ali mesmo, diante de todo mundo, sem nunca ter
navegado um metro.

Foi fotografado. As imagens existem: um transatlântico novo, com a pintura fresca, deitado de
lado na água rasa do próprio estaleiro.""",

"""É um dos desastres navais mais constrangedores da história italiana, e ele não matou
ninguém que se saiba — matou uma reputação.

O <em>Jolanda</em> foi lançado com o acabamento interno já instalado, mobília e tudo, e sem
lastro suficiente. Ficou pesado demais em cima.

Um navio pesado em cima tomba. É a mesma física que ia importar dezenove anos depois, do outro
lado do Atlântico, numa noite de outubro.""",

"""E o <em>Jolanda</em> tinha um gêmeo.

Mesmo projeto, mesmo estaleiro, casco já em construção ao lado.

Depois do desastre, refizeram os cálculos, corrigiram o que havia para corrigir, e lançaram o
segundo navio em <strong>1908</strong>. Esse desceu direito. Entrou em serviço em 1909.""",

"""<strong>Esse navio se chamava Principessa Mafalda.</strong>

Ele existe, na forma em que existiu, por causa de um acidente. Foi construído duas vezes: uma
vez no papel, junto com o irmão, e outra vez depois que o irmão afundou na frente da imprensa
italiana.""",

"""O nome veio de uma criança.

<strong>Mafalda di Savoia</strong> nasceu em 1902, segunda filha de Vittorio Emanuele III, rei
da Itália. Tinha seis anos de idade quando um casco de nove mil toneladas recebeu o nome dela.

Era o que se fazia. Navio grande de bandeira nacional levava nome de gente da casa real,
porque o navio era propaganda antes de ser transporte: dizia ao mundo que a Itália construía
coisas grandes.""",

"""Ela não escolheu nada disso, e não teve como saber o que estava sendo posto no nome dela.

Que em 1927 aquele casco ia afundar no Atlântico com trezentas e catorze pessoas dentro.

E que quarenta anos depois, num sítio do interior de São Paulo, ia haver uma mulher brasileira
com o nome dela e com o nome do navio, sem que as duas coisas fossem distinguíveis.""",

"""As medidas, para quem quiser: nove mil duzentas e dez toneladas. Velocidade de serviço por
volta de dezoito nós. Capacidade para pouco mais de mil e quatrocentos passageiros, a grande
maioria em terceira classe.

Entre 1909 e 1927 ele fez cerca de <strong>noventa travessias</strong> do Atlântico.

Levou, em dezoito anos de serviço, algo como cem mil pessoas.""",

"""E em 1908, quando aquele casco entrou na água pela primeira vez, em Monfumo não aconteceu
nada.

<strong>Rosa Forner tinha cinco anos.</strong> Santa Pandolfo, a mãe, estava viva e ainda ia
viver seis anos. Vincenzo trabalhava a terra. Sante tinha quinze e ainda não tinha ouvido falar
em Caporetto. Maria Luigia tinha doze.

Ninguém naquela casa tinha ouvido falar de Riva Trigoso, nem do <em>Jolanda</em>, nem da filha
do rei.""",

"""A distância entre Monfumo e Riva Trigoso é de uns trezentos quilômetros.

Naquele ano, numa ponta, uma família de agricultores plantava milho num pedaço de encosta que
já não bastava.

E na outra, um estaleiro punha na água a coisa que ia decidir a vida daquela família dezenove
anos depois.""",
]

CAP17 = [
"""O que se conta sobre esses navios é sempre a mesma coisa.

Os salões. A escadaria. O jantar servido em várias etapas. A orquestra. As senhoras descendo
para o jantar. O fumoir. A biblioteca.

Tudo isso é verdade, e é a parte menos importante do navio.""",

"""A rota do <em>Principessa Mafalda</em> era esta:

<strong>Gênova — Barcelona — Dakar — Rio de Janeiro — Montevidéu — Buenos Aires.</strong>

Catorze dias entre a Itália e a Argentina, em condições normais. Cerca de noventa vezes, entre
1909 e 1927.

Era uma linha de ônibus. Uma linha de ônibus de catorze dias, atravessando um oceano e uma
linha do equador, mas uma linha: sempre os mesmos portos, sempre na mesma ordem, sempre para o
mesmo lado.""",

"""E agora a aritmética, que é onde a glória desses navios costuma se desmanchar.

Na última viagem, a de outubro de 1927, o <em>Mafalda</em> levava pouco mais de
<strong>sessenta passageiros na primeira classe</strong>. Cerca de <strong>oitenta na
segunda</strong>.

E quase <strong>mil na terceira</strong>.

Mais uns trezentos de tripulação.""",

"""Leia esses números outra vez, devagar.

<strong>Cento e quarenta pessoas em cima. Mil embaixo.</strong>

Para cada passageiro que jantava com orquestra, havia sete dormindo em beliche de ferro num
porão sem janela.""",

"""Então é preciso inverter a frase que se usa para descrever esses navios.

Um transatlântico da rota sul-americana não era um hotel de luxo que também levava imigrante.

<strong>Era um transporte de imigrante com um hotel montado em cima.</strong>

O dinheiro estava embaixo. Mil passagens de terceira classe pagavam o navio. As sessenta
cabines de primeira pagavam a reputação dele.""",

"""E a reputação servia para uma coisa muito concreta.

O luxo do andar de cima era o que gerava a reportagem, a fotografia no jornal, o nome
conhecido e o cartaz colado na parede de uma praça de província.

<strong>A propaganda era feita com a escadaria e vendida para quem ia no porão.</strong>

O panfleto que Rosa e Fausto podem ter visto em Asolo não trazia foto de beliche. Trazia uma
palavra: <em>América</em>.""",

"""Isso não é hipocrisia particular daquele navio nem daquela companhia.

É o modelo inteiro da emigração transatlântica, e funcionou por sessenta anos justamente
porque funcionava: quem ia embaixo chegava, na esmagadora maioria das vezes, e mandava buscar a
família.

O <em>Principessa Mafalda</em> foi apenas competente nesse modelo. Dezoito anos, noventa
travessias, cem mil pessoas atravessadas.""",

"""E havia uma coisa que a primeira e a terceira classe daquele navio nunca faziam: se ver.

Conveses separados. Escadas separadas. Refeitórios separados. Horários de banho separados.
Grades e portas que se abriam num sentido só.

Uma pessoa podia atravessar o Atlântico inteiro naquele casco sem trocar uma palavra com
alguém que estivesse três andares abaixo dela.""",

"""Foi assim durante dezoito anos.

E numa única noite, em 25 de outubro de 1927, as duas partes daquele navio foram para a mesma
água, ao mesmo tempo, com os mesmos coletes.

O que aconteceu ali está no capítulo 19, e é a primeira e a última vez que os dois lados
daquele casco falaram um sobre o outro.

<strong>Não gostaram do que viram.</strong>""",
]

CAP18 = [
"""Um navio não envelhece sozinho.

Ele envelhece porque chegam outros.""",

"""Em 1909, quando entrou em serviço, o <em>Principessa Mafalda</em> era o que a Itália tinha
de melhor para mandar à América do Sul.

Casco novo, nome de princesa, nove mil toneladas, a linha inteira de Gênova a Buenos Aires. Era
o navio que se mostrava.

Dezoito anos depois, era o navio que sobrava.""",

"""O que aconteceu no meio não foi ferrugem. Foram duas coisas que nada tinham a ver com aquele
casco.

<strong>A primeira: os Estados Unidos fecharam a porta.</strong>

As leis de cota de 1921 e de 1924 cortaram brutalmente a entrada de gente do sul e do leste da
Europa. Um italiano que em 1910 iria para Nova York, em 1925 já não ia.

O fluxo não parou. <strong>Virou.</strong> Desceu para Buenos Aires, Montevidéu e Santos.

De repente, a rota da América do Sul deixou de ser a rota secundária e virou o negócio
principal da emigração italiana.""",

"""<strong>A segunda: as companhias italianas encomendaram navios novos.</strong>

<em>Giulio Cesare</em>, 1922. <em>Conte Rosso</em>, 1922. <em>Conte Verde</em>, 1923.
<em>Duilio</em>, 1923.

Maiores, mais rápidos, com máquinas de outra geração, projetados depois da guerra para
exatamente aquela rota que tinha acabado de ficar valiosa.

Um navio de 1908 não compete com um de 1923. Não é questão de conservação. É questão de
projeto.""",

"""E aí acontece com um navio o que acontece com qualquer frota.

<strong>O <em>Mafalda</em> não foi aposentado. Foi rebaixado.</strong>

Cada navio novo que entrava na água o empurrava um degrau para baixo. O melhor navio faz a
viagem de prestígio, com o nome no jornal. O segundo faz a mesma rota sem barulho. O terceiro
faz o que sobra: a data que ninguém quer, a carga que ninguém disputa, a manutenção que der.""",

"""E há uma consequência econômica disso que é fria e é direta.

Um navio cujo dinheiro vem de mil passagens de terceira classe, e cujo prestígio já foi para
outro casco, é um navio em que <strong>consertar custa caro e rende pouco</strong>.

Não porque alguém seja mau. Porque cada lira gasta na casa de máquinas de um navio de dezenove
anos é uma lira que não foi para o navio de quatro.

As avarias sucessivas da última viagem — Barcelona, a escala africana, os mecânicos trabalhando
durante a travessia — não foram azar de outubro de 1927.

Foram o fim de uma sequência de decisões que começou quando o primeiro navio novo entrou na
água.""",

"""E nada disso chegava até quem comprava a passagem.

O panfleto colado numa parede de Asolo não dizia <em>navio de dezenove anos, terceiro na fila
da companhia, casa de máquinas remendada</em>.

Dizia <strong>América</strong>.

Essa informação existia dentro da companhia, dentro do estaleiro e dentro da casa de máquinas.
Não existia em Monfumo, não existia em Castelcucco, e não existia no bolso de ninguém que
subisse aquela prancha.""",

"""Rosa Forner e Maria Luigia viram o que qualquer pessoa naquela situação teria visto.

Um navio enorme, encostado no cais de Gênova, com bandeira italiana e nome de princesa.

A maior coisa construída que qualquer uma das duas tinha visto na vida.

<strong>Ninguém sobe uma prancha olhando para o eixo.</strong>""",
]

CAP_BUSCA = [
"""Tudo o que existe neste livro e não é lembrança de família veio de papel.

E papel mente. Não do jeito que se imagina — quase nunca por má-fé. Mente porque foi escrito
depressa, porque o escrivão ouviu errado, porque a pessoa que respondeu não sabia, porque o
formulário não tinha campo para a verdade.

Este capítulo é sobre isso, e sobre uma coisa pior que descobri no caminho.""",

"""Comecemos por um quadro numa parede.

Existe, num livro sobre Castelcucco, uma árvore genealógica impressa da família Forner. Ela
traz catorze nomes de filhos, distribuídos em duas fileiras.

Angela, 1886. Pietro, 1889. Martino, 1891. Sante, 1893. Bonfiglio, 1898. Giulio, 1900. Rosa.
Maria M., 1907.

E depois: Angela, 1898. Onorato, 1900. Alessandro Domenico, 1903. Ausilio Fortunato e Roberto,
gêmeos de 1908. Francesco, 1913.

Lida corrida, a lista diz o que não é: <strong>catorze filhos de um casal só</strong>.""",

"""Foi preciso ampliar a fotografia do quadro para enxergar por quê.

Descendo pela direita, a partir de <strong>Cadonà Maria Teresa</strong>, nascida em Monfumo em
1869 e casada com <strong>Abele Alessandro Forner</strong> — irmão de Vincenzo —, há uma linha
vertical.

Ela passa ao lado da primeira fileira sem tocar em nada, e vai se ligar à barra horizontal da
segunda.

<strong>A segunda fileira não é de Vincenzo. É do irmão dele.</strong>

Oito filhos de Vincenzo e Santa, seis de Abele e Maria Teresa. Um traço de dois centímetros,
num quadro impresso, decidindo quem é irmão de quem.""",

"""E aqui está a coisa mais difícil desta pesquisa inteira, e eu levei meses para entender.

<strong>Aquele quadro não está errado.</strong>

Ele está certo, e é ilegível no tamanho em que foi impresso. A linha existe, e faz exatamente
o que devia fazer.

A diferença entre um documento errado e um documento mal lido não aparece sozinha. Ela só
aparece quando alguém desconfia.

E quando finalmente li o quadro direito, ele tinha um único erro de verdade — e o erro era na
minha bisavó. Ali Rosa aparece nascida em 1905. O ato de nascimento do comune de Monfumo diz
<strong>24 de junho de 1903</strong>.""",

"""Depois veio o nome da mãe dela, e esse quase derrubou um capítulo inteiro.

Nos índices de nascimento do comune, a mulher de Vincenzo aparece <strong>seis vezes como
Pandolfo Santa</strong>.

No registro de 1893 — justamente o de Sante — aparece como <strong>Pandolfo
Domenica</strong>.

E num outro documento, como <strong>Santa Pandelfa</strong>.

Três grafias. Ou é a mesma mulher escrita por três escrivães diferentes, ou são duas mulheres
distintas com sobrenome parecido.""",

"""E isso não é preciosismo de genealogista. É a diferença entre este livro estar certo ou
estar contando a história de outra família.

Se a mulher do registro de 1893 não fosse a mesma dos outros seis, então <strong>Sante não
seria irmão de Rosa</strong>. Seria primo, ou meio-irmão, ou nada.

E o capítulo sobre as três medalhas da Grande Guerra seria sobre um homem que não tem parentesco
nenhum com esta história.""",

"""O que resolveu isso estava dentro de casa o tempo todo.

Numa pasta, entre papéis de família, a <em>carta d'identità</em> que Sante Forner tirou no
comune de Asolo em 8 de março de 1940.

No campo da filiação, com as duas fórmulas fixas do italiano burocrático:

<em>Padre: <strong>di</strong> Vincenzo. Madre: <strong>fu</strong> Pandolfo Domenica
Santa.</em>

<strong>Pandolfo Domenica Santa.</strong> As três grafias eram pedaços do mesmo nome inteiro,
e cada escrivão tinha escolhido um. E o <em>di</em> contra o <em>fu</em> dizia, de quebra, que
em 1940 o pai estava vivo e a mãe não.

Eu passei semanas escrevendo para arquivos italianos atrás de uma informação que estava numa
gaveta em São Paulo.""",

"""E aí a busca virou outra coisa, e virou por causa de um cemitério em Vancouver.

<strong>Luigi Miotto, pai de Fausto, também emigrou.</strong> Não para o Brasil.

Existe neste acervo uma <em>Registration of Death</em> da Província da Colúmbia Britânica,
número 5509-008734. Ela registra a morte de <strong>Louie Miotto</strong>, em 15 de agosto de
1955, na chegada ao Vancouver General Hospital.

Setenta e cinco anos. Quarenta e oito anos no Canadá. Lenhador aposentado, vinte e cinco anos
de profissão, última vez que trabalhou em 1951. Morava na Prior Street, 566.

Pai: <strong>Miotto Jack</strong>. Mãe: <strong>Fedato Anna</strong>.

Jack é como um oficial canadense escreve Giacomo. Fedato é como ele escreve Fidato. São
Jacobus Miotto e Anna Fidato — o casal que abre o tronco Miotto deste livro.""",

"""Só que o documento tem duas linhas que não fecham.

Diz que ele nasceu em <strong>março de 1880</strong>. O certificado de casamento de Maser diz
que Luigi Miotto tinha vinte e cinco anos em junho de 1900, o que o põe nascendo por volta de
1875.

E no campo do estado civil traz uma palavra só: <strong>Single</strong>.

Ou são dois irmãos diferentes, ambos filhos de Jacobus e Anna, e o Luigi de Vancouver não é o
pai de Fausto.

Ou é o mesmo homem — que deixou mulher e um filho de três anos em Castelcucco por volta de
1907, refez a vida do outro lado do mundo, e morreu meio século depois registrado como
solteiro por um irmão que ou não sabia, ou não quis dizer.""",

"""Fui olhar como essa hipótese tinha entrado na minha pesquisa, e achei a hora exata.

Numa árvore genealógica colaborativa da internet, o Luigi de Vancouver e o Luigi de Monfumo
eram, até pouco tempo atrás, dois perfis separados.

Em <strong>18 de novembro de 2024, às onze e vinte e um da manhã</strong>, um colaborador que
eu não conheço unificou os dois. Preservou o canadense, eliminou o de Monfumo, e deu como
motivo o texto padrão que o próprio sistema oferece: <em>a maioria das informações de dados
vitais e de parentescos correspondem</em>.

<strong>Um clique, num minuto de uma segunda-feira, e o meu bisavô passou a ter um pai que
morreu sozinho no Canadá.</strong>""",

"""Desfazer não deu.

O sistema desabilita o botão quando já existem edições posteriores à fusão. Foi preciso
reconstruir o perfil à mão.

E quem reconstruiu foi um documento brasileiro que estava ali o tempo todo:
<strong>a declaração de óbito do próprio Fausto</strong>, lavrada em 13 de agosto de 1979, em
São João da Boa Vista.

Ela nomeia por extenso o pai e a mãe dele: <strong>Luigi Miotto e Domenica Ganeo</strong>.

Setenta e cinco anos depois de Fausto nascer, do outro lado do oceano, um escrivão paulista
escreveu os dois nomes certos.""",

"""<strong>Louie Miotto morreu solteiro em Vancouver e não é pai de ninguém desta linha.</strong>

A sepultura no Mountain View Cemetery continua lá, e continua sem ter sido visitada por
ninguém desta família. Só mudou de título: pode ser a de um tio-avô, não a de um bisavô.

O que continua aberto é outra coisa, e menor: quem foi o pai do Luigi. A árvore registra um
Luigi Miotto nascido em 10 de abril de 1874, em Monfumo, filho de um Giovanni Miotto e de uma
Luigia Forner — e <em>esses perfis não têm nenhum documento anexado</em>.""",

"""Não estou dizendo que aquele colaborador agiu de má-fé. Provavelmente fez o que eu faria.

O ponto é outro, e é sobre a época em que estamos pesquisando.

Um livro velho erra e continua parecendo um livro velho: o papel amarelo avisa o leitor para
desconfiar. <strong>Uma árvore colaborativa erra e continua parecendo verdade.</strong> O erro
entra com data, hora e justificativa, e no minuto seguinte já não se distingue do resto.

E quando outra pessoa copia aquele nó para a árvore dela, o erro deixa de ter autor.""",

"""E agora eu preciso dizer que a memória de família faz exatamente a mesma coisa.

Há uma versão desta história, contada nesta família há décadas, segundo a qual
<strong>Rosa embarcou grávida</strong>, e foi por isso que tiraram as duas mulheres do navio:
duas mulheres, cinco crianças e uma grávida.

Enrico tinha um ano e quinze dias e estava a bordo — está no Livro 100 da Hospedaria do Brás.
E a filha seguinte, Erminda, nasceu em 10 de novembro de 1928, <strong>doze meses e meio depois
do naufrágio</strong>.

Rosa não estava grávida naquele navio. Não há como estar.""",

"""E dá para localizar de onde a versão veio.

Quem contava essa história na família era <strong>João Betti</strong>, marido da Pulcheria, que
não estava a bordo e ouviu de quem estava.

Repare no que aconteceu, porque é bonito e não é vergonhoso: uma mulher grávida com um bebê de
colo é uma imagem mais forte do que uma mulher com um bebê de colo. <strong>A memória escorrega
sempre na direção da imagem que se sustenta melhor.</strong>

E o resto do que ele contou está de pé. Que a terceira classe não tinha preferência. Que elas
chegaram pretas de carvão. Que os maridos passaram os olhos por elas e não as reconheceram.

Uma testemunha que erra num detalhe não é uma testemunha ruim. É uma testemunha.""",

"""Há ainda uma coisa que só ficou visível quando os dois lados desta família voltaram a se
falar.

Um galho guardou o cozinheiro de pele escura e a menina que acha o pai no meio da multidão.

O outro galho guardou o carvão, a hospedaria e os dois homens procurando sem achar.

<strong>Nenhum dos dois está mentindo. Nenhum dos dois está inteiro.</strong>

Foi preciso um site de genealogia, cem anos e duas pessoas digitando os próprios avós para que
aquela noite voltasse a ter começo e fim ao mesmo tempo.""",

"""E aqui vem a parte que não tem conserto.

<strong>Pulcheria Pasqua Dei Agnoli morreu em 2013.</strong>

A menina de seis anos que estava na cozinha daquele navio, que viu tudo, que viveu noventa e
dois anos — estava viva, no Brasil, quando eu já era um adulto feito.

<strong>Maria Luigia morreu em 1992</strong>, aos noventa e seis anos, sessenta e cinco anos
depois de ter atravessado aquela noite com quatro filhos pequenos. Eu era menino.

As duas estavam vivas, neste país, e eu não sabia que existiam.""",

"""Então este capítulo não é sobre papel velho.

Eu sei ler <em>di</em> e <em>fu</em>. Sei que uma linha de dois centímetros muda uma família
inteira. Sei que uma árvore da internet erra com hora marcada. Aprendi tudo isso, e aprender
foi a parte fácil.

Nenhum arquivo do mundo me devolve vinte minutos de conversa com uma mulher de noventa e dois
anos que estava lá.

<strong>A minha avó tem oitenta e nove anos.</strong>""",
]

CAP_CASA = [
"""Eu nunca estive na Itália.

Este capítulo era para ser escrito lá — em Castelcucco, com a casa na frente. Está sendo
escrito no Brasil, com fotografia, mapa e o que um primo me contou por telefone.

Vou dizer o que sei e como sei, e o que não sei fica em branco até eu ir.""",

"""A vila tem pouco mais de oito quilômetros quadrados e fica a cento e oitenta e nove metros
acima do mar, no sopé do Monte Grappa.

Isso eu já escrevi no primeiro capítulo, e escrevi para descrever 1861.

Vale para hoje. Um lugar daquele tamanho, encostado numa montanha, não vira cidade. Ele
continua sendo o que era, com carro na estrada e telhado novo.""",

"""A montanha é a única coisa desta história inteira que não mudou.

Mil setecentos e setenta e cinco metros. Estava lá quando Luigi Forner nasceu em 1817, quando
Sante subiu para a guerra em 1915, e quando Rosa desceu a estrada pela última vez em 1927.

Quem chega hoje de carro vê exatamente o que eles viam da janela.""",

"""E ficaram coisas lá.

O quadro com as <strong>três medalhas de guerra do Sante</strong>, emoldurado pela família e
pendurado numa parede há quase um século. O retrato do <strong>Galliano</strong>, filho dele,
fardado com as tropas alpinas em 1950, também emoldurado.

Nenhum dos dois atravessou o oceano. Eu os conheço por fotografia de fotografia.""",

"""E existe a casa.

<strong>Giorgio Forner</strong> — bisneto do Sante, o ramo que ficou — mora na região e já
esteve nela. Foi ele quem me mostrou.

Eu não sei o número da porta. Não sei se ainda é da família, se foi vendida, se alguém mora
dentro. Sei que ela existe e que ele sabe onde fica.""",

"""Foi por uma porta em Castelcucco que Rosa Forner saiu, num dia de outubro de 1927, com
Enrico de um ano no colo.

Ela desceu a estrada até Asolo, pegou o trem para Treviso, e de Treviso foi a Gênova.

<strong>Nunca mais voltou.</strong>""",

"""E não foi só ela.

Maria Luigia não voltou. Fausto não voltou. Angelo não voltou.

Quatro adultos saíram daquele pedaço do Vêneto entre 1925 e 1927, e nenhum dos quatro pisou na
Itália outra vez. Rosa morreu em São João da Boa Vista em 1986, cinquenta e nove anos depois.

Que eu saiba, ninguém desta linha voltou desde então. São quatro gerações.""",

"""Eu poderia ter ido antes. Não fui, e as razões são banais: dinheiro e tempo, que são as
razões pelas quais quase ninguém faz quase nada.

Mas há uma que não é banal, e essa eu escolhi.

<strong>Eu não queria chegar lá sem saber.</strong>

Chegar em Castelcucco antes de ler os índices do comune, antes de aprender que <em>di</em> é
pai vivo e <em>fu</em> é pai morto, antes de descobrir que a segunda fileira do quadro é do
irmão do Vincenzo — isso não é voltar. É turismo.""",

"""A viagem tem data, e a data não é minha.

<strong>25 de outubro de 2027.</strong> Cem anos exatos da noite em que aquele navio afundou.

Não escolhi por efeito. Escolhi porque um livro que passou trinta capítulos dizendo que
documento tem data precisa respeitar a única data que esta família tem.""",

"""O que eu vou fazer lá cabe em cinco linhas.

A igreja, que caiu no terremoto de 1695 e foi levantada de novo. O cemitério, e os sobrenomes
nas lápides. O comune, para pedir de uma vez os atos que eu venho pedindo por carta. A estrada
que desce para Asolo, a pé, que é o caminho que eles fizeram.

E a casa.""",

"""E tem uma coisa que eu quero fazer, e que é a razão de a viagem ter data em vez de ter mês.

Um dia eu vou estar de pé naquela porta com o telefone na mão, e do outro lado vai atender uma
mulher chamada Mafalda, que vai ter noventa anos.

<strong>Ela nunca viu essa porta. A mãe dela saiu por ela.</strong>

Eu não sei o que vou dizer. Sei que é para isso que este livro está sendo escrito.""",
]

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

Rosa Forner tinha vinte e quatro anos e um filho de um ano. Enrico tinha
feito um ano em Gênova, na véspera do embarque.""",

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

Nas linhas 26 e 27 daquela folha, e depois nas linhas 44 a 48, estão as sete
pessoas desta história.

Todas as sete.

É o único fato que este capítulo precisa dar, e é o que ele dá: elas
atravessaram a noite que vem a seguir. O que mais aquele papel diz sobre elas
diz muito, e chega na hora certa.""",

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
próprias.

A mesma tabela responde por ela, em parte.

<strong>Monfumo: 307 refugiados numa população de 1.661. Dezoito vírgula cinco por
cento.</strong>

Oito vezes a taxa de Castelcucco. Não é Cavaso e não é catástrofe, mas também não são os
dois por cento do vilarejo do Fausto. Um em cada cinco saiu.

O que a tabela não diz é quem saiu, quando, nem se os Forner estavam entre eles. Diz só que
a vila de Rosa esvaziou bem mais que a vila de Fausto, e que os dois adolescentes desta
história passaram o mesmo inverno em dois lugares que responderam de maneira diferente à
mesma montanha.

A segunda é sobre o que se costuma dizer. Quase todo relato geral sobre aquele front
repete que os civis que viviam colados à linha foram retirados em 1917. É plausível e é
compatível com a documentação, mas a ordem específica, com a lista de quais localidades
e quais casas, ainda não apareceu.

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

A história de Luigi Forner parecia terminar aí: o homem que nunca foi a lugar nenhum e a
quem o mapa mudou debaixo dos pés.

Não termina.""",

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

Mas isso é dali a catorze capítulos.""",

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

CHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 8: CAP8, 9: CAP9, 10: CAP10, 11: CAP12, 12: CAP14, 13: CAP16, 14: CAP17, 15: CAP18, 16: CAP19, 17: CAP20, 18: CAP21, 19: CAP22, 20: CAP23, 21: CAP24, 22: CAP25, 23: CAP26, 24: CAP27, 25: CAP28, 26: CAP29, 27: CAP30, 28: CAP31, 29: CAP32, 30: CAP_BUSCA, 31: CAP_CASA}

# ------------------------------------------------------------------ paginas
pages = []
def P(**kw): pages.append(kw)

P(t='capa')
P(t='rosto')
P(t='dedicatoria')
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
 13: [('vapor_mafalda','O vapor Principessa Mafalda. Lançado em 1908, afundou em 25 de outubro de 1927.')],
 14: [('princess_mafalda_of_savoy','A princesa Mafalda de Saboia, que deu nome ao navio. Morreu em Buchenwald, em 1944.')],
 16: [('princessa_mafalda','O Principessa Mafalda. Saiu de Gênova em 11 de outubro de 1927 com 971 passageiros e 288 tripulantes, e já saiu atrasado.')],
 18: [('mafalda_naufragando','O naufrágio do Principessa Mafalda em representação de época.')],
 21: [('passageiros_agnoli','Lista de passageiros: a família Agnoli, terceira classe, resgatada pelo navio Alhena.')],
 23: [('rosa_forner','Rosa Forner Miotto, 1903 a 1986. Sobreviveu ao naufrágio aos vinte e quatro anos.'),
      ('rosa_forner_documento','Documento de identificação de Rosa Forner Miotto.')],
 24: [('maria_lugia_forner','Maria Luigia Forner, 1896 a 1992, irmã de Rosa.'),
      ('forner_maria_luigia_col_marito_dei_agnoli_angelo','Maria Luigia Forner e o marido, Angelo dei Agnoli.')],
 26: [('enrico','Enrico Miotto, 1926 a 1998. Tinha um ano e quinze dias na noite do naufrágio.'),
      ('enrico_registro_de_estrangeiro','Registro de Estrangeiros de Enrico Miotto, 29 de dezembro de 1949. Data de nascimento: 10.10.1926.')],
 27: [('mafalda_miotto_forner','Mafalda Miotto Terra, nascida em 1937, dez anos depois do naufrágio, com o nome do navio.')],
 29: [('sante_e_familia','Sante Forner e família, na Itália.'),
      ('giorgio_e_sua_familia','Giorgio Forner e família, o ramo que permaneceu no Vêneto.')],
}

AUDIO_BY_CAP = {
 24: [('patricia-01',
       'A fonte é o avô',
       'Patrícia Betti · 8 de setembro de 2026 · 1min06',
       'Ela diz de quem ouviu tudo o que sabe: João Betti, o marido da Pulcheria, que não '
       'estava no navio. E recusa confirmar o cozinheiro. "Pukéria" é como a transcrição '
       'registrou Pulcheria; o áudio está aqui como veio, sem limpeza.',
       'Primo, quem me contou todas as histórias foi meu avô, né, que era o marido da Pukéria. Então, eu só sei da fonte dele. Ele não me falou nada disso, né, não posso dizer… Às vezes, sim, gostava como criança mesmo, né, porque estava todo mundo na terceira classe.\n\nMas o que ele falou é que, por ser terceira classe, eles não tinham preferência, né, e que tinham saído porque eram duas mulheres com cinco crianças, né, e uma grávida, a sua bisa, no caso. Então, eu só sei disso. Agora, se teve um cozinheiro que ajudou ou não… Assim, eu, como pesquisadora, se fosse você, colocaria, se você quiser mencionar, mencionaria que tem essa informação citada por fulana, né, mas que você não tem outra confirmação.\n\nComo que ela soube disso?'),
      ('patricia-02',
       'O carvão, e a hospedaria',
       'Patrícia Betti · 8 de setembro de 2026 · 32s',
       'A versão do avô para o reencontro, e a frase que localiza a cena em São Paulo.',
       'Acho que essa história do navio de carvão é verdade, porque quando o meu avô contou que o meu bisavô foi encontrar a família lá em São Paulo, ele não reconheceu porque a viúva, não sei se foi a minha avó mesmo que estava na frente, na frente da hospedaria ali, onde ele passou, onde ele passou na frente do quarto, não sei, e ele não reconheceu porque disse que ela estava toda suja de carvão. Então, tem uma história, sim.')],
}

AGRADECIMENTOS = """À minha avó <strong>Mafalda</strong>, por ter contado as histórias. Foi ela que despertou em mim, anos atrás, o interesse pela busca de um elo familiar que havia se perdido. Sem ela, este livro não teria começado.

Ao meu primo <strong>Giorgio Forner</strong>, que mora na Itália, por tudo o que contribuiu de informação e de fotografia. Apesar da dificuldade do idioma, sempre demos um jeito de conversar.

À minha prima <strong>Patrícia Betti</strong>, que eu encontrei nas pesquisas do FamilySearch e que também me ajudou com este livro.

Aos meus familiares, aos netos e aos sobrinhos, que vão ter nas mãos a história dos seus eternizada. Que este livro desperte no coração deles o mesmo interesse pela história que a minha avó Mafalda despertou em mim.

E ao principal amigo, aquele que me ajudou a concluir este livro: <strong>Deus</strong>. Que sempre me deu forças para continuar durante estes nove anos."""

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
        for k, tit, meta, nota, tr in AUDIO_BY_CAP.get(num, []):
            P(t='audio', key=k, tit=tit, meta=meta, nota=nota, tr=tr, book=bn)

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
P(t='agradecimentos')
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
    elif t == 'audio':
        folio += 1
        pid = 'au%d' % folio
        tx = ''.join('<p>%s</p>' % E(x.strip()) for x in p['tr'].split('\n\n'))
        out.append(sheet(
            '<div class="aud">'
            '<p class="aud-h">Documento sonoro</p>'
            '<h3 class="aud-t">%s</h3>'
            '<p class="aud-m">%s</p>'
            '<div class="player" data-src="%s">'
              '<button class="pbtn" type="button" aria-label="Tocar">'
                '<svg class="i-play" viewBox="0 0 12 14" aria-hidden="true">'
                  '<path d="M0 0 L12 7 L0 14 Z"></path></svg>'
                '<svg class="i-pause" viewBox="0 0 12 14" aria-hidden="true" hidden>'
                  '<path d="M0 0h4v14H0z M8 0h4v14H8z"></path></svg>'
              '</button>'
              '<div class="ptrack" role="slider" tabindex="0" aria-label="Posição"><i></i></div>'
              '<span class="ptime">0:00</span>'
            '</div>'
            '<p class="aud-n">%s</p>'
            '<div class="aud-x">%s</div>'
            '</div><span class="folio">%d</span>'
            % (E(p['tit']), E(p['meta']), b64aud(p['key']), E(p['nota']), tx, folio)))
    elif t == 'dedicatoria':
        out.append(sheet(
            '<div class="dedic"><p class="dd-1">Para o meu filho</p>'
            '<p class="dd-2">João Luca Soares de Andrade</p></div>',
            '', data_nav='Dedicatória'))
    elif t == 'agradecimentos':
        paras = ''.join('<p>%s</p>' % x.strip() for x in AGRADECIMENTOS.split('\n\n'))
        out.append(sheet(
            '<div class="agrad"><h2 class="ag-t">Agradecimentos</h2>%s'
            '<p class="ag-a">João José de Andrade Neto</p></div>'
            % paras, '', data_nav='Agradecimentos'))
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

/* dedicatoria e agradecimentos */
.dedic{margin:auto 0;text-align:center}
.dd-1{font-family:var(--fu);font-size:.72em;letter-spacing:.22em;text-transform:uppercase;
 color:var(--faint);margin:0 0 1.6em}
.dd-2{font-family:var(--fd);font-style:italic;font-weight:400;font-size:1.9em;line-height:1.25;
 margin:0;color:var(--ink)}
.agrad{margin:auto 0}
.ag-t{font-family:var(--fu);font-size:.7em;letter-spacing:.22em;text-transform:uppercase;
 color:var(--accent);font-weight:400;margin:0 0 1.6em}
.agrad p{font-size:1em;line-height:1.66;margin:0 0 .9em;text-align:justify;hyphens:auto}
.ag-a{font-family:var(--fd);font-style:italic;font-size:1.05em;text-align:right!important;
 color:var(--soft);margin-top:1.8em!important}

/* leitura em voz alta */
.readbtn{position:fixed;z-index:42;bottom:3.6rem;left:1.1rem;font-family:var(--fu);
 font-size:.7rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);
 background:var(--sheet);border:1px solid var(--rule);padding:.45rem .8rem;cursor:pointer;
 min-width:6.4rem}
.readbtn:hover,.readbtn:focus-visible{border-color:var(--accent);color:var(--accent);outline:none}
.readbtn[data-on="1"]{border-color:var(--accent);color:var(--accent)}
.readbtn[hidden]{display:none!important}
.reading{position:relative}
.reading::before{content:"";position:absolute;left:-1.15em;top:.22em;bottom:.22em;width:2px;
 background:var(--accent)}

/* audio */
.aud{margin:auto 0;display:flex;flex-direction:column;gap:.75em;min-height:0}
.aud-h{font-family:var(--fu);font-size:.62em;letter-spacing:.2em;text-transform:uppercase;
 color:var(--accent);margin:0}
.aud-t{font-family:var(--fd);font-style:italic;font-weight:400;font-size:1.5em;line-height:1.15;
 margin:0}
.aud-m{font-family:var(--fu);font-size:.66em;letter-spacing:.04em;color:var(--faint);margin:0}
.aud-n{font-family:var(--fu);font-size:.68em;line-height:1.55;color:var(--soft);margin:0}
.player{display:flex;align-items:center;gap:.85em;border:1px solid var(--rule);
 padding:.7em .85em;margin:.15em 0}
.pbtn{flex:none;width:2.5em;height:2.5em;border-radius:50%;border:1px solid var(--accent);
 background:transparent;color:var(--accent);cursor:pointer;display:grid;place-items:center;
 padding:0;transition:background .15s,color .15s}
.pbtn:hover,.pbtn:focus-visible{background:var(--accent);color:var(--sheet);outline:none}
.pbtn svg{width:.72em;height:.84em;fill:currentColor;display:block}
.pbtn svg[hidden]{display:none}
.ptrack{flex:1;height:3px;background:var(--rule);position:relative;cursor:pointer}
.ptrack:focus-visible{outline:1px solid var(--accent);outline-offset:4px}
.ptrack i{position:absolute;left:0;top:0;bottom:0;width:0;background:var(--accent)}
.ptime{flex:none;font-family:var(--fu);font-size:.66em;color:var(--faint);
 font-variant-numeric:tabular-nums;min-width:5.4em;text-align:right}
.aud-x{font-size:.8em;line-height:1.62;color:var(--soft);overflow-y:auto;min-height:0;
 border-top:1px solid var(--rule);padding-top:.7em;text-align:justify;hyphens:auto}
.aud-x p{margin:0 0 .65em}
.aud-x p:last-child{margin:0}

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
  if(e.target&&e.target.closest&&e.target.closest('.player')) return;
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
 window.__tc={go:go,cur:cur,leaves:leaves};
})();

/* ---- leitor de audio ---- */
(function(){
 var tocando=null;
 function mmss(t){ if(!isFinite(t))return '0:00';
  var m=Math.floor(t/60),s=Math.floor(t%60); return m+':'+(s<10?'0':'')+s; }
 Array.prototype.forEach.call(document.querySelectorAll('.player'),function(pl){
  var btn=pl.querySelector('.pbtn'), tr=pl.querySelector('.ptrack'),
      fill=tr.querySelector('i'), lab=pl.querySelector('.ptime'),
      ip=btn.querySelector('.i-play'), iz=btn.querySelector('.i-pause'), a=null;
  function make(){ if(a) return a;
   a=new Audio(pl.dataset.src); a.preload='metadata';
   a.addEventListener('loadedmetadata',pinta);
   a.addEventListener('timeupdate',pinta);
   a.addEventListener('ended',function(){ a.currentTime=0; para(); pinta(); });
   return a; }
  function pinta(){ var d=a&&isFinite(a.duration)?a.duration:0, c=a?a.currentTime:0;
   fill.style.width=(d?(c/d*100):0)+'%';
   lab.textContent=mmss(c)+(d?' / '+mmss(d):'');
   tr.setAttribute('aria-valuetext',mmss(c)); }
  function toca(){ if(tocando&&tocando!==pl) tocando.__para();
   make(); a.play(); tocando=pl;
   ip.hidden=true; iz.hidden=false; btn.setAttribute('aria-label','Pausar'); }
  function para(){ if(a) a.pause();
   ip.hidden=false; iz.hidden=true; btn.setAttribute('aria-label','Tocar');
   if(tocando===pl) tocando=null; }
  pl.__para=para;
  btn.addEventListener('click',function(){ (a&&!a.paused)?para():toca(); });
  function busca(x){ make(); var r=tr.getBoundingClientRect();
   var p=Math.min(1,Math.max(0,(x-r.left)/r.width));
   if(isFinite(a.duration)) a.currentTime=p*a.duration; pinta(); }
  tr.addEventListener('click',function(e){ busca(e.clientX); });
  tr.addEventListener('keydown',function(e){ make();
   if(e.key==='ArrowRight'){e.preventDefault();a.currentTime=Math.min(a.duration||0,a.currentTime+5);pinta();}
   else if(e.key==='ArrowLeft'){e.preventDefault();a.currentTime=Math.max(0,a.currentTime-5);pinta();}
   else if(e.key===' '||e.key==='Enter'){e.preventDefault();(a&&!a.paused)?para():toca();} });
  pinta();
 });
 /* virou a pagina, para o som */
 var stg=document.getElementById('stage');
 if(stg) stg.addEventListener('scroll',function(){
  if(!tocando) return;
  var r=tocando.getBoundingClientRect();
  if(r.bottom<0||r.top>window.innerHeight) tocando.__para();
 },{passive:true});
 window.__pararAudio=function(){ if(tocando) tocando.__para(); };
})();

/* ---- leitura em voz alta ---- */
(function(){
 var btn=document.getElementById('readbtn');
 var synth=window.speechSynthesis;
 if(!btn) return;
 if(!synth||typeof SpeechSynthesisUtterance==='undefined'){ btn.hidden=true; return; }

 var lendo=false, pedacos=[], i=0, voz=null;
 var ger=0;        /* geracao: invalida callbacks de falas canceladas */
 var virando=false;/* true enquanto a pagina vira sozinha */
 var pagina=-1;

 function acharVoz(){
  var vs=[]; try{ vs=synth.getVoices()||[]; }catch(e){ vs=[]; }
  var pt=vs.filter(function(v){ return /^pt[-_]?br/i.test(v.lang||''); });
  if(!pt.length) pt=vs.filter(function(v){ return /^pt/i.test(v.lang||''); });
  var boa=pt.filter(function(v){ return /natural|neural|online/i.test(v.name||''); });
  voz=(boa[0]||pt[0]||null);
 }
 acharVoz();
 try{ synth.addEventListener('voiceschanged',acharVoz); }catch(e){ synth.onvoiceschanged=acharVoz; }

 /* trechos curtos: o Chrome corta falas longas, e o remendo do resume() e' o
    que fazia o texto repetir. Curto resolve sem remendo. */
 function fatia(el,txt){
  txt=(txt||'').replace(/\s+/g,' ').trim();
  if(!txt) return;
  var fr=txt.split(/(?<=[.!?…:;])\s+/), buf='';
  for(var k=0;k<fr.length;k++){
   var p=fr[k];
   while(p.length>150){                       /* frase gigante, corta na virgula */
    var c=p.lastIndexOf(', ',150);
    if(c<60) c=p.lastIndexOf(' ',150);
    if(c<40) c=150;
    pedacos.push({el:el,t:p.slice(0,c+1).trim()}); p=p.slice(c+1);
   }
   if((buf+' '+p).trim().length>150 && buf){ pedacos.push({el:el,t:buf.trim()}); buf=p; }
   else { buf=(buf?buf+' ':'')+p; }
  }
  if(buf.trim()) pedacos.push({el:el,t:buf.trim()});
 }

 function monta(){
  pedacos=[];
  var leaf=window.__tc&&window.__tc.leaves[window.__tc.cur()];
  if(!leaf) return;
  var ps=leaf.querySelectorAll('.corpo p');
  if(ps.length){ Array.prototype.forEach.call(ps,function(p){ fatia(p,p.textContent); }); return; }
  var t=leaf.querySelector('.co-t');
  if(t){ fatia(t,t.textContent);
         var sy=leaf.querySelector('.co-s'); if(sy) fatia(sy,sy.textContent); return; }
  var pa=leaf.querySelector('.pa-t'); if(pa){ fatia(pa,pa.textContent); return; }
  var q=leaf.querySelector('.epig blockquote'); if(q){ fatia(q,q.textContent); return; }
  var ax=leaf.querySelector('.aud-x'); if(ax){ fatia(ax,ax.textContent); return; }
  var fc=leaf.querySelector('figcaption'); if(fc){ fatia(fc,fc.textContent); return; }
 }

 function limpaMarca(){
  Array.prototype.forEach.call(document.querySelectorAll('.reading'),function(e){
   e.classList.remove('reading'); });
 }
 function marca(el){ limpaMarca(); if(el&&el.classList) el.classList.add('reading'); }

 function fala(){
  if(!lendo) return;
  if(i>=pedacos.length){ vira(); return; }
  var g=ger, c=pedacos[i];
  marca(c.el);
  var u=new SpeechSynthesisUtterance(c.t);
  if(voz) u.voice=voz;
  u.lang='pt-BR'; u.rate=0.98; u.pitch=1;
  var seguiu=false;
  function adiante(){ if(seguiu) return; seguiu=true;
   if(g!==ger||!lendo) return;              /* fala cancelada: nao avanca */
   i++; fala(); }
  u.onend=adiante; u.onerror=adiante;
  try{ synth.speak(u); }catch(e){ parar(); }
 }

 function vira(){
  var c=window.__tc.cur();
  if(c>=window.__tc.leaves.length-1){ parar(); return; }
  virando=true; pagina=c+1;
  window.__tc.go(c+1);
  setTimeout(function(){
   virando=false;
   if(!lendo) return;
   monta(); i=0; fala();
  },620);
 }

 function comecar(){
  if(window.__pararAudio) window.__pararAudio();
  ger++; try{ synth.cancel(); }catch(e){}
  lendo=true; btn.textContent='Parar'; btn.setAttribute('data-on','1');
  pagina=window.__tc.cur(); virando=false;
  monta(); i=0;
  if(!pedacos.length){ vira(); return; }
  setTimeout(fala,80);
 }
 function parar(){
  lendo=false; ger++; btn.textContent='Ouvir'; btn.setAttribute('data-on','0');
  try{ synth.cancel(); }catch(e){}
  limpaMarca();
 }

 btn.addEventListener('click',function(){ lendo?parar():comecar(); });
 document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&lendo) parar(); });

 /* virou a pagina na mao no meio da leitura: para. Nao tenta continuar sozinho,
    porque tentar era o que fazia repetir. */
 var st=document.getElementById('stage');
 if(st) st.addEventListener('scroll',function(){
  if(!lendo||virando) return;
  var c=window.__tc.cur();
  if(c===pagina) return;
  parar();
 },{passive:true});
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
<button class="readbtn" id="readbtn" type="button" data-on="0"
        title="Lê o livro em voz alta com a voz do seu computador">Ouvir</button>
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
