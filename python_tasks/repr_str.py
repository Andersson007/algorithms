#!/usr/bin/python3
# __repr__ is a special method in Python that defines
# the official string representation of an object.
# Python uses the object's __repr__ method when you:
# * print an object in the Python interpreter
# * inspect it in a debugger,
# * or call repr(obj).

# * __repr__	Unambiguous representation, mainly for developers/debugging
# * __str__	User-friendly representation
# ! The difference is not what they must return, but when Python uses each method.

class Developer():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Developer(name='{self.name}', age={self.age})"



class User():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"User(name='{self.name}', age={self.age})"


d = Developer("Alice", 30)
u = User("Bob", 32)

print(repr(d))  # Calls __repr__
print(u)  # Calls __str__
