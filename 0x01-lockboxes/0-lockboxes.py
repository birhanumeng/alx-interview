#!/usr/bin/python3
""" Lockboxes
"""


def canUnlockAll(boxes):
    """ Determines if all the boxes can be opened.
            - boxes is a list of lists
            - All keys are positive integers
            - The first box boxes[0] is unlocked
            - Return True if all boxes can be opened,
              else return False
    """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False
