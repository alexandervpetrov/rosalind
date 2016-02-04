#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


k, m, n = numbers_from_line()


N = float(k + m + n)
N1 = N - 1

P_AA = k / N
P_Aa = m / N
P_aa = n / N

P = 0
P += P_AA
P += P_Aa * (k/N1 + (m-1)/N1 * 3/4 + n/N1 * 1/2)
P += P_aa * (k/N1 + m/N1 * 1/2)


ofs.write('%.6f\n' % (P))
