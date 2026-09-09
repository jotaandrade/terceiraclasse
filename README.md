# Terceira Classe

Livro de não-ficção sobre a travessia italiana para o Brasil e o naufrágio do
**Principessa Mafalda** (25 de outubro de 1927), escrito por João José de Andrade Neto,
bisneto de duas sobreviventes.

> **Subtítulo:** *A travessia italiana para o Brasil e o naufrágio do Principessa Mafalda*
> **Epílogo:** *As Três Mafaldas* — a princesa morta em Buchenwald em 1944, o navio
> afundado em 1927, e a avó nascida em 1937 com o nome do navio.
> **Pergunta central:** por que Rosa batizou a filha com o nome do navio que quase a matou.

---

## Como o livro é gerado

⚠️ **A fonte do texto é `livro/build_livro.py`.** Os arquivos em `manuscrito/` são
**exportados** dele — editar os `.md` não altera o livro.

```bash
python livro/build_livro.py    # gera terceira-classe.html (não versionado)
python livro/export_md.py      # regenera manuscrito/ e docs/ a partir da fonte
```

---

## Estrutura

```
livro/
  build_livro.py      fonte do livro: texto, estrutura, imagens
  export_md.py        exporta manuscrito/ e docs/ em Markdown
  html2md.py          conversor HTML → Markdown usado pelo export
  img/                98 imagens em webp, embutidas no HTML em base64

manuscrito/           um .md por capítulo escrito (gerado)
docs/                 dossiê, caderno de bordo, pesquisa documental, roteiros
documentos/           fontes primárias digitalizadas
artefatos/            fontes HTML das páginas publicadas
scripts/              histórico das rodadas de correção e escrita
```

---

## Estado (08.09.2026)

| | |
|---|---|
| Capítulos | 27, em 4 livros + epílogo — I: 1-7 · II: 8-11 · III: 12-18 · IV: 19-27 |
| **Escritos** | **27 de 27 capítulos, 36.308 palavras** |
| Aparato | créditos, nota de método, fontes, créditos de imagem e índice onomástico — prontos |
| Falta | só o **epílogo**, que depende de gravar a avó Mafalda |
| Centenário do naufrágio | 25.10.2027 |

---

## Dedicatoria e agradecimentos

**Dedicatoria:** ao filho, **Joao Luca Soares de Andrade**. Fica logo depois da folha de
rosto, sozinha na pagina, sem explicacao - o cap. 2 ja diz que ele e a oitava geracao.

**Agradecimentos** (fim do livro, antes do fecho): a avo **Mafalda**, o primo **Giorgio
Forner**, a prima **Patricia Betti**, os familiares e netos, e **Deus**.

IMPORTANTE: **a pesquisa levou nove anos** (informado pelo autor em 08.09.2026). Esta dito
nos agradecimentos. O corpo do livro usa expressoes vagas de tempo ("levei anos", "passei
anos", "me tomou meses") - nenhuma contradiz, mas vale considerar tornar uma delas
explicita.

## O livro sera IMPRESSO

Decidido em 08.09.2026. Consequencia imediata: **paginas de documento sonoro sairam do
miolo** - livro impresso nao toca audio. O mecanismo continua no gerador, desligado, porque
serve ao site do centenario, que e digital. Audios preservados em `livro/audio/` e os
originais `.ogg` em `documentos/`; as falas ja estao citadas dentro dos caps. 24 e 30.

Fica valendo para o resto: o que existe so na tela - botao **Ouvir**, controle de tamanho,
sumario clicavel, botoes de virar pagina - e **ferramenta de trabalho**, nao conteudo. Nada
disso vai para o impresso, e nada disso deve influenciar decisao de texto.

## Regra das imagens

**Dentro de capitulo, so entra documento ou fotografia.** Ilustracao nao entra - e se
entrar por algum motivo, a legenda tem que dizer que e ilustracao.

**Imagem editada e permitida; esconder a edicao nao.** Vale para restauracao (a fotografia
da Rosa, no cap. 23) e para tarja (o medico na Declaracao de Obito, no cap. 26). Nos dois
casos a legenda declara o que foi feito e por que.

**Tratamento visual:** `oval` em retrato de estudio de uma pessoa, `montada` em documento,
foto de grupo e caderno. Foto de documento com data carimbada na borda fica montada, para
a dissolucao nao apagar a data.

## Regras de escrita

**Voz.** Primeira pessoa contida. O autor aparece só quando está fazendo alguma coisa —
acha o documento, liga para o Giorgio, chega na casa. O resto em terceira pessoa, no
passado.

**O narrador é o João em 2026 fazendo a pesquisa.** Ele pode dizer o que não sabe. Ele
**não** pode dizer o que escreveu antes. Passagens sobre versões anteriores do próprio
manuscrito não entram no livro.

**Conclusão nos capítulos de narrativa, demonstração no capítulo da busca.** O capítulo 4
diz *"Vincenzo e Santa tiveram dez filhos"*; a prova disso vive em
`docs/notas-cap33-a-busca.md`.

**Escreva a lacuna.** O que não foi encontrado vira parágrafo, com data e com o motivo. Num
livro de busca, o buraco declarado é enredo, não falha. Nenhuma pendência de arquivo trava
um capítulo.

**Enrico (cap. 22).** Escrever seco, sem adjetivo. Não transformar a doença dele em
metáfora. A causa registrada é neoplasia de orofaringe, não câncer de língua.

**Autorizações de nome e imagem: todas obtidas (08.09.2026).** Giorgio Forner, Mafalda
Miotto Terra, João Luca (pelos responsáveis), Patrícia Betti e a família que aparece no
caderno de imagens autorizaram o uso do nome e da imagem. O registro está na página de
créditos e na nota de método do próprio livro.

**Nome em arquivo público não se tarja.** *(08.09.2026)* A relação do vapor <em>Alhena</em> e
o livro de matrícula da Hospedaria do Brás são acervo público — aqueles nomes já estão
publicados, inclusive pelo Museu da Imigração, e reproduzi-los é o que a pesquisa histórica
faz. A tarja fica para o outro caso: dado pessoal de quem não é da família nem figura
histórica, dentro de **papel particular** — o médico da declaração de óbito.

**Patrícia Betti.** Neta da Pulcheria e bisneta de Maria Luigia. Aparece nos caps. 13, 14, 20, 21 e 25. É
fonte de boa parte da tradição oral deste projeto — o cozinheiro, o bote dos cozinheiros,
o navio de carvão e a menina que achou o pai. Creditar sempre que o material for dela.

**A cadeia oral tem dois galhos, e eles não contam a mesma coisa.** *(08.09.2026)*
O carvão e o não-reconhecimento vêm do **João Betti** (1920-2008), marido da Pulcheria,
via **Patrícia Betti** — e a cena é em **São Paulo, na Hospedaria**, não no Rio. **O
cozinheiro e a menina que acha o pai** vêm de outra prima, de outro ramo, e a Patrícia
**não os confirma**. Nunca apresentar o cozinheiro como consenso da família: atribuir e
dizer que a outra linha não tem essa lembrança.

**Cena reconstruída se declara.** *(08.09.2026)* O livro pode montar uma cena que ninguém
descreveu — a prancha em Gênova, o porão às 17h15, a porta da Hospedaria — desde que **diga
no próprio texto que está reconstruindo**, e desde que a cena seja feita só de duas coisas: o
que os documentos dão (data, nome, idade, planta do navio) e o **procedimento de época**, que
era escrito e igual para todo mundo. O que nunca entra é o que se passou dentro de alguém.
Memória do autor também não é reconstrução: se só o João viveu, só o João escreve.

**Negrito é caro.** *(08.09.2026)* Duas funções, e mais nenhuma: a **frase que é o golpe do
bloco**, e a **palavra que é a própria prova** (CHEFE, Náufragos, Espontâneos, Subsidiados,
*di*, *fu*). Nome próprio, data e número não vão em negrito. Fala de documento vai em
**itálico**. Referência de dose: um negrito a cada **200 palavras**; a um a cada 90 o negrito
para de destacar e vira textura.

**Um fato, uma vez.** *(08.09.2026)* Nome, número e depoimento entram **num capítulo só**.
A lista das sete pessoas se recita no cap. 8 (a relação de Gênova) e no cap. 10 (o capítulo
delas), e em nenhum outro. Cada depoente tem o capítulo dele: Sanfilippo nos botes, Gabassi
nos 314, Ottaviani no 22h10. Antes de repetir um fato para reforçar um argumento, procurar
onde ele já está e apontar para lá.

**O fecho não pode virar métrica.** *(08.09.2026)* A frase-martelo curta no fim do capítulo
é o melhor recurso deste livro, e se todos os capítulos a usarem o leitor aprende o padrão e
para de sentir. Um em cada cinco termina liso — num dado, numa data, no meio de um
documento.

**"E" no começo do bloco.** *(08.09.2026)* Fica onde faz trabalho: virada curta, pergunta,
continuação real de uma lista. Nos outros casos some. Referência: um bloco em nove, não um
em cinco.

**Folha de estilo.** *(08.09.2026)* Para a preparação não "consertar" o que está certo:

- **Números por extenso**, sempre. As exceções deliberadas são horas (17h15, 22h10), anos,
  números de documento e porcentagens com decimal.
- **Dei Agnoli** com D maiúsculo, inclusive quando o documento traz minúsculo.
- **Grama** na primeira ocorrência de cada parte vem como *Grama, hoje São Sebastião da
  Grama*; depois só Grama.
- **Grafia de documento** é preservada quando o documento está sendo citado (Ginneta,
  Pulgheria, Maria Luiza, Forner Rosina) e normalizada no resto do texto.
- **Itálico** para nome de navio, palavra em língua estrangeira e fala de documento.
  **Negrito** só nos dois casos da regra acima.
- **Vêneto** maiúsculo quando é a região, minúsculo quando é adjetivo.

**Fontes orais.** Não corrigir a entrevistada durante a gravação, nunca — nem data errada.
Divergência entre depoimento e documento se resolve no papel, depois.

**Não atacar e não expor ninguém.** *(regra do autor, 07.09.2026)* O livro mostra que as
testemunhas discordam; não julga qual delas mente, e não usa a vida pessoal de um depoente
para descredibilizar o que ele disse. Não insinua encobrimento sem documento. Não nomeia
pessoas vivas em episódios que as constranjam — colaboradores de árvores genealógicas,
funcionários, parentes distantes entram anônimos ou não entram.

Quando duas versões se contradizem, procurar primeiro **o que elas têm em comum** — quase
sempre existe, e quase sempre é mais forte do que a disputa.

---

## Pendências que bloqueiam publicação

A lista completa, com prazos e manifesto de arquivos, está em **`docs/04-producao.md`**. Em
uma linha cada:

1. **Gravações com Mafalda Miotto Terra** — o epílogo depende delas, e ela faz 90 em
   02.01.2027. É a única pendência sem substituto.
2. **Originais em alta resolução** — 41 das 43 imagens do miolo estão abaixo de 1.200 px no
   menor lado, e o problema está nos originais, não na conversão.
3. **Nove liberações de direito de imagem e texto**, incluindo a procedência do corpus de vinte
   depoimentos (jornal, data, página).
4. **Conflito de calendário**: a viagem a Castelcucco está marcada para o dia do lançamento.

Resolvidas em 08.09.2026: as **autorizações de nome e imagem** (todas obtidas) e a **tarja de
terceiros** (nome em arquivo público não se tarja — ver a nota de método do livro).

---

## Estratégia

1. **Site no ar em 25.10.2027**, o centenário — storytelling em scroll guiado, com fotos,
   documentos reais e a voz gravada da avó. Astro + GSAP + Lenis + Howler, sem WebGL.
2. **Viagem à Itália na mesma data**, como clímax do livro e do site.
3. **Livro em 2028**, vendido ao público que o site já captou.

**Prioridade absoluta:** gravar a avó Mafalda toda semana. Ela tem 89 anos e faz 90 em
2 de janeiro de 2027. É a única testemunha viva da cadeia oral, e o depoimento dela já foi
aferido contra documento primário.
