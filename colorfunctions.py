import colorsys
from math import ceil

'''
Color rules within program:
rgb values should be integers 0 <= x <= 255
h values should be floating point numbers 0 <= x < 1.0
sv values should be floating point numbers 0 <= x <= 1.0
'''

#wraps colorsys so code is cleaner elsewhere
def rgb_to_hsv(red, green, blue):
    h, s, v = colorsys.rgb_to_hsv(red / 255, green / 255, blue / 255)
    return h, s, v

#wraps colorsys so code is cleaner elsewhere
def hsv_to_rgb(hue, saturation, value):
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    return ceil( 255 * r ), ceil( 255 * g ), ceil( 255 * b )

#returns a complementary color (+180 degrees) given a hsv color
def complementary_color(hue, saturation, value):
    return (hue + 0.5) % 1.0 , saturation, value

#TODO: Generalize conversion of bytes to colors
#evaluation of a byte of the file to a 3 byte reprentation
def byte_to_rgb(byte_in):
    return bytes(hsv_to_rgb(byte_in / 255, 0.7, 0.7))
