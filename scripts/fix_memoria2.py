# -*- coding: utf-8 -*-
"""Memoria: corrige o erro do Antenati e registra os adendos 1-3 + FamilySearch."""
import io

P = r"C:\Users\joand\.claude\projects\D--\memory\italiaminha.md"
s = io.open(P, encoding='utf-8').read()
n = [0]


def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
    s = s.replace(old, new, 1)
    n[0] += 1
    print('  ok  ' + label)


# --- CORRECAO do erro do Antenati -------------------------------------
sub(u'''**Pesquisa gratuita** (consulado cobra em euros, isto não): **Portale Antenati** '''
    u'''(antenati.cultura.gov.it — stato civile de Treviso 1871-1941, com a imagem do ato inteiro), '''
    u'''**Hemeroteca Digital Brasileira** (memoria.bn.gov.br — jornais de 1927, é a fonte do Livro III '''
    u'''inteiro), FamilySearch, e o Giorgio indo a pé ao comune.''',
u'''**Pesquisa gratuita** (consulado cobra em euros, isto não): **Hemeroteca Digital Brasileira** '''
    u'''(memoria.bn.gov.br — jornais de 1927, é a fonte do Livro III inteiro), Museu da Imigração/SP, '''
    u'''e o Giorgio indo a pé ao comune.

🔴 **ERRO MEU, corrigido em 06.09.2026: o Portale Antenati NÃO serve para este caso.** Eu havia '''
    u'''afirmado que Treviso tinha stato civile de 1871-1941 lá. Não tem — o acervo do Archivio di '''
    u'''Stato di Treviso no Antenati é só **napoleônico, 1806-1812**. A coleção "Treviso, Stato civile: '''
    u'''Tribunale, 1871-1941" é do **FamilySearch** e é da **cidade** de Treviso, não da província; '''
    u'''nenhum Miotto de Monfumo nela. No catálogo do FamilySearch, Monfumo e Castelcucco só têm '''
    u'''**1806-1814**. **Conclusão: os atos de Monfumo e Castelcucco de 1874-1926 não estão on-line '''
    u'''em lugar nenhum** — só por pedido ao comune, ao Archivio di Stato di Treviso (atende por '''
    u'''correspondência) ou à paróquia. Não repetir a afirmação errada.''',
 'CORRECAO do erro do Antenati')

# --- Vancouver resolvido ----------------------------------------------
sub(u'''🟡 Ou é outro irmão, ou é o pai de Fausto que abandonou mulher e filho — datas não fecham (1880 vs ≈1875).''',
u'''✅ **RESOLVIDO em 06.09.2026: Louie morreu SOLTEIRO e não é pai de ninguém desta linha.** A '''
    u'''declaração de óbito do próprio Fausto (13.08.1979, São João da Boa Vista) nomeia **Luigi '''
    u'''Miotto e Domenica Ganeo** como pais. 🔴 A confusão veio de uma **unificação errada no '''
    u'''FamilySearch em 18.11.2024, às 11h21**, que fundiu o canadense no Luigi de Monfumo e eliminou '''
    u'''o perfil correto — desfeita à mão. Consequência: o "tronco Miotto" que começava em **Jacobus '''
    u'''Miotto × Anna Fidato NÃO é desta linha**, é a família de Vancouver importada em bloco. '''
    u'''🟡 Continua aberto quem foi o pai do Luigi: a árvore diz **Luigi n. 10.04.1874 em Monfumo**, '''
    u'''filho de Giovanni Miotto × Luigia Forner, mas **sem nenhuma fonte anexada** (perfis criados '''
    u'''por *Bruno Boletta Marques*, ago/2025). **Atalho mais barato de todo o projeto: mandar '''
    u'''mensagem a ele pelo FamilySearch perguntando a fonte.**''',
 'Vancouver resolvido')

# --- K: a imigracao subvencionada ainda existia em 1923 ----------------
sub(u'''## Censo de profughi, out/1918 (ISTRIT vol. 9, tabela 3, p. 60)''',
u'''## Manifestos do Principessa Mafalda (APESP) — 25 listas, 1919-1924

**Nenhuma contém Fausto, Rosa ou os Dei Agnoli** (as digitalizadas param em 1923/24; a família '''
    u'''veio em 1927).

🔴 **K, prioridade alta, já aplicada aos caps. 5 e 6:** a **imigração subvencionada ainda existia '''
    u'''em 1923, e neste navio**. Anexo à lista de 23.02.1923: *"Relação dos immigrantes ITALIANOS '''
    u'''AGRICOLTORES… em virtude do Decreto N. 2400 de 13 de julho de 1918, por conta da Companhia '''
    u'''Commercial de SÃO PAULO"*, com colunas de **Passagens (1, 1/2, 1/4)** e **Destino declarado → '''
    u'''Estação, Município e PATRÃO**. Caiu a cadeia causal do cap. 6 (Rosa **não** viajou em navio '''
    u'''comercial *porque* a subvenção acabara). **O motivo verdadeiro e melhor: ela não estava sendo '''
    u'''recrutada, estava indo encontrar o marido — reunião familiar, não colonização.** E os '''
    u'''subsidiados viajavam na **terceira classe**, no mesmo porão de quem comprou bilhete.

⭐ **Achado mais útil (R):** as folhas de 3ª classe de 1923-24 trazem colunas manuscritas '''
    u'''**Bauli | Valigie | Denaro | Indirizzo** — dinheiro declarado por pessoa e endereço de '''
    u'''destino. **Se a lista de out/1927 mantiver o padrão, dirá com quanto dinheiro e para onde '''
    u'''Rosa desembarcou.** Ao pedir as listas de 1927: exigir folhas completas + **os cadernos de '''
    u'''terceira classe separadamente**, e testar as grafias P. Mafalda / Prin. Mafalda / Princepessa. '''
    u'''Nomes riscados em vermelho = "sbarcato a Rio", não ausência.

Outros dados primários (caps. 16-19): tonelagem **5.087 líquida** (as 9.210 são brutas), 16-17 nós, '''
    u'''matrícula 410, comandantes **Parodi** (1919-1922) e **Tarabotto** (1922-1924) — nenhum é Gulì. '''
    u'''Fluxo numa direção só: ~800 na 3ª descendo da Europa, 23 subindo. ⚠️ "Passageiros em trânsito" '''
    u'''= a bordo, **não** desembarcados. Entre 1923 e 1924 os italianos viraram minoria a bordo '''
    u'''(sírios 40 × italianos 32 em jan/1924).

## Censo de profughi, out/1918 (ISTRIT vol. 9, tabela 3, p. 60)''',
 'manifestos e secao K')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes' % n[0])
