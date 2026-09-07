# -*- coding: utf-8 -*-
"""Pendencias, verificacoes e as inconsistencias da arvore FamilySearch."""
import io

P = r"D:\italiaminha\As Tres Mafaldas\02-pesquisa-documental.md"
s = io.open(P, encoding='utf-8').read()
n = [0]


def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
    s = s.replace(old, new, 1)
    n[0] += 1
    print('  ok  ' + label)


# --- pendencias de arquivo, reordenadas -------------------------------
sub(u'''1. **Ficha de estrangeiro de Fausto Miotto.** Arquivo Público do Estado de SP, grupo de
   imagens **007451428** e vizinhos (de onde saiu a ficha de Rino). As fichas desse conjunto
   trazem campo de **local de desembarque** — pode resolver a entrada de Fausto sem depender
   da lista de bordo. Testar as variantes **Mioto, Miotti, Miotta**.''',
u'''0. 🥇 **Mensagem a Bruno Boletta Marques pelo FamilySearch**, perguntando qual fonte
   sustenta o nascimento de Luigi Miotto em 10.04.1874 em Monfumo e a filiação Giovanni
   Miotto × Luigia Forner. **Custo zero, retorno mais alto da lista inteira.** Se ele tiver o
   atto em mãos, fecha o único elo aberto da linha Miotto.
1. **Ficha de estrangeiro de Fausto Miotto.** Arquivo Público do Estado de SP, grupo de
   imagens **007451428** e vizinhos (de onde saiu a ficha de Rino). As fichas desse conjunto
   trazem campo de **local de desembarque** — pode resolver a entrada de Fausto sem depender
   da lista de bordo. Testar as variantes **Mioto, Miotti, Miotta**.''',
 'pendencias · Bruno Boletta Marques em primeiro')

sub(u'''8. **Registros Dei Agnoli em Grama.** Se a família de Maria Luigia consta no mesmo cartório,
   as duas irmãs viveram lado a lado — e isso deixa de ser inferência a partir de um carimbo.''',
u'''8. **Registros Dei Agnoli em Grama.** Se a família de Maria Luigia consta no mesmo cartório,
   as duas irmãs viveram lado a lado — e isso deixa de ser inferência a partir de um carimbo.
9. **Listas de passageiros de 1927 (30.04 e outubro), com TODAS as colunas.** Ver seção 10-A,
   itens R e M/P: pedir as folhas completas e **os cadernos de terceira classe** como itens
   separados. É onde estão *Denaro* e *Indirizzo*.
10. **Archivio di Stato di Treviso**, que guarda a segunda via do Tribunale pós-1871 — a série
    que o FamilySearch filmou só parcialmente. Atende pesquisa genealógica por correspondência.
11. **Parrocchia di San Nicola Vescovo, Monfumo**, ou o Archivio Storico da Diocese de Treviso.
    O batismo também nomeia os pais.
12. **Atto di matrimonio de Vincenzo Forner × Santa Pandolfo** (Monfumo, 1887), que traz a
    filiação de Santa — hoje a única bisavó sem ascendência registrada.
13. **Sobrenome de solteira de Elisabetta Forner**, via atto di matrimonio de Luigi Forner.''',
 'pendencias · novas entradas')

# --- verificacoes ----------------------------------------------------
sub(u'''| 4 | Idade do comandante **Simone Gulì**: 55 (Museu da Imigração) ou 62 (fonte italiana) | cap. 20 |''',
u'''| 4 | Idade do comandante **Simone Gulì**: 55 (Museu da Imigração) ou 62 (fonte italiana) | cap. 20 |
| 5 | **Do lado italiano**, quando a proibição de 1902 deixou de valer na prática (o Decreto brasileiro 2400/1918 é só o lado de cá) | cap. 6 — já declarado como buraco no texto |
| 6 | A palavra na margem da linha 92 de 25.01.1924, lida como *"falecido 19/1/24"* | cap. 10 |''',
 'verificacoes · novas entradas')

# --- inconsistencias da arvore ---------------------------------------
sub(u'''## 13. Onde pesquisar de graça''',
u'''## 12-A. 🔴 Inconsistências da árvore FamilySearch, a corrigir lá

A árvore foi reconstruída em 06.09.2026 (ver seção 5), mas ainda carrega erros que este
acervo já refuta. Vale corrigir no FamilySearch para não voltarem por unificação.

| Na árvore | O que o acervo diz |
|---|---|
| **Vincenzo Forner † 1914** | ❌ A carta d'identità de 1940 escreve *di Vincenzo* — **pai vivo aos 77**. Data de 1914 provavelmente copiada do perfil de Santa |
| **"Vinda da família ao Brasil entre nov/1928 e jun/1931"** | ❌ **Livro 100, p. 290: Rosa e Enrico deram entrada na Hospedaria do Brás em 31.10.1927.** Erminda nasceu em Grama em 10.11.1928. A janela está errada em pelo menos um ano |
| **Imigração de Rosa lançada em 1976** | ❌ Impossível. 1976 é o ano da **ficha de estrangeiro para aposentadoria** (ver seção 10, item 4) |
| **Enrico † 07.10.1998** | 🟡 A certidão de óbito diz **06.10.1998** (quatro dias antes de completar 72). A data do FamilySearch vem da consulta de sepultados de Sorocaba. **Prevalece a certidão** |
| **Elisabetta Forner** com o sobrenome do marido | 🟡 Provavelmente o de casada. Interrompe a subida por esse ramo |
| **Angela Forner n. 1886**, casamento dos pais em 1887 | ✅ Não é erro — é o mesmo padrão da geração seguinte (Enrico nasceu 54 dias antes do casamento de Rosa e Fausto). Está no cap. 4 |
| Local de nascimento de **Erminda (1928)** em branco | ✅ **Resolvido:** Grama, pelo assento de casamento nº 660 |

**IDs úteis:** Mafalda `LTBQ-LKN` · Fausto `GGDR-8CN` · Rosa `LTB7-QSQ` · Luigi Miotto
`PQ8L-8TY` · Domenica Ganeo `LYTY-SKL` · Vincenzo `LTB7-8GS` · Santa Pandolfo `LTB7-QY8` ·
Sante `GPS5-RKL` · Maria Luigia `L5L5-3NL` · Angelo dei Agnoli `L5L5-D18` · João `LRZ9-8NX`.
Perfis em `familysearch.org/tree/person/details/<ID>`.

➕ **Verónica Miotto Amabile** (`PS3R-V8F`) passou de meia-irmã a **irmã plena** de Fausto após
a unificação de "Nina Ganeo" em Domenica Ganeo. É uma tia-avó que o livro ainda não menciona.

---

## 13. Onde pesquisar de graça''',
 'secao 12-A · inconsistencias da arvore')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes' % n[0])
