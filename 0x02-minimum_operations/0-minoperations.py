#!/usr/bin/python3
"""
Minimum Operations
Given an int. n, implement a method calculating the minim. numb. of operations
required to generate exactly n 'H' characters in a file.
Prototype: def minOperations(n)
Returns an integer
If it is not possible to achieve n characters, return 0.
"""


def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
