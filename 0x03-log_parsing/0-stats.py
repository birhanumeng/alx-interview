#!/usr/bin/python3
""" Reads stdin line by line and computes metrics """

import sys


st_code = { "200": 0,
		"301": 0,
		"400": 0,
		"401": 0,
		"403": 0,
		"404": 0,
		"405": 0,
		"500": 0 }
file_size = 0
count = 0
def file_size(line):
    """ Get the file size of each line """
    try:
            parsed_line = line.split()
            status_code = parsed_line[-2]
            if status_code in st_code.keys():
                st_code[status_code] += 1
            return int(parsed_line[-1])
        except Exception:
            return 0

def print_metrics():
    """ Print the line metrics """
    print("File size: {}".format(file_size))
        for key in sorted(st_code.keys()):
            if st_code[key]:
                print("{}: {}".format(key, st_code[key]))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            file_size += file_size(line)
            if count % 10 == 0:
                print_metrics()
            count += 1
    except KeyboardInterrupt:
        print_metrics()
        raise
    print_metrics()
