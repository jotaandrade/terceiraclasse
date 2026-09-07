# -*- coding: utf-8 -*-
"""Adendos 1-3 + FamilySearch no arquivo de pesquisa documental."""
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


# --- 🔴 CORRECAO: o Antenati nao tem Treviso pos-1871 ------------------
sub(u'''**Portale Antenati** — <https://antenati.cultura.gov.it>
Registros civis digitalizados do Ministério da Cultura italiano. A província de **Treviso
tem stato civile de 1871 a 1941** — cobre Fausto 1904, Rosa 1903, o casamento de 1926, os
filhos de Vincenzo, os Dei Agnoli em Cavaso. Dá a **imagem da página inteira do registro**,
que é o que o *estratto* corta. *Falta confirmar Castelcucco, Monfumo, Maser e Cavaso ano a ano.*''',
u'''🔴 **Portale Antenati — CORRIGIDO em 06.09.2026. Não serve para este caso.**
<https://antenati.cultura.gov.it>
O acervo do **Archivio di Stato di Treviso no Antenati tem um fundo só: *Stato civile
napoleonico*, 1806 a 1812.** Não há stato civile italiano pós-1871 publicado para Treviso.

⚠️ Eu havia afirmado aqui que Treviso tinha 1871-1941 no Antenati. **Estava errado.** A
coleção "Italia, Treviso, Treviso. Stato civile : Tribunale, 1871-1941" existe, mas é do
**FamilySearch** e é da **cidade** de Treviso, não da província — verificado folha a folha
na capa dos filmes. Nos índices dessa coleção os Miotto aparecem em Vidor, Pederobba,
Montebelluna, Castelfranco, Roncade, Salgareda, Gorgo al Monticano e Fanzolo. **Nenhum em
Monfumo.**

**FamilySearch, catálogo por comune:** Monfumo tem uma entrada só, "Italia, Treviso,
Monfumo. Stato civile", **1806 a 1814**. Castelcucco, a mesma limitação. A paróquia de San
Nicola Vescovo de Monfumo aparece com **zero registros**.

**Conclusão prática: os atos de Monfumo e Castelcucco de 1874-1926 não estão on-line em
lugar nenhum.** Só saem por pedido ao comune, ao Archivio di Stato di Treviso (que guarda a
segunda via do Tribunale pós-1871 e atende por correspondência) ou à paróquia.

⚠️ A URL do Comune di Monfumo anexada como fonte nos perfis de Vincenzo e Santa no
FamilySearch (índice de atti di nascita 1871-1900) retorna **404** — o site foi
reestruturado desde 2018.''',
 'Antenati - correcao do erro')

# --- 5. Vancouver: resolvido ------------------------------------------
sub(u'''## 5. 🔴 Vancouver: o que o livro pode e não pode afirmar''',
u'''## 5. ✅ Vancouver: RESOLVIDO — e a causa do erro foi encontrada''',
 'titulo secao 5')

sub(u'''O capítulo 4 expõe as duas hipóteses e recusa escolher. **Os capítulos 5 e 8 afirmavam a
ida ao Canadá como fato consumado** e foram corrigidos nesta revisão.

🟡 **O que resolve:** *atto di nascita* de **Luigi Miotto, Comune di Monfumo, c. 1874-1875**.
Se vier Giacomo Miotto e Anna Fidato, o ramo canadense é família e Louie é irmão de Luigi
e tio de Fausto. Se vier outro casal, o ramo se desanexa.''',
u'''### ✅ Resolvido: Louie não é o pai de Fausto

**Ele morreu solteiro.** O informante foi o irmão John Miotto, do mesmo endereço. E a
**declaração de óbito do próprio Fausto**, de 13.08.1979, São João da Boa Vista (coleção
"Brasil, São Paulo, Registro Civil, 1925-2023"), **nomeia expressamente Luigi Miotto como
pai e Domenica Ganeo como mãe**. Documento brasileiro oficial, indexado, com imagem.

### 🔴 A causa do erro: uma unificação equivocada no FamilySearch

O histórico do perfil `LBV2-SP9` mostra que em **18.11.2024, às 11h21**, um colaborador
unificou o canadense com `LYTY-HNV` — o Luigi Miotto verdadeiro, criado em 30.01.2018 com
cônjuge Domenica Ganeo, filho Fausto e a fonte brasileira. Preservou o canadense, eliminou
o de Monfumo. Motivo registrado: o texto padrão do sistema.

O botão "Desfazer unificação" está desabilitado (houve edições posteriores). **Reconstruído
à mão em 06.09.2026.** Ver seção 5.1.

### 🟡 O que continua aberto: quem foi o pai do Luigi

A árvore hoje registra **Luigi Miotto n. 10.04.1874, Monfumo**, filho de **Giovanni Miotto
e Luigia Forner** (`PQ8L-8TY`, `PQ7H-8R6`, `PQ7H-Q4D`). A data conversa com o ato de Maser
(25 anos declarados em 06/1900; teria 26 — divergência de um ano é rotina).
⚠️ **Os três perfis não têm nenhuma fonte anexada.** Criados por **Bruno Boletta Marques**
em agosto de 2025. A data cheia sugere um atto em mãos, mas isso é dedução.

**Resolve:** *atto di nascita* de Luigi Miotto, Comune di Monfumo, 1874.
**Atalho mais barato:** mandar mensagem ao Bruno Boletta Marques pelo FamilySearch
perguntando qual é a fonte. Maior retorno pelo menor esforço da lista inteira.

### O ramo canadense, sob hipótese fraterna

Louie (`LBV2-SP9`), Jacobus/Jack (`LBV2-Z4F`), Anna Fidato/Fedato (`LBV2-JRH`), Giuseppe
1884-1971 (`LBV2-DWK`), Antonio 1887-1981 (`LBVK-9JT`), Giovanni (`LBV2-WKS`).

Pesa contra: Jacobus registrado em 1860 (sem fonte) geraria Luigi aos 14; o Giovanni da
árvore nasceu em Quinto di Treviso e morreu na França, e não descreve o John de 566 Prior
Street; a geografia do grupo é Tavagnacco (Udine) e Quinto, não Monfumo.

**Descartado com segurança:** Luigi Giuseppe Miotto (`GXLT-5N3`), n. 12.04.1875 em Riese,
† 1949 em Londrina. Já era casado com Ortensia Macor desde 1895, com filhos desde 1896.

🔴 **Consequência para o livro:** o "tronco Miotto" que começava em Jacobus + Anna Fidato
**não é desta linha** — é a família de Vancouver, importada em bloco pela unificação errada.
O capítulo 4 foi reescrito para dizer isso.''',
 'secao 5 · Vancouver resolvido')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes' % n[0])
