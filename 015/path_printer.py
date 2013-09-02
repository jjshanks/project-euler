# Since problem 15 is just a permutation problem I wanted to do something a little different. This code prints all the paths
# that can be take through the latice. While it would for solving the problem it is to slow to be useful.

# From http://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# 1) Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
# 2) Find the largest index l such that a[k] < a[l].
# 3) Swap the value of a[k] with that of a[l].
# 4) Reverse the sequence from a[k + 1] up to and including the final element a[n].

import sys

size = 3
if len(sys.argv) >= 2:
    size = int(sys.argv[1])

path = list("d" * size + "r" * size)

found = True

while found:
    found = False
    for k in xrange(len(path)-2, -1, -1):
        # step 1
        if path[k] < path[k+1]:
            for l in xrange(len(path)-1, -1, -1):
                # step 2
                if path[k] < path[l]:
                    print path
                    found = True
                    # step 3
                    tmp = path[k]
                    path[k] = path[l]
                    path[l] = tmp
                    # step 4
                    path = path[0:k + 1] + path[-1:k:-1]
                    break
            if found:
                break

print path
