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


def majority_element_hash_table(A):
    freqs = collections.Counter(A)
    a, n = freqs.most_common(1)[0]
    return a if (n > len(A) // 2) else -1


def majority_element_n_log_n(A):

    def mjel(A, l, r):
        assert l <= r
        if l == r:
            return A[l]
        m = (l + r) // 2
        ml = mjel(A, l, m)
        mr = mjel(A, m + 1, r)
        cl = sum(1 for i in range(l, r + 1) if A[i] == ml)
        cr = sum(1 for i in range(l, r + 1) if A[i] == mr)
        n2 = (r - l + 1) // 2
        if cl > n2:
            return ml
        if cr > n2:
            return mr
        return None

    a = mjel(A, 0, len(A) - 1)
    return a if (a is not None) else -1


def majority_element_linear(A):

    def shrink(A):
        n = len(A)
        for i, j in zip(range(0, n-1, 2), range(1, n, 2)):
            if A[i] != A[j]:
                continue
            yield A[i]

    B = A
    while len(B) > 1:
        B = list(shrink(B))
    if len(B) == 0:
        return -1
    candidate = B[0]
    nc = sum(1 for a in A if a == candidate)
    return candidate if (nc > len(A) // 2) else -1


def majority_element_best(A):
    c = 0
    candidate = None
    for a in A:
        if c == 0:
            candidate = a
            c = 1
            continue
        c += 1 if (a == candidate) else -1
    nc = sum(1 for a in A if a == candidate)
    return candidate if (nc > len(A) // 2) else -1


k, n = numbers_from_line()
tests = []
for __ in range(k):
    A = numbers_from_line()
    tests.append(A)

answers = []
for A in tests:
    r1 = majority_element_hash_table(A)
    r2 = majority_element_n_log_n(A)
    r3 = majority_element_linear(A)
    r4 = majority_element_best(A)
    # print(r1, r2, r3, r4)
    assert r1 == r2
    assert r1 == r3
    assert r1 == r4
    answers.append(r1)

ofs.write(' '.join(map(str, answers)))
ofs.write('\n')
