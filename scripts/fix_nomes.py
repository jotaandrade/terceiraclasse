# -*- coding: utf-8 -*-
"""Acrescenta ao capitulo 4 a discussao sobre a instabilidade do nome de Santa Pandolfo."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

NOVO = u'''"""Há uma dificuldade que qualquer pessoa que mexa nesses registros conhece, e que nesta
família aparece em cheio: <strong>o nome da minha bisavó não é estável</strong>.

Nos índices de nascimento do comune ela aparece seis vezes como <em>Pandolfo Santa</em>.

Numa sétima, no registro de 1893, aparece como <em>Pandolfo Domenica</em>.

E num outro documento, como <em>Santa Pandelfa</em>.

Três grafias. Ou é a mesma mulher escrita por três escrivães diferentes, ou são duas
mulheres distintas e uma coincidência de sobrenome.""",

"""Isso não seria grave se não fosse pelo filho em questão.

O registro de 1893, o da grafia divergente, é o de um menino chamado <em>Sante
Domenico</em>.

Sante, nascido em 1893, é o homem do quadro das medalhas. É o irmão que ficou, o que
defendeu o Monte Grappa, o bisavô do Giorgio.

Se a mãe do registro de 1893 não for Santa Pandolfo, então Sante Forner não é irmão de
Rosa. É primo. E o capítulo 7 deste livro conta a história de outra pessoa.""",

"""Meu palpite é que é a mesma mulher, e o palpite tem fundamento.

Santa e Domenica são as duas nomes de calendário religioso, e nome de batismo composto
do tipo Santa Domenica, truncado de um jeito por um escrivão e de outro por outro, é o
erro mais comum que existe nesses livros. Pandolfo virando Pandelfa, com o sobrenome
feminizado, é padrão vêneto e aparece o tempo todo.

E há um detalhe que empurra na mesma direção: a criança registrada naquele ato chama-se
<em>Sante <strong>Domenico</strong></em>. O escrivão tinha a palavra Domenico na frente
dos olhos no instante em que foi preencher o campo da mãe.

Seis registros consistentes contra um divergente, e o divergente tendo, na mesma linha, a
palavra que explica o deslize.""",

"""Contra isso pesam duas coisas, e são sérias.

A primeira: no mesmo índice existem filhos de outros Vincenzo com Berton Maria, com
Boletta Maria, com Menegon Teresa e com Silvestrin Domenica. Vincenzo era nome comum
naquela vila e nada garante que houvesse um só.

A segunda é pior. Os índices que tenho <strong>não trazem o sobrenome do pai</strong>, só
o primeiro nome. E existem duas transcrições do mesmo índice, uma em planilha e outra em
PDF, que discordam entre si exatamente na linha vizinha à que me interessa: onde uma diz
Martino Giuseppe, a outra diz Valentina.

Índice é ferramenta de busca. Não é prova. Eu tinha me esquecido disso.""",

"""O que resolve não é o extrato, é o ato inteiro.

Um ato de nascimento italiano completo, ao contrário do extrato de meia página que se
pede hoje, traz a idade do pai, a profissão dele, o endereço da casa, o nome de quem foi
declarar e a idade da mãe.

Bastam duas folhas, pedidas ao Comune: o <strong>ato número 15 de 1893</strong>, o do
Sante, e o <strong>ato número 47 de 1889</strong>, o do Pietro Luigi, que é
inquestionavelmente filho de Vincenzo e Santa.

Se o pai tiver a mesma profissão e o mesmo endereço nos dois, é o mesmo homem. Se a mãe do
ato de 1893 tiver vinte e sete anos, é Santa Pandolfo, nascida em 1º de novembro de 1865.

Uma tarde de trabalho decide se o capítulo 7 deste livro é sobre um irmão ou sobre um
primo. Enquanto isso não estiver na mão, ele está escrito como irmão, que é o que a
genealogia impressa afirma, e esta página existe para que ninguém tome isso por
certeza.""",

'''

anchor = u'"""Agora olhe para Santa Pandolfo.'
assert anchor in s, 'anchor nao encontrado'
s = s.replace(anchor, NOVO + anchor, 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 4: passagem sobre as grafias do nome inserida')

# ---------------------------------------------------------- caderno de bordo
cb = os.path.join(SP, 'caderno-de-bordo.html')
c = io.open(cb, encoding='utf-8').read()
anchor2 = u'      <li><strong>As duas Angelas e as três Marias.</strong>'
novo_item = u'''      <li><strong>Sante é irmão ou primo da Rosa?</strong> A mãe aparece como <em>Pandolfo Santa</em>
      (6 vezes), <em>Pandolfo Domenica</em> (1 vez, justamente no registro de Sante em 1893) e
      <em>Santa Pandelfa</em>. Provavelmente a mesma mulher, mas os índices não têm sobrenome do pai e
      as duas transcrições existentes discordam entre si. <strong>Resolve-se pedindo os atos completos
      n. 15/1893 e n. 47/1889</strong> e comparando idade, profissão e endereço do pai e idade da mãe.
      Decide se o capítulo 7 é sobre um irmão ou um primo. <em>Capítulos 4 e 7.</em></li>
      <li><strong>Quando morreu Vincenzo Forner?</strong> A genealogia impressa dá 06/08/1862 de
      nascimento e nenhuma data de morte. Se estava vivo em 1927, despediu-se de duas filhas sabendo
      que não as veria mais. <em>Capítulos 4 e 8.</em></li>
      <li><strong>As duas Angelas e as três Marias.</strong>'''
if anchor2 in c:
    c = c.replace(anchor2, novo_item, 1)
    io.open(cb, 'w', encoding='utf-8').write(c)
    print('caderno de bordo atualizado')
else:
    print('AVISO: anchor do caderno nao encontrado')
