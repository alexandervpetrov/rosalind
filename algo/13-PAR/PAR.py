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


def partition_by_first(A):
    n = len(A)
    p = 0
    a = A[p]
    for i in xrange(1, n):
        if A[i] <= a:
            A[p], A[i] = A[i], A[p]
            A[p+1], A[i] = A[i], A[p+1]
            p += 1
    return A


C = partition_by_first(A)

ofs.write('%s\n' % ' '.join(map(str, C)))
