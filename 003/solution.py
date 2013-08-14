# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

target = 600851475143

# find the max prime factor
max_prime_factor = math.sqrt(target)
max_prime_factor = int(math.floor(max_prime_factor))

primes = []

# build initial 1 based sieve 
lookup = [1] * max_prime_factor

# Build seive
for i in xrange(2, max_prime_factor):
  # if not prime don't mark multiples
  if lookup[i] == 0:
    continue
  # add to prime list
  primes += [i]
  # mark all multiples of the found prime as not prime
  for mark in xrange(i * 2, max_prime_factor, i):
    lookup[mark] = 0

# for each found prime in reverse order check if it is a multiple of the target
for prime in primes[::-1]:
  if target % prime == 0:
    print prime
    break
