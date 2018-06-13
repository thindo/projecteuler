#!/usr/bin/env python3
#
# Solution to Project Euler problem 48
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''
import math


def get_deficient(n):
    s = 0
    t = math.sqrt(n)
    s = -t if t.is_integer() else 1

    for i in range(2, int(t)+1):
        if n % i == 0:
            s += i + n/i
    return s


def solve(target):
    s = 0
    for i in range(1, target + 1):
        s += i**i
    return s % 10**10


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
