# https://projecteuler.net/problem=22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

from heapq import *

def alpha_value(string):
    total = 0
    for l in list(string):
        total += ord(l) - 64
    return total

value_map = {}
heap = []

f = open("names.txt")
names = f.read().split(",")
for name in names:
    value_map[name] = alpha_value(name[1:-1])
    heappush(heap, name)

total = 0
position = 1
while heap:
    name = heappop(heap)
    total += position * value_map[name]
    position += 1

print total
