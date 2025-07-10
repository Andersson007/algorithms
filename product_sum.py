#!/usr/bin/python3
# Product Sum.
# * Write a function that takes in a "special"
#   array and returns its product sum.
# * The "special" array is a non-empty array that
#   contains either integers or other special arrays.
# * The "product sum" of a "special" array is the
#   sum of its elements where "special" arrays inside
#   it are summed up themselves and then are multiplied
#   by their level of depth.
# * [x, y] is x + y
# * [x, [y, z]] is x + 2(y + z)
# * [x, [y, [z]] is x + 2(y + 3z)

arr = [1, 2, [5, 8]]

# Time O(N), where N is a number of elements
# Space O(D), where D is the largest depth of subarrays
def product_sum(arr, depth=1):
    # Use recursion

    s = 0
    for elem in arr:
        if type(elem) is int:
            s += elem
        else:
            s += product_sum(elem, depth + 1)

    return depth * s


print(product_sum(arr))
