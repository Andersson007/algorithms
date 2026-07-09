#!/usr/bin/python3
# Write a generator that supports `.send()`
# to dynamically change its behavior mid-iteration.
# This task is about learning that generators are two-way communication
# mechanisms—not just producers of values.
# The .send() method allows you to send a value into a paused generator
# at the point where it last yielded

# 1. Write a generator
# A normal generator only does this:
#   yield value
# The caller repeatedly does:
#   next(gen)
# to receive values.

# 2. Support .send()
# Instead of only receiving next(), your generator should also accept values from the caller:
#   gen.send(value)
# Those values influence what the generator does next.

# 3. Change behavior during iteration
# For example, the generator might:
# * change its increment,
# * switch modes,
# * update a filter threshold,
# * change a multiplier,
# without being restarted.

# 1. yield total sends total back to the caller.
# 2. The generator pauses and waits
# 3. When .send(x) is called, the yield expression evaluates to x, so
# value = x
def accumulator():
    total = 0

    while True:
        value = yield total

        # next() is equivalent to .send(None),
        # so this condition prevents total += None
        if value is not None:
            total += value


gen = accumulator()

# Start the generator
print(next(gen))  # 0

# Send values into it
print(gen.send(5))  # 5
print(gen.send(3))  # 8
print(next(gen))    # 8
print(next(gen))    # 8


# Practical example: A classic and more practical use case for .send()
# is maintaining state without using a class.
# For example, This generator keeps track of all numbers sent to it
# and returns the current average.
def running_average():
    total = 0
    count = 0

    while True:
        number = yield total / count if count else 0.0

        if number is not None:
            total += number
            count += 1


avg = running_average()
print(next(avg))      # 0.0

print(avg.send(10))   # 10.0
print(avg.send(20))   # 15.0
print(avg.send(30))   # 20.0

print(next(avg))      # 20.0 (peek without changing)
