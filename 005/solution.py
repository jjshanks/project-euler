# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def applyPowers(values, powers):
  total = 1
  for (v,m) in zip(values, powers):
    total *= v ** m
  return total

primes = [2,3,5,7,11,13,17,19]
powers = [4,2,1,1, 1, 1, 1, 1]

print applyPowers(primes, powers)
