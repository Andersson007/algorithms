#!/usr/bin/python3
# Nth Fibonacci number.
# A Fibonacci number is a number in the sequence
# where each number is the sum of
# the two preceding ones, starting from 0 and 1.
# Therefor:
# * F(0) = 0
# * F(1) = 1
# * F(n) = F(n-1) + F(n-2) for n >= 2

# Recursive solution:
# O(2^n) Time
# O(n) Space
def gen_nth_fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return gen_nth_fibonacci_rec(n - 1) + gen_nth_fibonacci_rec(n - 2)


# Iterative solution:
# O(n) Time
# O(1) Space
# Returns F_n where F_0=0, F_1=1
def nth_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        # a becomes the next fib number
        # b becomes the one after that
        a, b = b, a + b

    return a


print(gen_nth_fibonacci_rec(5))
print(nth_fibonacci(5))
