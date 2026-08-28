#!/usr/bin/python3
# Minimum Number Of Coins To Make Change.
# Given an array of distinct positive ints
# representing coin denominations and a single
# non-negative int "target_amount" representing a target amount
# of money, write a function that returns the minimum number
# of ways to make change for that target amount
# using the given coin denominations.

target_amount = 7
coins = [1, 2, 5]
# output is 2 because you could use:
# * 1+1+1+1+1+1+1
# * 1+1+1+2+2
# * 2+5


# Time O(nd): where n is the target amount
#   and d is the number of coin denominations.
# Space O(n)
def num_ways_make_change(target_amount, coins):
    # Create an array to store the minimum coins
    # for each amount from 0 to 'amount'.
    # We initialize it with a value larger than any possible solution.
    nums_of_coins = [float("inf") for amount in range(target_amount + 1)]
    # Base case: the min coins needed to make amount 0 is 0
    nums_of_coins[0] = 0

    # Iterate through all amounts from 1 to the target amount
    for amount in range(1, target_amount + 1):
        # For each amount, try every coin:
        for coin in coins:
            # If a coin is usable (i.e., less than or equal to the curr amount)
            if amount - coin >= 0:
                # We calculate the potential new minimum:
                # 1 (for the current coin) + the stored
                # minimum for the remainder.
                new_min = 1 + nums_of_coins[amount - coin]

                # Update nums_of_coins[amount] if this path is better than
                # we've found so far.
                nums_of_coins[amount] = min(nums_of_coins[amount], new_min)

    # The final answer is in the last element of our dp array.
    # If the value is still 'inf', it means the amount could not be formed.
    result = nums_of_coins[target_amount]
    return result if result != float('inf') else -1


print(num_ways_make_change(target_amount, coins))
