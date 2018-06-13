#!/usr/bin/env python3
#
# Solution to Project Euler problem 18
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
][::-1]


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
    print(solve(triangle))


if __name__ == "__main__":
    main()
