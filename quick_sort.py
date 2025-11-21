# Quick Sort.
# It's a divide-and-conquer sorting algorithm
# that works by repeatedly partitioning the list around
# a chosen “pivot” element. Its power comes from splitting
# the problem into smaller subproblems that can be solved independently.

# 1. Choose a pivot: can be anything, say, the mid or random element.
# 2. Partition the array around the pivot to rearrange the array so that:
#   * all elements smaller than the pivot are moved to its left
#   * all elements greater than the pivot are moved to its right
#   * the pivot ends up in its final, sorted position
# 3. Recursively apply quicksort to the subarrays
#    smaller and larger than the pivot.
#    Each subarray chooses its own pivot, get partitioned,
#    and continue to shrink until it has zero or one element
#    which is automatically sorted.
# 4. When all recursive partitions are resolved,
#    every pivot is in its correct place,
#    and the entire array is sorted.

# Intuition:
# Quicksort is like organizing books around a reference book:
# 1. Pick a book (the pivot).
# 2. Move all books alphabetically before it to the left.
# 3. Move all books alphabetically after it to the right.
# 4. Now repeat the same process separately on the left pile and the right pile.
# You never touch the pivot again after placing it;
# you only work on the pieces around it.

# Time O(N log N) average, O(N^2) worst (when constantly picking a bad pivot)
# Space O(log N) due to recursion, but can be worse depending on pivot selection.
#  O(1) is possible, but the solution would be a way more complicated.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Let's use mid elem as pivot
    pivot = arr[len(arr) // 2]
    left  = [x for x in arr if x < pivot]
    mid   = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


print(quick_sort([5, 1, 2, 3, 100, 50, 34, 6, 8, 9]))
