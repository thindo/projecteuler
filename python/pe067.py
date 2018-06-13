#!/usr/bin/env python3
#
# Solution to Project Euler problem 67
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt
(right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
It is not possible to try every route to solve this problem,
as there are 299 altogether! If you could check one trillion (1012)
routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)

'''


def max_path(list_):
    if len(list_) <= 1:
        return list_[0][0]
    for index, num in enumerate(list_[1]):
        list_[0][index] = num + max(list_[0][index: index + 2])
    del list_[0][len(list_[0]) - 1]
    del list_[1]
    return max_path(list_)


def solve(triangle):
    return max_path(triangle)


def main():
    with open('p067_triangle.txt', 'rt') as f:
        triangle = [
            [int(n) for n in l.strip().split()]
            for l in f.readlines()][::-1]
    print(solve(triangle))


if __name__ == "__main__":
    main()
