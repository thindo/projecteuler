#!/usr/bin/env python3
#
# Solution to Project Euler problem 10
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def solve(target):
    prime_sum = [0]*(target + 2)
    s = 0
    for i in range(2, target + 2):
	    if prime_sum[i] == 0:
		    s += i
		    prime_sum[i::i] = [-1]*((target + 1)//i)
	    prime_sum[i] = s
    return prime_sum[target]  


def main():
    print(solve(2000000))


if __name__ == "__main__":
    main()
