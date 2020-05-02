#!/usr/bin/env python3
#
# Solution to Project Euler problem 11
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
This script solves the Project Euler problem "Lattice paths". The problem
is: How many such routes are there through a 20x20 grid?
'''
import math


def solve(grid_size):
    size = grid_size
    routes = math.factorial(size + size) / math.pow(math.factorial(size), 2)
    return int(routes)


def main():
    # Constants
    GRID_SIZE = 20
    print(solve(GRID_SIZE))


if __name__ == "__main__":
    main()
