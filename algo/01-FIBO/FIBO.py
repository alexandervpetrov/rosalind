#!/usr/bin/env python

import sys
import functools

ifs = sys.stdin
ofs = sys.stdout


@functools.lru_cache()
def fib_recursive_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive_dp(n - 1) + fib_recursive_dp(n - 2)


def fib_generator():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, (f1 + f2)


def fib(n):
    f1 = 0
    f2 = 1
    for __ in range(n):
        f1, f2 = f2, (f1 + f2)
    return f1


n = int(ifs.readline())

fn1 = fib_recursive_dp(n)

for k, fk in enumerate(fib_generator()):
    if k == n:
        break
fn2 = fk

fn3 = fib(n)

assert fn1 == fn2
assert fn1 == fn3

fn = fn1

ofs.write(str(fn))
ofs.write('\n')
