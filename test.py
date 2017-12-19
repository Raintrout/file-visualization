#!/usr/bin/python3
import os
from math import ceil, sqrt
from generateimage import *

#ANSI Terminal Color Codes
class format:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def test_file_functions(function, read_filename, write_filename, colorer, expected_output = None):
    if(function(read_filename, write_filename, colorer) == expected_output):
        print(format.BOLD + format.SUCCESS + "Success:" + format.ENDC,
         function.__name__ + "(" + read_filename + ", " + write_filename + ")")
    else:
        print(format.BOLD + format.FAIL + "Failure:" + format.ENDC,
         function.__name__ + "(" + read_filename + ", " + write_filename + ")")

def run_tests():
    folder = "tests/"
    results = folder + "results/"
    tests = folder + "files/"

    #clean up results
    for name in os.listdir(results):
        os.remove(results + name)

    gen_Relational2D = True
    gen_Polar2D = True
    
    gen_Byte = True
    gen_Printable = True
    gen_Greyscale = True


    #generate test results for all files
    for name in os.listdir(tests):
        if gen_Byte:
            test_file_functions(file_to_image, tests + name, results + name + '.byte.png', ByteColorer)
        if gen_Relational2D:
            test_file_functions(file_to_image, tests + name, results + name + '.2D.png', Relational2DColorer)
        if gen_Printable:
            test_file_functions(file_to_image, tests + name, results + name + '.print.png', PrintableColorer)
        if gen_Greyscale:
            test_file_functions(file_to_image, tests + name, results + name + '.grey.png', ByteGreyscaler)
        if gen_Polar2D:
            test_file_functions(file_to_image, tests + name, results + name + '.polar2D.png', Polar2DColorer)


if __name__ == '__main__':
    run_tests()
