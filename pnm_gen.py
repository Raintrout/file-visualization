import io
import math
from colorfunctions import *

#TODO: Generalize all the functions to deal with arrays of input

def file_to_raw_ppm(read_filename, write_filename):
    f_in = open(read_filename, mode='rb')
    f_out = open(write_filename, mode='wb')

    length = get_file_length(f_in)

    #calculates a square image based on the file size
    width = math.ceil(math.sqrt(length))
    total_data = (width ** 2)

    write_ppm_raw_header(f_out, width, width)

    for i in range(total_data):
        if i < length:
            f_out.write(byte_to_rgb(f_in.read(1)[0]))
        else:
            f_out.write(b'\x00\x00\x00')


    f_in.close()
    f_out.close()

def file_to_raw_pgm(read_filename, write_filename):
    f_in = open(read_filename, mode='rb')
    f_out = open(write_filename, mode='wb')

    length = get_file_length(f_in)

    #calculates a square image based on the file size
    width = math.ceil(math.sqrt(length))
    total_data = (width ** 2)

    write_pgm_raw_header(f_out, width, width)

    for i in range(total_data):
        if i < length:
            f_out.write(f_in.read(1))
        else:
            f_out.write(b'\00')


    f_in.close()
    f_out.close()

def file_to_simple_ppm(read_filename, write_filename):
    f_in = open(read_filename, mode='rb')
    f_out = open(write_filename, mode='w')

    length = get_file_length(f_in)

    #calculates a square image based on the file size
    width = math.ceil(math.sqrt(length / 3))
    total_data = 3 * (width ** 2)

    write_ppm_simple_header(f_out, width, width)

    for y in range(width):
        for x in range(width):
            for p in range(3):

                if((y * width * 3) + (x * 3) + p < length):
                    f_out.write(str(f_in.read(1)[0]))
                else:
                    f_out.write("0")

                f_out.write(" ")

            f_out.write('\t')

        f_out.write("\n")

    f_in.close()
    f_out.close()

def file_to_simple_pgm(read_filename, write_filename):
    f_in = open(read_filename, mode='rb')
    f_out = open(write_filename, mode='w')

    length = get_file_length(f_in)

    #calculates a square image based on the file size
    width = math.ceil(math.sqrt(length))
    total_data = (width ** 2)

    write_pgm_simple_header(f_out, width, width)

    for y in range(width):
        for x in range(width):
            if((y * width) + x < length):
                f_out.write(str(f_in.read(1)[0]))
            else:
                f_out.write("0")

            f_out.write('\t')

        f_out.write("\n")

    f_in.close()
    f_out.close()

#http://netpbm.sourceforge.net/doc/ppm.html
def write_ppm_raw_header(file_obj, width, height, color_size = 255, comment = "# none"):
    file_obj.write(generate_pnm_header('P6', width, height, color_size, comment).encode('ascii'))

def write_ppm_simple_header(file_obj, width, height, color_size = 255, comment = "# none"):
    file_obj.write(generate_pnm_header('P3', width, height, color_size, comment))

#http://netpbm.sourceforge.net/doc/pgm.html
def write_pgm_raw_header(file_obj, width, height, color_size = 255, comment = "# none"):
    file_obj.write(generate_pnm_header('P5', width, height, color_size, comment).encode('ascii'))

def write_pgm_simple_header(file_obj, width, height, color_size = 255, comment = "# none"):
    file_obj.write(generate_pnm_header('P2', width, height, color_size, comment))

#http://netpbm.sourceforge.net/doc/pnm.html
def generate_pnm_header(magic, width, height, color_size, comment):
    return magic + '\n' + comment + '\n' + str(width) + '\t' + str(height) + '\n' + str(color_size) + '\n'

#It seems like there should be a library function for this
def get_file_length(file_obj):
    curr = file_obj.tell()
    file_obj.seek(0, 2)
    length = file_obj.tell()
    file_obj.seek(curr, 0)
    return length

#######################################################################################################
