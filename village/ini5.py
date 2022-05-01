#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


n = 1
for line in ifs:
    if n % 2 == 0:
        ofs.write(line)
    n += 1
