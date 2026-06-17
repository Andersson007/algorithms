#!/usr/bin/python3
# Write decorators for caching and logging, use functools.wraps
# and inspect.signature, print functions' matadata.

from functools import wraps
from inspect import signature

# Logging decorator example
def logger(func):
    @wraps(func)
    def wrapper(*args):
        print("Going to execute:", args[0])
        return func(*args)

    return wrapper


@logger
def execute_query(query):
    print(query)
    return True


execute_query("SELECT version()")


# Cache decorator example.
# A cache decorator stores the result of a function call
# so that if the function is called again with the same arguments,
# the saved result is returned instead of recomputing it.
def cacher(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        # Check if the argument is in the cache first.
        # If yes, return result not executing the function again.
        if args in cache:
            print(f"Cache hit! {args}: {cache[args]}")
            return cache[args]

        print("Computing result")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@cacher
def execute_statement(statement):
    print(statement)
    return True


execute_statement("SELECT version()")
execute_statement("SELECT version()")

print()
print(f"execute_query metadata: \n"
      f"name: {execute_query.__name__}\n"
      f"signature: {signature(execute_query)}\n")

print(f"execute_statement metadata: \n"
      f"name: {execute_statement.__name__}\n"
      f"signature: {signature(execute_statement)}\n")
