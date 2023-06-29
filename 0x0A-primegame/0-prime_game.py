#!/usr/bin/python3
""" Prime game module
"""


def isPrime(n):
        """ Check if a number in the argument is prime number.
                - returns true if the argument is prime number
                - otherwise returns false
        """
        if n == 1:
            return False

        for num in range(2, (n // 2) + 1):
            if n % num == 0:
                return False
        return True


def checkMultiplies(num, numbers):
    """ Find out all its multplies for number 'num' in the
        list of numbers.
            - num is number
            - numbers is a list of numbers
    """
    multiplies = []
    for n in numbers:
        if n % num == 0:
            multiplies.append(n)
    return multiplies


def isWinner(x, nums):
    """ Given a set of consecutive integers starting from 1 up
        to and including n, they take turns choosing a prime number
        from the set and removing that number and its multiples from
        the set. The player that cannot make a move loses the game.
            - x is the number of rounds and nums is an array of n
            - Return: name of the player that won the most rounds
            - If the winner cannot be determined, return None
            - You can assume n and x will not be larger than 10000
            - n may be diiferen for each round.
    """
    l = len(nums)
    if l == 0 or l > 1000 or x < 1 or x > 10000 or l != x:
        return None

    m_win = 0
    b_win = 0
    for i in nums:
        m_selected = 1
        b_selected = 0
        for s in range(1, i + 1):
            if isPrime(s):
                if m_selected:
                    b_selected = 1
                    m_selected = 0
                else:
                    m_selected = 1
                    b_selected = 0
        if m_selected:
            b_win += 1
        else:
            m_win += 1
    if m_win > b_win:
        return 'Maria'
    return 'Ben'
