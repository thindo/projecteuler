#!/usr/bin/env python3
#
# Solution to Project Euler problem 23
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
A perfect number is a number for which the sum of its proper divisors
is exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
s the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers
which cannot be written as the sum of two abundant numbers.

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
    abundant = set()
    for n in range(1, target + 1):
        if get_deficient(n) > n:
            abundant.add(n)
        if not any((n - a in abundant) for a in abundant):
            s += n
    return s


def main():
    print(solve(20161))


if __name__ == "__main__":
    main()
