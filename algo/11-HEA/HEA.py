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


def make_max_heap(A):

    def parent(i):
        return (i-1)/2

    def bubble_up(H, i):
        while i > 0 and H[parent(i)] < H[i]:
            H[parent(i)], H[i] = H[i], H[parent(i)]
            i = parent(i)

    H = []
    for a in A:
        H.append(a)
        bubble_up(H, len(H)-1)
    return H


H = make_max_heap(A)

ofs.write('%s\n' % ' '.join(map(str, H)))
