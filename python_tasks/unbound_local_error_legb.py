#!/usr/bin/python3
# Write code that triggers LEGB scoping confusion
# (`UnboundLocalError` from a variable that "exists"), then fix it.
# 1. Create a variable (e.g. x) in an outer scope
# 2. Inside a function run:
# print(x)
# x = 20
# which will result in UnboundLocalError: local variable 'x'
# referenced before assignment, even though x exists globally.
# Why? Python sees x = 20 inside the function and decides
# at compile time that x is a local variable throughout the entire function,
# so Python effectively interprets 1. read local x 2. assign local x.
# The read happens before the local variable has a value, causing the error.

# Python searches names in the LEGB order:
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# ! Main takeway: If a variable is assigned anywhere in a function,
# Python treats it as local throughout that function
# unless you explicitly declare it global or nonlocal.

# 1. If you intend to modify the global variable, use "global".
x = 10

def f():
    global x
    print(x)
    x = 20


f()

# 2. For nested functions, use "nonlocal".
# This modifies the enclosing scope's variable instead of
# creating a new local one.
def outer():
    x = 10

    def inner():
        nonlocal x
        print(x)
        x += 1

    inner()


outer()
