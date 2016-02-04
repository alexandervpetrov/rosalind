#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


from itertools import izip


S = ifs.readline().strip()
T = ifs.readline().strip()

hamm = sum((1 if s != t else 0) for s, t in izip(S, T))

ofs.write('%d\n' % (hamm))
