#!/usr/bin/python3
"""
Prime Game Module: Defines function that determines the winner after a certain
number of rounds in the Prime Game.
"""


def isWinner(x, nums):
    """isWinner

    Identifies the winner after a series of rounds.

    Arguments:
        x (int): The total number of rounds
        nums (List[int]): List of values for each round.

    Return:
        (str): The name of the winning player.
    """
    if not nums or x < 1:  # checks if nums is empty or x is less than 1
        return None
    n = max(nums)  # finds the largest value in nums list
    sieve = [True for _ in range(max(n + 1, 2))]  # initializes a sieve with True values
    for i in range(2, int(pow(n, 0.5)) + 1):  # iterates through the sieve
        if not sieve[i]:  # skips if the value is False (not prime)
            continue
        for j in range(i*i, n + 1, i):  # iterates through the sieve
            sieve[j] = False  # marks the value as False (not prime)

    sieve[0] = sieve[1] = False  # marks 0 and 1 as False (not prime)
    count = 0  # sets count to 0 (Maria's score)
    for i in range(len(sieve)):  # iterates through the sieve to count the primes
        if sieve[i]:  # if the value is True (prime)
            count += 1
        sieve[i] = count  # updates the value with the count of primes

    player1 = 0
    for n in nums:  # iterates through the nums list to count Maria's wins
        player1 += sieve[n] % 2 == 1  # Maria wins if her score is odd
    if player1 * 2 == len(nums):  # checks if Maria wins half the rounds
        return None
    if player1 * 2 > len(nums):  # checks if Maria wins more than half the rounds
        return "Maria"  # Maria wins
    return "Ben"  # Ben wins
