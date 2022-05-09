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


def find_connected_components_recursive(G):

    def mark_with_color_via_dfs(G, v, C, color):
        C[v] = color
        for u in G[v]:
            if C[u] is None:
                mark_with_color_via_dfs(G, u, C, color)

    C = {v: None for v in G}
    color = 1
    for v in range(1, len(G) + 1):
        if C[v] is not None:
            continue
        mark_with_color_via_dfs(G, v, C, color)
        color += 1
    return C, (color -1)


def find_connected_components(G):

    def mark_with_color_via_dfs(G, v, C, color):
        C[v] = color
        stack = [v]
        while stack:
            v = stack.pop()
            for u in G[v]:
                if C[u] is not None:
                    continue
                C[u] = color
                stack.append(u)

    C = {v: None for v in G}
    color = 1
    for v in range(1, len(G) + 1):
        if C[v] is not None:
            continue
        mark_with_color_via_dfs(G, v, C, color)
        color += 1
    return C, (color -1)


n, m = numbers_from_line()
G = {v: [] for v in range(1, n+1)}
for __ in range(m):
    a, b = numbers_from_line()
    G[a].append(b)
    G[b].append(a)

CC, nc = find_connected_components(G)
CCR, ncr = find_connected_components_recursive(G)
assert nc == ncr
assert CC == CCR

ofs.write(str(nc))
ofs.write('\n')
