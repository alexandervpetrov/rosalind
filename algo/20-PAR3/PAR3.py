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
    ml = beg + 1
    mr = end
    r = end
    while ml <= mr:
        if key_fn(A[mr]) == pivot_key:
            mr -= 1
        elif key_fn(A[mr]) > pivot_key:
            swap(A, mr, r)
            mr -= 1
            r -= 1
        elif key_fn(A[ml]) == pivot_key:
            ml += 1
        elif key_fn(A[ml]) < pivot_key:
            swap(A, l, ml)
            l += 1
            ml += 1
        else:
            # here we have: A[ml] > pivot and A[mr] < pivot
            swap(A, ml, mr)
            # other swaps and indices updates will be on next iterations
            # inside if-braches above

    l -= 1
    swap(A, beg, l)

    # A[i] < pivot for all i in [beg; l)
    # A[i] == pivot for all i in [l; r]
    # A[i] > pivot for all i in (r; end]
    verify(A, beg, end, pivot, l, r, key_fn=key_fn)

    return l, r


def verify(A, beg, end, pivot, l, r, key_fn=identity):
    assert beg <= l <= r <= end
    pivot_key = key_fn(pivot)
    assert all(
        key_fn(A[i]) < pivot_key
        for i in range(beg, l)
    )
    assert all(
        key_fn(A[i]) == pivot_key
        for i in range(l, r+1)
    )
    assert all(
        key_fn(A[i]) > pivot_key
        for i in range(r+1, end+1)
    )


n = int(ifs.readline())
A = numbers_from_line()

pivot_pos = 0

partition(A, 0, len(A)-1, pivot_pos)

ofs.write(' '.join(map(str, A)))
ofs.write('\n')
