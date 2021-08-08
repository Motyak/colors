#!/usr/bin/env python3
from c import nmToRgb

def _hexColorToRgb(str):
    tmp = str[1:7]
    a = int(tmp[:2], 16)
    b = int(tmp[2:4], 16)
    c = int(tmp[4:6], 16)
    return (a, b, c)

def _getMatchingColorRange(rgb):
    #      (r=0/g=1/b=1,  value)
    lowest = (-1, 999999)
    highest = (-1, -999999)

    for i, c in enumerate(rgb):
        if c > highest[1]:
            highest = (i, c)
        else: # if c <= lowest[1]
            lowest = (i, c)
    
    # composante extreme = la plus grande (proche de 255)
    if 255-highest[1] < lowest[1]:
        # red
        if highest[0] == 0:
            return range(580, 701)
        # green
        elif highest[0] == 1:
            return range(490, 581)
        # blue
        elif highest[0] == 2:
            return range(420, 491)

    # composante extreme = la plus petite (proche de 0)
    else:
        # red
        if lowest[0] == 0:
            return range(440, 511)
        # green
        elif lowest[0] == 1:
            return range(0, 441)
        # blue
        elif lowest[0] == 2:
            return range(510, 781)

    return []

# returns the average delta between r, g and b
def _howmuchdifference(rgb1, rgb2):
    sum = 0.0
    for i in range(3):
        sum += abs(rgb1[i]-rgb2[i])
    return sum


# fonction qui retourne la longueur d'onde la plus proche du code hex
def closestWavelength(hexColor):
    rgbInput = _hexColorToRgb(hexColor)
    colorRangeNm = [*_getMatchingColorRange(rgbInput)]
    colorRangeRgb = [*map(lambda x: nmToRgb(x), colorRangeNm)]

    closestRGB = (-1, -1, -1)
    closestWavelength = -1
    smallestDifference = 999999
    
    for index, c in enumerate(colorRangeRgb):
        # print("nm ", index + 380) #debug
        diff = _howmuchdifference(rgbInput, c)
        # print(rgbInput, c, diff) #debug
        if diff < smallestDifference:
            closestRGB = c
            closestWavelength = index + colorRangeNm[0]
            smallestDifference = diff
            # print(closestRGB, ";", closestWavelength, ";", smallestDifference) #debug

    # print(closestRGB)#debug
    return closestWavelength

print(closestWavelength("#285714"))

