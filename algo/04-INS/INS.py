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


def run_insertion_sort(A):
    swaps = 0
    for i in range(1, n):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A[k-1], A[k] = A[k], A[k-1]
            swaps += 1
            k -= 1
    return swaps


n = int(ifs.readline())
A = numbers_from_line()

swaps = run_insertion_sort(A)

ofs.write(str(swaps))
ofs.write('\n')
