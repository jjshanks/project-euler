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

# From http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# 1) Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
# 2) Find the largest index l such that a[k] < a[l].
# 3) Swap the value of a[k] with that of a[l].
# 4) Reverse the sequence from a[k + 1] up to and including the final element a[n].
#
# Returns a permutated list unless there are no permutations left then None is returned
def lex_permut(chars):
    for k in xrange(len(chars)-2, -1, -1):
        # step 1
        if chars[k] < chars[k+1]:
            for l in xrange(len(chars)-1, -1, -1):
                # step 2
                if chars[k] < chars[l]:
                    # step 3
                    tmp = chars[k]
                    chars[k] = chars[l]
                    chars[l] = tmp
                    # step 4
                    return chars[0:k + 1] + chars[-1:k:-1]
    return None

# Simple prime checker
def is_prime(num):
    if num < 2:
        return False
    if num > 2 and num % 2 == 0:
        return False
    if num == 2:
        return True
    for n in xrange(3, int(math.ceil(math.sqrt(num)) + 1), 2):
       if num % n == 0:
           return False
    return True

