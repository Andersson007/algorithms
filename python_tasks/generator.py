#!/usr/bin/python3
# Write a generator that reads a 1GB+ file and yields
# parsed records without loading the file into memory.
# This task is about streaming data instead of loading it all into memory.
# Don't do something like:
# data = file.read()
# or
# lines = file.readlines()
# Both load the entire file into memory, which is impractical for a 1 GB+ file.
# Instead, read one line (or one chunk) at a time.

# A custom generator in Python is a function that uses
# the yield keyword to produce values one at a time
# instead of returning them all at once.
# The generator pauses after each yield and resumes where it left off when:
# * you call next(gen), or
# * you iterate over it with a for loop.

# Key points:
# * Use yield instead of return to produce values lazily
#   (generates a value on demand; it doesn't compute all values upfront).
# * The generator remembers its state between iterations.
# * It is memory-efficient because it generates values on demand.

# Example
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

# Use next() to retrieve values manually
gen = count_up_to(3)
print(next(gen))
print(next(gen))
print(next(gen))


# Write a generator that reads a 1GB+ file and yields
# parsed records without loading the file into memory.
# Solution:
def parse(file):
    for line in file:
        # Do some complex parsing
        # Transform and/or filter data here
        yield line.strip()


with open("example.txt", "r") as file:
    for line in parse(file):
        print(line)
