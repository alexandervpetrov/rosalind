#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import Counter


s = ifs.readline().strip()

C = Counter(s)

a = C['A']
c = C['C']
g = C['G']
t = C['T']

ofs.write('%d %d %d %d\n' % (a, c, g, t))
