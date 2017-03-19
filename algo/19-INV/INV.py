#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


def count_inv_and_merge_sorted(A, B):
    n = len(A)
    m = len(B)
    C = []
    i = 0
    j = 0
    inversions = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
            inversions += (n - i)
    if i < n:
        C.extend(A[i:])
    if j < m:
        C.extend(B[j:])
    return C, inversions


def count_inv(A):
    if len(A) <= 1:
        return A, 0
    mid = len(A) // 2
    L, Li = count_inv(A[:mid])
    R, Ri = count_inv(A[mid:])
    AS, Ai = count_inv_and_merge_sorted(L, R)
    return AS, (Li + Ri + Ai)


n = int(ifs.readline())
A = numbers_from_line()
__, ni = count_inv(A)
ofs.write('{}\n'.format(ni))
