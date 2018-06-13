#!/usr/bin/env python3
#
# Solution to Project Euler problem 22
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working
out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import string


def calc_score(index, name):
    return sum([string.ascii_uppercase.index(n) + 1 for n in name]) * index


def solve():
    with open('p022_names.txt', 'rt') as f:
        names = sorted([n.strip('"') for n in f.read().split(',')])
    return sum([
        calc_score(index + 1, name)
        for (index, name) in enumerate(names)])


def main():
    print(solve())


if __name__ == "__main__":
    main()
