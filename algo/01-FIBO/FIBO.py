#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


n = int(ifs.readline())

f_cur = 0
f_next = 1
for __ in range(n):
    f_cur, f_next = f_next, f_cur + f_next

ofs.write('{}\n'.format(f_cur))
