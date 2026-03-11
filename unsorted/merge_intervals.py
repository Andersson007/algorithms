#!/usr/bin/python
# Merge Intervals.
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals and return an array of
# the non-overlapping intervals that cover all the intervals in the input.


intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Since intervals [1, 3] and [2, 6] overlap,
# they are merged into [1, 6].

# The typical approach to solve the problem is to
# 1. sort the intervals by their start time,
# 2. then iterate through them, comparing each interval
#    with the previous one to see if they overlap.
#    * If they do, you merge them by updating the end time;
#    * if not, you add the interval to the result list.
# It’s a good test of understanding sorting, iteration,
# and edge case handling in algorithms.

# Time O(N log N): sorting complexity
# Space O(N): because we create a new list
def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals

    # Sort a list in place based on the first element
    # of each sub-list (interval):
    # key= tells Python how to compare the items in the list
    # lambda x: x[0] is an anonymous function
    #   "ad hoc" function that takes each sub-list "x" and
    #   returns its first element
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # If merged list is empty OR current interval does not overlap
        # with the previous one
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # There is an overlap, so merge the current interval
            # with the previous one
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

print(merge_intervals(intervals))
print(merge_intervals([[1, 4], [3, 6], [8, 9], [9, 12]]))
print(merge_intervals([[1, 2]]))
print(merge_intervals([[1, 2], [4, 5]]))


# Time O(N log N): sorting complexity
# Space O(N): because we create a new list
def merge_intervals2(intervals):
    intervals.sort(key=lambda x: x[0])

    output = [intervals[0]]
    i = 0
    j = 1

    while j < len(intervals):
        print(output)
        if output[i][1] >= intervals[j][0]:
            if intervals[j][1] > output[i][1]:
                output[i][1] = intervals[j][1]

            j += 1
            continue

        output.append(intervals[j])
        i += 1
        j += 1

    return output


print(merge_intervals2(intervals))
