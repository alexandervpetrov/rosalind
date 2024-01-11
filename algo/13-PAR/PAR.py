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


def identity(x):
    return x


def swap(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, beg, end, pivot_pos, key_fn=identity):

    assert beg <= pivot_pos <= end

    pivot = A[pivot_pos]
    pivot_key = key_fn(pivot)

    swap(A, beg, pivot_pos)

    l = beg + 1
    r = end
    while l <= r:
        if key_fn(A[r]) > pivot_key:
            r -= 1
        elif key_fn(A[l]) <= pivot_key:
            l += 1
        else:
            # here we have: A[l] > pivot and A[r] <= pivot
            swap(A, l, r)
            # indices will be updated on next iterations
            # inside if-braches above
    l -= 1
    r += 1
    assert l + 1 == r

    swap(A, beg, l)

    # A[i] <= pivot for all i in [beg; l]
    # A[l] == pivot
    # A[i] > pivot for all i in [l+1; end]
    verify(A, beg, end, pivot, l, key_fn=key_fn)

    return l


def verify(A, beg, end, pivot, l, key_fn=identity):
    assert beg <= l <= end
    pivot_key = key_fn(pivot)
    assert all(
        key_fn(A[i]) <= pivot_key
        for i in range(beg, l)
    )
    assert A[l] == pivot
    assert all(
        key_fn(A[i]) > pivot_key
        for i in range(l+1, end+1)
    )


n = int(ifs.readline())
A = numbers_from_line()

pivot_pos = 0

partition(A, 0, len(A)-1, pivot_pos)

ofs.write(' '.join(map(str, A)))
ofs.write('\n')
