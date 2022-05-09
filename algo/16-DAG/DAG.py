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


def is_acyclic_recursive(G):

    CHECKING = 'C'
    ACYCLIC = 'A'

    def has_cycle_via_dfs(G, v, C):
        C[v] = CHECKING
        for u in G[v]:
            if C[u] == CHECKING:
                return True
            if C[u] is None:
                has_cycle = has_cycle_via_dfs(G, u, C)
                if has_cycle:
                    return True
        C[v] = ACYCLIC
        return False

    C = {v: None for v in G}
    for v in G:
        if C[v] is not None:
            continue
        has_cycle = has_cycle_via_dfs(G, v, C)
        if has_cycle:
            return False
    return True


def is_acyclic(G):

    CHECKING = 'C'
    ACYCLIC = 'A'

    def has_cycle_via_dfs(G, v, C):
        IN = 'I'
        OUT = 'O'
        stack = [(IN, v)]
        while stack:
            state, v = stack.pop()
            if state == IN:
                C[v] = CHECKING
                stack.append((OUT, v))
                for u in G[v]:
                    if C[u] == CHECKING:
                        return True
                    if C[u] is None:
                        stack.append((IN, u))
            else:
                C[v] = ACYCLIC
        return False

    C = {v: None for v in G}
    for v in G:
        if C[v] is not None:
            continue
        has_cycle = has_cycle_via_dfs(G, v, C)
        if has_cycle:
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
    tests.append(G)

A = []
for G in tests:
    is_ac = is_acyclic(G)
    is_acr = is_acyclic_recursive(G)
    assert is_ac == is_acr
    a = '1' if is_ac else '-1'
    A.append(a)

ofs.write(' '.join(A))
ofs.write('\n')
