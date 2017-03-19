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


def majority_element_linear(A):
    """O(n)"""
    c = 0
    current_major_candidate = None
    for a in A:
        if c == 0:
            current_major_candidate = a
            c = 1
        elif a == current_major_candidate:
            c += 1
        else:
            c -= 1
    nc = sum(1 for a in A if a == current_major_candidate)
    return current_major_candidate if nc > len(A)/2 else -1

# M = map(majority_element_lazy_to_think, AA)
M = map(majority_element_linear, AA)

ofs.write('%s\n' % ' '.join(map(str, M)))
