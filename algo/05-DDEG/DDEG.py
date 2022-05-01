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
G = collections.defaultdict(list)
for __ in range(m):
    a, b = numbers_from_line()
    G[a].append(b)
    G[b].append(a)

L = [
    sum(len(G[vn]) for vn in G[v])
    for v in range(1, n + 1)
]

ofs.write(' '.join(map(str, L)))
ofs.write('\n')
