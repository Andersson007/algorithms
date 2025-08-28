#!/usr/bin/python3
# Number of Ways To Make Change.
# Given an array of distinct positive ints
# representing coin denominations and a single
# non-negative int "n" representing a target amount
# of money, write a function that returns the number
# of ways to make change for that target amount
# using the given coin denominations.
# * Note that an unlimited amount of coins as at your disposal.
# The solution uses a technique called dynamic programming: the core
# idea is to solve the problem by breaking it down into smaller,
# simpler subproblems. Think of it like building a staircase: to know
# how to get to the 1st, then the 2nd, etc., using the information
# from the previous steps to build up the solution.

# 1. Try building an array of the number of ways to make change
#    for all amounts between 0 and n inclusive.
#    Note that there's only one way to make change for 0: that is
#    to not use any coins.
# 2. Build up the array ^ one coin denomination at a time, i.e.
#    find the number of ways to make change for all amounts
#    between 0 and n whith only one denomination, then with
#    two, etc. until you use all denominations.

# Additional clarification:
# Imagine you have a big goal, like climbing a staircase.
# It's daunting to think about jumping to the top step all at once.
# A simpler way is to figure out how to get to step 1, then step 2,
# then step 3, and so on. The solution for getting to step 5 uses
# the information you already figured out for steps 1, 2, 3, and 4.
# This is the exact idea behind the dynamic programming solution here.
# We solve the problem for a tiny amount (like 0) and use that result
# to solve for a slightly larger amount (like 1), then use those
# results to solve for amount 2, and so on, until we reach our target amount.

target_amount = 4
coins = [1, 2, 3]
# output is 4


# Time O(nd): where n is the target amount
#   and d is the number of coin denominations.
# Space O(n)
def num_ways_make_change(target_amount, coins):
    # This list keeps track of the number of ways
    # to make change for every single amount from 0
    # up to our target_amount.
    ways = [0 for amount in range(target_amount + 1)]
    # ways[0] will store the number of ways to make change for 0
    # ways[1] will store the number of ways to make change for 1
    # etc. up to ways[target_amount]

    ways[0] = 1  # Our base case to make 0 and
                 # there's only one way to make it:
                 # not to use any coins.

    # The key insight is that for any given coin, the number of ways
    # you can make a certain curr_amount is increased by the number of
    # ways you could make curr_amount - coin.
    # Why? Because you can take all the combination made curr_amount - coin
    # and simply add your current coin to the to make curr_amount.
    for coin in coins:
        for curr_amount in range(coin, target_amount + 1):
            ways[curr_amount] += ways[curr_amount - coin]

    return ways[target_amount]


print(num_ways_make_change(target_amount, coins))
