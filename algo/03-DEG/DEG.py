#!/usr/bin/env python

import sys
import collections

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [
        int(s)
        for s in ifs.readline().strip().split(d)
        if len(s.strip()) > 0
    ]


n, m = numbers_from_line()
G = collections.defaultdict(int)
for __ in range(m):
    a, b = numbers_from_line()
    G[a] += 1
    G[b] += 1

L = [(v, G[v]) for v in range(1, n+1)]

ofs.write(' '.join(str(n) for __, n in L))
ofs.write('\n')
