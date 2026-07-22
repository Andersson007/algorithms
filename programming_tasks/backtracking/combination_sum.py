#!/usr/bin/python3
# Combination Sum.
# You're given a list of distinct positive integers called candidates
# and a positive integer target.
# Find all unique combinations of numbers from candidates whose
# sum is exactly equal to target.
# You may use each number in candidates as many times as you want.
# Two combinations are considered the same if they contain the same numbers,
# regardless of their order. Your solution should return
# each unique combination only once.

# The expected solution is backtracking (depth-first search).
# The key idea is to build combinations incrementally,
# trying each candidate while keeping track of the remaining target.

# Core Idea (Language-agnostic): At any point in the recursion:
# * Keep a current combination.
# * Keep track of the remaining sum needed to reach the target.
# * Starting from a given index, try each candidate:
#   * Add it to the current combination.
#   * Recurse with the reduced target.
#   * Remove it (backtrack) and try the next candidate.
# Why do we start from the current index instead of always from the beginning?
# * It allows us to reuse the current number.
# * It prevents generating duplicate combinations in different orders.
# For example, if you've already chosen 2, you don't want
# to later generate [3, 2, 2] after already finding [2, 2, 3].

candidates = [2, 3, 6, 7]
target = 7
# Output: [[2, 2, 3], [7]]

# Time O(N^(T/M)): in the worst case, where N is the number of candidates,
#   T is the target, and M is the smallest candidate, because the algorithm
#   explores all possible combinations.
# Space O(K * T/M): where K is the number of valid combinations,
#   because we store K combinations and each combination can
#   contain up to T/M elements, plus the recursion stack.
def backtrack(candidates, remaining, start, combination, result):
    """
    Recursively builds combinations that sum up to the target.

    Args:
        candidates: List of available numbers to choose from.
        remaining: Amount still needed to reach the target sum.
        start: Index from which to consider candidates. Prevents duplicate
               combinations and allows reusing the same candidate.
        combination: Current combination being built during recursion.
        result: List storing all valid combinations found.
    """
    if remaining == 0:
        # Save current combination in the result
        result.append(list(combination))
        return

    # The combination doesn't sum up to the target
    if remaining < 0:
        return

    # For every candidate from start index
    for i in range(start, len(candidates)):
        combination.append(candidates[i])  # Choose the candidate

        # Recurse with remaining - candidate
        # Pass i (not i + 1) because the same candidate may be reused.
        backtrack(candidates, remaining - candidates[i], i, combination, result)

        # Undo the choice.
        combination.pop()


def get_combination_sum(candidates, target):
    result = []
    backtrack(candidates, target, 0, [], result)
    return result


print(get_combination_sum(candidates, target))
