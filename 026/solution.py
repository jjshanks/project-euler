# https://projecteuler.net/problem=26
#
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 
# 1/2 =   0.5
# 1/3 =   0.(3)
# 1/4 =   0.25
# 1/5 =   0.2
# 1/6 =   0.1(6)
# 1/7 =   0.(142857)
# 1/8 =   0.125
# 1/9 =   0.(1)
# 1/10    =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *

# 1/d = x = 0.qqqq... where q is the repeating part of the number
# To find q we need to solve for n in the simplified formula x = q/(10^n-1)
# example 1/7 = 142857/(10^6-1) = 142857/999999 or where (10^n-1) % d == 0

longest = 0
value = 0
for d in xrange(6,1000):
    # multiplying the denominator by 2 or 5 doesn't change the period of repeating decimals
    if d % 5 == 0 or d % 2 == 0:
        continue
    base = 9
    while(base % d > 0):
        base = base * 10 + 9
    if len(str(base)) > longest:
        longest = len(str(base))
        value = d

print value
