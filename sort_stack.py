#!/usr/bin/python3
# Write a func that takes in an array of ints
# representing a stack, recursively sorts the stack in place,
# and return it.
# * The array must be treated as a stack, with the end of the
#   array as the top of the stack.
# * You're only allowed to pop elements from the top of the stack
#   by removing elements from the end of the array using
#   the builtin .pop() methid.
# * Push elements to the top using the builtin .append() method.
# * Peek at the element on the top by accessing the last element.
# * You're not allowed to perform any other operations.
stack = [-5, 2, -2, 4, 3, 1]  # <- top of the stack
# output = [-5, -2, 1, 2, 3, 4]


# Time O(N^2)
# Space O(N): where N is the length of the stack
# We are going to pop everything from the stack
# recursively and put everything back in a correct order.
def sort_stack(stack):
    # If stack has no elements, return
    if len(stack) == 0:
        return stack

    # Pop the top element
    top = stack.pop()
    # Recursively sort the rest of the stack
    sort_stack(stack)
    # Insert the popped element back in sorted order
    insert(stack, top)

    return stack


def insert(stack, num):
    # Base case: if stack is empty OR
    # value is greater than the top element
    # so it doesn't need to be sorted
    if len(stack) == 0 or num > stack[-1]:
        stack.append(num)
        return

    # Otherwise,
    # 1. Remove top element
    # 2. Recurse until we find a proper placei for num
    # 3. Add the top element back
    top = stack.pop()
    insert(stack, num)
    stack.append(top)
    return


print(sort_stack(stack))
