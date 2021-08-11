#!/usr/bin/env python3
from c import nmToHex
from c2 import _hexColorToHsl, closestWavelength

from functools import cmp_to_key

def nbToHexColor(nb):
    return '#%06d' % nb

def sumOfDigits(n):
    return sum([int(i) for i in str(n)])

# where a and b are both pair items with hex color & wavelength
def compareColor(a, b):
    # d'abord la longueur d'onde
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    # puis la valeur hue
    if _hexColorToHsl(a[0])[0] > _hexColorToHsl(b[0])[0]:
        return 1
    if _hexColorToHsl(a[0])[0] < _hexColorToHsl(b[0])[0]:
        return -1
    # puis la valeur saturation
    if _hexColorToHsl(a[0])[1] > _hexColorToHsl(b[0])[1]:
        return 1
    if _hexColorToHsl(a[0])[1] < _hexColorToHsl(b[0])[1]:
        return -1
    # et enfin la valeur lightness
    if _hexColorToHsl(a[0])[2] > _hexColorToHsl(b[0])[2]:
        return 1
    if _hexColorToHsl(a[0])[2] < _hexColorToHsl(b[0])[2]:
        return -1
    return 0



seq = [i*999999//91 for i in range(1,91) if i%10!=0 and sumOfDigits(i)<10]
colors = {key: closestWavelength(key) for key in [*map(nbToHexColor, seq)]}
sortedColors = {k: v for k,v in sorted(colors.items(), key=cmp_to_key(compareColor))}

for k,v in sortedColors.items():
    # print(k)
    print(k, v)
    # print(nmToHex(v))

