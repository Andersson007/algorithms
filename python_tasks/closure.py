#!/usr/bin/python3
# Write a closure inside a loop that captures a variable incorrectly;
# fix it with a default argument and with functools.partial.
# * This task is about closures and late binding.
# * A closure is a function that remembers and can access variables
#   from its enclosing scope, even after the outer function finished executing.
#   They are useful when you want a function to carry around some private
#   state or configuration w/o creating a class

functions = []

for i in range(3):
    def f():
        return i
    functions.append(f)


# Here's a bug: it'll print 2, 2, 2 because after the loop
# finishes, i == 2, so every closure refers to that same variable and returns.
for f in functions:
    print(f())


# Fix 1: Use a default argument f(i=i): i is stored as a default param,
# so each func gets its own copy
functions = []

for i in range(3):
    def f(i=i):
        return i
    functions.append(f)


for f in functions:
    print(f())


# Fix 2: functools.partial creates a new callable with some arguments already bound
from functools import partial
functions = []
for i in range(3):
    def f(i):
        return i
    functions.append(partial(f, i))


for f in functions:
    print(f())
