#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


def make_max_heap(A):

    def parent(i):
        return (i-1) // 2

    def bubble_up(H, i):
        while i > 0 and H[parent(i)] < H[i]:
            H[parent(i)], H[i] = H[i], H[parent(i)]
            i = parent(i)

    H = []
    for a in A:
        H.append(a)
        bubble_up(H, len(H)-1)
    return H


def child_first(i):
    return 2 * i + 1


def max_child(A, i):
    ci1 = child_first(i)
    n = len(A)
    if ci1 >= n:
        return None
    ci2 = ci1 + 1
    if ci2 >= n:
        return ci1
    v1 = A[ci1]
    v2 = A[ci2]
    if v2 > v1:
        return ci2
    return ci1


def sink_down(A, i):
    while True:
        ci = max_child(A, i)
        if ci is not None and A[ci] > A[i]:
            A[i], A[ci] = A[ci], A[i]
            i = ci
        else:
            break


def heap_sort(A):
    H = make_max_heap(A)
    S = []
    while H:
        H[0], H[-1] = H[-1], H[0]
        S.append(H.pop())
        sink_down(H, 0)
    return reversed(S)


n = int(ifs.readline())
A = numbers_from_line()
S = heap_sort(A)
ofs.write('%s\n' % ' '.join(map(str, S)))
