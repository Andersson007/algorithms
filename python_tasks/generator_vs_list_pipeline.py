#!/usr/bin/python3
# Build a pipeline of three generators chained together (filter, transform, aggregate)
# and measure peak memory vs the equivalent list approach.
# This task is about generator pipelines and why they are
# more memory-efficient than building intermediate lists.

# What the task wants you to do
# 1. Create a data source. For example, numbers from a file or a large range().
# 2. Chain three generators
#   * Filter: keep only items matching a condition.
#   * Transform: convert each item into something else.
#   * Aggregate: consume the stream and compute a final result (e.g. sum, count, average).

# For example:
# Source: 1, 2, 3, 4, 5
# Filter: keep even numbers → 2, 4
# Transform: square them → 4, 16
# Aggregate: sum → 20

# Then compare with a list-based approach.
# The list-based approach creates a new list in memory.
# With generators, no intermediate lists are created—values flow through the pipeline one at a time.

# Generators let you build pipelines where each stage processes one item at a time.
# This keeps memory usage low because you never materialize all intermediate results.
# A list-based pipeline is often simpler but uses more memory,
# while a generator pipeline scales much better to very large datasets.

import tracemalloc


# Generator pipeline
def filter_even(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n


def square(numbers):
    for n in numbers:
        yield n * n


def total(numbers):
    return sum(numbers)


numbers = range(1_000_000)

# Start memory measurement
tracemalloc.start()

result = total(square(filter_even(numbers)))
# In real life, this specific problem solution should look like:
# result = sum(n * n for n in numbers if n % 2 == 0)

current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")

print(result)


# Equivalent list-based approach
numbers = range(1_000_000)

# Start memory measurement
tracemalloc.start()

filtered = [n for n in numbers if n % 2 == 0]
squared = [n * n for n in filtered]
result = sum(squared)

current, peak = tracemalloc.get_traced_memory()
print(f"Peak memory: {peak / 1024 / 1024:.2f} MB")

print(result)


# Generator-based approach peak memory: 0.00 MB
# List-based approach peak memory: 38.46 MB
