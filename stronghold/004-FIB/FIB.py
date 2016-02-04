#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


n, k = numbers_from_line()

f_cur = 1
f_next = 1
for __ in xrange(n-1):
    f_cur, f_next = f_next, k*f_cur+f_next


ofs.write('%d\n' % (f_cur))
