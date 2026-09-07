# -*- coding: utf-8 -*-
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

CAP8 = u'''
CAP8 = [
"""Não existe fotografia do casamento.

Não existe convite, não existe lista de convidados, não existe registro do que se comeu.
O que existe é um ano, 1926, anotado numa árvore genealógica montada quase um século
depois.

Rosa Forner tinha vinte e três anos. Fausto Miotto tinha vinte e dois.

Ela era de Monfumo, ele de Castelcucco, e entre as duas casas havia quatro quilômetros de
estrada que os dois conheciam desde sempre.""",

"""Vale olhar quem eram essas duas pessoas em 1926, porque a essa altura do livro já
sabemos.

Rosa era órfã de pai e de mãe desde os onze anos. Tinha perdido um irmão na guerra, o
Pietro Luigi, em 1916. Tinha outro irmão, o Sante, que voltou do Monte Grappa com três
medalhas e o silêncio que normalmente vem junto. Tinha sido criada, na prática, pela irmã
mais velha, Maria Luigia.

Fausto era filho de um homem que tinha atravessado o Atlântico para o Canadá e morrido em
Vancouver. Cresceu sabendo que ir embora era uma coisa que os homens da família dele
faziam.

Nenhum dos dois tinha herança para receber.""",

"""Em 10 de outubro de 1926 nasceu Enrico Miotto.

Essa data não vem de memória de família. Vem do Registro de Estrangeiros que ele assinou
em São Paulo em 1949, com nacionalidade italiana, pai Fausto Miotto, mãe Rosa Forner.

Ponha as duas informações lado a lado: casamento em 1926, filho nascido em outubro de
1926.

Se o casamento foi no começo do ano, a criança veio logo depois. Se foi mais tarde, Rosa
já estava grávida quando se casou. As duas coisas eram absolutamente corriqueiras naquele
mundo, e nenhuma das duas é assunto de ninguém.

Registro só porque o livro da paróquia tem a data exata do casamento, e um dia alguém vai
lê-la.""",

"""E aí, com o filho recém-nascido, Fausto foi embora.

Não juntos. Não a família toda num navio. Ele primeiro, sozinho.

É importante não ler isso com olhos de hoje. Não foi abandono, foi o procedimento. Depois
que o decreto de 1902 acabou com a passagem paga, emigrar virou uma operação em duas
etapas: um homem vai na frente com o dinheiro que a família conseguiu juntar, trabalha,
arruma onde morar, e então manda buscar.

Angelo dei Agnoli, casado com Maria Luigia, foi junto ou por perto. Os dois cunhados
atravessaram, e as duas irmãs ficaram.""",

"""Pense no que sobrou para Rosa Forner naquele ano.

Vinte e três anos. Um filho de meses. Um marido do outro lado do oceano, alcançável
apenas por carta, com semanas de atraso entre a pergunta e a resposta. Sem pai, sem mãe.

A casa em que ela estava não tinha adulto nenhum acima dela.

E o inverno de 1926 para 1927 no sopé do Grappa foi o inverno que sempre foi.""",

"""Quatro quilômetros dali, em Cavarzo, Maria Luigia estava fazendo a mesma coisa com
quatro crianças.

Dinetta com seis anos. Pulcheria com cinco. Dino com três. Danilo com um.

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
parados, o imposto sobre a moagem, a pelagra, os dezesseis filhos, as duas Angelas, os
cinco mil subagentes, o cônsul escrevendo de Vitória, o chicote nas fazendas, o bronze
inimigo no peito do Sante, tudo isso existe neste livro por um motivo só.

Para que quando o navio afundar, o leitor saiba exatamente o que aquelas pessoas estavam
tentando alcançar, e o que já tinham atravessado antes de chegar à água.""",
]
'''

anchor = "\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 20: CAP20}"
assert anchor in s, 'anchor CHAPTERS nao encontrado'
s = s.replace(anchor, "\n" + CAP8.strip() +
              "\n\nCHAPTERS = {1: CAP1, 2: CAP2, 3: CAP3, 4: CAP4, 5: CAP5, 6: CAP6, 7: CAP7, 8: CAP8, 20: CAP20}", 1)

# imagem de fecho da Parte I
old_img = u" 9:  [('italianos_no_barco'"
new_img = u" 8:  [('fausto','Fausto Miotto, nascido em Castelcucco em 1904. Casou-se com Rosa Forner em 1926 e partiu sozinho para o Brasil.')],\n 9:  [('italianos_no_barco'"
assert old_img in s
s = s.replace(old_img, new_img, 1)

io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 8 inserido; Parte I completa')
