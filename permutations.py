#!/usr/bin/python3
# Permutations.
# * A permutation is a unique ordering.
# * A combination is another form of groupping
#   of elements of a set, but the ordering doesn't matter.
# 
# Write a function that takes in an array of unique
# integers and returns an array of all permutations
# of those integers in no particular order.
#
# * If the input array is empty, the func should
#   return an empty array.
#
# The core idea of backtracking is to build a solution step-by-step.
# It explores a potential path, and as soon as it determines
# the path cannot lead to a valid solution, it "backtracks" (goes back)
# and tries a different path.
# Imagine you have a set of numbers like [1, 2, 3] and you want to find
# all their arrangements:
# 1. Choose: Start by picking an element for the first position.
#    You can choose 1, 2, or 3. Let's pick 1.
# 2. Explore: Now, with 1 in the first position,
#    you need to pick an element for the second position from
#    the remaining numbers [2, 3]. Let's pick 2.
# 3. Explore Further: With [1, 2] fixed, only 3 is left for the last position.
#    This gives you your first complete permutation: [1, 2, 3].
# 4. Backtrack: Go back to the previous step (step 2).
#    You already explored picking 2. Now, try the other option for
#    the second position, which is 3. This gives you [1, 3].
# 5. Explore Again: With [1, 3] fixed, only 2 is left for the last position.
#    This gives you another permutation: [1, 3, 2].
# 6. Backtrack Further: Go back to the very first step (step 1).
#    You've now found all permutations that start with 1.
#    You backtrack and "un-choose" 1. Now, you choose the next available
#    number for the first position, which is 2.
# 7. Repeat: You repeat the entire process, which will find all
#    permutations starting with 2 ([2, 1, 3] and [2, 3, 1]) and
#    then all permutations starting with 3 ([3, 1, 2] and [3, 2, 1]).
#
# This "choose, explore, and un-choose (backtrack)" pattern is the essence
# of the algorithm. A clean way to implement this is by swapping elements
# in the array to represent "choosing" an element for the current position.

array = [1, 2, 3]

# Helper function to perform the backtracking
def find_permutations(index, array, result):
    """
    Recursively finds permutations by swapping elements.

    Args:
        index: The current position we are trying to fill.
        array: The list of numbers (modified in place).
        result: A list to store all the found permutations.
    """
    # Base case: If we have filled all positions (index is at the end),
    # we have found a complete permutation.
    if index == len(array):
        # Add a copy of the current state of 'array' to the result.
        result.append(list(array))
        return

    # Recursive step: Iterate through the remaining numbers to place at the 'index'.
    for i in range(index, len(array)):
        # 1. Choose: Swap the current element with the element at 'index'.
        # This effectively places the i-th element at the current 'index' position.
        # I.e. you put 1 in the first position and then calculate permutations
        # for the remaining positions, then you put 2 and do the same for 1 and 3,
        # then you put 3, and calculate remaining positions for 2 and 1, etc.
        array[index], array[i] = array[i], array[index]

        # 2. Explore: Recursively call the function for the next position.
        find_permutations(index + 1, array, result)

        # 3. Un-choose (Backtrack): Swap the elements back to their original
        # positions to explore other possibilities in the next loop iteration.
        array[index], array[i] = array[i], array[index]

# Time O(N!N): as we have a loop inside the helper method
#   that we call recursively
# Time O(N!N): as we construct the final array
def get_permutations(array):
    """
    Generates all permutations for a given list of numbers.

    Args:
        array: A list of numbers.

    Returns:
        A list of lists, where each inner list is a unique permutation.
    """
    result = []
    find_permutations(0, array, result)
    return result


print(get_permutations(array))
