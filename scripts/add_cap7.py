# -*- coding: utf-8 -*-
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

CAP7 = u'''
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

Filho de Vincenzo Forner e Santa Pandolfo. Quarto na lista dos dezesseis. Irmão mais
velho de Rosa, a que atravessaria o Atlântico dez anos depois de tudo isso terminar.

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
manuais de história não registram: o pai e a mãe tinham morrido no ano anterior, em
1914. Rosa tinha doze anos. O caçula tinha dois.

Ele saiu de uma casa que já estava órfã.""",

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

"""Em 1916 a família recebeu a notícia que aquelas famílias recebiam.

Pietro Luigi Forner, irmão mais velho de Sante, nascido em 1889, morreu naquele ano, aos
vinte e sete.

Não tenho o documento que diz onde nem como, e já registrei isso no capítulo 4. Mas 1916
foi o segundo ano da Itália na guerra, ele tinha idade de convocação, e a hipótese óbvia
é a hipótese óbvia.

Aquela casa mandou pelo menos dois irmãos. Um voltou.""",

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

Essa é a medalha que importa. E é a que tem um documento associado que ainda pode ser
encontrado.""",

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

As barras são a folha de serviço dele, em metal, na parede da casa do Giorgio.

Se a fotografia do quadro tiver resolução suficiente, ou se alguém puder tirar uma nova
de perto, dá para contar as barras e ler os anos. Isso diz, sem precisar de arquivo
nenhum, em quantas campanhas Sante Forner esteve e quais foram.

É a pesquisa mais barata deste livro inteiro e ainda não foi feita.""",

"""A terceira medalha eu não consigo identificar pela descrição.

A família a chama de medalha de campanha. Pode ser a Medalha Interaliada da Vitória, que
os países vencedores emitiram em versões nacionais a partir de 1922, pode ser uma
comemorativa da unidade, pode ser outra coisa.

Fica registrado como não identificado, porque inventar aqui seria fácil e seria errado.
Uma foto frontal do quadro, com luz e sem reflexo, resolve em cinco minutos para quem
entende de numismática militar italiana.""",

"""Sante Forner voltou.

Casou, teve filhos, e continuou onde sempre esteve. Leo, Delfina e Galliano são dele. De
Galliano veio Giorgio, que hoje mora na mesma região, conhece a história inteira, e é
quem guarda o quadro.

Morreu em 1947, aos cinquenta e quatro anos.

Nunca emigrou. Nunca viu o Brasil. E é quase certo que nunca voltou a ver a irmã Rosa
depois de 1927, porque ninguém naquela condição atravessava o Atlântico duas vezes.""",

"""Repare no que ficou de cada lado.

O ramo que partiu tem fotografias, documentos de imigração, uma certidão de óbito em
Sorocaba e a lembrança de uma senhora de oitenta e nove anos.

O ramo que ficou tem um quadro na parede, com três medalhas e uma Vitória alada de
bronze inimigo.

Nenhum dos dois lados escapou. Um enfrentou o Atlântico, o outro enfrentou o Grappa. A
diferença é que um dos dois foi obrigado a levar tudo o que tinha numa mala de madeira, e
por isso quase nada sobrou.

Por isso este capítulo existe. Porque o objeto que melhor conta essa família nunca esteve
no Brasil.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP7.strip() +
              "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 20: CAP20}", 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 7 inserido')
