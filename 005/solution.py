# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

max_value = 20

# return the product of the values to the powers of the same index
def applyPowers(values, powers):
  total = 1
  for (v,m) in zip(values, powers):
    total *= v ** m
  return total

# increment power values till they would otherwise exceed the max number you want to divide by (max_value)
def incrementPowers(values, powers, max_value):
  for index, value in enumerate(values):
    while values[index] ** (powers[index] + 1) < max_value:
      powers[index] += 1

primes = [2,3,5,7,11,13,17,19]
powers = [1] * len(primes)

incrementPowers(primes, powers, max_value)
print applyPowers(primes, powers)
