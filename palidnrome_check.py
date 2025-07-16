#!/usr/bin/python3
# Palindrome Check.
# * The function takes in a non-empty string
#   and returns a boolean representing if the
#   string is a palindrome.
# * A palindrome is defined as a string that's written
#   the same forward and backward.
# * Note that single-character strings are palindromes.

string1 = "abba"
string2 = "abcba"
string3 = "xyz"

# Naive, Python-specific solution
def is_palindrome_python_solution(string):
    return string == string[::-1]


# Universal solution.
# Use 2 pointers: start with a pointer at the first index
# of the string and a pointer at the final index of the string.
# Time O(N): because we iterate through all characters of the
#            input string.
# Space O(1): because we handle the string in place
def is_palindrome_universal(string):
    if len(string) == 1:
        return True

    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome_python_solution(string1))
print(is_palindrome_universal(string2))
print(is_palindrome_universal(string3))
