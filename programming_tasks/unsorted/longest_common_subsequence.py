#!/usr/bin/python3
# Longest common subsequence.
# Find the longest possible sequence of chars
# that can be found in two other sequences, in the same order.
# The chars do not need to be next to each other.
seq1 = "banana"
seq2 = "bandana"
# output = 6  # as he longest common subsequence is "banana"

# Dynamic programming: break the problem down into smaller,
# overlapping subproblems and build up a solution from
# the bottom up. Store the results of these subproblems
# in a 2D array to avoid re-calculating them.

# Let's say we have two sequences, X and Y.
# We'll create a 2D table, let's call it dp,
# ********************************************************************
# to store the length of the LCS for all possible prefixes of X and Y.
# ********************************************************************
# The cell dp[i][j] will hold the length of the LCS between
# the first i characters of Y and the first j characters of X.
# Let's use our previous example: X = "banana" and Y = "bandana".
# Our table will have rows corresponding to characters of Y (plus an empty prefix)
# and columns for characters of X (plus an empty prefix).
# db[column][row] == db[i][j].

# X = banana
# Y = bandana
#      -> i
#      b a n a n a
# j  0 0 0 0 0 0 0 (m)
#  b 0 1 1 1 1 1 1
#  a 0 1 2 2 2 2 2
#  n 0 1 2 3 3 3 3
#  d 0 1 2 3 3 3 3
#  a 0 1 2 3 4 4 4
#  n 0 1 2 3 4 5 5
#  a 0 1 2 3 4 5 6
#   (n)

# Time O(M x N)
# Space O(M x N)
def longest_common_subsequence(seq1, seq2):
    m = len(seq1)  # Length of "banana"
    n = len(seq2)  # Length of "bandana"

    # Create a DP table to store results of subproblems.
    # dp[i][j] will contain the length of LCS of seq1[0..i-1] and seq2[0..j-1]
    # We add +1 to dimensions to handle empty string cases easily.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill out the table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If the characters at the current position match
            if seq1[i - 1] == seq2[j - 1]:
                # Add 1 to the result of the subproblem without these characters
                dp[i][j] = 1 + dp[i - 1][j - 1]
            # If the characters do not match
            else:
                # Take the maximum from the previous subproblems
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The value in the bottom-right corner is the length of the LCS
    # for the entire sequences.
    return dp[m][n]


print(longest_common_subsequence(seq1, seq2))
print(longest_common_subsequence(" ", " "))
