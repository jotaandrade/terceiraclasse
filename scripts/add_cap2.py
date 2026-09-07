# -*- coding: utf-8 -*-
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

CAP2 = u'''
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

"""Luigi Forner nunca foi a lugar nenhum.

Nasceu súdito austríaco em 1817, virou italiano aos quarenta e nove anos sem sair de
casa, e foi enterrado numa terra que trocou de país debaixo dos pés dele. O filho,
Vincenzo, nasceu austríaco em 1862 e virou italiano aos quatro.

Nenhum dos dois atravessou coisa alguma. A fronteira é que atravessou os dois.

Foi a neta de Luigi, filha de Vincenzo, quem finalmente se mexeu. Ela se chamava Rosa,
nasceu em 1903, e para ela a Itália sempre tinha existido.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP2.strip() + "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 20: CAP20}", 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 2 inserido')
