# -*- coding: utf-8 -*-
"""Capitulo 10 — A terceira classe."""
import io

SRC = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad\build_livro.py"
s = io.open(SRC, encoding='utf-8').read()

CAP10 = u'''CAP10 = [
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
em jornal. É lembrança de família, contada pela própria Pulcheria, e chegou até mim por uma
prima, bisneta de Maria Luigia.

Três elos, e o primeiro deles é uma menina de seis anos que estava lá.""",

"""Guarde esse cozinheiro.

Daqui a onze capítulos, quando o navio estiver inclinado e cheio de água e as duas irmãs
tiverem se escondido no fundo de um porão, é ele que vai descer atrás delas.

O papel de repartição registrou o dinheiro, a bagagem, o destino e a morte daquela gente.

Não registrou isso.""",
]

'''

anchor = u'CAP19 = ['
assert anchor in s and s.count(anchor) == 1
s = s.replace(anchor, CAP10 + anchor, 1)

old = u'9: CAP9, 19: CAP19, 20: CAP20}'
new = u'9: CAP9, 10: CAP10, 19: CAP19, 20: CAP20}'
assert old in s
s = s.replace(old, new, 1)

# a declaracao de procedencia migra para o cap. 10; o 19 usa direto
a19 = u'''"""E aqui eu preciso dizer de onde vem quase tudo o que vem a seguir.

Nos dias seguintes ao naufrágio, jornais da Argentina e do Brasil entrevistaram dezenas de
sobreviventes. Vinte desses depoimentos chegaram até mim, em tradução, com nome, idade e
procedência de cada depoente.

São a melhor fonte que existe sobre esta travessia. São, na prática, a <em>única</em> fonte
sobre o que se passou dentro daquele navio.

Ainda não localizei o jornal, a data e a página de cada um. Estou atrás. Enquanto não achar,
uso os depoimentos e digo, toda vez, o que eles são: relatos colhidos por repórteres, poucos
dias depois, de gente que tinha acabado de sair da água.

Isso não é pouco. E não é prova.""",

'''
assert a19 in s, 'NAO ACHOU a declaracao no cap 19'
s = s.replace(a19, u'', 1)

io.open(SRC, 'w', encoding='utf-8', newline='\n').write(s)
print('CAP10 inserido; declaracao de procedencia migrada do 19 para o 10')
