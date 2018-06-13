#!/usr/bin/env python3
#
# Solution to Project Euler problem 21
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220
are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


def sum_divisors(number):
    return sum(
        [n for n in range(1, number)
            if number % n == 0]
        )


def solve(target):
    result = 0
    for i in range(1, target):
        m = sum_divisors(i)
        if m != i and sum_divisors(m) == i:
            result += i
    return result


def main():
    print(solve(10000))


if __name__ == "__main__":
    main()
