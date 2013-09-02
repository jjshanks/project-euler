# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# NOTE: See path_printer.py for more interesting code around this problem

import math

# 40!/(20! * 20!)
print math.factorial(40)/(math.factorial(20)*math.factorial(20))
