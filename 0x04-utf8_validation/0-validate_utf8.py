#!/usr/bin/python3
""" UTF-8 validation module. """

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
    if data > 127:
        return False
    return True
