# https://projecteuler.net/problem=19
# You are given the following information, but you may prefer to do some research for yourself.
#
# * 1 Jan 1900 was a Monday.
# * Thirty days has September,
#   April, June and November.
#   All the rest have thirty-one,
#   Saving February alone,
#   Which has twenty-eight, rain or shine.
#   And on leap years, twenty-nine.
# * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# http://en.wikipedia.org/wiki/Doomsday_rule
# tl;dr for a years doomsday subtract the difference in days from a well known date that always falls on a 
# a doomsday and the date in question then mod 7 to get the day of week where Sunday = 0

common_days = [0, 3, 28, 14, 4, 9, 6, 4, 8, 5, 10, 7, 12]
leap_days = [0, 4, 29, 14, 4, 9, 6, 4, 8, 5, 10, 7, 12]

def get_anchor_date(year):
  return 5 * (year/100 % 4) % 7 + 2

def get_doomsday(year):
  # odd + 11
  t = year % 100
  if t & 1 == 1:
    t += 11
  t /= 2
  if t & 1 == 1:
    t += 11
  return (get_anchor_date(year) + 7 - (t % 7)) % 7

def leap_year(year):
  if year % 400 == 0:
    return True
  if year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  return False

def get_dow(year, month, day):
  if leap_year(year):
    known_day = leap_days[month]
  else:
    known_day = common_days[month]
    
  doomsday = get_doomsday(year)
  diff_days = known_days - day
  return doomsday - diff_days % 7

total_sundays = 0

for y in xrange(1901, 2001):
  for m in xrange(1,13):
    if get_dow(y,m,1) == 0:
      total_sundays += 1

print total_sundays
