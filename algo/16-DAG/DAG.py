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
    GG.append(G)


def explore_and_find(G, s, colors):
    result = True
    colors[s] = 1
    for v in G[s]:
        cv = colors[v]
        if cv == 1:
            return False
        elif cv is None:
            result = result and explore_and_find(G, v, colors)
    colors[s] = 2
    return result
 
 
def is_acyclic(G):
    n = len(G)
    colors = [None] * n
    for v in G.iterkeys():
        if colors[v] is None:
            r = explore_and_find(G, v, colors)
            if not r:
                return False
    return True


A = map(is_acyclic, GG)

ofs.write('%s\n' % (' '.join('1' if a else '-1' for a in A)))
