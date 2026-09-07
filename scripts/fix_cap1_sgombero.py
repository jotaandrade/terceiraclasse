# -*- coding: utf-8 -*-
"""Corrige o trecho da evacuacao no capitulo 1 conforme pesquisa documental do Joao."""
import io, os
SP = os.path.dirname(os.path.abspath(__file__))
f = os.path.join(SP, 'build_livro.py')
s = io.open(f, encoding='utf-8').read()

old = u'''"""A partir de novembro de 1917 o Grappa deixou de ser uma montanha e virou uma linha
de frente.

A primeira batalha foi entre 13 e 26 de novembro. A segunda entre 11 e 21 de
dezembro. Os austro-húngaros precisavam tomar aquele maciço para descer na planície
e chegar a Veneza. Não tomaram.

O que isso significa lá embaixo, no sopé, é outra coisa: estrada tomada por comboio
militar, mula, hospital de campanha, tropa aquartelada em casa de gente, e o
barulho. Artilharia de montanha ouvida de baixo não é um estrondo, é um som
contínuo, que muda de tom conforme o vento vira.

Os civis colados na linha foram retirados e as casas ficaram com os soldados. Não
achei documento que diga se Castelcucco foi evacuada, e por isso não afirmo. O que é
certo é que a guerra ficou a poucos quilômetros de subida, por um ano.""",'''

new = u'''"""A partir de novembro de 1917 o Grappa deixou de ser uma montanha e virou uma linha
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

"""A evacuação mais ampla só veio na primavera de 1918, e aí sim alcançou Castelcucco e
outros municípios da retaguarda do Grappa.

Fausto Miotto tinha treze anos em novembro de 1917, quando a ordem foi dada e
revogada. Tinha catorze na primavera seguinte, quando ela finalmente veio para valer.

Foi essa a adolescência dele. Não a de quem foge de uma catástrofe num dia, mas a de
quem passa um ano e meio esperando para saber se vai ter que ir embora.""",

"""Duas precisões, porque elas importam.

A primeira: tudo isso é sobre Castelcucco, o vilarejo de Fausto. Rosa morava em
Monfumo, quatro quilômetros dali, outro comune, com administração própria e ordens
próprias. O que aconteceu em Monfumo naqueles mesmos meses eu ainda não sei, e não
vou presumir que tenha sido igual.

A segunda é uma correção minha. Quase todo relato geral sobre aquele front repete que
os civis que viviam colados à linha foram retirados em 1917, e eu escrevi isso antes
de verificar. É plausível e é compatível com a documentação, mas a ordem específica,
com a lista de quais localidades e quais casas, ainda não apareceu.

Então fica assim, e só assim: ordem e revogação em novembro de 1917, sgombero
facultativo e parcial em fevereiro de 1918, evacuação ampla na primavera de 1918. O
resto é provável, e está esperando documento.""",'''

assert old in s, 'trecho original do capitulo 1 nao encontrado'
s = s.replace(old, new, 1)
io.open(f, 'w', encoding='utf-8').write(s)
print('capitulo 1 corrigido: sgombero de Castelcucco')

# ------------------------------------------------ caderno de bordo
cb = os.path.join(SP, 'caderno-de-bordo.html')
c = io.open(cb, encoding='utf-8').read()
old_item = u'''      <li><strong>Castelcucco foi evacuada em 1917?</strong> Os civis colados à linha foram retirados,
      mas não achei documento sobre o comune. Arquivo comunal ou histórias locais do Grappa.
      <em>Capítulo 1.</em></li>'''
new_item = u'''      <li><strong>RESOLVIDO. O sgombero de Castelcucco.</strong> Ordem de evacuação em novembro de 1917,
      revogada em poucas horas; vilarejo habitado durante o inverno; sgombero <em>facoltativo e parziale</em>
      na documentação da Prefettura di Treviso em 27 de fevereiro de 1918; evacuação ampla na primavera de
      1918. Capítulo 1 reescrito com essa gradação. <em>Pesquisa do autor.</em></li>
      <li><strong>E Monfumo?</strong> Rosa morava em outro comune, a quatro quilômetros, com ordens
      próprias. O que aconteceu lá em 1917 e 1918 continua desconhecido. <em>Capítulo 1.</em></li>
      <li><strong>A retirada dos civis colados à linha em 1917.</strong> Plausível e compatível com a
      documentação, mas falta a ordem específica com a lista de localidades e casas atingidas. Não usar
      como fato. <em>Capítulo 1.</em></li>'''
if old_item in c:
    c = c.replace(old_item, new_item, 1)
    io.open(cb, 'w', encoding='utf-8').write(c)
    print('caderno de bordo atualizado')
else:
    print('AVISO: item do caderno nao encontrado')
