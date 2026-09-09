#!/usr/bin/python3
# Max Subarray of Size K
# You are given an array of integers nums and an integer k.
# Write a Python function that finds the maximum sum
# of any contiguous subarray of exactly size k.
# Your solution should return the maximum sum.

# Input:
nums = [2, 1, 5, 1, 3, 2]
k = 3

# Output: 9
# Explanation: The contiguous subarray [5, 1, 3] has size 3 and the maximum sum:
# 2 + 1 + 5 = 8
# 1 + 5 + 1 = 7
# 5 + 1 + 3 = 9  ← maximum
# 1 + 3 + 2 = 6

# Your task: Implement the solution in Python and aim for O(n) time complexity.

# Solution: The clearest approach is a sliding window.
# 1. Calculate the sum of the first k elements.
# 2. This is your first window and current maximum.
# 3. Move the window one element at a time:
#   * subtract the element leaving the window
#   * add the new element entering the window
# 4. Update the maximum sum.
# This avoids recalculating every subarray sum from scratch.
# The key interview insight is that when the window moves,
# most elements remain the same, so you only need to subtract
# one old element and add one new element.

# Time O(n)
# Space O(1)
def max_subarray_of_size_k(nums, k):
    # Sum of the first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window through the rest of the array
    for i in range(k, len(nums)):
        # Remove the element leaving the window
        window_sum -= nums[i - k]

        # Add the element entering the window
        window_sum += nums[i]

        # Keep track of the maximum
        max_sum = max(max_sum, window_sum)

    return max_sum


print(max_subarray_of_size_k(nums, k))



