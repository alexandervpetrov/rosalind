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


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, beg, end, pivot_pos):

    pivot = A[pivot_pos]
    swap(A, beg, pivot_pos)

    l = beg
    r = end
    while l <= r:
        if A[l] <= pivot:
            l += 1
        elif A[r] > pivot:
            r -= 1
        else:
            swap(A, l, r)
            l += 1
            r -= 1

    swap(A, beg, l-1)


def verify(A, pivot):
    p = len(A) - 1
    while p >= 0 and A[p] > pivot:
        p -= 1
    assert p >= 0
    assert A[p] == pivot
    assert all(A[i] <= pivot for i in range(p + 1))


n = int(ifs.readline())
A = numbers_from_line()

pivot_pos = 0
pivot = A[pivot_pos]

partition(A, 0, len(A)-1, pivot_pos)
verify(A, pivot)

ofs.write(' '.join(map(str, A)))
ofs.write('\n')
