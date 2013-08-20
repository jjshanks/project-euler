# http://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

found = False

# test all a's from 1 to 999
for a in xrange(1, 1000):
  # test all b's from 1000 to (a + 1)
  for b in xrange(1000, a, -1):
    c = math.sqrt(a ** 2 + b ** 2)
    if a + b + c == 1000:
      found = True
      break
  if found:
    break
  
print a * b * int(c)
