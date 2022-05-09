#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [
        int(s)
        for s in ifs.readline().strip().split(d)
        if len(s.strip()) > 0
    ]


def is_bipartite_recursive(G):

    BLACK = 'B'
    WHITE = 'W'

    def other_color(c):
        return BLACK if c == WHITE else WHITE

    def try_mark_with_color_via_dfs(G, v, C, color):
        C[v] = color
        other = other_color(color)
        for u in G[v]:
            if C[u] == color:
                return False
            if C[u] is None:
                marked_all = try_mark_with_color_via_dfs(G, u, C, other)
                if not marked_all:
                    return False
        return True

    C = {v: None for v in G}
    color = WHITE
    for v in range(1, len(G) + 1):
        if C[v] is not None:
            continue
        marked_all = try_mark_with_color_via_dfs(G, v, C, color)
        if not marked_all:
            return False
    return True


def is_bipartite(G):

    BLACK = 'B'
    WHITE = 'W'

    def other_color(c):
        return BLACK if c == WHITE else WHITE

    def try_mark_with_color_via_dfs(G, v, C, color):
        C[v] = color
        stack = [v]
        while stack:
            v = stack.pop()
            other = other_color(C[v])
            for u in G[v]:
                if C[u] is not None:
                    if C[u] != other:
                        return False
                    continue
                C[u] = other
                stack.append(u)
        return True

    C = {v: None for v in G}
    color = WHITE
    for v in range(1, len(G) + 1):
        if C[v] is not None:
            continue
        marked_all = try_mark_with_color_via_dfs(G, v, C, color)
        if not marked_all:
            return False
    return True


k = int(ifs.readline())
tests = []
for __ in range(k):
    ifs.readline()
    n, m = numbers_from_line()
    G = {v: [] for v in range(1, n+1)}
    for __ in range(m):
        a, b = numbers_from_line()
        G[a].append(b)
        G[b].append(a)
    tests.append(G)

A = []
for G in tests:
    is_bp = is_bipartite(G)
    is_bpr = is_bipartite_recursive(G)
    assert is_bp == is_bpr
    a = '1' if is_bp else '-1'
    A.append(a)

ofs.write(' '.join(A))
ofs.write('\n')
