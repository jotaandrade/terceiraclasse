# -*- coding: utf-8 -*-
"""Atualiza a memoria do projeto com a revisao factual de 06.09.2026."""
import io

P = r"C:\Users\joand\.claude\projects\D--\memory\italiaminha.md"
s = io.open(P, encoding='utf-8').read()
n = [0]


def sub(old, new, label):
    global s
    assert old in s, 'NAO ACHOU: ' + label
    assert s.count(old) == 1, 'AMBIGUO (%d): %s' % (s.count(old), label)
    s = s.replace(old, new, 1)
    n[0] += 1
    print('  ok  ' + label)


# ---- Enrico: causa da morte -----------------------------------------
sub(u'morreu de **câncer na língua, sozinho**',
    u'morreu sozinho de **neoplasia de orofaringe** (DO nº 5501831) — **não** câncer de língua, como a família conta e como este arquivo registrava',
    'Enrico · causa da morte')

sub(u'porque o tio morreu de câncer na língua e lembrar',
    u'porque o tio morreu de câncer e lembrar',
    'Enrico · nota de sensibilidade, sem alterar a regra')

sub(u'🔴 **Regra de escrita acordada:** NÃO transformar o câncer na língua em metáfora',
    u'🔴 **Regra de escrita acordada:** NÃO transformar a doença em metáfora',
    'Enrico · regra de escrita')

sub(u'- **06.10.1998** morre no Conjunto Hospitalar de Sorocaba, 71 anos, aposentado, solteiro.',
    u'- **06.10.1998** morre no Conjunto Hospitalar de Sorocaba de **neoplasia de orofaringe** '
    u'(insuficiência respiratória como causa direta, desnutrição na parte II), 71 anos, aposentado, solteiro.',
    'Enrico · linha do tempo')

# ---- Vincenzo estava vivo em 1940 -----------------------------------
sub(u'🔴 **Vincenzo NÃO tem data de morte** — a tese de "órfã de pai e mãe em 1914" foi corrigida no livro.',
    u'✅ **Vincenzo estava VIVO em março de 1940**, aos 77 anos — a *carta d\'identità* de Sante '
    u'(Comune di Asolo, 08.03.1940) escreve **"di Vincenzo"** (pai vivo) e **"fu Pandolfo Domenica Santa"** '
    u'(mãe falecida) em linhas consecutivas. Rosa não saiu órfã de pai em 1927; ele tinha 65 anos na '
    u'despedida. Falta o atto di morte, a partir de 1940. A tese de "órfã de pai e mãe em 1914" está '
    u'corrigida no livro.',
    'Vincenzo vivo em 1940')

# ---- Sante: pendencia resolvida -------------------------------------
sub(u'🟡 **Sante (1893) NÃO aparece** com mãe Santa Pandolfo; existe "Sante Domenico, pat. Vincenzo, '
    u'mat. Pandolfo **Domenica**, 1893" — pode ser outro casal. Verificar.',
    u'✅ **RESOLVIDO: Sante é irmão de Rosa.** A carta d\'identità de 1940 registra a mãe como '
    u'**"Pandolfo Domenica Santa"** — dois prenomes, uma mulher só. O registro de 1893 de "Sante Domenico, '
    u'mat. Pandolfo Domenica" é dela mesma, não de outro casal.',
    'Sante · pendencia resolvida')

# ---- o quadro tem duas fileiras de casais diferentes -----------------
sub(u'**Índice de matrimônios/nascimentos 1871-1900** (provavelmente Monfumo): filhos de Vincenzo+Santa '
    u'confirmados no registro civil —',
    u'🔴 **O quadro de *Storia di Castelcucco* tem DUAS fileiras, de DOIS casais.** Uma linha vertical '
    u'desce de **Cadonà Maria Teresa** (esposa de Abele Alessandro Forner, irmão de Vincenzo) e se liga à '
    u'**segunda** fileira. Primeira fileira = 8 filhos de Vincenzo+Santa; segunda = 6 filhos de '
    u'Abele+Cadonà. Somando Maria Elisabetta 1895 e Maria Luigia 1896, **Vincenzo e Santa tiveram DEZ '
    u'filhos**, não catorze nem dezesseis. Consequências: as duas Angelas são primas (não irmãs); os '
    u'gêmeos Ausilio/Roberto são de Cadonà (39 anos), não de Santa (42); Alessandro Domenico e Francesco '
    u'não são irmãos de Rosa; a caçula da casa é **Maria M., 1907**, e a anotação "Ccucco" sob ela mostra '
    u'que a família mudou de Monfumo para Castelcucco entre 1903 e 1907 — o que explica os casamentos de '
    u'1917 e 1926 em Castelcucco e o "nata a Castelcucco" do ato de 1926.\n\n'
    u'**Índice de matrimônios/nascimentos 1871-1900** (provavelmente Monfumo): filhos de Vincenzo+Santa '
    u'confirmados no registro civil —',
    'quadro · duas fileiras')

# ---- nomes dos Dei Agnoli -------------------------------------------
sub(u'**FORNER MARIA, 31, chefe, residência Cavarzo** (= Maria Luigia), com **Dinetta 7, Pulcheria 6, '
    u'Dino 4, Danilo 2**. Registradas como **Forner**, não Agnoli.',
    u'**FORNER MARIA, 31, residência Cavaso del Tomba** (= Maria Luigia), com **Gina 7, Pulcheria 6, '
    u'Rino 4, Danilo 2**. Registradas como **Forner**, não Dei Agnoli.\n\n'
    u'🔴 **Nomes corrigidos:** *Cavarzo* não existe, é **Cavaso del Tomba**. *Dino* é **Rino** '
    u'(n. 26.01.1923). *Dinetta* é **Gina Oliva** (n. 28.03.1920, atto 21/1920, via Costalunga); '
    u'"Dinetta" e "Ginita" são grafias de escrivães brasileiro e argentino. Danilo Angelo n. 11.02.1925 '
    u'(atto 16/1925). Pulcheria ~1921, sem ato localizado.\n\n'
    u'🔎 **Não afirmar que Rosa foi registrada como "chefe de família"** sem conferir a coluna de '
    u'parentesco numa digitalização em alta resolução.',
    'Dei Agnoli · nomes e lugares')

# ---- pasta nova + artefatos -----------------------------------------
sub(u'## Artefatos publicados',
    u'## Export em Markdown (06.09.2026)\n\n'
    u'Tudo exportado para **`D:/italiaminha/As Tres Mafaldas/`** (dentro do Drive, com backup): '
    u'`README.md`, `00-dossie.md`, `01-caderno-de-bordo.md`, `02-pesquisa-documental.md`, '
    u'`03-roteiro-gravacoes.md` e `manuscrito/` (um `.md` por capítulo).\n\n'
    u'⚠️ **A fonte do texto continua sendo o `build_livro.py`**, não os `.md`. Fluxo: editar o gerador → '
    u'`python build_livro.py` → `python export_md.py`. Os scripts `export_md.py` e `html2md.py` estão no '
    u'scratchpad da sessão 96f3cc2a.\n\n'
    u'Pasta de áudio criada: `Familia Miotto/Gravacoes/`.\n\n'
    u'## Artefatos publicados',
    'export markdown')

sub(u'- **Terceira Classe, o livro folha a folha**: https://claude.ai/code/artifact/41ce6f44-12bd-4905-b442-61e3a150e441',
    u'- **Terceira Classe, o livro folha a folha**: https://claude.ai/code/artifact/41ce6f44-12bd-4905-b442-61e3a150e441\n'
    u'- **Gravar a Mafalda** (roteiro de campo da sessão 1): https://claude.ai/code/artifact/5c9e0235-fae1-4257-9ef0-26798a3c0105\n\n'
    u'**Estado do manuscrito (06.09.2026):** 9 capítulos, **15.666 palavras**. Livro I completo (caps. 1-8) '
    u'+ cap. 20. Revisão factual de 32 correções aplicada.\n\n'
    u'**Pesquisa gratuita** (consulado cobra em euros, isto não): **Portale Antenati** '
    u'(antenati.cultura.gov.it — stato civile de Treviso 1871-1941, com a imagem do ato inteiro), '
    u'**Hemeroteca Digital Brasileira** (memoria.bn.gov.br — jornais de 1927, é a fonte do Livro III '
    u'inteiro), FamilySearch, e o Giorgio indo a pé ao comune.',
    'artefatos e estado')

io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('\n%d atualizacoes na memoria' % n[0])
