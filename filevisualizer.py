#!/usr/bin/python3

import argparse
from generateimage import *

parser = argparse.ArgumentParser(description='Provides visual representations of files through several methods')

parser.add_argument("file", help='The file to be converted to a picture')

parser.add_argument("-D", "--digram", help="Outputs a digram of the file", action="store_true")
parser.add_argument("-P", "--polar", help="Outputs a polar digram of the file", action="store_true")
parser.add_argument("-C", "--printable", help="Colors based on printable characters", action="store_true")
parser.add_argument("-G", "--greyscale", help="Converts each byte to greyscale", action="store_true")
parser.add_argument("-A", "--color", help="Converts each byte to a distinct color", action="store_true")

args = parser.parse_args()

if args.color:
    file_to_image(args.file, args.file + ".color.png", ByteColorer)

if args.greyscale:
    file_to_image(args.file, args.file + ".greyscale.png", ByteGreyscaler)

if args.printable:
    file_to_image(args.file, args.file + ".print.png", PrintableColorer)

if args.polar:
    file_to_image(args.file, args.file + ".polar.png", Polar2DColorer)

if args.digram:
    file_to_image(args.file, args.file + ".digram.png", Relational2DColorer)
