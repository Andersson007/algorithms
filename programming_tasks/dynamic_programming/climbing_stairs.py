#!/usr/bin/python3
# Climbing Stairs
# You are given a staircase with n steps.
# You can climb either 1 step or 2 steps at a time.
# Your task is to determine how many distinct ways
# there are to reach the top of the staircase.
# The order of the steps matters. For example,
# 1 + 2 and 2 + 1 are considered different ways.
# Try to find a solution that runs in O(n) time
# and uses O(1) extra space.

n = 5
# Expected output: 8 possible ways, they are:
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 2 + 1
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 1 + 2 + 2
# 2 + 1 + 2
# 2 + 2 + 1

# Solution: The simplest dynamic programming version
# is to keep only the previous two results.
# The idea: To reach step n, your last move must have been either:
# 1 step  → you came from step n - 1
# 2 steps → you came from step n - 2
# For example:
# n = 5
# step:    0  1  2  3  4  5
# ways:    1  1  2  3  5  8
# Therefore:
# ways(n) = ways(n - 1) + ways(n - 2)

# Different way to explain it:
# To reach step 5, there are only two possibilities:
# 1. We came from step 4, so every way of reaching step 4
#    gives us a way of reaching step 5. So the last move was 1 step.
# 2. We came from step 3, so the last move was 2 steps.
# Therefore: ways to reach 5 = ways to reach 4 + ways to reach 3
# The important insight to remember for an interview is:
# To reach a step, I can only arrive from one step below or
# two steps below, so the number of ways is the sum of
# those two numbers.

# We only need to remember those two previous values, which gives:
# Time: O(n) — we calculate the answer for each step once.
# Space: O(1) — we store only a few variables, regardless of n
def climb_stairs(n):
    one_step_before = 1
    two_steps_before = 1

    for i in range(2, n + 1):
        current = one_step_before + two_steps_before

        two_steps_before = one_step_before
        one_step_before = current

    return one_step_before


print(climb_stairs(n))
