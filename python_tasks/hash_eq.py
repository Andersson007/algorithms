#!/usr/bin/python3
# Create a set of objects with a custom __hash__/__eq__; demonstrate
# what breaks when a mutable field changes after insertion.

# The key idea: Sets and dictionaries use the hash value
# to determine where an object lives internally.
# ! The value returned by __hash__ should not change during
# the object's lifetime while it's being used as a set member or dict key.
# Never base __hash__ on mutable state!
# An object's hash must remain stable for as long as it participates
# in a set or serves as a dictionary key.

# Key notions:
# __eq__ defines what it means for two objects to be equal.
# __hash__ returns an integer used by hash tables (set and dict).

class Person():
    def __init__(self, name):
        self.name = name

# If you do:
obj = Person("Alice")
s = {obj}

# and later change the field used in __hash__:
obj.name = "Bob"

# then the following may return False even though
# the object is literally inside the set.
# Why? Because the set stored it using the old hash value,
# but now Python computes a different hash.
print(obj in s)

a = 1
b = 1
# The rule you should learn
# If a == b, then hash(a) == hash(b) must also be true.
print(a == b, hash(a) == hash(b))
print(hash(a), hash(b))


# An example of class that uses custom __hash__ and __eq__
class Product():
    def __init__(self, product_id, name, price=None):
        self._product_id = product_id
        self.name = name
        self.price = price

    @property
    def product_id(self):
        return self._product_id

    # You don't need this setter to make the attribute read-only: just
    # omit it entirely - it will also raise AttributeError though
    # maybe with a bit less obvious message.
    @product_id.setter
    def product_id(self, value):
        raise AttributeError("product_id attribute cannot be changed")

    # Defines what it means for two objects to be equal
    def __eq__(self, other):
        return self.product_id == other.product_id

    # Returns an integer used by hash tables (set and dict)
    def __hash__(self):
        return hash(self.product_id)

# Now Python can efficiently store and look up Product objects in sets and dicts

p = Product(123, "Foo")
print(p.__hash__)  # W/o the custom __hash__ method, would return None
p.product_id = 234
