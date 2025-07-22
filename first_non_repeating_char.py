#!/usr/bin/python3
# First Non-Repeating Character.
# Write a function that takes in a string
# of lowercase English-alphabet letters and
# returns the index of the string's first
# non-repeating character.
# * The first non-repeating char is the first char
#   in a string that occurs only once.
# * If the input string doesn't have any
#   non-repeating chars the function will return -1

string = "abcb"

# Time O(N)
# Space O(1): because it can contain max 26 chars
def first_non_repeating_char(string):
    char_map = {}
    for c in string:
        if c not in char_map:
            char_map[c] = 0
        char_map[c] += 1

    for i in range(0, len(string)):
        if char_map[string[i]] == 1:
            return i

    return -1


print(first_non_repeating_char(string))
