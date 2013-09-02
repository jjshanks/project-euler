# https://projecteuler.net/problem=14
# The following iterative sequence is defined for the set of positive integers:
 
# n . n/2 (n is even)
# n . 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# cache already computed values
cache = {1:1}
max_number = 0
max_chain = 0

for number in xrange(2,1000001):
    k = number
    # track the actul steps in the chain
    steps = [number]

    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1

        steps.append(number)

        # use alrady calculated value if found
        if cache.has_key(number):
            break
   
    total_steps = len(steps) + cache[number]

    # for each new step add it the cache with its chain length
    for i in xrange(0, len(steps)):
        cache[steps[i]] = total_steps - i

    if max_chain < total_steps:
        max_chain = total_steps
        max_number = k

print max_number
