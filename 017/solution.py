# http://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

sub20 = ["","one","two","three","four","five","six","seven","eight","nine",
            "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
sub100 = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

# This only work for numbers of 1000 or less
def numWordLength(num):
    parts = []
    if num == 1000:
        return len("onethousand")
    # find hundred's spelling
    if num >= 100:
        parts.append(sub20[num / 100] + "hundred")
        # if not an even hundred we need an and
        if num % 100 != 0:
            parts.append("and")

    hundred_part = num % 100
    if hundred_part < 20 and hundred_part > 0:
        parts.append(sub20[hundred_part])
    else:
        parts.append(sub100[hundred_part / 10] + sub20[hundred_part % 10])

    # sum all calculated parts for total
    return sum(len(s) for s in parts)

total = 0
for i in xrange(1,1001):
    total += numWordLength(i)

print total
