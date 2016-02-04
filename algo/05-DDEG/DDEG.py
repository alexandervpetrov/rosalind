#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import defaultdict


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n, m = numbers_from_line()
G = defaultdict(list)
for __ in xrange(m):
    a, b = numbers_from_line()
    G[a].append(b)
    G[b].append(a)


L = [sum(len(G[vn]) for vn in G[v]) for v in xrange(1, n+1)]


ofs.write('%s\n' % ' '.join(map(str, L)))
