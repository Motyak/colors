#!/usr/bin/env python3
from c2 import compareHexColors

from functools import cmp_to_key

def nbToHexColor(nb):
    return '#%06d' % nb

def sumOfDigits(n):
    return sum([int(i) for i in str(n)])

seq = [i*999999//91 for i in range(1,91) if i%10!=0 and sumOfDigits(i)<10]
hexColors = [*map(nbToHexColor, seq)]
sortedHexColors = [*sorted(hexColors, key=cmp_to_key(compareHexColors))]

for c in sortedHexColors:
    print(c)
