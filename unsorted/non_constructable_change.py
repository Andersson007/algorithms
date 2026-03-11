#!/usr/bin/python3
# Non-constructible change.
# Given an array of positive integers representing
# values of coins in your posession, write a function that
# returns the minimum amount of change (the minimum sum of
# money) that you CANNOT create.
# The given coins can have any positive integer value
# and aren't necessarily unique. It can also be empty.
# For example, if you're given coins = [1, 2, 5],
# the non-constructible minimum is 4:
# we can create 1, 2, 3, 5, ...
# If you're given [7,], the minumum is 1

array = [1, 2, 5]

# 1. Sort the input array.
# 2. Create a "change" variable and
#    go through the array to sum up all the values.
# 3. If the first element of the array is not one,
#    we just return one as it's the min amount of change
#    we cannot create.
# 4. When we reach 5, we can't create all values
#    between 3 and 5 because 5 is greater than our
#    current "change" + 1.

# Time: O(n log n) because it's the probable
# sorting algorithm complexity
# Space: O(1) as we don't consume any extra space
def non_constr_change(coins):
    coins.sort()

    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1

        change += coin

    return change + 1
