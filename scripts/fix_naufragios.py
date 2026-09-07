# -*- coding: utf-8 -*-
"""Registra naufragiosdobrasil.com.br como fonte de pistas, e o conflito de numeros."""
import io

P = r"D:\italiaminha\As Tres Mafaldas\02-pesquisa-documental.md"
s = io.open(P, encoding='utf-8').read()

NOVA = u'''## 10-B. naufragiosdobrasil.com.br — fonte de PISTAS, não de números

<https://www.naufragiosdobrasil.com.br/naufragio/principessa-mafalda/> · consultado 06.09.2026

🔴 **Não usar os números deste site.** Ele diverge do livro em praticamente todos os dados de
cabeçalho, e a Wikipédia em inglês — cruzada em 06.09.2026 — **concorda com o livro, não com
ele**.

| Dado | **Livro** | Wikipédia | naufragiosdobrasil |
|---|---|---|---|
| Saída de Gênova | **11.10.1927** | 11.10.1927 ✅ | 3.10.1927 ❌ |
| Passageiros + tripulação | **971 + 288** | 971 + 288 ✅ | 993 + 288 ❌ |
| Rompimento do eixo | **17h15** | ~17h15 ✅ | 16h20 ❌ |
| Afundamento | **22h10** | 22h10 ✅ | 21h14 ❌ |
| Mortos | **314** | 314 ✅ | 272 ❌ |

**Três títulos de capítulo dependiam disso** — cap. 20 "17h15", cap. 23 "22h10" e cap. 25
"Os 314". Todos os três **permanecem**.

### Por que o site não é confiável nos números

A aritmética dele não fecha. Ele lista resgatados: Empire Star 146, Formosa 111, Athenas 331,
Mossela 55, Alhena 331, Avelona 217, Rosetti 85 = **1.276 resgatados**. Somados aos 272 mortos
que ele próprio dá, resultam **1.548 pessoas** num navio que, segundo ele, levava 1.281.
Além disso *Athenas* e *Alhena* são quase certamente **o mesmo navio contado duas vezes**, com
o mesmo número em ambas as linhas.

⚠️ **A Wikipédia também não fecha:** Alhena 450, Avelona 300, Empire Star 202, Formosa 151,
Rosetti 122, Moselle 49 = **1.274 resgatados** + 314 mortos = **1.588**, contra 1.259 a bordo.

➕ **Isso é material do capítulo 24.** *A conta do resgate não fecha em nenhuma fonte* — muito
provavelmente porque náufragos foram transferidos de navio em navio no escuro e contados mais
de uma vez. É um fato sobre a noite, não um defeito das fontes.

### O que o site tem de aproveitável (pistas, a confirmar)

- **Barcelona como escala**, com atraso de cerca de um dia por problema mecânico. A Wikipédia
  confirma. **O livro não menciona Barcelona.** → caps. 19 e 20
- **São Vicente (Cabo Verde) como parada emergencial** — reforça a hedge do item F.2 contra
  Dakar
- 🔴 **"Desde a véspera do sinistro o vapor navegava adernado"**, com as bombas fazendo o navio
  adernar de **7º a 10º**. Se confirmado, muda o cap. 19: o navio já estava tombado *antes* do
  eixo partir → caps. 19 e 21
- **Banheiros e refrigeração com mau funcionamento** na travessia → cap. 19
- **24.10, às 13h: apitos de sirene**, exercício de incêndio. Véspera do naufrágio → cap. 19
- **SOS às 19h15** (o site) contra **17h35** (Wikipédia). 🔎 Conflito não resolvido
- **Lista ampliada de navios que responderam por telegrama:** Rossetti, Formosa, Alhena, Empire
  Star, Avelona, Mosella, **Salem, Forthmouth, Frederik, Piauhy**. O cap. 24 hoje se chama
  "Alhena, Mosella, Empire Star" — **foram mais de três**
- Sobreviventes relatando **ataques de tubarão** → cap. 22

### 🔎 NOVA VERIFICAÇÃO: a posição do naufrágio

As três fontes dão coordenadas e distâncias diferentes, e isso afeta **dois pontos já escritos**.

| Fonte | Coordenadas | Distância declarada |
|---|---|---|
| Wikipédia | 16°56′S 37°46′W | 130 km da costa |
| naufragiosdobrasil | 16°45′S 37°41′W | 75 milhas de Porto Seguro; 80 milhas **NW** dos Abrolhos |
| Livro (cap. 20) | — | ~70 km **a leste** dos Abrolhos, que ficam a ~70 km da costa |

🔴 **Dois problemas.** (1) O arquipélago dos Abrolhos fica em ~17°58′S 38°42′W; um naufrágio em
16°56′S 37°46′W está a **nordeste** dele, não a leste nem a noroeste, e a cerca de **150 km**,
não 70. (2) O cálculo do pôr do sol do item F.5 usou **latitude 17°54′S**, que não é nenhuma das
coordenadas em circulação — a diferença até 16°56′S move o pôr do sol em dois ou três minutos,
pouco, mas a latitude citada precisa ser a correta.

**Não alterar o cap. 20 ainda.** Resolver com a Hemeroteca (os jornais de 1927 dão a posição
telegrafada) antes de mexer em F.4 e F.5.

---

'''

a = u'## 11. Pendências de arquivo, por ordem de retorno'
assert a in s and s.count(a) == 1
s = s.replace(a, NOVA + a, 1)

b = u'''| 6 | A palavra na margem da linha 92 de 25.01.1924, lida como *"falecido 19/1/24"* | cap. 10 |'''
assert b in s and s.count(b) == 1
s = s.replace(b, b + u'''
| 7 | **A posição do naufrágio** e a distância real aos Abrolhos e à costa (ver 10-B) | cap. 20, itens F.4 e F.5 |
| 8 | Hora do **SOS**: 17h35 (Wikipédia) ou 19h15 (naufragiosdobrasil) | caps. 20 e 21 |
| 9 | O navio **já navegava adernado na véspera**? 7º a 10º por falha de bombas | caps. 19 e 21 |''', 1)

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('secao 10-B e 3 verificacoes novas')
