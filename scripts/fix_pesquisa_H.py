# -*- coding: utf-8 -*-
"""Atualiza 02-pesquisa-documental.md apos a incorporacao da secao H."""
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


# --- 3. Vincenzo: verificacao concluida ------------------------------
sub(u'''🔎 Confirmar *di* × *fu* numa digitalização em alta resolução.
🟡 Procurar o **ato de óbito de Vincenzo** em Castelcucco ou Monfumo, a partir de 1940.''',
u'''✅ **VERIFICADO em 06.09.2026** por leitura direta da imagem em alta resolução
(`Familia Miotto/Fotos Familiares/Sante Forner Documento.jpg`). As duas fórmulas estão na
mesma caligrafia, em linhas consecutivas, sem ambiguidade. O hedge saiu do capítulo 4.
🟡 Procurar o **ato de óbito de Vincenzo** em Castelcucco ou Monfumo, a partir de 1940.''',
 'Vincenzo · verificacao concluida')

# --- 4. Sante: dados novos da carteira -------------------------------
sub(u'''**Sante Forner é irmão de Rosa.** A pendência que existia sobre isso está encerrada.''',
u'''**Sante Forner é irmão de Rosa.** A pendência que existia sobre isso está encerrada.

✅ A mesma carteira dá a **data e o lugar exatos de nascimento**, que a genealogia impressa
não trazia: **16 de abril de 1893, em Monfumo** — antes, portanto, da mudança da família
para Castelcucco.''',
 'Sante · data exata de nascimento')

# --- nova secao: a carta d'identita ----------------------------------
sub(u'''---

## 5. 🔴 Vancouver: o que o livro pode e não pode afirmar''',
u'''### A carta d'identità de Sante Forner, por inteiro

Comune di Asolo, **8 de março de 1940**. Arquivo: `Familia Miotto/Fotos Familiares/Sante
Forner Documento.jpg`. Incorporada ao **capítulo 7** em 06.09.2026.

| Campo | Conteúdo |
|---|---|
| Cognome / Nome | Forner / Sante |
| Padre | **di** Vincenzo *(pai vivo)* |
| Madre | **fu** Pandolfo Domenica Santa *(mãe falecida)* |
| Nato il | **16 aprile 1893**, a **Monfumo** d'Asolo |
| Stato civile | Coniugato |
| Nazionalità | Italiana |
| Professione | **Bracciante** *(diarista, sem terra)* |
| Residenza | Asolo |
| Statura | **m. 1,62** |
| Connotati | occhi castani · naso regolare · bocca regolare · capelli castani · barba: — · baffi castani |
| Segni particolari | N.N. *(nenhum)* |
| Firma del titolare | *Forner Sante*, de próprio punho |
| Emissão | Asolo, lì 8-3-1940 · **A. XVIII** *(era fascista)* · assinada pelo **Podestà** |

Traz a **fotografia** dele: homem de 46 anos, paletó escuro, camisa clara, bigode,
encostado numa parede. É o único retrato civil dele no acervo.

Três meses depois dessa emissão a Itália entrou na Segunda Guerra Mundial.

---

## 5. 🔴 Vancouver: o que o livro pode e não pode afirmar''',
 'nova secao · a carta d identita')

# --- censo: tabela completa ------------------------------------------
sub(u'''**6. Censo de refugiados de guerra, outubro de 1918**, por comune de origem no *distretto
di Asolo* (volume do ISTRIT, no acervo): **Cavaso 2.795 · Maser 561 · Monfumo 307 ·
Castelcucco 39.**
Maria Luigia casou em 1917 e foi morar em Cavaso, o comune que **esvaziou**. Rosa ficou em
Castelcucco, que **quase não esvaziou**. → **caps. 1 e 7.**

---''',
u'''**6. ✅ INCORPORADO (caps. 1 e 8). Censo de refugiados de guerra, outubro de 1918.**
*Censimento dei profughi di guerra*, Ufficio Censimento do Ministero per le Terre Liberate,
Roma 1919; reelaborado no volume 9 do ISTRIT, *La linea della memoria*, **tabela 3, p. 60**
(no acervo). Conferido página por página na imagem, porque o `pdftotext` embaralha as
colunas dessa tabela.

*Distretto di Asolo — proveniência dos refugiados:*

| Comune | profughi | pop. 1911 | **%** |
|---|---:|---:|---:|
| Borso | 3.700 | 3.733 | **99,1** |
| Paderno d'Asolo | 2.161 | 2.233 | **96,8** |
| Crespano Veneto | 2.910 | 3.316 | **87,8** |
| **Cavaso** | **2.795** | 3.258 | **85,8** |
| Possagno | 1.782 | 2.180 | **81,7** |
| **Monfumo** | **307** | 1.661 | **18,5** |
| Maser | 561 | 3.818 | 14,7 |
| Altivole | 342 | 4.032 | 8,5 |
| Asolo | 259 | 6.416 | 4,0 |
| S. Zenone degli E. | 153 | 4.263 | 3,6 |
| **Castelcucco** | **39** | **1.729** | **2,3** |
| Fonte | 72 | 3.319 | 2,2 |

Os doze comuni batem: profughi ÷ população = a porcentagem impressa ao lado.

⚠️ Ressalvas que o próprio autor do volume faz: o censo conta por comune de **origem** e não
indica destino; e os totais do distretto di Asolo não fecham, por provável erro de impressão
na publicação ministerial.

**O que isso rende.** Castelcucco perdeu **39 pessoas, 2,3%** — a segunda menor taxa do
distrito. Cavaso, a quatro quilômetros, perdeu **85,8%**. Oitenta e três pontos de diferença
em quatro quilômetros: é a distância entre a montanha e o que fica atrás dela.
E **responde a lacuna que o capítulo 1 declarava em voz alta sobre Monfumo**: 18,5%, oito
vezes a taxa de Castelcucco. A vila de Rosa esvaziou bem mais que a vila de Fausto.
Maria Luigia casou em 1917 e foi morar justamente em Cavaso → **cap. 8**.

---''',
 'censo · tabela completa e incorporado')

sub(u'''**5. A carta d'identità de Sante tem o rosto e o corpo dele.** Comune di Asolo, 08.03.1940:
fotografia, statura **1,62**, olhos castanhos, cabelos castanhos, bigode castanho, sem
barba, profissão **bracciante**, casado, residente em Asolo, com a assinatura do titular.
O capítulo 7 é sobre um homem representado por um quadro na parede. **Ele também tem um
retrato.** → **cap. 7.**''',
u'''**5. ✅ INCORPORADO (cap. 7). A carta d'identità de Sante tem o rosto e o corpo dele.**
Transcrição completa na seção 4 acima. O capítulo 7 era sobre um homem representado por um
quadro na parede; agora termina com o retrato, a profissão de diarista e o carimbo do
Podestà.''',
 'carta d identita · incorporado')

# --- 12. pendencias de verificacao: cai a primeira -------------------
sub(u'''| # | O quê | Onde aparece |
|---|---|---|
| 1 | *di* × *fu* na carta d'identità de 1940 | cap. 4, cap. 8 |
| 2 | Rosa registrada como **chefe de família** na p. 290 | cap. 20 |
| 3 | Em qual porto ocorreu a avaria de máquina — Dakar ou São Vicente | cap. 20, **e o título do cap. 13** |
| 4 | Idade do comandante **Simone Gulì**: 55 (Museu da Imigração) ou 62 (fonte italiana) | cap. 20 |''',
u'''| # | O quê | Onde aparece |
|---|---|---|
| ~~1~~ | ~~*di* × *fu* na carta d'identità de 1940~~ | ✅ **verificado 06.09.2026** |
| 2 | Rosa registrada como **chefe de família** na p. 290 | cap. 20 |
| 3 | Em qual porto ocorreu a avaria de máquina — Dakar ou São Vicente | cap. 20, **e o título do cap. 13** |
| 4 | Idade do comandante **Simone Gulì**: 55 (Museu da Imigração) ou 62 (fonte italiana) | cap. 20 |''',
 'pendencias de verificacao')

# --- bibliografia: precisar a referencia do ISTRIT -------------------
sub(u'''- **Istrit, La linea della memoria 09** — *Storie dalla Grande Guerra*, vol. 2. Fonte do
  *sgombero*, do Albo d'Oro e do censo de refugiados de 1918''',
u'''- **Istrit, La linea della memoria 09** — *Storie dalla Grande Guerra*, vol. 2 (Treviso,
  2009). Fonte do *sgombero*, do Albo d'Oro e do **censo de refugiados de 1918 (tabela 3,
  p. 60)**. ⚠️ Extrair com `pdftotext` embaralha as colunas da tabela 3 — renderizar a
  página como imagem (é a página 59 no índice do PDF) e ler visualmente''',
 'bibliografia · ISTRIT preciso')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes' % n[0])
