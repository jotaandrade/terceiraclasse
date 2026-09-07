# -*- coding: utf-8 -*-
"""Segunda rodada: propaga a revisao de 06.09.2026 ao dossie e ao caderno."""
import io, os

OLD = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad"
n = [0]


def fix(path, pairs):
    p = os.path.join(OLD, path)
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        assert old in s, 'NAO ACHOU em %s: %s' % (path, label)
        assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
        s = s.replace(old, new, 1)
        n[0] += 1
        print('  ok  ' + label)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)


# =====================================================================
fix('caderno-de-bordo.html', [

    # 1. Os obitos de 1914 -> Vincenzo estava vivo
    (u'''      <li><strong>Óbitos de 1914: Vincenzo Forner e Santa Pandolfo.</strong> Data e causa. É o item mais
      importante da lista inteira, porque a morte dos dois no mesmo ano é o que torna Rosa órfã aos onze
      e reescreve a cena da partida. Forte, provável e não confirmado. <em>Capítulo 4.</em></li>''',
     u'''      <li><strong>RESOLVIDO EM PARTE. Óbito de Santa Pandolfo, 1914.</strong> Data e causa continuam
      valendo a pena. O que caiu foi a outra metade: <strong>Vincenzo não morreu em 1914</strong>. A
      <em>carta d'identità</em> de Sante, Comune di Asolo, 08.03.1940, escreve <em>di Vincenzo</em> e
      <em>fu Pandolfo Domenica Santa</em> em linhas consecutivas. Em documento italiano <em>di</em> é pai
      vivo e <em>fu</em> é falecido. Rosa não saiu da Itália órfã dos dois. <em>Capítulos 4 e 8,
      reescritos.</em></li>''',
     'caderno · obitos de 1914'),

    # 2. Sante irmao ou primo -> resolvido
    (u'''      <li><strong>Sante é irmão ou primo da Rosa?</strong> A mãe aparece como <em>Pandolfo Santa</em>
      (6 vezes), <em>Pandolfo Domenica</em> (1 vez, justamente no registro de Sante em 1893) e
      <em>Santa Pandelfa</em>. Provavelmente a mesma mulher, mas os índices não têm sobrenome do pai e
      as duas transcrições existentes discordam entre si. <strong>Resolve-se pedindo os atos completos
      n. 15/1893 e n. 47/1889</strong> e comparando idade, profissão e endereço do pai e idade da mãe.
      Decide se o capítulo 7 é sobre um irmão ou um primo. <em>Capítulos 4 e 7.</em></li>''',
     u'''      <li><strong>RESOLVIDO. Sante é irmão da Rosa.</strong> A mãe aparecia como <em>Pandolfo Santa</em>
      (6 vezes), <em>Pandolfo Domenica</em> (1 vez, justamente no registro de Sante em 1893) e
      <em>Santa Pandelfa</em>. A <em>carta d'identità</em> de 1940 registra o nome dela por extenso:
      <strong>Pandolfo Domenica Santa</strong>. Dois prenomes, uma mulher só, exatamente como o capítulo 4
      supôs. O registro de 1893 não é de outro casal. Os atos n. 15/1893 e n. 47/1889 continuam valendo
      pelo endereço e pela profissão, mas não decidem mais nada. <em>Capítulos 4 e 7.</em></li>''',
     'caderno · Sante irmao, resolvido'),

    # 3. Quando morreu Vincenzo
    (u'''      <li><strong>Quando morreu Vincenzo Forner?</strong> A genealogia impressa dá 06/08/1862 de
      nascimento e nenhuma data de morte. Se estava vivo em 1927, despediu-se de duas filhas sabendo
      que não as veria mais. <em>Capítulos 4 e 8.</em></li>''',
     u'''      <li><strong>Quando morreu Vincenzo Forner?</strong> A pergunta mudou de forma. Ele estava vivo em
      março de 1940, aos 77 anos, segundo a carta d'identità do filho. Então despediu-se mesmo das duas
      filhas em 1927, aos 65. Falta o <strong>atto di morte, a partir de 1940</strong>, em Castelcucco ou
      Monfumo. <em>Capítulos 4 e 8.</em></li>''',
     'caderno · quando morreu Vincenzo'),

    # 4. As duas Angelas
    (u'''      <li><strong>As duas Angelas e as três Marias.</strong> Óbitos infantis entre 1886 e 1907 confirmam
      a leitura de nome repassado depois da morte de uma criança. <em>Capítulo 4.</em></li>''',
     u'''      <li><strong>CAIU. As duas Angelas eram primas, não irmãs.</strong> A segunda fileira do quadro de
      <em>Storia di Castelcucco</em> é de Abele Alessandro e Cadonà Maria Teresa, não de Vincenzo. Angela
      de 1886 é de uma casa, Angela de 1898 é da outra. O costume de repassar o nome de uma criança morta
      existe, mas esta família deixou de servir de exemplo. As três Marias continuam de pé como suspeita.
      <em>Capítulo 4, reescrito.</em></li>''',
     'caderno · as duas Angelas'),

    # 5. contagem de pendencias
    (u'''      Os oito capítulos escritos deixam catorze pontos marcados no texto como não confirmados.''',
     u'''      Os oito capítulos escritos deixavam catorze pontos marcados no texto como não confirmados.
      A revisão de 6 de setembro de 2026 fechou três e derrubou um.''',
     'caderno · contagem de pendencias'),
])

# =====================================================================
fix('tres-mafaldas.html', [

    # Cavaso del Tomba, Gina, Rino
    (u'''        Família 19260, linha 5: <strong>Forner Maria, 31, chefe, residência Cavarzo</strong>, com Dinetta 7,
        Pulcheria 6, Dino 4 e Danilo 2. Registradas como Forner, não como Agnoli, que é por que ninguém
        as encontrava.''',
     u'''        Família 19260, linha 5: <strong>Forner Maria, 31, residência Cavaso del Tomba</strong>, com Gina 7,
        Pulcheria 6, Rino 4 e Danilo 2. Registradas como Forner, não como Dei Agnoli, que é por que ninguém
        as encontrava. <em>Cavarzo</em> não existe: é Cavaso del Tomba. <em>Dinetta</em> é Gina Oliva,
        nascida em 28.03.1920, e <em>Dino</em> é Rino, nascido em 26.01.1923.''',
     'dossie · Cavaso del Tomba, Gina, Rino'),

    # chefe de familia -> sinalizado
    (u'''        Família 19270, linha 6: <strong>Forner Rosa, 24, chefe, última residência Castelcucco.</strong>
        Linha 7: <strong>Enrico, 1 ano, filho.</strong><br>''',
     u'''        Família 19270: <strong>Forner Rosa, 24, última residência Castelcucco</strong>, e
        <strong>Enrico, 1 ano, filho.</strong> A coluna de parentesco parece registrar Rosa como chefe da
        própria família, mas a digitalização disponível não permite afirmar isso com segurança —
        <strong>conferir em alta resolução antes de usar no texto.</strong><br>''',
     'dossie · chefe de familia sinalizado'),

    # Dakar no Parte III
    (u'''            <span class="pd">1908 a 1928. Construção, o batismo com o nome da princesa, os anos de glamour,
            a decadência, as falhas mecânicas, a parada em Dakar. A viagem final e quem estava a bordo.''',
     u'''            <span class="pd">1908 a 1928. Construção, o batismo com o nome da princesa, os anos de glamour,
            a decadência, as falhas mecânicas e a escala africana — Dakar aparece na rota habitual, mas o que
            as fontes registram da última viagem é a saída de São Vicente, Cabo Verde, em 18.10.1927.
            A viagem final e quem estava a bordo.''',
     'dossie · escala africana sinalizada'),

    # cena do mapa
    (u'''<div class="sc"><div><b>A travessia</b><span>Mapa animado: Gênova, Dakar, Abrolhos. Os dias correndo.</span></div></div>''',
     u'''<div class="sc"><div><b>A travessia</b><span>Mapa animado: Gênova, Cabo Verde, Abrolhos. Os dias correndo.</span></div></div>''',
     'dossie · cena do mapa'),
])

print('\n%d correcoes' % n[0])
