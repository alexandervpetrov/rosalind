#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


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


def gc_content_percent(dna):
    return 100.0 * sum(1 if nt in 'GC' else 0 for nt in dna) / len(dna)


data = read_fasta_format(ifs)

max_label = None
max_gc = 0
for label, dna in data.iteritems():
    gc = gc_content_percent(dna)
    if gc > max_gc:
        max_label = label
        max_gc = gc


ofs.write('%s\n%.4f\n' % (max_label, max_gc))
