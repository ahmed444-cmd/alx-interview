#!/usr/bin/python3
"""Making Change"""

def makeChange(coins, total):
    """Making Change"""
    if total <= 0:
        return 0
    elif total > 0:
        newList = sorted(coins[:])
        newList = list(reversed(newList))
        count = 0
        value = total + 0
        index = 0
        while value >= 0 and (index < len(newList)):
            if value >= newList[index]:
                value = value - newList[index]
                count += 1
            elif value < newList[index]:
                index += 1
        if index == len(newList):
            if value != 0:
                return -1
            elif value == 0:
                return count
