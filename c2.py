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

def compareHexColors(a, b):
    RANGES = range(0, 361, 30)
    hsl1, hsl2 = _hexColorToHsl(a), _hexColorToHsl(b)

    if hsl1[0] > hsl2[0]:
        return 1
    elif hsl1[0] < hsl2[0]:
        return -1
    else:
        return 0

    # # if they're in the same range (each 30°)
    # for i in RANGES:
    #     if hsl1[0]>=i and hsl1[0]<i+30 and hsl2[0]>=i and hsl2[0]<i+30:
    #         if hsl1[0]>hsl2[0]:
    #             return 1
    #         elif hsl1[0]<hsl2[0]:
    #             return -1
    #         else:
    #             return 0
    # # otherwise compare lightness
    # if hsl1[1]>hsl2[1]:
    #     return 1
    # elif hsl1[1]<hsl2[1]:
    #     return -1 
    # else:
    #     return 0
    # # otherwise compare saturation
    # if hsl1[2]>hsl2[2]:
    #     return 1
    # if hsl1[2]<hsl2[2]:
    #     return -1
    # else:
    #     return 0

# COLOR_RANGE_HSL = [nmToHsl(i) for i in range (380, 781)]

# # fonction qui retourne la longueur d'onde la plus proche du code hex
# def closestWavelength(hexColor):
#     hslInput = _hexColorToHsl(hexColor)
#     closestHsl = (-1, -1, -1)
#     closestWavelength = -1
#     smallestDifference = 999999
    
#     for index, c in enumerate(COLOR_RANGE_HSL):
#         diff = _compareHsl(hslInput, c)
#         if diff < smallestDifference:
#             # print("smallest was", smallestDifference, "now it's", diff)#debug
#             closestHsl = c
#             closestWavelength = index + 380
#             smallestDifference = diff
#         # print(c, diff)#debug

#     return closestWavelength

if __name__ == '__main__':
    print(_hexColorToHsl("#142857"))
    print(_compareHexColors("#142857", "#010989"))
    # print(closestWavelength("#593406"))



