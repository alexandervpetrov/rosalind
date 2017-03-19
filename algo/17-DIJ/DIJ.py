#!/usr/bin/env python3

import math
import sys

import dijkstra

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n, m = numbers_from_line()
G = {v: [] for v in range(n)}
W = {}
for __ in range(m):
    a, b, w = numbers_from_line()
    a -= 1
    b -= 1
    G[a].append(b)
    # Rosalind input data contains multi-graph
    if (a, b) not in W:
        W[(a, b)] = w
    else:
        W[(a, b)] = min(w, W[(a, b)])


A = dijkstra.shortest_paths(G, W, 0)
D = [A[v] if A[v] < math.inf else -1 for v in range(n)]

ofs.write('%s\n' % (' '.join(str(a) for a in D)))
