# http://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage

# NOTE: This is an alternative solution where the string lengths are calculated just once. There is no noticeable difference in run time though.

sub20 = [len(""),len("one"),len("two"),len("three"),len("four"),len("five"),len("six"),len("seven"),len("eight"),len("nine"),
            len("ten"),len("eleven"),len("twelve"),len("thirteen"),len("fourteen"),len("fifteen"),len("sixteen"),len("seventeen"),len("eighteen"),len("nineteen")]
sub100 = [len(""), len(""), len("twenty"),len("thirty"),len("forty"),len("fifty"),len("sixty"),len("seventy"),len("eighty"),len("ninety")]

# This only work for numbers of 1000 or less
def numWordLength(num):
    if num == 1000:
        return 11 # len("onethousand")

    total = 0

    if num >= 100:
        total += sub20[num / 100] + 7 # len("hundred")
        if num % 100 != 0:
            total += 3 # len("and")
    hundred_part = num % 100
    if hundred_part < 20 and hundred_part > 0:
        total += sub20[hundred_part]
    else:
        total += sub100[hundred_part / 10] + sub20[hundred_part % 10]
    return total

total = 0
for i in xrange(1,1001):
    total += numWordLength(i)

print total
