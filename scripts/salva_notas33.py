# -*- coding: utf-8 -*-
"""Salva o material de crítica de fontes que saiu do cap. 4, para o cap. 33."""
import io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SP = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad"
BAK = os.path.join(SP, 'cap4_antigo.py.bak')
OUT = r"D:\italiaminha\As Tres Mafaldas\notas-cap33-a-busca.md"

src = io.open(BAK, encoding='utf-8').read()
ns = {}
exec(compile(src, 'cap4bak', 'exec'), ns)
blocos = ns['CAP4']


def md(t):
    t = re.sub(r'<em>(.*?)</em>', r'*\1*', t, flags=re.S)
    t = re.sub(r'<strong>(.*?)</strong>', r'**\1**', t, flags=re.S)
    t = re.sub(r'<[^>]+>', '', t)
    paras = [re.sub(r'\s*\n\s*', ' ', p).strip()
             for p in re.split(r'\n[ \t]*\n', t) if p.strip()]
    return '\n\n'.join(paras)


# blocos que SAIRAM do cap 4 (por assunto), na ordem em que estavam
CHAVES = [
    (u'O quadro impresso em', u'O quadro de duas fileiras'),
    (u'Foi preciso ampliar a fotografia', u'A linha vertical, vista na lupa'),
    (u'A primeira coisa que a lista diz', u'A ordem dos acontecimentos'),
    (u'Angela em 1886, na casa de Vincenzo', u'As duas Angelas'),
    (u'Uma linha não precisa de interpretação', u'Os gêmeos de 1908'),
    (u'Há uma dificuldade que qualquer pessoa', u'O nome instável da bisavó'),
    (u'Isso não seria grave', u'O risco: Sante é irmão ou primo?'),
    (u'Meu palpite é que é a mesma mulher', u'O palpite, e o fundamento dele'),
    (u'Contra isso pesam duas coisas', u'O que pesava contra'),
    (u'O que decidiu a questão', u'A carta d\u2019identità resolve'),
    (u'O que resolve não é o extrato', u'Extrato x ato inteiro: o que pedir ao Comune'),
    (u'Contra o quadro sobra uma coisa', u'O único erro real do quadro'),
    (u'E há o que o quadro simplesmente não tem', u'O que o quadro omite: Maria Elisabetta e Maria Luigia'),
    (u'E há uma anotação minúscula', u'A anotação "Ccucco"'),
    (u'Some tudo e o retrato é este', u'Três fontes ruins que, cruzadas, chegam perto'),
    (u'O Albo d\u2019Oro é o registro oficial', u'A busca no Albo d\u2019Oro'),
    (u'Isso não prova que ele não tenha sido soldado', u'O que o Albo d\u2019Oro não prova'),
    (u'Durante um tempo eu escrevi que o pai', u'A orfandade dupla que não existiu'),
    (u'A resposta estava na mesma carteira', u'O "di" e o "fu"'),
    (u'Do outro lado da história estão os Miotto', u'O tronco Miotto e a família de Vancouver'),
    (u'E aqui há uma simetria', u'Louie Miotto, Vancouver, 1955'),
    (u'Só que o documento traz duas linhas', u'As duas linhas que não fecham'),
    (u'Numa árvore genealógica colaborativa', u'A unificação de 18.11.2024, às 11h21'),
    (u'Desfazer não deu', u'A reconstrução, e a declaração de óbito de 1979'),
    (u'O que não está resolvido', u'Quem foi o pai do Luigi'),
    (u'Existe uma quarta fonte', u'A quarta fonte: a árvore colaborativa'),
]

L = [u'# Notas para o capítulo 33 — "A busca"',
     u'',
     u'> **Material retirado do capítulo 4 em 07.09.2026.** Nada aqui foi descartado: são as',
     u'> passagens de crítica de fontes e de investigação que tiravam o capítulo 4 do registro',
     u'> narrativo. O plano já reserva o capítulo 33 para isto — *"A pesquisa como enredo. O dia',
     u'> em que o registro apareceu."*',
     u'',
     u'> **Regra que motivou a mudança:** conclusão nos capítulos de narrativa, demonstração no',
     u'> capítulo da busca. O capítulo 4 passou a dizer *"Vincenzo e Santa tiveram dez filhos"*;',
     u'> a prova disso está aqui.',
     u'',
     u'> ⚠️ O texto abaixo está **como estava**, com as passagens de autocorreção ainda dentro.',
     u'> Ao montar o capítulo 33, aplicar o mesmo critério: o narrador pode dizer o que não sabe,',
     u'> não o que escreveu antes. Aqui, porém, a busca **é** o assunto — então o erro de leitura',
     u'> do quadro e a fusão equivocada na árvore deixam de ser confissão e passam a ser enredo.',
     u'']

usados = 0
for chave, titulo in CHAVES:
    for b in blocos:
        if b.lstrip().startswith(chave):
            L += [u'', u'---', u'', u'## ' + titulo, u'', md(b)]
            usados += 1
            break

L += [u'', u'---', u'',
      u'## Sequência sugerida para o capítulo 33',
      u'',
      u'1. **O quadro na parede e a lupa** — a linha vertical de dois centímetros que reatribui',
      u'   seis filhos a outro casal. É a melhor cena de pesquisa do acervo italiano.',
      u'2. **O nome instável da bisavó** — seis grafias contra uma, e o risco real de que o',
      u'   capítulo 7 fosse sobre outra pessoa. Tensão verdadeira, com desfecho.',
      u'3. **A carta d\u2019identità na pasta** — o documento que estava em casa o tempo todo e',
      u'   resolve duas perguntas de uma vez (o nome da mãe e o *di/fu* do pai).',
      u'4. **Vancouver** — a sepultura com o sobrenome da família, as duas linhas que não fecham.',
      u'5. **A unificação de 18.11.2024, às 11h21** — o clímax. Um clique de um estranho, e o',
      u'   bisavô ganha um pai que morreu sozinho no Canadá.',
      u'6. **A quarta fonte** — o fecho: a árvore colaborativa erra de um jeito que nenhum livro',
      u'   velho erra, e o erro tem a mesma aparência de tudo o mais.',
      u'']

io.open(OUT, 'w', encoding='utf-8', newline='\n').write(u'\n'.join(L) + u'\n')
print('%d de %d blocos salvos em %s' % (usados, len(CHAVES), OUT))
print('%d palavras' % len(u' '.join(L).split()))
