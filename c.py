#!/usr/bin/env python3

_rgb = {
    440: lambda x: (-(x-440)/(440-380),0.0,1.0),
    490: lambda x: (0.0,(x-440)/(490-440),1.0),
    510: lambda x: (0.0,1.0,-(x-510)/(510-490)),
    580: lambda x: ((x-510)/(580-510),1.0,0.0),
    645: lambda x: (1.0,-(x-645)/(645-580),0.0),
    781: lambda x: (1.0,0.0,0.0)
}

_fac = {
    420: lambda x: 0.3+0.7*(x-380)/(420-380),
    701: lambda x: 1.0,
    781: lambda x: 0.3+0.7*(780-x)/(780-700)
}

# calculate rgb in decimal format
def _getRgbDec(wavelength):
    for sep in sorted(_rgb.keys()):
        if wavelength < sep:
            return _rgb[sep](wavelength)

# Let the intensity fall off near the vision limits
def _getFactor(wavelength):
    for sep in sorted(_fac.keys()):
        if wavelength < sep:
            return _fac[sep](wavelength)

# adapt color and convert dec to 0-255
def _apply(factor, colors):
    GAMMA, MAX_INTENSITY = 0.80, 255
    return map(lambda x: round(MAX_INTENSITY * (x * factor) ** GAMMA), colors)

def _isInSpectrum(wavelength):
    return wavelength >= 380 and wavelength <= 780

def nmToRgb(wavelength):
    red = green = blue = 0.0

    if not _isInSpectrum(wavelength):
        return
    
    red, green, blue = _apply(_getFactor(wavelength), _getRgbDec(wavelength))

    return (int(red),int(green),int(blue))

def _rgbToHexColor(rgb):
    return '#%02x%02x%02x' % rgb

def nmToHex(wavelength):
    return _rgbToHexColor(nmToRgb(wavelength))

if __name__ == '__main__':
    print(nmToRgb(592))
    print(nmToHex(780))
