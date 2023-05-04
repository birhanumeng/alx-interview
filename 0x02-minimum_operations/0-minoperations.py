#!/usr/bin/python3
""" In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given
    a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """ Minimum Operations. """
    if n < 2:
        return 0
    
    num_op = 0
    num_H = 1
    tmp = 1

    while True:
        flag = 0
        if n % num_H == 0:
            num_op = num_op + 2
            num_H = 2 * num_H
            flag = 1
        else:
            num_op = num_op + 1
            num_H = num_H + tmp
        
        if flag:
            tmp = num_H / 2
        if n == num_H:
            return num_op
