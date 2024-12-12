#!/usr/bin/python3

"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds of playing the Prime Game.
"""

def isWinner(x, nums):
    """isWinner

    Determine who is the winner after a certain number of rounds.

    Argumnets:
        x (int): The number of rounds
        nums (List[int]): List of all the n's for each round.

    Return:
        (str): The name of the player who wins.
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not sieve[i]:
            continue
        for j in range(i*i, n + 1, i):
            sieve[j] = False

    sieve[0] = sieve[1] = False
    count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            count += 1
        sieve[i] = count

    player1 = 0
    for n in nums:
        player1 += sieve[n] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"

