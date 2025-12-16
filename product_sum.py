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


# Time O(N): as each element is visited only once.
# Space O(D): where D is maximun nested depth
#   of the input list. Space is used by the
#   recursion call stack.
#   Poses the stack overflow risk.
def product_sum_rec(nums, depth):
    total = 0
    for elem in nums:
        if isinstance(elem, list):
            total += product_sum_rec(elem, depth + 1)

        else:
            total += elem

    return total * depth


# Time O(N)
# Space O(D): where D is max stack (list/array) size.
#  Both the recursive and iterative solutions use O(D) space,
#  where D is the maximum nesting depth.
#  However, here the dynemic memory (heap) is used.
def product_sum_iter(nums):
    stack = [(nums, 1)]
    total = 0

    while stack:
        current, depth = stack.pop()
        subtotal = 0

        for elem in current:
            if isinstance(elem, list):
                stack.append((elem, depth + 1))
            else:
                subtotal += elem

        total += subtotal * depth

    return total


print(product_sum_rec([1, 2, [3, 4], 5], 1))
print(product_sum_iter([1, 2, [3, 4], 5]))
