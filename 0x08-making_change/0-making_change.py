#!/usr/bin/python3
"""Making change"""

def makeChange(coins, total):
"""
Determine the fewest number of coins needed to meet a given amount total.

:param coins: List of coin values.
:param total: Target total amount.
:return: Fewest number of coins needed, or -1 if not possible.
"""
    
if total <= 0:
return 0

# Initialize an array to store the minimum coins for each amount from 0 to total
dp = [float('inf')] * (total + 1)
dp[0] = 0  # Base case: 0 coins are needed to make the total 0

# Fill the dp array
for coin in coins:
for amount in range(coin, total + 1):
dp[amount] = min(dp[amount], dp[amount - coin] + 1)

# If dp[total] is still infinity, it means we cannot make that amount
return dp[total] if dp[total] != float('inf') else -1
