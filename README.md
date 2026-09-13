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
python livro/build_livro.py         # gera terceira-classe.html (não versionado)
python livro/export_md.py           # regenera manuscrito/ e docs/ a partir da fonte
python livro/export_livro_unico.py  # regenera o livro inteiro num único .md
```

---

## Estrutura

```
livro/
  build_livro.py      fonte do livro: texto, estrutura, imagens
  export_md.py        exporta manuscrito/ e docs/ em Markdown
  export_livro_unico.py  exporta o volume inteiro num único Markdown
  html2md.py          conversor HTML → Markdown usado pelo export
  img/                98 imagens em webp, embutidas no HTML em base64

terceira-classe-livro-completo.md   o volume inteiro num arquivo só (gerado)
manuscrito/           um .md por capítulo escrito (gerado)
docs/                 dossiê, caderno de bordo, pesquisa documental, roteiros,
                      produção e o caderno da Hemeroteca (05)
documentos/           fontes primárias digitalizadas
artefatos/            fontes HTML das páginas publicadas
scripts/              histórico das rodadas de correção e escrita
```

---

## Estado (12.09.2026)

| | |
|---|---|
| Capítulos | 27, em 4 livros + epílogo — I: 1-7 · II: 8-11 · III: 12-18 · IV: 19-27 |
| **Escritos** | **27 de 27 capítulos, 37.640 palavras, 615 páginas** |
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

**Direitos de imagem e texto: assumidos pelo autor (08.09.2026).** As peças sem procedência
fechada são material de época e o livro diz, em cada crédito, que a procedência não foi
localizada. A página de créditos traz a cláusula de diligência. **Nunca inventar um acervo
para preencher um crédito** — é ela que sustenta a cláusula.

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

**A cadeia oral tem três galhos, e eles não contam a mesma coisa.** *(09.09.2026)*
Dois estão no Brasil e vieram do navio. O carvão e o não-reconhecimento vêm do **João Betti**
(1920-2008), marido da Pulcheria, via **Patrícia Betti** — e a cena é em **São Paulo, na
Hospedaria**, não no Rio. **O cozinheiro e a menina que acha o pai** vêm de outra prima, de
outro ramo, e a Patrícia **não os confirma**. Nunca apresentar o cozinheiro como consenso da
família: atribuir e dizer que a outra linha não tem essa lembrança.

**O terceiro galho é o do Vêneto, e é o do Giorgio.** Ele não guardou o navio — guardou **como
morreram os homens que não embarcaram**: o avô **Sante**, na mina de Monfumo em 1947, e o
tio-avô **Pietro Luigi**, numa mina nos Estados Unidos, sem ano. Do lado de cá não havia
versão nenhuma para comparar: **ninguém aqui sabia**. Vale a mesma regra dos outros dois —
atribuir ao Giorgio, dizer que não há documento e dizer qual documento resolveria. Ver
`docs/02-pesquisa-documental.md`, seção 35.

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
3. **Procedência do corpus de vinte depoimentos** (jornal, data, página) — item de pesquisa,
   não de liberação. Já declarado como lacuna dentro do livro. *(12.09.2026: continua aberta,
   mas bloqueia menos — a Hemeroteca deu um **segundo corpus, independente e datado**, que
   confirma vários dos mesmos fatos. Ver `docs/05-hemeroteca.md`.)*
4. **Viagem a Castelcucco: abril de 2027** — decidido em 08.09.2026, para o capítulo 27 ser escrito de volta dela. O centenário, 25.10.2027, fica sendo o lançamento.
5. **Os dois documentos das minas** *(aberto em 09.09.2026)* — o papel do acidente do Sante, que
   o Giorgio diz ter em casa, e o *atto di morte* de 1947 no Comune di Monfumo. Não bloqueiam a
   leitura (os caps. 3 e 6 declaram que são depoimento), mas fecham o capítulo 6. E, antes de
   tudo, **achar de onde veio o `† 1916` do Pietro Luigi**: este acervo o repete sem procedência.

Resolvidas em 08.09.2026: as **autorizações de nome e imagem** (todas obtidas) e a **tarja de
terceiros** (nome em arquivo público não se tarja — ver a nota de método do livro).

### O que a Hemeroteca mudou no texto *(12.09.2026)*

Detalhe e transcrição em `docs/05-hemeroteca.md`; verificações abertas na seção 36 de
`docs/02-pesquisa-documental.md`.

**Aplicado:**

- **Grafia:** o paquete francês é **Formose**, não *Formosa* — caps. 16 e 17 e o índice
  onomástico.
- **Cap. 17:** "a conta do resgate não fecha em nenhuma fonte" virou "quase nenhuma conta
  do resgate fecha", e entrou a que fecha — *O Malho*: 969 recolhidos + 312 mortos = 1.281
  a bordo, com o preço de deixar o *Empire Star* e o *Avelona* fora.
- **Cap. 18:** entrou o número que mede a assimetria — **46 mortos em 288 tripulantes**, um
  em cada seis, contra mais de um em cada quatro entre os passageiros.
- **Fontes** dos caps. 17 e 18 atualizadas; a nota do 17 que dizia que nenhuma soma fechava
  foi corrigida.

### Revisão documental: o que foi corrigido *(12.09.2026)*

Um parecer externo apontou treze pontos; cada um foi conferido contra o documento, não contra
o parecer. Conferência completa na seção 37 de `docs/02-pesquisa-documental.md`.

**Aplicado (Bloco A — erros factuais):**

- 🔴 **A palavra da coluna de parentesco.** O livro dizia que Rosa e Maria entram como *CHEFE*
  na relação do *Alhena*. **Não entram: está escrito *mãi*.** A palavra *Chefe* está na mesma
  folha, em outras linhas. E a folha está reproduzida dentro do livro. ✅ Mas **no Livro 100 do
  Brás está escrito Chefe** — conferido no PDF do acervo. O cap. 19 foi reescrito para mostrar
  a mudança de palavra entre os dois registros, que vale mais que a repetição suposta.
- **A numeração do Livro 100 é por pessoa, não por família.** Rosa é o registro **19276** e
  Enrico o **19277**; Maria é **19265** e as crianças 19266 a 19269. Não existe "família 19270".
- **Cap. 18:** os cinquenta nomes do *Alhena* são **manuscritos**, não datilografados.
- **Caps. 20, 25 e 26:** o relato da Patrícia fala de **um** homem e **uma** mulher, e ela
  declara não saber quem estava na frente do Angelo. O livro dizia "Angelo e Fausto… por elas".
- **Cap. 22:** é **Declaração de Óbito**, não certidão; e o texto omitia a **neoplasia de
  orofaringe** ao listar as causas. A promessa "nada além do que eles dizem" foi ajustada: o
  estado civil vem dos documentos, o resto de quem conviveu com ele.
- **Cap. 6:** o selo é de **vinte e cinco centesimi**, direitos de secretaria do Comune di
  Asolo — não "vinte e cinco centavos".
- **Legenda da folha do *Alhena*** (cap. 17): era *Dinetta 7, Dino 4*; no documento está
  **Ginneta** e **Rino**.

**Bloco B, ainda não aplicado** — são excessos de inferência, e mexem em argumento: "sete
ficaram no Rio" (cap. 19), a prova de ausência de documentos (cap. 10), a negativa categórica
sobre a gravidez (cap. 26), a contradição do Monte Grappa (cap. 6).

**Não aplicado, e por quê:**

- **Cap. 16 — a hora.** O diário do *Formose* marca **21h45**; o livro usa 22h10. A própria
  reportagem denuncia que os relógios não batem (SOS às 15h30 contra ruptura do eixo às
  16h55), e em 1927 a hora de bordo era corrigida por longitude. Provavelmente são a mesma
  hora em dois relógios. **Não trocar sem um terceiro horário de procedência independente.**
- **Cap. 19 — os três dias.** *O Malho* diz que os náufragos seguiram para Santos no *Duca
  degli Abruzzi* "na segunda-feira", que é 31.10 — o mesmo dia do registro da Rosa no Brás,
  em São Paulo. **A data não fecha.** Não escrever antes de ler *A Tribuna*, de Santos
  (bib 153931_00, 29.10 a 02.11.1927).

---

## Estratégia

1. **Site no ar em 25.10.2027**, o centenário — storytelling em scroll guiado, com fotos,
   documentos reais e a voz gravada da avó. Astro + GSAP + Lenis + Howler, sem WebGL.
2. **Viagem à Itália na mesma data**, como clímax do livro e do site.
3. **Livro em 2028**, vendido ao público que o site já captou.

**Prioridade absoluta:** gravar a avó Mafalda toda semana. Ela tem 89 anos e faz 90 em
2 de janeiro de 2027. É a única testemunha viva da cadeia oral, e o depoimento dela já foi
aferido contra documento primário.
