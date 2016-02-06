#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from operator import itemgetter
from bisect import bisect_left, bisect_right
from collections import defaultdict


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


k, n = numbers_from_line()
AA = []
for _ in xrange(k):
    A = numbers_from_line()
    AA.append(A)


def get_indices_sorting(A):
    AI = sorted(enumerate(A), key=itemgetter(1))
    I = map(itemgetter(0), AI)
    S = map(itemgetter(1), AI)
    N = len(S)
    zero_l = bisect_left(S, 0)
    zero_r = bisect_right(S, 0)
    if zero_r == 0:
        return None
    if zero_r == N:
        return None
    if zero_l < zero_r - 1:
        p, q = I[zero_l], I[zero_r-1]
        return min(p, q), max(p, q)
    neg = zero_l - 1
    pos = zero_r
    while 0 <= neg and pos < N:
        if -S[neg] < S[pos]:
            neg -= 1
        elif -S[neg] > S[pos]:
            pos += 1
        else:
            p, q = I[neg], I[pos]
            return min(p, q), max(p, q)
    return None


def get_indices_hashing(A):
    I = defaultdict(list)
    for i, a in enumerate(A):
        I[a].append(i)
    if 0 in I:
        I0 = I[0]
        if len(I0) > 1:
            p, q = I0[0], I0[1]
            return min(p, q), max(p, q)
    for a in I.iterkeys():
        if a != 0 and (-a) in I:
            p, q = I[a][0], I[-a][0]
            return min(p, q), max(p, q)
    return None


#I = map(get_indices_sorting, AA)
I = map(get_indices_hashing, AA)

for i in I:
    if i is not None:
        ofs.write('%d %d\n' % (i[0]+1, i[1]+1))
    else:
        ofs.write('-1\n')
