#!/usr/bin/python3
""" In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given
    a number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file. 
"""


def minOperations(n):
    """ Minimum Operations. """
    if n < 1:
        return 0
    
    count = 0

    while n > 1:
        if n % count == 0:
            count = count + 2
        else:
            count = count + 1
        if n == count:
            return count
    return 1
