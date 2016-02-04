#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def read_codon_table(filename):
    CT = {}
    tokens = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            tokens.extend(t for t in line.split() if t.strip())
    assert len(tokens) % 2 == 0
    for i in xrange(0, len(tokens), 2):
        CT[tokens[i]] = tokens[i+1]
    return CT


CT = read_codon_table('rna-codon-table.txt')


rna = ifs.readline().strip()

protein = []
for i in xrange(0, len(rna), 3):
    c = rna[i:i+3]
    acid = CT[c]
    if acid == 'Stop':
        break
    protein.append(acid)

protein = ''.join(protein)

ofs.write('%s\n' % (protein))
