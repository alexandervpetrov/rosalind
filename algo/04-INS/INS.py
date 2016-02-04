#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n = int(ifs.readline())
A = numbers_from_line()

# according to site, following can be improved to O(n*log(n))

def insertion_sort_lazy_to_think(A):
    swaps = 0
    for i in xrange(1, n):
        k = i
        while k > 0 and A[k] < A[k-1]:
            A[k-1], A[k] = A[k], A[k-1]
            swaps += 1
            k -= 1
    return swaps


swaps = insertion_sort_lazy_to_think(A)


ofs.write('%d\n' % swaps)
