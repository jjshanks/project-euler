# Since problem 15 is just a permutation problem I wanted to do something a little different. This code prints all the paths
# that can be take through the latice. While it would for solving the problem it is to slow to be useful.

# From http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# 1) Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
# 2) Find the largest index l such that a[k] < a[l].
# 3) Swap the value of a[k] with that of a[l].
# 4) Reverse the sequence from a[k + 1] up to and including the final element a[n].
import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *

size = 3
if len(sys.argv) >= 2:
    size = int(sys.argv[1])

path = list("d" * size + "r" * size)

found = True

while path != None:
    print path
    path = lex_permut(path)

