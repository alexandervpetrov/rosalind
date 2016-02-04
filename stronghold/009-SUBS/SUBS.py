#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


s = ifs.readline().strip()
t = ifs.readline().strip()

P = []
beg = 0
while beg < len(s):
    p = s.find(t, beg)
    if p == -1:
        break
    else:
        P.append(p + 1)
        beg = p + 1


ofs.write('%s\n' % (' '.join(map(str, P))))
