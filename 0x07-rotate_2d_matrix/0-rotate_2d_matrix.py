#!/usr/bin/python3
""" Rotate 2D matrix module
"""


def rotate_2d_matrix(matrix):
    """ Rotate n x n 2D matrix by 90 degrees clockwise.
    """
    n = len(matrix)
    index = n - 1

    # Make a deep copy of the 2D list
    tmp = []
    deep_copy = []
    for i in range(n):
        for j in range(n):
            tmp.append(matrix[i][j])
        deep_copy.append(tmp)
        tmp = []

    # Rotate the 2D matrix using 2D deep_copy
    for i in range(n):
        for j in range(n):
            matrix[j][index] = deep_copy[i][j]
        index -= 1
