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
  img/                66 imagens em webp, embutidas no HTML em base64

manuscrito/           um .md por capítulo escrito (gerado)
docs/                 dossiê, caderno de bordo, pesquisa documental, roteiros
documentos/           fontes primárias digitalizadas
artefatos/            fontes HTML das páginas publicadas
scripts/              histórico das rodadas de correção e escrita
```

---

## Estado (07.09.2026)

| | |
|---|---|
| Capítulos planejados | 34, em 4 livros + epílogo |
| **Escritos** | **29 capítulos, 33.484 palavras** |
| Livro I | caps. 1 a 8 |
| Livro III | caps. 19 e 20 |
| Centenário do naufrágio | 25.10.2027 |

---

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

**Enrico (cap. 29).** Escrever seco, sem adjetivo. Não transformar a doença dele em
metáfora. A causa registrada é neoplasia de orofaringe, não câncer de língua.

**Patrícia Betti.** Neta da Pulcheria e bisneta de Maria Luigia. **Consentiu em ser
nomeada e creditada no livro (08.09.2026).** Aparece nos caps. 10, 21, 27, 31 e 32. É
fonte de boa parte da tradição oral deste projeto — o cozinheiro, o bote dos cozinheiros,
o navio de carvão e a menina que achou o pai. Creditar sempre que o material for dela.

**A cadeia oral tem dois galhos, e eles não contam a mesma coisa.** *(08.09.2026)*
O carvão e o não-reconhecimento vêm do **João Betti** (1920-2008), marido da Pulcheria,
via **Patrícia Betti** — e a cena é em **São Paulo, na Hospedaria**, não no Rio. **O
cozinheiro e a menina que acha o pai** vêm de outra prima, de outro ramo, e a Patrícia
**não os confirma**. Nunca apresentar o cozinheiro como consenso da família: atribuir e
dizer que a outra linha não tem essa lembrança.

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
