#!/usr/bin/python3
import os
from math import ceil, sqrt
from pnm_gen import *

def test():
    folder = "tests/"
    results = folder + "results/"
    tests = folder + "files/"

    gen_color = True    #generate color tests
    gen_greyscale = False    #generate greyscale tests

    gen_raw = True    #generate raw tests
    gen_simple = False    #generate simple tests

    #clean up results
    for name in os.listdir(results):
        os.remove(results + name)

    #generate test results for all files
    for name in os.listdir(tests):
        if gen_color and gen_raw:
            file_to_raw_ppm(tests + name, results + name + 'cr.ppm')
        if gen_color and gen_simple:
            file_to_simple_ppm(tests + name, results + name + 'cs.ppm')
        if gen_greyscale and gen_raw:
            file_to_raw_pgm(tests + name, results + name + 'gr.pgm')
        if gen_greyscale and gen_simple:
            file_to_simple_pgm(tests + name, results + name + 'gs.pgm')


if __name__ == '__main__':
    test()
