# -*- coding: utf-8 -*-
# https://projecteuler.net/problem=31
#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1x1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#How many different ways can £2 be made using any number of coins?

import os, sys, inspect
cmd_folder = os.path.dirname(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0])))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from euler_helpers import *

coins = [1,2,5,10,20,50,100,200]

def sub_coin(value, start):
    total = 0
    for coin in coins:
        if coin <= start:
            # if coin would result in negative skip
            if value < coin:
                continue
            # if coin is equal to reminder return total + 1
            elif value == coin:
                total += 1
            else:
                total += sub_coin(value - coin, coin)
        else:
            break
    return total

print sub_coin(200,200)
