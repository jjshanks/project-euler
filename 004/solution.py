# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
  return str(number) == str(number)[::-1]

max_value = 0
# only check 3 digit numbers
for left in xrange(999, 99, -1):
  # only check 3 digit numbers less than left side
  for right in xrange(left - 1, 99, -1):
    result = left * right
    # if the result is less than the current max break because value will only decrease
    if result < max_value:
      break
    if isPalindrome(result):
      max_value = max(result, max_value)

print max_value
