# http://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# This solution is a modification of the sieve solution for problem 3

max_value = 2000000
total = 0

lookup = [1] * max_value

for i in xrange(2, max_value):
  # skip known non primes
  if lookup[i] == 0:
    continue
  total += i
  # mark all multiples as not prime
  for mark in xrange(i * 2, max_value, i):
    lookup[mark] = 0  

print total
