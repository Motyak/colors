#!/usr/bin/env python3
from c import nmToRgb

from colorsys import rgb_to_hls
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976
from functools import cmp_to_key

# hex string to HSL
def _hexColorToHsl(str):
    tmp = str[1:7]
    red = int(tmp[:2], 16) / 256
    green = int(tmp[2:4], 16) / 256
    blue = int(tmp[4:6], 16) / 256
    hls = rgb_to_hls(red, green, blue)

    # hls to proper hsl
    return (hls[0] * 360, hls[2] * 100, hls[1] * 100)

# hex string to RGB
def _hexColorToRgb(str):
    tmp = str[1:7]
    red = int(tmp[:2], 16)
    green = int(tmp[2:4], 16)
    blue = int(tmp[4:6], 16)
    return (red, green, blue)

# a and b are rgb values (0-255)
def _compareRgb(a, b):
    rgb1 = sRGBColor(a[0], a[1], a[2], True)
    rgb2 = sRGBColor(b[0], b[1], b[2], True)
    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)
    return delta_e_cie1976(lab1, lab2)

# wavelength converted to sRGB
COLOR_RANGE_RGB = [nmToRgb(i) for i in range (380, 781)]

# fonction qui retourne la longueur d'onde la plus proche du code hex
def closestWavelength(hexColor):
    rgbInput = _hexColorToRgb(hexColor)
    closestRgb = (-1, -1, -1)
    closestWavelength = -1
    smallestDiff = 999999
    
    for index, c in enumerate(COLOR_RANGE_RGB):
        diff = _compareRgb(rgbInput, c)
        if diff < smallestDiff:
            closestRgb = c
            closestWavelength = index + 380
            smallestDiff = diff

    return closestWavelength

# where a and b are both pair items with hex color & wavelength
def compareColors(a, b):
    # d'abord la longueur d'onde la plus proche
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

def _nbToHexColor(nb):
    return '#%06d' % nb

def _sumOfDigits(n):
    return sum([int(i) for i in str(n)])

seq = [i*999999//91 for i in range(1,91) if i%10!=0 and _sumOfDigits(i)<10]
colors = {key: closestWavelength(key) for key in [*map(_nbToHexColor, seq)]}
sortedColors = {k: v for k,v in sorted(colors.items(), key=cmp_to_key(compareColors))}

# print(closestWavelength("#142857"))

for k,v in sortedColors.items():
    print(k)
    # print(k, v)



