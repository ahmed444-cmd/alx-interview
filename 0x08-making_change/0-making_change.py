#!/usr/bin/python3
"""Compute the fewest coins needed to match the target total.
"""


def makeChange(coins, total):
    """Return the fewest coins needed; 0 if total ≤ 0, -1 if impossible.
    """
    if total <= 0:
        return 0

    # Coins validity check
    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    available_coins = sorted(coins, reverse=True)
    change_left = total

    for coin in available_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin

    change = change if change_left == 0 else -1

    return change
