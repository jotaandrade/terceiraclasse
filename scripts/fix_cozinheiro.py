# -*- coding: utf-8 -*-
"""Registra o relato oral do ramo de Maria Luigia: o cozinheiro e o navio de carvao."""
import io

P = r"D:\italiaminha\As Tres Mafaldas\02-pesquisa-documental.md"
s = io.open(P, encoding='utf-8').read()

NOVA = u'''## 8-B. ⭐ O RELATO DO COZINHEIRO — tradição oral do ramo de Maria Luigia

**Recebido em 07.09.2026, de João, que ouviu de uma prima, bisneta de Maria Luigia Forner.**

🔴 **É o único episódio do naufrágio que a família guarda em detalhe, e não existe em
documento nenhum.** Registrado aqui exatamente como foi transmitido, com as lacunas à vista.

### O relato

> A bordo havia um **cozinheiro de pele escura**. Ele gostava muito da **Pulcheria** — a
> menina, então com seis anos, brincava com todo mundo e **não saía da cozinha**.
>
> Quando o navio começou a afundar e a encher de água, no meio da correria, **Maria Luigia
> e Rosa foram se esconder no fundo de um porão**.
>
> **Foi o cozinheiro que foi atrás delas e as tirou de lá**, e as levou para o **bote dos
> cozinheiros**.
>
> Depois foram levadas para **outro vapor, que carregava carvão** — não era um navio de
> passageiros.
>
> Por causa disso, **chegaram todas sujas de carvão**, e isso dificultou muito que
> **Angelo Dei Agnoli e Fausto** as localizassem no desembarque.
>
> Quem achou Angelo foi **uma das filhas pequenas dele**.

### Por que isso importa

**É a única coisa que a cadeia oral guardou e o papel não tem.** Todos os documentos deste
projeto — o Alhena, o Livro 100, as listas — registram *que* elas sobreviveram. Nenhum
registra *como*. O relato responde a pergunta que o arquivo não responde.

E inverte a relação que o livro vinha estabelecendo: até aqui o documento corrigia a
memória (o Enrico a bordo, a gravidez que não houve). **Aqui a memória tem o que o
documento não tem.**

### ✅ Compatível com o que está documentado

O item 10-B registra que **a conta do resgate não fecha em nenhuma fonte** — nem no site
brasileiro, nem na Wikipédia —, provavelmente porque **os náufragos foram transferidos de
navio em navio no escuro e contados mais de uma vez**.

O relato descreve exatamente esse percurso: bote → um vapor → e, ao final, o **Alhena**, que
é onde o documento do Arquivo Nacional as encontra em 28.10.1927. Não há contradição.

### 🔎 Perguntas em aberto, a fechar com a prima e com a avó Mafalda

1. **Quem contou originalmente?** A frase recebida é *"como ela era a mais velha, ela
   relatou"*. Não está claro se "ela" é **Maria Luigia** ou **Gina Oliva**, a filha mais
   velha, que tinha sete anos na noite e seria a única criança do grupo com idade para
   lembrar. **A cadeia de transmissão muda o peso do relato e precisa ser fixada.**
2. **O nome da prima**, para citar a fonte.
3. **O cozinheiro tem nome na história da família?** Registrar a descrição exatamente como
   é contada.
4. **Qual era o navio de carvão?** O Alhena era holandês, da Zuid Rotterdam, de carga e
   passageiros. Entre os navios que responderam ao SOS há nomes ainda não investigados —
   Salem, Forthmouth, Frederik, **Piauhy**. Vale perguntar à prima se o nome sobreviveu.
5. **O desembarque com Angelo e Fausto foi onde?** Se as duas chegaram ao Rio no Alhena em
   28.10, e deram entrada no Brás em 31.10, o reencontro pode ter sido no Rio ou em São
   Paulo. O relato não diz.

### Destino no livro

| Elemento | Capítulo |
|---|---|
| **Pulcheria na cozinha durante a travessia**, e o cozinheiro que gostava dela | **10 — A terceira classe** |
| As duas irmãs se escondendo no fundo do porão | 21 / 22 |
| O cozinheiro que vai buscá-las e o bote dos cozinheiros | **22 — Os botes** |
| A transferência para o navio de carvão | 24 — Alhena, Mosella, Empire Star |
| Chegar cobertas de carvão; Angelo e Fausto sem reconhecê-las; a filha que o avista | **27 — O reencontro** |

🔴 **Regra de escrita para este material:** é tradição oral de terceira geração, não
documento. Entra no livro **nomeado como tal** — quem contou, para quem, quando — e não
misturado com o que os manifestos provam. É exatamente o contraste que o livro existe para
mostrar.

---

'''

a = u'## 9. Enrico Miotto (1926-1998)'
assert a in s and s.count(a) == 1
s = s.replace(a, NOVA + a, 1)
io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('secao 8-B gravada')
