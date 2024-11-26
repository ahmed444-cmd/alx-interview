#!/usr/bin/python3
"""
Making change
"""
def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of coin values.
    :param total: Target total amount.
    :return: Fewest number of coins needed, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to start with the largest denomination
    coins.sort(reverse=True)

    # Initialize variables
    count = 0
    remaining = total

    for coin in coins:
        if remaining <= 0:
            break
        # Use as many of this coin as possible
        count += remaining // coin
        remaining %= coin

    # If there's any amount remaining, return -1
    return count if remaining == 0 else -1
