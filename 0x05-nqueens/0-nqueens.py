#!/usr/bin/python3
""" Solve the N queens puzzle. """

from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    places = []

    def solve_queens(row, n, places):
	""" Solving the puzzle. """
        if (row == n):
            print(places)
        else:
            for col in range(n):
                new = [row, col]
                if valid_placement(places, new):
                    places.append(new)
                    solve_queens(row + 1, n, places)
                    places.remove(new)

    def valid_placement(places, new):
	""" Check the validity of the place of the queen. """
        for queen in places:
            if queen[1] == new[1]:
                return False
            if (queen[0] + queen[1]) == (new[0] + new[1]):
                return False
            if (queen[0] - queen[1]) == (new[0] - new[1]):
                return False
        return True

    solve_queens(0, n, places)
