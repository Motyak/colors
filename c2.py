#!/usr/bin/env python3
from c import nmToHsl

from colorsys import rgb_to_hls
from colormath.color_objects import HSLColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976

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
    # return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])
    hsl1 = HSLColor(a[0] / 360, hsl_s=a[1] / 100, hsl_l=a[2] / 100)
    hsl2 = HSLColor(b[0] / 360, hsl_s=b[1] / 100, hsl_l=b[2] / 100)
    lab1 = convert_color(hsl1, LabColor)
    lab2 = convert_color(hsl2, LabColor)
    return delta_e_cie1976(lab1, lab2)

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
    print(_hexColorToHsl("#175824"))
    print(_compareHsl((132,59,22), (222,63,21)))
    print(closestWavelength("#175824"))



