#!/usr/bin/env python

import sys

ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [
        int(s)
        for s in ifs.readline().strip().split(d)
        if len(s.strip()) > 0
    ]


a, b = numbers_from_line()

s = sum(
    x
    for x in range(a, b+1)
    if x % 2 != 0
)

ofs.write('{}\n'.format(s))
