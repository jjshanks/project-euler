import math

# returns the sum of the diviros for the given number
# example: 12 would return 1 + 2 + 3 + 4 + 6 = 16
def sum_divisors(num):
    root = int(math.floor(math.sqrt(num)))
    total = 0
    for d in xrange(1, root + 1):
        if num % d == 0:
            total += d + num / d
    if root * root == num:
        total -= root
    return total - num

