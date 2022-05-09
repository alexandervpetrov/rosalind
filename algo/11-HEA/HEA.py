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


def parent(i):
    return (i - 1) // 2


def left_child(i):
    return i * 2 + 1


def bubble_up(H, i):
    while i > 0 and H[parent(i)] < H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)


def make_max_heap_by_insertions(A):
    H = []
    for a in A:
        H.append(a)
        bubble_up(H, len(H) - 1)
    return H


def bubble_down(H, i):
    while True:
        lc = left_child(i)
        if lc >= len(H):
            return
        rc = lc + 1
        child = lc
        if rc < len(H) and H[child] < H[rc]:
            child = rc
        if H[i] < H[child]:
            H[i], H[child] = H[child], H[i]
        i = child


def make_max_heap_linear_inplace(A):
    H = A[:]
    for k in range(len(A)-1, -1, -1):
        bubble_down(H, k)
    return H


def verify_max_heap_property(A):
    for i in range(1, len(A)):
        assert A[i] <= A[parent(i)]


n = int(ifs.readline())
A = numbers_from_line()

H = make_max_heap_by_insertions(A)
verify_max_heap_property(H)
H = make_max_heap_linear_inplace(A)
verify_max_heap_property(H)

ofs.write(' '.join(map(str, H)))
ofs.write('\n')
