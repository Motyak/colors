#!/usr/bin/env python3
from c2 import closestWavelength

# # retourne la couleur à la longueur d'onde associée la plus loine
# def compare(hexColor1, hexColor2):
#     return closestWavelength(hexColor1) > closestWavelength(hexColor2)

arr = ["#142857", "#285714", "#571428"]
arr = [*map(closestWavelength, arr)]
# arr.sort(key=lambda x: closestWavelength(x))
print(arr)
