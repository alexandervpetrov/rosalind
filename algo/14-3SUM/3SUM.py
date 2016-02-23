#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import defaultdict


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


k, n = numbers_from_line()
AA = []
for _ in xrange(k):
    A = numbers_from_line()
    AA.append(A)


def get_indices_hashing(A):
    I = defaultdict(list)
    for i, a in enumerate(A):
        I[a].append(i)
    if 0 in I:
        I0 = I[0]
        if len(I0) > 2:
            p, q, r = I0[0], I0[1], I0[2]
            return tuple(sorted([p, q, r]))
    n = len(A)
    for i in xrange(n):
        for j in xrange(i):
            b = A[i] + A[j]
            if b != 0 and -b in I:
                return tuple(sorted([i, j, I[-b][0]]))
    return None


I = map(get_indices_hashing, AA)

for i in I:
    if i is not None:
        ofs.write('%d %d %d\n' % (i[0]+1, i[1]+1, i[2]+1))
    else:
        ofs.write('-1\n')
