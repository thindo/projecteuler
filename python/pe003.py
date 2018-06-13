#!/usr/bin/env python3
#
# Solution to Project Euler problem 3
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def solve(target):
    factor = 1
    while factor < target:
        factor += 2
        while target % factor == 0:
            target /= factor
    return factor


def main():
    print(solve(600851475143))


if __name__ == "__main__":
    main()
