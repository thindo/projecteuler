#!/usr/bin/env python3
#
# Solution to Project Euler problem 1
# Copyright (c) ThinDo. All rights reserved.
#
# https://github.com/thindo/projecteuler
#

print(sum(x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)))
