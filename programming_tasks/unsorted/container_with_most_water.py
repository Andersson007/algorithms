#!/usr/bin/python

# Container with most water.
# You’re given an array of non-negative integers height,
# where each element represents the height of a vertical line on a chart.
# The index represents the x-coordinate.
# Your task is to find two lines that together with the x-axis
# form a container that holds the maximum amount of water.

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Expected output: 49
# Explanation:
# The maximum area is formed between the lines
# at index 1 (height = 8) and index 8 (height = 7):
# * Width = 8 - 1 = 7
# * Height = min(8, 7) = 7
# * Area = 7 × 7 = 49

# Graphical explanation
# Index:   0 1 2 3 4 5 6 7 8
# Height:  1 8 6 2 5 4 8 3 7
#  8 |     |       |       |
#  7 |     |       |       |   |
#  6 |     |   |   |       |   |
#  5 |     |   |   |   |   |   |
#  4 |     |   |   |   |   |   |
#  3 |     |   |   |   |   |   |   |
#  2 |     |   |   |   |   |   |   |
#  1 | |   |   |   |   |   |   |   |
#    +--------------------------------
#      0   1   2   3   4   5   6   7   8
# Key Insight:
# * Wider is better
# * Taller is better
# * But you're always limited by the shorter line

# Solution, core idea
# Use two pointers:
# * One at the start (left)
# * One at the end (right)
#
# At each step:
# * Compute the area between them
# * Update the maximum
# * Move the pointer pointing to the shorter line
# Why? Because moving the taller line cannot increase
# the area (the height is limited by the shorter one).

# Time O(N): we iterate across the array once
# Space O(1): we create no additional datastructures
def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        area = h * w

        if area > max_area:
            max_area = area

        # Move the pointer with the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(max_area(height))
