#!/usr/bin/env python3
#
# Solution to Project Euler problem 4
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#

'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


def solve():
    largest = max(
            i * j
            for i in range(100, 1000)
            for j in range(100, 1000)
            if str(i * j) == str(i * j)[:: -1])
    return largest


def main():
    print(solve())


if __name__ == "__main__":
    main()
