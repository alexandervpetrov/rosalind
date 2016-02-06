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
m = int(ifs.readline())
B = numbers_from_line()


def merge_sorted(A, B):
    C = []
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    if i < n:
        C.extend(A[i:])
    if j < m:
        C.extend(B[j:])
    return C


C = merge_sorted(A, B)

ofs.write('%s\n' % ' '.join(map(str, C)))
