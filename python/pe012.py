#!/usr/bin/env python3
#
# Solution to Project Euler problem 11
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
This script solves the Project Euler problem "Highly divisible triangular
number". The problem is: What is the value of the first triangle number to
have over five hundred divisors?
'''
import math


def get_factors(number):
    """Get all factors of a number"""

    factors = [1, number]

    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            factors.extend([i, number / i])

    return(factors)


def solve(num_divisor):
    """Highly divisible triangular number"""

    ordinal = 1
    triangle_number = 1
    num_factors = 1

    while num_factors <= num_divisor:
        ordinal += 1
        triangle_number += ordinal
        num_factors = len(get_factors(triangle_number))

    return triangle_number


def main():
    # Constants
    NUM_DIVISOR = 500
    print(solve(NUM_DIVISOR))


if __name__ == "__main__":
    main()
