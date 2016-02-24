#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


k = int(ifs.readline())
GG = []
for __ in xrange(k):
    ifs.readline()
    n, m = numbers_from_line()
    G = dict((v, []) for v in xrange(n))
    for __ in xrange(m):
        a, b = numbers_from_line()
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    GG.append(G)


def explore_and_paint(G, s, c, colors):
    result = True
    colors[s] = c
    for v in G[s]:
        vc = colors[v]
        if vc is None:
            result = result and explore_and_paint(G, v, -c, colors)
        else:
            if vc == c:
                return False
    return result
 
 
def is_bipartite(G):
    n = len(G)
    colors = [None] * n
    for v in G.iterkeys():
        if colors[v] is None:
            r = explore_and_paint(G, v, 1, colors)
            if not r:
                return False
    return True


A = map(is_bipartite, GG)

ofs.write('%s\n' % (' '.join('1' if a else '-1' for a in A)))
