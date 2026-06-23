#!/usr/bin/python3
# Write a function using functools.partial.
# functools.partial creates a new function with some arguments 
# of an existing function pre-filled. It's useful when you want 
# a specialized version of a more general function.
# Think of partial as a lightweight way to create customized functions
# without writing a wrapper function yourself.

from functools import partial

# Example 1: Pre-fill one argument
def sum(a, b):
    return a + b

add_two = partial(sum, 2)

# This is equivalent to sum(2, x)
print(add_two(5))


# Example 2: Pre-fill keyword arguments
def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"


greet_excited = partial(greet, punctuation="!!!")

print(greet_excited("Bob"))
