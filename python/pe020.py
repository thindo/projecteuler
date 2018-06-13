#!/usr/bin/env python3
#
# Solution to Project Euler problem 20
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def solve(target):
    return sum([
        int(number)
        for number in list(str(factorial(100)))])


def main():
    print(solve(100))


if __name__ == "__main__":
    main()
