#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


n = int(ifs.readline())

f_cur = 0
f_next = 1
for __ in xrange(n):
    f_cur, f_next = f_next, f_cur+f_next


ofs.write('%d\n' % (f_cur))
