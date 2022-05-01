#!/usr/bin/env python

import sys
import collections

ifs = sys.stdin
ofs = sys.stdout


s = ifs.readline().strip()
words = s.split()
C = collections.Counter(words)

for k, c in C.items():
    ofs.write('{} {}\n'.format(k, c))
