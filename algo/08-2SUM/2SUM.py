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


def find_by_hash_table(A, s_needed):
    M = collections.defaultdict(list)
    for i, a in enumerate(A):
        M[a].append(i)
    numbers = list(M.keys())
    for a in numbers:
        a_indices = M[a]
        b = s_needed - a
        b_indices = M.get(b)
        if b_indices is None:
            continue
        if a == b and len(a_indices) < 2:
            continue
        for p in a_indices:
            for q in b_indices:
                if p != q:
                    return p, q
    return None


def find_by_iteration_in_sorted(A, s_needed):
    A = [(n, i) for i, n in enumerate(A)]
    A = sorted(A)
    i = 0
    j = len(A) - 1
    while i < j:
        s = A[i][0] + A[j][0]
        if s == s_needed:
            return (A[i][1], A[j][1])
        if s < s_needed:
            i += 1
        else:
            j -= 1
    return None


def make_ordered_indices(a):
    if a is None:
        return None
    p, q = a
    return (min(p, q), max(p, q))


k, n = numbers_from_line()
tests = []
for __ in range(k):
    A = numbers_from_line()
    tests.append(A)

s_needed = 0

I = []
for A in tests:
    r1 = find_by_iteration_in_sorted(A, s_needed)
    r1 = make_ordered_indices(r1)
    r2 = find_by_hash_table(A, s_needed)
    r2 = make_ordered_indices(r2)
    assert (r1 is None) == (r2 is None)
    if r1 is not None:
        assert A[r1[0]] + A[r1[1]] == s_needed
    if r2 is not None:
        assert A[r2[0]] + A[r2[1]] == s_needed
    I.append(r2)

for i in I:
    if i is not None:
        p, q = i
        p, q = p + 1, q + 1
        ofs.write('{} {}'.format(p, q))
    else:
        ofs.write('-1')
    ofs.write('\n')
