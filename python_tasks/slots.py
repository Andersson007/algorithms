#!/usr/bin/python3
# Build a class that uses `__slots__` and measure the memory
# difference vs a regular class with 100k instances.

# __slots__ is a class attribute that tells Python
# 1) which instance attributes are allowed and
# 2) lets Python store them more efficiently.
# Without __slots__, each object has a __dict__ to hold attributes.

# Main takeways:
# * Regular objects store attributes in a per-instance dictionary.
# * __slots__ removes that dictionary (in most cases).
# * This can save a lot of memory when you create many instances.
# * The benefit becomes noticeable at large scales (like 100k+ objects).
# * Install pympler and use asizeof.asizeof for getting accurate memory
#     usage including referenced objects.

# Use __slots__ when:
# * You create lots of objects.
# * Their attributes are known in advance.
# * You want to save memory.

from pympler import asizeof

class PersonRegular():
    def __init__(self):
        self.name = None

p = PersonRegular()
p.name = "Alice"
# You can add random attributes w/o __slots__
# because they are stored in a dictionary called  __dict__
p.age = 30  # !


class PersonMemEfficient():
    __slots__ = ("name", "age")

    def __init__(self):
        self.name = None
        self.age = None


# Measure the memory difference
regular_people = []
for _ in range(100000):
    p = PersonRegular()
    p.name = "Alice"
    p.age = 30
    regular_people.append(p)


slots_people = []
for _ in range(100000):
    p = PersonMemEfficient()
    p.name = "Alice"
    p.age = 30
    slots_people.append(p)


# Get mem footprint in MB
size_regular_mb = int(asizeof.asizeof(regular_people) / (1024 ** 2))
size_slots_mb = int(asizeof.asizeof(slots_people) / (1024 ** 2))

print("People 100k objects total memory footprint in MB:\n"
      f"- regular: {size_regular_mb}\n"
      f"- __slots__: {size_slots_mb}")  # Occupies almost 3 times less space!
