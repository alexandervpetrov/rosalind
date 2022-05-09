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


def merge_sorted(A, B):
    n = len(A)
    m = len(B)
    C = []
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < n:
        C.extend(A[i:])
    if j < m:
        C.extend(B[j:])
    return C


def sorted_by_merging(A):
    n = len(A)
    if n == 1:
        return A
    elif n == 2:
        return [min(A[0], A[1]), max(A[0], A[1])]
    else:
        A1 = sorted_by_merging(A[n//2:])
        A2 = sorted_by_merging(A[:n//2])
        return merge_sorted(A1, A2)


n = int(ifs.readline())
A = numbers_from_line()

C = sorted_by_merging(A)

ofs.write(' '.join(map(str, C)))
ofs.write('\n')
