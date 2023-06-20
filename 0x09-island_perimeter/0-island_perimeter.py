#!/usr/bin/python3
""" Island perimeter module
"""


def island_perimeter(grid):
    """ Find returns the perimeter of the island described in grid:
        - grid is a list of list of integers:
            * 0 represents water
            * 1 represents land
            * Each cell is square, with a side length of 1
            * Cells are connected horizontally/vertically not diagonal
            * grid is rectangular, with its sides not exceeding 100
        - The grid is completely surrounded by water
        - There is only one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t
          connected to the water surrounding the island).
    """
    perimeter = 0
    row = len(grid)
    column = len(grid[0])

    for i in range(1, row - 1):
        for j in range(1, column - 1):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1

    return perimeter
