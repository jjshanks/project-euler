# https://projecteuler.net/problem=24
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *
import math

chars = ['0','1','2','3','4','5','6','7','8','9']
ans = []

target = 1000000
# 0 as the first digit is the first 362880 (9!) numbers
# 362880 goes wholly into 1,000,000 twice so we grab
# index 2 which is '2' as the first digiti and remove
# it as a candidate. Then continue the process with 8!
# down to 0!
for i in xrange(9,-1,-1):
    char_idx = 0
    base = math.factorial(i)
    while target > base:
        target -= base
        char_idx += 1
    ans.append(chars.pop(char_idx))

print "".join(ans)
