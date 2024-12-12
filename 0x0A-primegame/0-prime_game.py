#!/usr/bin/python3
"""
Prime Game Module: Defines a function to determine the winner after a
certain number of rounds of playing the Prime Game.
"""


def isWinner(x, nums):
    """
    isWinner

    Determine the winner after a certain number of rounds.

    Arguments:
        x (int): The number of rounds
        nums (List[int]): List of all the n's for each round.

    Returns:
        (str): The name of the winning player.
"""
    if not nums or x < 1:  # if nums is empty or x < 1
        return None
    n = max(nums)  # max value in nums list
    sieve = [True for _ in range(max(n + 1, 2))]  # create a sieve of True val.
    for i in range(2, int(pow(n, 0.5)) + 1):  # loop through the sieve
        if not sieve[i]:  # if the value = False (not prime)
            continue
        for j in range(i*i, n + 1, i):  # loop through the sieve
            sieve[j] = False  # set the value = False (not prime)

    sieve[0] = sieve[1] = False  # set 0 and 1 => False (not prime)
    count = 0
    for i in range(len(sieve)):  # loop through the sieve and count the primes
        if sieve[i]:  # if the value is True (prime)
            count += 1
        sieve[i] = count  # set the value to the count of primes

    player1 = 0
    for n in nums:  # loop through the nums list and count Maria's wins
        player1 += sieve[n] % 2 == 1  # if Maria's score is odd, she wins
    if player1 * 2 == len(nums):  # if Maria wins half the rounds
        return None
    if player1 * 2 > len(nums):  # if Maria wins more than half the rounds
        return "Maria"  # Maria wins
    return "Ben"  # Ben wins
