
import math
import random
from hashlib import sha1
from PIL import Image
from colorfunctions import *

#Generates based on individual bytes, by using each byte as a hue value in hsv
class ByteColorer:
    sv = (0.7, 0.8)

    def __init__(self, width, hue = random.random()):
        self.size = width
        self.hue = hue
        self.calls = 0

    def get_size(self):
        return (self.size, self.size)

    def get_position(self):
        return (self.calls % self.size, self.calls // self.size)

    def get_color(self, value):
        return hsv_to_rgb((self.hue + value / 255) % 1.0, *self.sv)

    def update(self, value, image):
        image.putpixel(self.get_position(), self.get_color(value))
        self.calls = self.calls + 1

#Generates greyscale with each value directly representative of its byte
class ByteGreyscaler(ByteColorer):
    def get_color(self, value):
        return (value, value, value)

#Generates colors based on printable or nonprintable characters, then scales for some variation
class PrintableColorer(ByteColorer):
    scale = 1/4

    def __init__(self, width, hue = random.random()):
        super().__init__(width, hue)
        self.primary = hue
        self.secondary = (hue + 0.5) % 1.0

    def get_color(self, value):
        if(value >= 32):
            return hsv_to_rgb(self.primary + self.scale * ((value - 32)/(256-32)), *self.sv)
        else:
            return hsv_to_rgb(self.secondary - self.scale * ((value)/(32)), *self.sv)

#Digram visualization. Plots each point based on relative frequency and two adjacent bytes
class Relational2DColorer(ByteColorer):
    scale = 1.4
    initial = 0.2

    def __init__(self, width, hue = random.random()):
        super().__init__(256, hue)
        self.prev = None
        self.curr = None

    def get_position(self):
        return (self.prev, self.curr)

    def get_color(self, saturation):
        saturation = self.scale * saturation

        if saturation > 1.0:
            saturation = 1.0
        elif saturation < self.initial:
            saturation = self.initial

        return hsv_to_rgb(self.hue, saturation, self.sv[1])

    def update(self,value, image):
        self.prev = self.curr
        self.curr = value

        if(self.prev != None and self.curr != None):
            pos = self.get_position()
            _, sat, _ = rgb_to_hsv(*image.getpixel(pos))
            image.putpixel(pos, self.get_color(sat))

#Digram visualization, based on treating two bytes of data as polar coordinates then plotting
class Polar2DColorer(Relational2DColorer):
    def __init__(self, width, hue):
        super().__init__(width, hue = random.random())
        self.size = 512

    def get_position(self):
        theta = 2 * math.pi * self.curr / 255
        r = self.prev * (self.size / 256 / 2)
        x = r * math.cos(theta) + self.size / 2
        y = r * math.sin(theta) + self.size / 2

        return (int(x), int(y))


def file_to_image(read_filename, write_filename, byte_converter = Relational2DColorer):
    f_in = open(read_filename, mode='rb')
    length = get_file_length(f_in)

    #calculates a square image based on the file size
    width = math.ceil(math.sqrt(length))
    total_data = (width ** 2)

    #clean and deterministic random color calculation
    color = get_file_color(f_in)

    converter = byte_converter(width, color)

    im = Image.new('RGB', converter.get_size())

    for i in range(length):
            converter.update(f_in.read(1)[0], im)

    im.save(write_filename)


def get_file_length(file_obj):
    curr = file_obj.tell()
    file_obj.seek(0, 2)
    length = file_obj.tell()
    file_obj.seek(curr, 0)
    return length

def get_file_color(file_obj):
    curr = file_obj.tell()
    m = sha1()
    m.update(file_obj.read())
    file_obj.seek(curr, 0)
    return m.digest()[0]
