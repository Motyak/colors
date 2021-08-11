#!/usr/bin/env python3
from c import nmToRgb

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976

#!/usr/bin/env python3

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

if __name__ == '__main__':
    print(_hexColorToRgb("#175824"))
    print(_compareRgb((46,209,192), (32,203,230)))
    print(closestWavelength("#175824"))



