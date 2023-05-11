#!/usr/in/python3
""" Reads stdin line by line and computes metrics """

import sys


if __name__ == "__main__":
    status_code = {"200": 0,
               "301": 0,
               "400": 0,
               "401": 0,
               "403": 0,
               "404": 0,
               "405": 0,
               "500": 0}
    count = 0
    file_size = 0

    def file_size(line):
        """ Get the file size """
        try:
            line_arr = line.split()
            code = line_arr[-2]
            if code in status_code.keys():
                status_code[code] += 1
            return int(line_arr[-1])
        except Exception:
            return 0

    def print_metrics():
        """ Print the metrics """
        print("File size: {}".format(file_size))
        for key in sorted(status_code.keys()):
            if status_code[key]:
                print("{}: {}".format(key, status_code[key]))

    try:
        for line in sys.stdin:
	    count += 1
            file_size += file_size(line)
            if count % 10 == 0:
                print_metrics()
    except KeyboardInterrupt:
        print_metrics()
        raise
    print_metrics()	
