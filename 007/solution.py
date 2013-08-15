# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

# DEV NOTES
# brute force solution took ~90 seconds
# only checking odds dropped the solution down to ~45 seconds
# only checking known primes less than the square root of the test gives a runtime of ~2 seconds
# breaking after finding the first divisable prime makes the runtime ~0.5 seconds
#   side note: testing all numbers (not just odd) gives the same approx run time
import math

# populate initial list of primes
primes = [2]
# total known primes at start is 1
total = 1
# the next test candidate is 3
test = 3
while total < 10001:
  prime = True
  for x in primes:
    # don't test above the square root of the value
    if x > math.sqrt(test):
      break
    # if divisable by a prime stop checking
    if test % x == 0:
      prime = False
      break
  # if no divisors found add to known list
  if prime:
    primes.extend([test])
    total += 1
  # only test odd numbers
  test += 2

print primes.pop()
