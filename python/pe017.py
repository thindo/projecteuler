#!/usr/bin/env python3
#
# Solution to Project Euler problem 17
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''

single_word = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
    'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ten_place = [
    '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety']


def english_number(n):
    if 0 <= n < 20:
        return single_word[n]
    elif 20 <= n < 100:
        return (
            ten_place[n // 10] +
            (single_word[n % 10] if n % 10 != 0 else ''))
    elif 100 <= n < 1000:
        return (
            single_word[n // 100] + 'hundred' +
            (('and' + english_number(n % 100)) if n % 100 != 0 else ''))
    elif 1000 <= n < 1000000:
        return (
            english_number(n // 1000) + 'thousand' +
            (english_number(n % 1000) if n % 1000 != 0 else ''))
    else:
        raise ValueError()


def solve(target):
    return sum(len(english_number(i)) for i in range(1, 1001))


def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
