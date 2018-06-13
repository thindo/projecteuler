#!/usr/bin/env python3
#
# Solution to Project Euler problem 16
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

'''


def solve(target):
    #  Using  built-in arbitrary precision integer type
    return sum(int(c) for c in str(target))


def main():
    print(solve(2**1000))


if __name__ == "__main__":
    main()
