#!/usr/bin/python3
# Write an exampe of using the @property descriptor.
# You use @property when you need to execute some method
# when accessing an attribute of your class.
# A typical use case is adding a setter for some validation
# without changing any pre-existing code.
# In the example below, the original Product class had no validation
# for the price field. It looked like:
# class Product()
#     def __init__(self):
#         self.price = None
#
# In our code, we assign some value to the price attribute,
# e.g. p.price = 5. When using the property descriptor, we don't
# need to touch it at all - we just need to add two methods (getter and setter)
# to our class as we did below

class Product():
    def __init__(self):
        self._price = None

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise ValueError("price must be an integer")
        elif value < 0:
            raise ValueError("price must be positive")
        self._price = value


p = Product()

p.price = 5
print(p.price)

try:
    p.price = -1
except Exception as e:
    print(e)

try:
    p.price = "blah"
except Exception as e:
    print(e)
