# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#   1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

MAX_VALUE = 4000000 # 4 million

def fibonacci_generator():
  a,b = 1,1 
  while True:
    a,b = b, a+b
    yield a

fib = fibonacci_generator()

total = 0
for number in fib:
  if number > MAX_VALUE:
    break
  if number % 2 == 0:
    total += number

print total
