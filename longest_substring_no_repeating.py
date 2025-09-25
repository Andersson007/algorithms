#!/usr/bin/python3
# Longest Substring Without Repeating.
# Find the longest continious chunk of a string
# that doesn't have any repeating characters.
# Use the "Sliding window" technic: use two pointers,
# a start and an end, that create a "window" on your string.
# The goal is to make this window as wide as possible w/o
# having any duplicate character inside it.

string = "aldjflsadj dsjfalkjfa fkjkjdkewwqrttpoiqwertyuy"

# Time O(N)
# Space O(1)
def longest_substring_no_repeating(string):
    # This dict stores the last seen index of each char
    char_map = {}
    max_length = 0
    start = 0

    for end in range(len(string)):
        current_char = string[end]

        # Check if we've seen this char before AND if its last
        # position is within our current window
        if current_char in char_map and char_map[current_char] >= start:
            # If so, we have a repeat. Shrink the window by moving
            # 'start' to the position right after the last repeat.
            start = end + 1

        # Update the last seen position of the current char
        char_map[current_char] = end

        # Calculate the current window's length and update max_length
        # if it's bigger
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length


print(longest_substring_no_repeating(string))
