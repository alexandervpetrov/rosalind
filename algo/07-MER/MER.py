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


n = int(ifs.readline())
A = numbers_from_line()
m = int(ifs.readline())
B = numbers_from_line()

C = merge_sorted(A, B)

ofs.write(' '.join(map(str, C)))
ofs.write('\n')
