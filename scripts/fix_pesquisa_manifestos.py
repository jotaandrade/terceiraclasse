# -*- coding: utf-8 -*-
"""Acrescenta a secao dos manifestos e atualiza a linhagem."""
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


MANIFESTOS = u'''## 10-A. Os manifestos do Principessa Mafalda (adendos 1 a 3)

**25 manifestos revisados** — Arquivo Público do Estado de São Paulo, Listas de Passageiros,
chegadas em Santos entre **24.04.1919 e 08.02.1924**.

🔴 **Nenhum contém Fausto Miotto, Rosa Forner ou os Dei Agnoli.** As datas param em 1924 e a
família atravessou em 1927. Confirma que os manifestos digitalizados deste navio cobrem só
1915-1923/24, e que a lista de 30.04.1927 está em outro conjunto.

---

### ✅ K. A imigração subvencionada ainda existia em 1923, e neste navio
**INCORPORADO nos capítulos 5 e 6 em 06.09.2026.**

Anexo à lista de **23.02.1923**, um formulário distinto dos demais, duas folhas, 67 pessoas
em dez famílias:

> RELAÇÃO dos immigrantes ITALIANOS AGRICOLTORES embarcados no Porto de GENOVA c/ o Vap.
> "PRINCIPESSA MAFALDA" sahido em 8 de FEVEREIRO de 1923 com destino SANTOS ao Estado de
> SÃO PAULO, **em virtude do Decreto N. 2400 de 13 de julho de 1918, por conta da Companhia
> Commercial de SÃO PAULO.**

Colunas: **Passagens** (1, 1/2, 1/4, 0), parentesco com o chefe, filiação, nascimento,
última residência, e **Destino declarado** → Estação, Município e **Patrão**.
Preenchidos com Chavantes, Barreiro, Fazenda Guatapará, S. Simão, e repetidamente
"Dr. Ralpho P. Silva". Ao pé: **TESTE N° 67, POSTI N° 57 1/4**.
Na lista geral do mesmo dia, a margem traz **"Subsidiados"** ao lado de dezenas de nomes.

**O que caiu.** O cap. 5 dizia *"essa máquina toda já não existia"*; o cap. 6 dizia *"não com
passagem paga pelo Estado de São Paulo"*. A máquina existia, operava neste navio, quatro anos
antes de Rosa. O Decreto Prinetti de 1902 continua fato — o que caiu foi a **cadeia causal**:
Rosa **não** viajou em transatlântico comercial *porque* a subvenção tinha acabado.

**O motivo verdadeiro, e melhor:** ela não estava sendo recrutada, estava indo encontrar o
marido. **Reunião familiar, não colonização.** Por isso não aparece em Relação de
subsidiados e por isso a família não foi encaminhada a fazenda com patrão declarado.

**Reforça o título do livro:** os subsidiados de 1923 viajaram na **terceira classe**, no
mesmo porão, ao lado de quem tinha comprado bilhete.

🔎 **[VERIFICAR]** Quando e como a proibição italiana de 1902 deixou de valer na prática para
São Paulo. O Decreto brasileiro nº 2400/1918 é a base legal do lado brasileiro. **Falta o
lado italiano.** Sem isso o cap. 6 não pode afirmar nem que a proibição durou até 1927 nem
que foi revogada. *(Está declarado como buraco aberto dentro do próprio capítulo.)*

---

### L + O + U. Dados operacionais por fonte primária → **caps. 16 a 19**

- **Tonelagem: 5.087** em todas as listas — é a arqueação **líquida**. As **9.210** das fontes
  secundárias são a **bruta**. Explicar a diferença no texto, porque o leitor vai achar as
  duas cifras e concluir que uma está errada.
- **Velocidade:** 16 nós, subindo a 17 em 1922-23. **Matrícula 410.**
- **Tripulação:** entre 251 e 302 (261-268 em 1923; 253-266 em 1923-24).
- **Comandantes:** Cav. **Vittorio E. Parodi** (1919 a maio/1922) e Cav. **Francesco
  Tarabotto** (junho/1922 a fev/1924). **Nenhum dos dois é Simone Gulì**, que comandou a
  viagem final — não resolve a idade dele (item F.3), mas dá contexto para tratá-la com margem.
- **Médicos de bordo**, em rotação alternada: Lorenzo Pignone (1921), Salvatore Vanasco
  (1921 a fev/1923), Pallega F. (abr/1923), Vallega A. (mai/1923), **Pignone Francesco**
  (jun a ago/1923), **Vallega At.** (out/1923 a fev/1924). O navio levava médico próprio,
  nomeado no manifesto.
- Em **15.06.1923** trazia **910 passageiros na terceira classe**, o maior do conjunto.

---

### N. O fluxo em uma direção só → **cap. 18**

| Data | Procedência | 1ª | 2ª | 3ª |
|---|---|---:|---:|---:|
| 17.12.1921 | Gênova | 58 | 57 | **820** |
| 21.08.1922 | Gênova | 71 | 76 | **823** |
| 23.02.1923 | Gênova | 109 | 40 | **781** |
| 03.11.1922 | Buenos Aires | 42 | 49 | **23** |
| 11.03.1923 | Buenos Aires | 14 | 27 | 196 |

Descendo da Europa, oitocentas pessoas na terceira classe. Subindo de volta, vinte e três.
**Não era um navio de passageiros que também levava imigrantes. Era um navio de imigrantes
que também levava passageiros, e só numa direção.**

⚠️ **Correção de leitura (adendo 2).** A coluna "Passageiros em Trânsito" conta quem estava
**a bordo**, não quem desembarcou em Santos — o desembarque está no **Resumo** manuscrito ao
pé de cada lista, e é muito menor (13.08.1923: cabeçalho 190 na 3ª, resumo 105 desembarques;
17.12.1921: cabeçalho 820, lista com pouco mais de 80). O restante seguia para Montevidéu e
Buenos Aires.
**Escrever "viajavam na terceira classe descendo da Europa", nunca "desembarcavam em Santos".**

➕ **Para o cap. 10:** o porão **não esvaziava em Santos**. Quem ficava assistia à maior parte
seguir viagem.

---

### O + S. A composição mudou entre 1923 e 1924 → **caps. 12 e 18**

Desembarques em Santos, terceira classe:

| 13.08.1923 | | 25.01.1924 | |
|---|---:|---|---:|
| Italianos | 65 | **Sírios** | **40** |
| Sírios | 28 | **Italianos** | **32** |
| Austríacos | 5 | Alemães | 10 |
| Armênios | 3 | Austríacos | 8 |
| Espanhóis | 2 | Espanhóis | 2 |
| Brasileiros | 2 | **Total** | **92** |

Em cinco meses, inverteu. **O Principessa Mafalda deixou de ser predominantemente um navio de
emigração italiana entre 1923 e 1924 — três anos antes da viagem da família.**
Consequência para o cap. 12: em 1927 Rosa viajava num transatlântico **multinacional de linha
regular**, não num transporte de colonos. Reforça K.

---

### ⭐ R. As listas registram o dinheiro que cada passageiro trazia
**A descoberta mais útil de todos os lotes.**

Nas folhas de terceira classe de **30.11.1923 e 25.01.1924**, as colunas impressas de bagagem
foram reaproveitadas com títulos manuscritos:

> **Bauli | Valigie | Denaro | Indirizzo**

Preenchidas assim: `1 | 1 | £ 120 | Araraquara` · `2 | 1 | £ 800 | S. Paolo` ·
`1 | 1 | £ 1.350 | Cuyabá` · `8 | 1 | £ — | S. Paolo`.

**Denaro** é o dinheiro declarado por pessoa ao desembarcar. De nada a duas mil liras; um
traço significa chegada sem recurso algum. **Indirizzo** (também grafada *Destinazione*) traz
cidade e por vezes fazenda.

**Se a lista de 30.04.1927 e a de outubro de 1927 mantiverem esse padrão, elas dirão com
quantas malas e com quanto dinheiro Rosa Forner desembarcou em Santos carregando um filho de
um ano, e para qual endereço seguiu.** Não há equivalente em nenhum outro documento do acervo.
Sustenta os caps. 10, 12 e 26 sem uma linha de reconstrução. E tira a hipótese de Grama (H.4 e
H.10) do terreno da inferência.

🔴 **Ao pedir as listas de 1927, exigir as folhas completas com todas as colunas, não apenas a
página de rosto.**

---

### T. Duas anotações de margem → **cap. 10**

**T.1. Mortes a bordo eram registradas na própria lista.** Folha da 3ª classe nº 3 de
25.01.1924, linha 92: nome riscado em vermelho e, na margem, o que se lê como
**"falecido 19/1/24"** — seis dias antes de o navio aportar. O procedimento era riscar o nome
e anotar a data. 🔎 **[VERIFICAR]** a leitura da palavra em maior resolução.

**T.2. Passageiros mudavam de classe durante a viagem.** Na mesma lista, ao lado das linhas
15, 16 e 20: **"passato in 2ª cl."** e **"passata in 2ª cl."**. Uma delas é Giannini Giovanni,
53, declarado *possidente*, viajando com a filha.
**O porão não era compartimento estanque. Quem tinha dinheiro subia durante a travessia.**
Contraria a imagem de três mundos separados por chapa de aço.

---

### M + P. Notas de busca para a lista de 30.04.1927

O formulário é padronizado: **Lista Geral de Passageiros, Inspectoria de Immigração no Porto
de Santos**, Decreto Estadual nº 1458 de 10.04.1907, Lei nº 1045 C de 27.12.1906. Colunas:
país de última residência, parentesco com o chefe, *Sabem ler?*, bagagem com marca e número
de volume, e Observações.

1. A lista de 30.04.1927 terá esse formato e deve trazer a **última residência declarada de
   Fausto**, o parentesco e a marca da bagagem.
2. **A grafia do navio varia:** PRINCIPESSA MAFALDA, Princepessa Mafalda, Prin. Mafalda,
   P. Mafalda. Provavelmente é por isso que `vapor=Mafalda` retorna zero. **Testar todas.**
3. A coluna de última residência traz **Treviso** com frequência. Em 16.10.1921 há quatro
   chefes de família com Treviso declarado — Bottesele Antonio (agricultor) e Pellegrinello
   Luigi (bracciante, três filhos) entre eles. Mesmo mundo, seis anos antes.
4. **A terceira classe vinha em cadernos separados** ("1a e 2a cl.", depois "3a classe N.1",
   "N.2", "N.3", "N.4"). Se os cadernos de 1927 estiverem catalogados como itens distintos,
   uma busca pelo navio pode devolver só a folha de primeira classe.
   🔴 **Pedir explicitamente os cadernos de terceira classe.**
5. **Passageiros riscados em vermelho** com "Sbarcato a Rio" / "Marcato a Rio" aparecem em
   quase todas as listas. **Se Fausto desembarcou no Rio, o nome dele estará riscado na lista
   de Santos, não ausente dela.** Não descartar uma lista por não achar o nome entre os válidos.
6. Os resumos ao pé confirmam que só uma fração dos desembarcados seguia para a Hospedaria.
   **A ausência de Fausto no registro de matrícula é compatível com entrada normal**, sem
   passar pelo Brás, e não indica entrada por outro porto.

---

### 🟡 Q. Banco de hipóteses — NÃO USAR NO LIVRO

**Classificação: possível, evidências insuficientes.**

Lista de 13.08.1923, caderno da 3ª classe nº 2, linhas 40-42:
**Migotto Giacomo**, capo, 51, contadino, 1 baule 2 valigie · " Giovanni, figlio, 2 ·
**Perin Teresa**, moglie, 29.

*A favor:* Perin é sobrenome de Treviso; profissão contadino; Giacomo é o nome que a árvore
atribui (sem fonte) ao pai de Luigi Miotto.
*Contra:* está escrito **Migotto**, com g, e Migotto é sobrenome vêneto próprio, não variante
de Miotto; 51 anos em 1923 põe o nascimento em ~1872 contra 1860 na árvore; o arranjo familiar
não corresponde a nada documentado nesta linha.

Só sai do banco se a copia integrale do ato de Fausto (1904) ou o ato de Luigi (Monfumo)
trouxerem um Giacomo com data compatível.

Na mesma lista, linha 47, um **Pandolfi Giuseppe**, 51, operaio. Pandolfi não é Pandolfo.
Registrado só para constar que apareceu.

---

'''

sub(u'## 11. Pendências de arquivo, por ordem de retorno',
    MANIFESTOS + u'## 11. Pendências de arquivo, por ordem de retorno',
    'secao 10-A · os manifestos')

# --- linhagem: os 11 filhos e a data do casamento de Maria Luigia -----
sub(u'''Rosa Forner × Fausto Miotto (cas. 03.12.1926)
  ├─ Enrico Miotto (10.10.1926 - 06.10.1998)
  ├─ Mafalda Miotto (n. 02.01.1937) × José Mariano Terra
  │    └─ Marta Terra (n. 06.10.1960) × Carlos A. de Andrade
  │         └─ João José de Andrade Neto (n. 1984) → João Luca (n. 2012)
  └─ Erminda (n. 10.11.1928, Grama)

Maria Luigia Forner × Angelo Dei Agnoli — Cavaso del Tomba, via Costalunga''',
u'''Rosa Forner × Fausto Miotto (cas. 03.12.1926) — ONZE filhos
  ├─  1. Enrico Miotto      10.10.1926 (Itália) - 06.10.1998 (Sorocaba)
  ├─  2. Erminda            10.11.1928 (Grama) × Lázaro Pereira de Mello, 14.06.1947
  ├─  3. Nair               10.06.1931 (reg. São Paulo) - 09.05.2017
  ├─  4. Maria Therezinha   1932 - 2017
  ├─  5. Izaira             1932 - 2021
  ├─  6. Fermino            1934 - †
  ├─  7. MAFALDA            02.01.1937 (S. J. do Rio Pardo) — VIVA
  │        × José Mariano Terra
  │        └─ Marta Terra (06.10.1960) × Carlos A. de Andrade
  │             └─ João José de Andrade Neto (1984) → João Luca (2012)
  ├─  8. Rosalia            1940 - 1941
  ├─  9. Luiz               1942 - †
  ├─ 10. Dionisio           1949 — vivo
  └─ 11. Erminda Aparecida  s/ data - †

Maria Luigia Forner × Angelo Dei Agnoli (1898-1983) — cas. 25.02.1917, CASTELCUCCO
Cavaso del Tomba, via Costalunga''',
 'linhagem · os 11 filhos')

sub(u'''       │    ├─ Rosa 24.06.1903 † 1986 × Fausto Miotto''',
u'''       │    ├─ Rosa 24.06.1903 † 28.11.1986 × Fausto Miotto (n. 05.07.1904 † 13.08.1979)''',
 'linhagem · datas de obito')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes' % n[0])
