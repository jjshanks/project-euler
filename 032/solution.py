# https://projecteuler.net/problem=32
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# 
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *

pandigitals = set()
for i in xrange(1,2000):
    for j in xrange(2000,1,-1):
        s = str(i*j) + str(i) + str(j)
        if len(s) < 9:
            continue
        if len(s) == 9 and len(set(list(s))) == 9:
            if '0' not in s:
                pandigitals.add(i*j)

total = 0
for x in pandigitals:
    total += x

print total
