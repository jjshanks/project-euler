# https://projecteuler.net/problem=27
#
# Euler discovered the remarkable quadratic formula:
#
# n^2+ n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2+ 41 + 41 is clearly divisible by 41.
#
# The incredible formula  n^2. 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, .79 and 1601, is .126479.
#
# Considering quadratics of the form:
#
# n^2+ an + b, where |a| < 1000 and |b| < 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |.4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *

primes = []
max_primes = 0
max_product = 0
for a in xrange(-999,999):
    for b in xrange(-999,999):
        prime = True
        n = 0
        while prime:
            result = n ** 2 +  a * n + b
            if result < 2:
                break
            if is_prime(result):
                n += 1
            else:
                prime = False
        if n > max_primes:
            max_primes = n
            max_product = a * b

print max_product
