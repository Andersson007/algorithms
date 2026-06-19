#!/usr/bin/python3
# Create a diamond inheritance hierarchy and predict/verify
# the MRO; override one method and trace the call chain.
# This task is about understanding multiple inheritance
# and Python's Method Resolution Order (MRO).
# 1. Create a diamond hierarchy
#      A
#     / \
#    B   C
#     \ /
#      D
# 2. Predict the MRO
# Before running the code, try to answer:
# > If I call a method on D, which class's implementation will Python use first?
# Then verify using:
# D.__mro__ or D.mro()
#
# 3. Override a method.
# Give several classes a method with the same name.
# For example:
# A.foo()
# B.foo()
# C.foo()
# and possibly D.foo().
# Predict which version gets called.
#
# 4. Trace the call chain using super()
# The most important part is usually:
# def foo(self):
#    ...
#    super().foo()
# in each class.
# When you call d.foo() observe the order.

# An important takeway: MRO in Python is a single liniar order
#   which prevents classes from being called twice.

class A():
    def foo(self):
        print("A")
        # End of chain

class B(A):
    def foo(self):
        print("B")
        super().foo()

class C(A):
    def foo(self):
        print("C")
        super().foo()

class D(B, C):
    def foo(self):
        print("D")
        super().foo()


print(D.__mro__)
# Same as
print(D.mro())

d = D()
print(d.foo())
