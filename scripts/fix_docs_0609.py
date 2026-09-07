# -*- coding: utf-8 -*-
"""Propaga a revisao de 06.09.2026 para o dossie e o caderno de bordo."""
import io, os

OLD = r"C:\Users\joand\AppData\Local\Temp\claude\D--italiaminha\d7ec32c9-3478-48c5-b4dc-cea1c4fb7830\scratchpad"
n = [0]


def fix(path, pairs):
    p = os.path.join(OLD, path)
    s = io.open(p, encoding='utf-8').read()
    for old, new, label in pairs:
        assert old in s, 'NAO ACHOU em %s: %s' % (path, label)
        assert s.count(old) == 1, 'AMBIGUO: ' + label
        s = s.replace(old, new, 1)
        n[0] += 1
        print('  ok  ' + label)
    io.open(p, 'w', encoding='utf-8', newline='\n').write(s)


fix('tres-mafaldas.html', [
    (u'''mais novo da família. Cresceu calado e reservado. Nunca casou, nunca teve filhos. Morreu de câncer
        na língua, sozinho.''',
     u'''mais novo da família. Cresceu calado e reservado. Nunca casou, nunca teve filhos. Morreu sozinho, de
        <strong>neoplasia de orofaringe</strong> &mdash; Declaração de Óbito nº 5501831, com insuficiência
        respiratória como causa direta e desnutrição na parte II. Não era câncer de língua, como a família
        conta e como este dossiê chegou a registrar. Num capítulo cuja regra de escrita é a contenção, o
        sítio exato importa.''',
     'dossie · orofaringe, nao lingua'),

    (u'''Não transformar o câncer na língua em metáfora. <em>O sobrevivente que perdeu a voz</em> é bonito''',
     u'''Não transformar a doença em metáfora. <em>O sobrevivente que perdeu a voz</em> é bonito''',
     'dossie · regra de escrita sem "lingua"'),
])

fix('caderno-de-bordo.html', [
    (u'''Vincenzo e Santa Pandolfo e os dezesseis filhos.''',
     u'''Vincenzo e Santa Pandolfo e os dez filhos.''',
     'caderno · cap 4, dez filhos'),
])

print('\n%d correcoes' % n[0])
