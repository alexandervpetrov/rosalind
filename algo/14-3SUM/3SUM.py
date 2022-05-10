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
        for b in numbers:
            b_indices = M[b]
            c = s_needed - a - b
            c_indices = M.get(c)
            if c_indices is None:
                continue
            for p in a_indices:
                for q in b_indices:
                    for r in c_indices:
                        if p != q and q != r and p != r:
                            return p, q, r
    return None


def find_by_iteration_in_sorted(A, s_needed):

    def _find_2sum(A, l, r, s_needed):
        i = l
        j = r
        while i < j:
            s = A[i][0] + A[j][0]
            if s == s_needed:
                return (A[i][1], A[j][1])
            if s < s_needed:
                i += 1
            else:
                j -= 1
        return None

    A = [(n, i) for i, n in enumerate(A)]
    A = sorted(A)
    n = len(A)
    for k in range(n - 2):
        a, i = A[k]
        result = _find_2sum(A, k + 1, n - 1, s_needed - a)
        if result is not None:
            return i, result[0], result[1]
    return None


def make_ordered_indices(a):
    if a is None:
        return None
    return tuple(sorted(a))


def verify(A, s_needed, indices):
    if indices is None:
        return
    p, q, r = indices
    assert p < q < r
    assert A[p] + A[q] + A[r] == s_needed


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
    verify(A, s_needed, r1)
    verify(A, s_needed, r2)
    I.append(r2)

for i in I:
    if i is not None:
        p, q, r = i
        p, q, r = p + 1, q + 1, r + 1
        ofs.write('{} {} {}'.format(p, q, r))
    else:
        ofs.write('-1')
    ofs.write('\n')
