#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


a, b = numbers_from_line()

s = 0
for x in xrange(a, b+1):
    if x % 2 != 0:
        s += x

ofs.write('%d\n' % (s))
