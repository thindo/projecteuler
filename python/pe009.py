#!/usr/bin/env python3
#
# Solution to Project Euler problem 9
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def solve(target):
    for n in range(1, 100):
        for m in range(n + 1, 100):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == target:
                return (a * b * c)


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
