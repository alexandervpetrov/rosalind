#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n, m = numbers_from_line()
G = dict((v, []) for v in xrange(1, n+1))
for __ in xrange(m):
    a, b = numbers_from_line()
    G[a].append(b)


def bfs(G, s):
    D = dict((v, None) for v in G.iterkeys())
    D[s] = 0
    Q = [s]
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if D[v] is None:
                D[v] = D[u] + 1
                Q.append(v)
    return D


D = bfs(G, 1)
DD = [D[v] for v in xrange(1, n+1)]

ofs.write('%s\n' % ' '.join(str(d) if d is not None else '-1' for d in DD))
