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


def find_shortest_distances_by_bfs(G, beg):
    D = {v: None for v in G}
    D[beg] = 0
    queue = collections.deque([beg])
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if D[u] is not None:
                continue
            D[u] = D[v] + 1
            queue.append(u)
    return D


n, m = numbers_from_line()
G = {v: [] for v in range(1, n+1)}
for __ in range(m):
    a, b = numbers_from_line()
    G[a].append(b)

D = find_shortest_distances_by_bfs(G, 1)

A = [
    D[v] if (D[v] is not None) else -1
    for v in range(1, n+1)
]

ofs.write(' '.join(map(str, A)))
ofs.write('\n')
