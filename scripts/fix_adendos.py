# -*- coding: utf-8 -*-
"""Adendos 1-3 + documento do FamilySearch.
   K  -> caps 5 e 6 (prioridade alta)
   FS -> cap 4 (Vancouver resolvido) e cap 8 (alinhamento)
"""
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


# =====================================================================
# K — cap 5: a maquina nao tinha acabado
# =====================================================================
sub(u'''"""Agora a parte que me obrigou a reescrever este capítulo depois de pesquisar melhor.

Quando Fausto Miotto embarcou, em meados dos anos 1920, essa máquina toda já não
existia.

A imigração subvencionada para o Brasil tinha sido proibida pelo governo italiano em
1902, pelo decreto que leva o nome do ministro Prinetti, e que é assunto do próximo
capítulo. As agências e os cinco mil subagentes são de 1892. O cartaz colorido na praça é
uma cena do século XIX.

Fausto nasceu em 1904. Ele nasceu depois de tudo isso acabar.""",''',
u'''"""Agora a parte que me obrigou a reescrever este capítulo duas vezes.

Na primeira versão eu escrevi que, quando Fausto Miotto embarcou, em meados dos anos
1920, essa máquina toda já não existia. Era uma frase limpa. Era falsa.

O que é verdade: a imigração subvencionada para o Brasil foi proibida pelo governo
italiano em 1902, pelo decreto que leva o nome do ministro Prinetti, e que é assunto do
próximo capítulo. As agências e os cinco mil subagentes são de 1892. O cartaz colorido na
praça é uma cena do século XIX.

Tudo isso continua de pé. E a máquina continuou funcionando mesmo assim.""",

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

"""Então a frase correta não é que a máquina tinha acabado.

É que ela já não era para gente como o Fausto.

Quem ainda vinha subsidiado em 1923 vinha recrutado, com estação, município e patrão
marcados antes do embarque, dentro de um contrato que outra pessoa assinou. Fausto veio
por conta própria, com dinheiro que a família juntou, sem patrão declarado e sem destino
determinado por ninguém.

Duas emigrações diferentes, no mesmo período, saindo do mesmo porto. E, como se vai ver,
dentro do mesmo navio.""",

"""Registro aqui uma coisa que muda o modo de ler o resto deste livro.

Os subsidiados de 1923 viajaram na <strong>terceira classe</strong>.

Não havia um convés de colono e um convés de passageiro. Havia o porão, e dentro dele
estavam misturados quem tinha comprado o bilhete e quem tinha sido recrutado com fazenda
marcada. As duas populações dormiam no mesmo lugar, comiam da mesma fila e desciam pela
mesma escada.

Quatro anos depois, Rosa Forner desceu por essa escada.

Fausto nasceu em 1904, quando o cartaz já tinha saído da praça.""",''',
 'K · cap 5, a maquina nao acabou')

# =====================================================================
# K — cap 6: cai a cadeia causal
# =====================================================================
sub(u'''Não como colono recrutado, não com passagem paga pelo Estado de São Paulo, não dentro de
um contrato assinado antes de sair. Foi por conta própria, primeiro, sozinho, do jeito
que se fazia depois de 1902: alguém vai, se estabelece, e chama.

Depois chamou a mulher.""",''',
u'''Não como colono recrutado, não com passagem paga por ninguém, não dentro de um contrato
assinado antes de sair. Foi por conta própria, primeiro, sozinho, do jeito que boa parte
da emigração vêneta passou a se fazer depois de 1902: alguém vai, se estabelece, e chama.

Isso é uma afirmação sobre ele, e não sobre o sistema. Como se viu no capítulo anterior,
em 1923 ainda saía de Gênova gente subsidiada, com patrão declarado, neste mesmo navio.
O que se pode dizer do Fausto é que ele não estava entre eles.

Depois chamou a mulher.""",''',
 'K · cap 6, afirmacao sobre ele e nao sobre o sistema')

sub(u'''"""E é por isso que Rosa Forner estava no <em>Principessa Mafalda</em>.

Não num navio fretado de imigrantes, não num transporte contratado por fazendeiro. Num
transatlântico comercial de linha regular, que levava primeira, segunda e terceira classe
na mesma viagem, com passageiros que tinham comprado bilhete.

Ela pagou para estar ali.

Junto com a irmã, com quatro sobrinhos e com um filho de um ano.""",''',
u'''"""E aqui eu preciso desfazer um raciocínio meu.

Durante muito tempo escrevi que Rosa Forner estava no <em>Principessa Mafalda</em> porque
a passagem subvencionada tinha acabado. Que o decreto de 1902 tinha empurrado esta família
para dentro de um transatlântico comercial.

Não foi isso. O documento de 1923 mostra que o transporte subsidiado ainda existia, e
existia neste navio.

O motivo é outro, é mais simples e é melhor: <strong>ela não estava sendo recrutada. Ela
estava indo encontrar o marido.</strong>""",

"""Reunião familiar não é colonização, e o Estado de São Paulo não pagava por ela.

É por isso que Rosa não aparece em nenhuma Relação de subsidiados. É por isso que a
família dela não foi encaminhada a uma fazenda com patrão declarado antes do embarque. E é
por isso que ela viajou num transatlântico de linha regular, que levava primeira, segunda
e terceira classe na mesma viagem, com passageiros que tinham comprado bilhete.

Ela pagou para estar ali.

Junto com a irmã, com quatro sobrinhos e com um filho de um ano.""",''',
 'K · cap 6, o motivo verdadeiro')

sub(u'''"""Não estou dizendo que uma lei de 1902 causou um naufrágio em 1927. Não causou.

Estou dizendo uma coisa mais estreita e mais verdadeira: uma decisão tomada em Roma,
escrita para proteger camponeses italianos de fazendeiros brasileiros, determinou em que
tipo de embarcação essa família atravessaria o oceano vinte e cinco anos depois.

Se o sistema de passagem subvencionada ainda existisse, Rosa provavelmente teria feito a
travessia em outro navio, em outra data, sob outro contrato.

História é feita disso. Uma canetada em um continente reorganiza a vida de gente que
nunca ouviu falar de quem assinou.""",''',
u'''"""Escrevi, na versão anterior deste capítulo, que uma canetada dada em Roma determinou em
que tipo de embarcação esta família atravessaria o oceano vinte e cinco anos depois.

Era uma boa frase. Não se sustenta.

O decreto de 1902 é fato, e o efeito imediato dele sobre o fluxo é fato. O que eu não posso
dizer é que ele pôs Rosa naquele navio, porque em 1923 aquele navio ainda transportava
gente subsidiada.

O que o decreto fez foi mais modesto e ainda assim grande: mudou quem podia ir sem dinheiro
e quem precisava juntar. Empurrou uma parte da emigração vêneta para o modelo de um por
vez, por conta própria, chamando os outros depois. A família Miotto cabe inteira dentro
desse modelo.

História é feita disso, e também é feita de corrigir a própria frase quando o documento
aparece.""",

"""Fica um buraco aberto, e ele é meu.

O Decreto N. 2400, de 13 de julho de 1918, citado no cabeçalho daquela Relação de 1923, é
a base legal <em>brasileira</em> do transporte subsidiado. Do lado italiano, eu não sei até
quando a proibição de 1902 continuou valendo na prática, nem se foi revogada, nem se
simplesmente deixou de ser aplicada.

Sem essa peça, este capítulo não pode afirmar que a proibição durou até 1927, e também não
pode afirmar que caiu antes.

Fica declarado assim até o documento aparecer.""",''',
 'K · cap 6, cai a cadeia causal')

# =====================================================================
# FamilySearch — cap 4: o tronco Miotto e Vancouver
# =====================================================================
sub(u'''"""Do outro lado da história estão os Miotto.

O tronco documentado começa em Jacobus Miotto, casado com Anna Fidato. Camponeses, sem
mais nada anotado. Dos filhos, quatro deixaram descendência registrada: Luigi, Giovanni,
Antonio e Giuseppe.

Registro desde já que a ligação entre esse casal e o Luigi que é pai de Fausto vem da
genealogia impressa, e não de um ato de nascimento. Falta o documento que amarra os dois.
Isso vai importar daqui a três páginas.''',
u'''"""Do outro lado da história estão os Miotto, e aqui eu preciso ser mais honesto do que fui.

Durante muito tempo escrevi que o tronco documentado desta família começa em Jacobus
Miotto, casado com Anna Fidato, camponeses, com quatro filhos que deixaram descendência:
Luigi, Giovanni, Antonio e Giuseppe.

Esse casal existe e esses quatro filhos existem. Só que eles não são, até prova em
contrário, os meus. São a família de Vancouver, e daqui a três páginas eu conto como foi
que entraram nesta árvore.

O que eu tenho documentado da linha Miotto começa e termina em um homem só: <strong>Luigi
Miotto, casado com Domenica Ganeo</strong>. Acima dele, por enquanto, não há papel
nenhum.''',
 'FS · cap 4, o tronco Miotto')

sub(u'''Não vou escolher entre as duas. Registro que existe uma sepultura em Vancouver com o
sobrenome desta família, e que ela ainda não foi visitada.

O que decide é uma folha só: o ato de nascimento de Luigi Miotto, no Comune di Monfumo,
por volta de 1874 ou 1875. Se vier com pai Giacomo e mãe Anna Fidato, o ramo canadense é
família, e Louie passa a ser irmão de Luigi e tio de Fausto, uma geração acima de onde eu
o tinha posto. Se vier outro casal, ele se desprende desta história e vai embora levando
só o sobrenome.""",''',
u'''Escrevi isso, e depois fui olhar como a hipótese tinha nascido. Achei a hora exata em que
ela entrou.""",

"""Numa árvore genealógica colaborativa da internet, o Luigi de Vancouver e o Luigi de
Monfumo eram, até pouco tempo atrás, dois perfis separados.

Em <strong>18 de novembro de 2024, às onze e vinte e um da manhã</strong>, um colaborador
que eu não conheço unificou os dois. Preservou o canadense, eliminou o de Monfumo, e deu
como motivo o texto padrão que o sistema oferece: <em>a maioria das informações de dados
vitais e de parentescos correspondem</em>.

O perfil eliminado tinha sido criado em 30 de janeiro de 2018, e trazia esposa Domenica
Ganeo, filho Fausto Miotto e a fonte brasileira anexada.

Um clique, num minuto de uma segunda-feira, e o meu bisavô passou a ter um pai que morreu
sozinho no Canadá.""",

"""Desfazer não deu. O sistema desabilita o botão quando existem edições posteriores à
fusão. Foi preciso reconstruir à mão.

E quem reconstruiu foi um documento brasileiro que estava ali o tempo todo: a
<strong>declaração de óbito do próprio Fausto</strong>, lavrada em 13 de agosto de 1979 em
São João da Boa Vista. Ela nomeia por extenso o pai e a mãe dele: <strong>Luigi Miotto e
Domenica Ganeo</strong>.

Setenta e cinco anos depois de ele nascer, do outro lado do oceano, um escrivão paulista
escreveu os dois nomes certos.

<strong>Louie Miotto morreu solteiro em Vancouver e não é pai de ninguém nesta linha.</strong>
Isso está resolvido, e a sepultura continua lá, sem ter sido visitada, agora sob outro
título: pode ser a de um tio-avô, não a de um bisavô.""",

"""O que não está resolvido é quem foi o pai do Luigi.

A mesma árvore hoje registra um <strong>Luigi Miotto nascido em 10 de abril de 1874, em
Monfumo</strong>, filho de um Giovanni Miotto e de uma Luigia Forner. A data conversa com
o ato de Maser, que lhe dá vinte e cinco anos em junho de 1900 quando ele teria vinte e
seis, e um ano de diferença numa idade declarada de cabeça é rotina naqueles livros.

Só que <strong>esses três perfis não têm nenhuma fonte anexada</strong>. Nenhum documento.
Uma data cheia como 10 de abril de 1874 costuma sair de um ato de nascimento em mãos, mas
isso é dedução minha, e dedução não é fonte.

Continua valendo a mesma folha, o ato de nascimento de Luigi Miotto no Comune di Monfumo,
1874. A diferença é que agora eu sei exatamente o que estou tentando confirmar, e sei o
nome de quem talvez já o tenha visto.""",

"""E fica a lição, que é a do capítulo inteiro.

Eu abri estas páginas dizendo que não existe uma fonte boa, existem três fontes ruins que
cruzadas chegam perto. Preciso acrescentar uma quarta, e ela é a mais perigosa das quatro,
porque não parece fonte: <strong>a árvore colaborativa</strong>.

Ela não erra por ser velha, nem por ter a tinta apagada, nem por ter tido escrivão
apressado. Erra porque qualquer pessoa, em qualquer lugar do mundo, pode juntar dois homens
num só às onze e vinte e um da manhã e seguir a vida.

E porque o erro, depois de feito, tem exatamente a mesma aparência de tudo o mais que está
ali.""",''',
 'FS · cap 4, Vancouver resolvido')

sub(u'''Uma marcada pela morte da mãe e pela guerra. A outra por uma ausência do outro lado do
mundo que eu ainda não consigo nomear com certeza.''',
u'''Uma marcada pela morte da mãe e pela guerra. Da outra eu já não sei dizer o quê: a história
do pai que atravessou o oceano caiu, e no lugar dela ficou um homem de quem eu tenho o
nome, a mulher, a data do casamento, e mais nada.''',
 'FS · cap 4, fecho sem Vancouver')

# =====================================================================
# cap 8 — alinhar com o cap 4 resolvido
# =====================================================================
sub(u'''Fausto cresceu sem o pai por perto, numa vila em que ir embora era uma das coisas que os
homens faziam. Para onde Luigi Miotto foi, e se é dele a sepultura de Vancouver, o
capítulo 4 deixa em aberto, e eu deixo também.''',
u'''Fausto cresceu numa vila em que ir embora era uma das coisas que os homens faziam. Do pai
dele, Luigi Miotto, eu tenho o casamento em Maser em 1900, e o nome repetido duas vezes,
na certidão de nascimento de 1904 e na declaração de óbito de 1979. Entre uma coisa e
outra, nada. Não é dele a sepultura de Vancouver, e é só isso que o capítulo 4 conseguiu
provar.''',
 'FS · cap 8, alinhado ao cap 4')

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d correcoes' % n[0])
