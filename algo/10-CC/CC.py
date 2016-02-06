#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n, m = numbers_from_line()
G = dict((v, []) for v in xrange(n))
for __ in xrange(m):
    a, b = numbers_from_line()
    G[a-1].append(b-1)
    G[b-1].append(a-1)


def explore(G, s, visited):
    visited[s] = True
    for v in G[s]:
        if not visited[v]:
            explore(G, v, visited)


cc = 0
visited = [False] * n
for v in G.iterkeys():
    if not visited[v]:
        explore(G, v, visited)
        cc += 1


ofs.write('%d\n' % cc)
