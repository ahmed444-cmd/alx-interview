#!/usr/bin/python3

"""Module defining isWinner function."""

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game after x rounds.

    Args:
        x (int): Number of rounds to be played.
        nums (list): List of integers defining the range for each round.

    Returns:
        str: Name of the player with the most wins or None if tied.
    """
    mariaWinsCount = 0  # Track Maria's total wins
    benWinsCount = 0  # Track Ben's total wins

    for num in nums:
        roundsSet = list(range(1, num + 1))  # Create a range for the round
        primesSet = primes_in_range(1, num)  # Get primes within the range

        if not primesSet:  # If no primes, Ben wins this round
            benWinsCount += 1
            continue

        isMariaTurns = True  # Maria starts the game

        while True:
            if not primesSet:  # No primes left means the game ends
                if isMariaTurns:
                    benWinsCount += 1  # Ben wins if Maria cannot play
                else:
                    mariaWinsCount += 1  # Maria wins if Ben cannot play
                break

            smallestPrime = primesSet.pop(0)  # Remove the smallest prime
            roundsSet.remove(smallestPrime)  # Remove it from the range

            # Remove multiples of the prime from the range
            roundsSet = [x for x in roundsSet if x % smallestPrime != 0]

            isMariaTurns = not isMariaTurns  # Alternate turns

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"  # Maria wins more rounds

    if mariaWinsCount < benWinsCount:
        return "Winner: Ben"  # Ben wins more rounds

    return None  # Tie if wins are equal

def is_prime(n):
    """Determine if n is a prime number."""
    if n < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Divisible by any number other than 1 and itself
    return True

def primes_in_range(start, end):
    """Generate a list of primes between start and end inclusive."""
    primes = [n for n in range(start, end + 1) if is_prime(n)]  # Filter primes
    return primes
