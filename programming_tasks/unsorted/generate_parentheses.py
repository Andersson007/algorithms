#!/usr/bin/python3
# Generate Parentheses.
# * You're given an integer "n".
# * The function must return a list of
#   all possible strings containing "n" pairs
#   of opening and closing parantheses that are
#   structurally valid. Rules are:
#   1. Every opening parenthesis "(" must have a
#      corresponding closing parenthesis ")".
#   2. An opening parentheses must always come before its
#      corresponding closing parenthesis.
# Examples:
# n = 1, output ["()"]
# n = 2, output ["(())", "()()"]
# n = 3, output ["((()))", "(()())", "(())()", "()(())", "()()()"]
# You solve this using *recursion* and *backtracking*,
# as you need to explore different combinations while ensuring
# you never violate the rules of well-formed parentheses (above).

# Backtracking technique:
# - Build the parenthesis string char by char.
# - Make a decision at each step: either add an opening parentheses
#   or a closing one.
# - We only proceed if the choice results in a valid
#   (or potentially valid) sequence.
# We need a recursive function that keeps track of three things:
# 1. The string we've built so far.
# 2. The number of opening parentheses left to add (open_count).
# 3. The number of closing parentheses left to add (close_count).
#
# This function follows two simple rules to decide what to do next.
#
# Rule 1: Add an opening parenthesis (
# You can always add an opening parenthesis as long as
# you have some left (i.e., open_count > 0).
#
# Rule 2: Add a closing parenthesis )
# You can only add a closing parenthesis if
# it wouldn't create an invalid string.
# This means you can only add a ) if there are more opening
# parentheses already in the string than closing ones.
# A simple way to check this is if close_count > open_count.
# This ensures there is an unmatched ( to pair with.
#
# The recursion stops and we have a valid solution
# when we've used up all parentheses (open_count and close_count are both 0).


# Time ~O(4^N): bad
# Space ~O(4^N): bad
def generate_parentheses(n):
    # This list will store all the valid combinations.
    result = []

    # Start the backtracking process with an empty string and n pairs.
    backtrack("", n, n, result)

    return result


# This is our recursive helper function.
# It builds the string and explores possibilities.
def backtrack(current_string, open_count, close_count, result):
    # Base Case: If we've used all parentheses, we found a valid combo.
    if open_count == 0 and close_count == 0:
        result.append(current_string)
        return

    # Rule 1: Only add an opening parenthesis if we have any left.
    if open_count > 0:
        backtrack(current_string + "(", open_count - 1, close_count, result)

    # Rule 2: Only add a closing parenthesis
    # if it doesn't break the syntax.
    # This means the number of closing brackets left must be greater than
    # the number of opening brackets left.
    if close_count > open_count:
        backtrack(current_string + ")", open_count, close_count - 1, result)


print(generate_parentheses(1))
print(generate_parentheses(2))
print(generate_parentheses(3))
