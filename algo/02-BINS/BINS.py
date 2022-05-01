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


def binary_search(A, a):
    l = 0
    r = len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] == a:
            return m
        if l == m:
            return -1
        if a < A[m]:
            r = m
        else:
            l = m
    return -1


n = int(ifs.readline())
m = int(ifs.readline())
A = numbers_from_line()
K = numbers_from_line()

J = [binary_search(A, k) for k in K]
J = [j+1 if j!=-1 else -1 for j in J]

ofs.write(' '.join(map(str, J)))
ofs.write('\n')
