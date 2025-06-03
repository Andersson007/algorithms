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
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return gen_nth_fibonacci_rec(n - 1) + gen_nth_fibonacci_rec(n - 2)


# Iterative solution:
# O(n) Time
# O(1) Space
def gen_nth_fibonacci_iter(n):
    if n == 1:
        return 0

    f0 = 0
    f1 = 1
    for _ in range(2, n + 1):
        next_fib = f1 + f0
        f0 = f1
        f1 = next_fib

    return f1

print(gen_nth_fibonacci_rec(10))
print(gen_nth_fibonacci_iter(10))
