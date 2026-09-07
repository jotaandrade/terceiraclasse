# -*- coding: utf-8 -*-
"""Corrige capitulos 4 e 7 com o resultado da busca no Albo d'Oro."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

# ------------------------------------------------------------- capitulo 4
old4 = u'''"""Pietro Luigi Forner: 1889 a 1916.

Vinte e sete anos de idade, morto em 1916.

Não tenho o documento que diz onde nem como, e por isso não vou afirmar. Mas 1916 é o
segundo ano da Itália na Grande Guerra, um homem de vinte e sete anos estava em plena
idade de convocação, e a família morava a poucos quilômetros do que viraria a frente.

A hipótese óbvia é a hipótese óbvia.

O capítulo 7 deste livro conta a história do irmão dele, Sante, que foi para a guerra e
voltou com três medalhas. Vale lembrar que a mesma casa mandou pelo menos dois, e que só
um voltou.""",'''

new4 = u'''"""Pietro Luigi Forner: 1889 a 1916.

Vinte e sete anos de idade, morto no segundo ano da Itália na guerra, em plena idade de
convocação, numa família que morava a poucos quilômetros do que viraria a frente.

A hipótese óbvia se escreve sozinha. Eu escrevi.

Depois fui procurar.""",

"""O Albo d'Oro é o registro oficial dos militares italianos mortos na Primeira Guerra.
Vinte e oito volumes organizados pelo Ministério da Guerra, cerca de quinhentos e trinta
mil nomes, hoje pesquisáveis por sobrenome e por patronímico, porque naquele registro um
homem é sempre fulano <em>di</em> beltrano.

Procurei Forner. Apareceram dezesseis.

Pietro Luigi Forner, filho de Vincenzo, classe 1889, não está entre eles.

Existe um Pietro Forner de Monfumo no Albo, mas é filho de Fortunato, classe 1887, e
morreu em 1917 num hospital de Bologna, de doença. Pai diferente, ano de nascimento
diferente, ano de morte diferente. Não é ele.""",

"""Isso não prova que ele não tenha sido soldado. O Albo tem omissões conhecidas, e
existem listas complementares de caídos que ficaram de fora.

Mas prova uma coisa: a explicação fácil não tem documento por trás.

Um homem de vinte e sete anos morreu em 1916 e eu não sei por quê. Pode ter sido a guerra
sem constar em lugar nenhum. Pode ter sido tuberculose, pode ter sido acidente, pode ter
sido uma das epidemias que atravessavam aquelas vilas.

Naquele mundo, morrer aos vinte e sete não exigia guerra nenhuma.

Fica assim: em 1916 aquela casa, que já tinha perdido o pai e a mãe dois anos antes,
perdeu mais um. Do resto, não sei.""",'''

assert old4 in s, 'trecho do capitulo 4 nao encontrado'
s = s.replace(old4, new4, 1)

# ------------------------------------------------------------- capitulo 7
old7 = u'''"""Em 1916 a família recebeu a notícia que aquelas famílias recebiam.

Pietro Luigi Forner, irmão mais velho de Sante, nascido em 1889, morreu naquele ano, aos
vinte e sete.

Não tenho o documento que diz onde nem como, e já registrei isso no capítulo 4. Mas 1916
foi o segundo ano da Itália na guerra, ele tinha idade de convocação, e a hipótese óbvia
é a hipótese óbvia.

Aquela casa mandou pelo menos dois irmãos. Um voltou.""",'''

new7 = u'''"""Em 1916 morreu Pietro Luigi Forner, irmão mais velho de Sante, aos vinte e sete anos.

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
sobre isso.""",'''

assert old7 in s, 'trecho do capitulo 7 nao encontrado'
s = s.replace(old7, new7, 1)

io.open(f, 'w', encoding='utf-8').write(s)
print('capitulos 4 e 7 corrigidos com o Albo d\'Oro')

# --------------------------------------------------------- caderno de bordo
cb = os.path.join(SP, 'caderno-de-bordo.html')
c = io.open(cb, encoding='utf-8').read()
old_item = u'''      <li><strong>Óbito de Pietro Luigi Forner, 1916.</strong> Confirma ou derruba a hipótese de morte
      na guerra. <em>Capítulos 4 e 7.</em></li>'''
new_item = u'''      <li><strong>Óbito de Pietro Luigi Forner, 1916.</strong> Agora é a pergunta mais aberta do livro.
      Ele <strong>não está no Albo d'Oro</strong>, o registro oficial dos militares italianos mortos na
      Primeira Guerra (busca feita em cadutigrandeguerra.it: dezesseis Forner, nenhum filho de Vincenzo
      classe 1889). Ou não morreu como soldado, ou é omissão do Albo. Só o atto di morte do Comune
      resolve. <em>Capítulos 4 e 7, já reescritos.</em></li>'''
if old_item in c:
    c = c.replace(old_item, new_item, 1)
    io.open(cb, 'w', encoding='utf-8').write(c)
    print('caderno de bordo atualizado')
else:
    print('AVISO: item do caderno nao encontrado')
