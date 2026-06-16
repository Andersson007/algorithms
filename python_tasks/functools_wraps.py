#!/usr/bin/python3
# Write a decorator that preserves the wrapped function's signature
# and metadata using `functools.wraps`, then test it with `inspect.signature`.

# 1. A decorator is a function that takes another function and returns
# a modified version of it. It lets you add behavior
# without changing the original function's code. Common use: logging, auth, caching.
#
# 2. A higher-order function is a function that:
#   * Accepts other functions as arguments, and/or
#   * returns a function. A decorator is an example of it.
#
# 3. Function metadata: Functions in Python contain special attributes that describe them
#   * __name__
#   * __doc___
#   * __module__  # The module where the function was defined
#   * __annotations__  # Stores type hints - a dict of arguments/ret vals and their types
#
# 4. functools.wraps: @wraps(func) copies metadata from the original function
#    to the wrapper function inside a decorator.
#
# 5. Introspection: means examining an object at runtime to learn about it.
#    E.g.: print(greet.__name__), print(greet.__annotations__).
#
# 6. inspect.signature() returns a function's parameter information.
#    You can instect each parameter:
#    sig = signature(my_func)
#    for name, param in sig.parameters.items()
#        print(name, param.default)

import inspect


def not_wrapped_decorator(func):
    def wrapper(*args, **kwargs):
        """wrapper func docstring"""
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@not_wrapped_decorator
def say_hello(name):
    """say_hello func docstring"""
    print(f"Hello, {name}!")


print("Signature", inspect.signature(say_hello))
print(say_hello.__name__, say_hello.__doc__)  # Metadata belongs to wrapper
print(say_hello.__module__)
print(say_hello.__annotations__)
say_hello("Bob")
print()

# Use functools.wraps to preserve the original
# function's metadata such as its name and doc string
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@my_decorator
def greet(name):
    """greet func docstring"""
    print(f"Hello, {name}!")


print("Signature:", inspect.signature(greet))
print(greet.__name__, greet.__doc__)  # The name will stay greet
print(greet.__module__)
print(greet.__annotations__)
greet("Alice")
print()


# Introspection: examining an object at runtime to learn about it.
def add(a: int, b: int = 0):
    return a + b

sig = inspect.signature(add)
print(type(sig), sig)

for name, param in sig.parameters.items():
    print(name, param.default)
