#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def read_fasta_format(stream):
    data = {}
    label = None
    dna = []
    for line in stream:
        line = line.strip()
        if line[0] == '>':
            if label is not None:
                data[label] = ''.join(dna)
            label = line[1:]
            dna = []
        else:
            dna.append(line)
    if label is not None:
        data[label] = ''.join(dna)
    return data


data = read_fasta_format(ifs)
G = data.values()

N = len(G[0])

P = {
    'A': [0] * N,
    'C': [0] * N,
    'G': [0] * N,
    'T': [0] * N,
}

for dna in G:
    for k, nt in enumerate(dna):
        P[nt][k] += 1


C = ['A'] * N
for i in xrange(N):
    max_c = None
    max_p = -1
    for c in ('A', 'C', 'G', 'T'):
        p = P[c][i]
        if p > max_p:
            max_c = c
            max_p = p
    C[i] = max_c


ofs.write('%s\n' % (''.join(map(str, C))))
for c in ('A', 'C', 'G', 'T'):
    ofs.write('%s: %s\n' % (c, ' '.join(map(str, P[c]))))
