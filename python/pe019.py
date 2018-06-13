#!/usr/bin/env python3
#
# Solution to Project Euler problem 19
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
You are given the following information,
but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4,
    but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''
from calendar import monthrange
from itertools import product


def solve():
    return (len([(year, month) for year, month in
            product(range(1901, 2001), range(1, 13))
            if monthrange(year, month)[0] == 6]))


def main():
    print(solve())


if __name__ == "__main__":
    main()
