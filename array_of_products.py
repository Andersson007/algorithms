#!/usr/bin/python3
# Array of Products.
# * A function takes in a non-empty array of ints
#   and returns an array of the same length.
# * Each element in the output array is equal to
#   the product of every other number in the input array,
#   i.e., the value at output[i] is equal to the product
#   of of every number in the input array other that input[i].
# * Note that you're expected to solve this problem
#   without using division.

input_array = [5, 1, 4, 2]
#    output = [8, 40, 10, 20]


# Time O(N)
# Space O(N)
def array_of_products(array):
    products = [1 for _ in range(len(array))]

    # When you go from left to right in this loop,
    # the products array will contain all products
    # to the left of the current position
    # [5, 1, 4, 2] input ->
    # [1, 5, 5, 20] products
    left_running_product = 1
    for i in range(len(array)):
        products[i] = left_running_product
        left_running_product *= array[i]

    # Same as above but to the right of
    # the current position. Then we multiply
    # the result by what we already have in
    # the products array in the current position
    # [5, 1, 4, 2] input <-
    # [8, 8, 2, 1] products
    right_running_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_running_product
        right_running_product *= array[i]

    return products


print(array_of_products(input_array))
