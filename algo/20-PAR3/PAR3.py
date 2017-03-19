#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


def partition(A, p):
    n = len(A)
    if n < 2:
        return
    beg = 0
    end = 0
    for i in range(n):
        a = A[i]
        if a > p:
            continue
        if a == p:
            A[end], A[i] = A[i], A[end]
            end += 1
        else:
            A[beg], A[i] = A[i], A[beg]
            beg += 1
            A[end], A[i] = A[i], A[end]
            end += 1
    return A


n = int(ifs.readline())
A = numbers_from_line()

partition(A, A[0])

ofs.write('%s\n' % ' '.join(map(str, A)))
