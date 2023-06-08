#!/usr/bin/python3
""" Rotate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """ Rotate n x n 2D matrix by 90 degrees clockwise.
    """
    tmp = matrix
    n = len(matrix)
    index = n - 1
    for j in range(n):
        for i in range(n):
            matrix[i][index] = tmp[j][i]
        index -= 1
