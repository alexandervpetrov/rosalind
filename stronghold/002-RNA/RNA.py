#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


dna = ifs.readline().strip()

rna = ''.join((nt if nt !='T' else 'U') for nt in dna)

ofs.write('%s\n' % (rna))
