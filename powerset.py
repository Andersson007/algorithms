#!/usr/bin/python3
# Write a func that takes in an array of unique
# integers and returns its powerset.
# The powerset P(X) of set X is the set of
# all subsets of X.
# Note that the sets in the powerset do not need
# to be in any particular order.

array = [1, 2]
# output: [[], [1], [2], [1, 2]]

# The function generates the powerset of an array
# by iteratively building upon existing subsets.
# Time O(N * 2^N): the outer loop runs N times.
#   The inner loop's number of iterations doubles with each step
#   of the outer loop. The total number of subsets generated is 2^N.
# Space O(N * 2^N): A set with N elements has 2^N subsets, see ^.
def powerset(array):
    # The algorithm builds the powerset incrementally.
    # Start with a base case: an empty set
    powerset = [[]]

    # Iterate through each element of
    # the input array one by one.
    # For each element, it goes through all the subsets that
    # have been generated so far and creates a new subset
    # by adding the current element to each of them.
    # These new subsets are then added to the powerset list.
    # This process effectively doubles the number of subsets
    # in the list for every element from the input array.
    for elem in array:
        for i in range(len(powerset)):
            curr_subset = powerset[i]
            powerset.append(curr_subset + [elem])

    return powerset


print(powerset(array))
