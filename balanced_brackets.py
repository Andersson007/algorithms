#!/usr/bin/python3
# Write a function that takes in a string made up of
# brackets (, [, {, }, ], ) and other optional characters
# and return a boolean representing whether the string
# is balanced with regards to brackets.

string1 = "([a])"  # is balanced
string2 = "(..}}"  # is not balanced


# Time O(N): where N is the length of the string
#       because we need to traverse the string
# Space O(N): because our stack can have the same
#       length as the input string in the worst case
def is_brackets_balanced(string):
    opening_brackets = {"(", "[", "{"}
    closing_brackets = {")", "]", "}"}
    matching_brackets = {
        "}": "{",
        ")": "(",
        "]": "[",
    }
    stack = []

    for char in string:
        if char in opening_brackets:
            # If we meet {, (, [,
            # push it to the stack
            stack.append(char)

        elif char in closing_brackets:
            # If we meet }, ), ],
            if len(stack) == 0:
                # If there's no opening brackets
                # in the stack, the string is not balanced
                return False

            if stack[-1] == matching_brackets[char]:
                # If the opening and closing brackets match,
                # just remove one from the stack and continue
                stack.pop()

            else:
                # If they don't match, the string isn't balanced
                return False

    return len(stack) == 0


print(is_brackets_balanced(string1))
print(is_brackets_balanced(string2))
