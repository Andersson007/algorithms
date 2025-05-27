#!/usr/bin/python
# Validate Sequence.
# A function takes two non-empty arrays of integers
# and determines if the second array is a subsequence
# of the first array.

array = [2, 3, 5, 10, 4, 8, 9]
sequence1 = [2, 10, 8]  # is a subsequence
sequence2 = [-1, 5, 11]  # is not a subsequence

# Time: O(n) when n is the length of the main array
# Space: O(1) as we're not storing anything extra
def validate_sequence(array, sequence):
    # Use a pointer to the array and a pointer
    # to the sequence in a loop that works until
    # we reach an end of one of them.
    seq_idx = 0
    arr_idx = 0

    while seq_idx < len(sequence) and arr_idx < len(array):
        if sequence[seq_idx] == array[arr_idx]:
            seq_idx += 1
        arr_idx += 1

    # If we are at the end of the sequence after traversing,
    # it means all its elements are in the array.
    return seq_idx == len(sequence)
