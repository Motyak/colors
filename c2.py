#!/usr/bin/env python3
from c import nmToHsl

from colorsys import rgb_to_hls

# hex string to HSL
def _hexColorToHsl(str):
    tmp = str[1:7]
    red = int(tmp[:2], 16) / 256
    green = int(tmp[2:4], 16) / 256
    blue = int(tmp[4:6], 16) / 256
    hls = rgb_to_hls(red, green, blue)

    # hls to proper hsl
    return (hls[0] * 360, hls[2] * 100, hls[1] * 100)

def _compareHsl(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

COLOR_RANGE_HSL = [nmToHsl(i) for i in range (380, 781)]

# fonction qui retourne la longueur d'onde la plus proche du code hex
def closestWavelength(hexColor):
    hslInput = _hexColorToHsl(hexColor)
    closestHsl = (-1, -1, -1)
    closestWavelength = -1
    smallestDiff = 999999
    
    for index, c in enumerate(COLOR_RANGE_HSL):
        diff = _compareHsl(hslInput, c)
        if diff < smallestDiff:
            closestHsl = c
            closestWavelength = index + 380
            smallestDiff = diff

    return closestWavelength

# Je me fais un kif

def nbToHexColor(nb):
    return '#%06d' % nb

def sumOfDigits(n):
    return sum([int(i) for i in str(n)])

if __name__ == '__main__':
    # print(_hexColorToHsl("#142857"))
    # print(_compareHsl(nmToHsl(500), nmToHsl(382)))
    # print(closestWavelength("#175824"))

    seq = [i*999999//91 for i in range(1,91) if i%10!=0 and sumOfDigits(i)<10]
    seq = [*map(nbToHexColor, seq)]

    for i in seq:
        print(i, closestWavelength(i))



