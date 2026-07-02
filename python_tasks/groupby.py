#!/usr/bin/python3
# Implement `itertools.groupby` from scratch and handle the "must be pre-sorted" gotcha.
# Notions to understand:
# * iterable
# * iterator
# * iter()
# * next()
# * generator vs iterator (a generator is a special type of iterator that uses yield)

# itertools.groupby groups consecutive items in an iterable that have the same key.
# Key points:
# * It does not group all equal values throughout the iterable—only adjacent ones.
# * If you want all equal values together, sort the data first using the same key.
#   * This can also be achieved on a database level by using "GROUP BY"
#   * or by using collections.defaultdict.
# Use cases examples:
#
# * Counting/grouping records by a field, e.g. for sorting and handling
#   employees by department
# * Splitting data into blocks (consecutive blank/non-blank lines,
#   consecutive rows with the same date or category.
# * Streaming large datases: process one group at a time w/o loading everything in memory.
#
# Example:

from itertools import groupby

data = [1, 1, 2, 2, 1]

for key, group in groupby(data):
    print(key, list(group))

# Output:
# 1 [1, 1]
# 2 [2, 2]
# 1 [1]

# Solution.
# The real itertools.groupby is more sophisticated:
# * It accepts a key function (e.g. key=len).
# * It yields iterators for each group instead of lists, making it more memory-efficient.
def groupby(iterable):
    # Calling iter() on an iterable (something you can loop over) creates an iterator.
    # Think of an iterator as a bookmark into a sequence.
    # Initially, the iterator points to the first element.
    iterator = iter(iterable)

    try:
        # next() asks the iterator: "Give me the next item."
        current = next(iterator)
    except StopIteration:
        # When there are no items left
        return

    # Build a new group
    group = [current]

    # We loop over iterator (not iterable) not to start
    # fron the beginning each time. We continue from the current position.
    for item in iterator:
        # If the next element is the same, add it to the group
        if item == current:
            group.append(item)
        else:
            # When the current group finishes, yield it and start a new group
            yield current, group
            current = item
            group = [item]

    # Yield the final group, otherwise we would loose it.
    yield current, group


# To make all the items grouped regardless of
# their order of appearance, sort you input list first
data = ["a", "a", "b", "b", "c", "c", "c", "a"]
data.sort()

for key, group in groupby(data):
    print(key, group)
