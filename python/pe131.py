#!/usr/bin/env python3
#
# Solution to Project Euler problem 11
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
This script solves the Project Euler problem "Prime cube partnership". The
problem is: How many primes below one million have this remarkable property?
'''
import math


def is_prime(num):
    """Test if number is prime"""

    if num == 1:      # 1 isn't prime
        return False
    if num < 4:       # 2 and 3 are prime
        return True
    if num % 2 == 0:  # Even numbers aren't prime
        return False
    if num < 9:       # 5 and 7 are prime
        return True
    if num % 3 == 0:  # Numbers divisible by 3 aren't prime
        return False

    num_sqrt = int(math.sqrt(num))
    factor = 5
    while factor <= num_sqrt:
        if num % factor == 0:        # Primes greater than three are 6k-1
            return False
        if num % (factor + 2) == 0:  # Or 6k+1
            return False
        factor += 6
    return True


def solve(limit):
    """Prime cube partnership"""

    count = 0

    n = 1
    while True:
        n += 1
        diff = n * n * n - (n - 1) * (n - 1) * (n - 1)
        if diff > limit:
            break
        if is_prime(diff):
            count += 1

    return count


def main():
    # Constants
    LIMIT = 1000000
    print(solve(LIMIT))


if __name__ == "__main__":
    main()
