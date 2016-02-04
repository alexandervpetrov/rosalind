#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import Counter


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


k, n = numbers_from_line()
AA = []
for __ in xrange(k):
    A = numbers_from_line()
    AA.append(A)


def majority_element_lazy_to_think(A):
    C = Counter(A)
    a, n = C.most_common(1)[0]
    return a if n > len(A)/2 else -1


M = map(majority_element_lazy_to_think, AA)

ofs.write('%s\n' % ' '.join(map(str, M)))
