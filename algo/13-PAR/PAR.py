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


def partition(A, l, r, pivot_pos):

    def _partition(A, l, r, pivot):
        assert l <= r
        while True:
            while l < r and A[l] <= pivot:
                l += 1
            while l < r and pivot < A[r]:
                r -= 1
            if l >= r:
                assert l == r
                return l
            A[l], A[r] = A[r], A[l]

    if l == r:
        return

    pivot = A[pivot_pos]
    A[l], A[pivot_pos] = A[pivot_pos], A[l]
    pivot_pos = _partition(A, l + 1, r, pivot)
    if pivot < A[pivot_pos]:
        pivot_pos = max(l, pivot_pos - 1)
    A[l], A[pivot_pos] = A[pivot_pos], A[l]


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
