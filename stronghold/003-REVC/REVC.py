#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


dna = ifs.readline().strip()

complement = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
}

rc = ''.join(complement[nt] for nt in reversed(dna))

ofs.write('%s\n' % (rc))
