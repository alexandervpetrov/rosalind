#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

from collections import Counter


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


s = ifs.readline().strip()
words = s.split()
C = Counter(words)

for k, c in C.iteritems():
    ofs.write('%s %d\n' % (k, c))
