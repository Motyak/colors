#!/usr/bin/env python3
from c2 import closestWavelength

def _nbToHexColor(nb):
    return '#%06d' % nb

def _sumOfDigits(n):
    return sum([int(i) for i in str(n)])

seq = [i*999999//91 for i in range(1,91) if i%10!=0 and _sumOfDigits(i)<10]
hexColors = [*map(_nbToHexColor, seq)]
sortedHexColors = [*sorted(hexColors, key=closestWavelength)]

print(sortedHexColors)
