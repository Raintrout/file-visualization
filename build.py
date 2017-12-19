#!/usr/bin/python3
import os
from math import ceil, sqrt
from PIL import Image
from generateimage import *

def run_build():
    folder = "tests/"
    results = folder + "build/"
    build = folder + "files/"

    #clean up results
    for name in os.listdir(results):
        os.remove(results + name)


    ConverterList = [ByteColorer, ByteGreyscaler, PrintableColorer, Relational2DColorer, Polar2DColorer]
    ConverterPref = ['color', 'grey', 'print', '2D', 'polar']

    #generate builds for all files
    for name in os.listdir(build):
        for i in range(len(ConverterList)):
            file_to_image(build + name, results + name +'.' + ConverterPref[i] + '.png', ConverterList[i])

    #resize all build results
    size = (512, 512)
    for name in os.listdir(results):
        image = Image.open(results + name)
        image.resize(size).save(results + name)




if __name__ == '__main__':
    run_build()
