#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


s = ifs.readline().strip()
a, b, c, d = numbers_from_line()

s1 = s[a:b+1]
s2 = s[c:d+1]

ofs.write('%s %s\n' % (s1, s2))
