#!/usr/bin/python3
# Longest Repeating Character Replacement
# You are given a string s containing only uppercase English letters and an integer k.
# You may replace at most k characters in the string with any other uppercase letter.
# Return the length of the longest substring that can be made
# to consist of the same character after at most k replacements.

# Example input:
s = "AABABBA"
k = 1

# Expected output: 4

# Explanation: The substring "AABA" can be changed to "AAAA"
# by replacing one B.

# Solution: We use a sliding window moving through the string. For each window:
# 1. Find the most common character.
# 2. Everything else would need to be replaced.
# 3. If the number of replacements is > k, move the left side of the window forward.
# 4. Otherwise, the window is valid, so remember its length.
#
# The key idea: replacements needed = window length - most common character count
# We want the largest window where replacements needed ≤ k.
#
# E.g., "A A B A" (valid):
# * Most common character = A (3 times)
# * Window length = 4
# * We need to replace 1 character (B)
# * 1 <= k, so this window is valid → length 4
#
# "A A B A B" (invalid):
# * Most common = A (3 times)
# * Length = 5
# * Need 5 - 3 = 2 replacements
# * 2 > k, so the window is too large → shrink it

# Time O(N)
# Space O(1)
def longest_char_replacement(string, k):
    char_counts = {}  # Keeps char counters
    max_frequency = 0  # Most frequent char in the current window
    longest = 0  # Keeps track of longest substring length with max k replacements

    start = 0

    for end in range(len(string)):
        # Add a new char to the window
        char = string[end]
        char_counts[char] = char_counts.get(char, 0) + 1

        # Keep track of frequency of the most frequent char in the curr window
        max_frequency = max(max_frequency, char_counts[char])

        # Calculate num of char that need to be replaced
        win_size = end - start + 1
        replacements_needed = win_size - max_frequency

        # Check if window is INvalid, shrink it
        if replacements_needed > k:
            char_counts[string[start]] -= 1
            start += 1

        # Keep track of the longest substring length
        longest = max(longest, end - start + 1)

    return longest


print(longest_char_replacement(s, k))
