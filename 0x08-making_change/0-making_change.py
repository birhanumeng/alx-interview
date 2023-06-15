#!/usr/bin/python3
""" Making change module
"""


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine
        the fewest number of coins needed to meet a given
        amount total.
            -If total is 0 or less, return 0
            -If total cannot be met return -1
    """
    if total < 1:
        return 0

    new_tot = total + 1
    my_dict = {0: 0}

    for i in range(1, total + 1):
        my_dict[i] = new_tot
        for c in coins:
            cur = i - c
            if cur < 0:
                continue
            my_dict[i] = min(my_dict[cur] + 1, my_dict[i])

    if store[total] > total:
        return -1

    return my_dict[total]
