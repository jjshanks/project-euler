# https://projecteuler.net/problem=21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math

# Taken from #12
def sum_divisors(num):
    root = int(math.ceil(math.sqrt(num)))
    total = 0
    for d in xrange(1, root + 1):
        if num % d == 0:
            total += d + num / d
    if root * root == num:
        total -= root
    return total - num

mapping = {}
for i in xrange(1, 10001):
    mapping[i] = sum_divisors(i)

total = 0
for a in xrange(2,10001):
    # discard about 10,000
    if mapping[a] > 10000 or mapping[a] <= 1 or mapping[mapping[a]] > 10000:
        continue
    # discard numbers that map to themselves
    if mapping[a] == mapping[mapping[a]]:
        continue
    b = mapping[a]
    # test for amicable pair
    if a != b and mapping[b] == a:
        total += a

print total
