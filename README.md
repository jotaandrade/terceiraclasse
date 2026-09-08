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
| Capítulos | 29, em 4 livros + epílogo — I: 1-8 · II: 9-12 · III: 13-20 · IV: 21-29 |
| **Escritos** | **29 de 29 capítulos, 37.996 palavras** |
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

**Enrico (cap. 24).** Escrever seco, sem adjetivo. Não transformar a doença dele em
metáfora. A causa registrada é neoplasia de orofaringe, não câncer de língua.

**Patrícia Betti.** Neta da Pulcheria e bisneta de Maria Luigia. **Consentiu em ser
nomeada e creditada no livro (08.09.2026).** Aparece nos caps. 5, 14, 16, 22, 23 e 27. É
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

- **Procedência do corpus de depoimentos** de sobreviventes (jornal, data, página). Está
  declarada como lacuna dentro do capítulo 19.
- **Crédito do panfleto** "…In América" usado no capítulo 5 — imagem obtida na internet.
- Quatro verificações abertas, listadas em `docs/02-pesquisa-documental.md`, seção 12.

---

## Estratégia

1. **Site no ar em 25.10.2027**, o centenário — storytelling em scroll guiado, com fotos,
   documentos reais e a voz gravada da avó. Astro + GSAP + Lenis + Howler, sem WebGL.
2. **Viagem à Itália na mesma data**, como clímax do livro e do site.
3. **Livro em 2028**, vendido ao público que o site já captou.

**Prioridade absoluta:** gravar a avó Mafalda toda semana. Ela tem 89 anos e faz 90 em
2 de janeiro de 2027. É a única testemunha viva da cadeia oral, e o depoimento dela já foi
aferido contra documento primário.
