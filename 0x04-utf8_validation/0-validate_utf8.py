#!/usr/bin/python3
""" UTF-8 validation module. """

def get_binary(num):
    """ Return binary representation of a number. """
    binary = []
    while(num > 1):
        binary.append(num % 2)
        num = num // 2
    binary.append(num)
    gap = len(binary) - 8
    if gap < 0:
        for i in range(abs(gap)):
            binary.append(0)
    binary.reverse()
    return binary

def validUTF8(data):
    """ determines if a given data set represents a valid
        UTF-8 encoding. Return: True if data is a valid
        UTF-8 encoding, else return False
        The specification is the follwing:
            - A character in UTF-8 can be 1 to 4 bytes long
            - The data set can contain multiple characters
            - The data will be represented by a list of integers
            - Each integer represents 1 byte of data, therefore
              only handle the 8 least significant bits of each
              integer
    """
    u = [[0], [1, 0], [1, 1, 0], [1, 1, 1, 0]]
    for d in data:
        bi = get_binary(d)
        if not(bi[:1] == u[0] or bi[:2] == u[1] or bi[:3] == u[2] or bi[:4] == u[3]):
            return False
    return True
