#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    T = []
    if n <= 0:
        return T
    T = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(T[i - 1]) - 1):
            curr = T[i - 1]
            temp.append(T[i - 1][j] + T[i - 1][j + 1])
        temp.append(1)
        T.append(temp)
    return T
