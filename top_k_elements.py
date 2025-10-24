#!/usr/bin/python
# Top K Frequent Elements.
# A func takes in a non-empty array of integers nums
# and an integer k, and returns an array of the k most
# frequent elements. The order of the answer is not important.
# To solve it is a two-step process:
# Step 1: count frequencies
# Step 2: find top K with a min-heap of size k
# 1. Iterate through the (elem, frequency) pairs
#    from our hash map
# 2. For each pair, we push it onto the heap
# 3. If the heap size grows larger than k, we remove
#    the smallest element (the one at the top of the heap).
# 4. By continuously removing the element with the lowest
#    frequency whenever the heap gets too big, we ensure
#    that the heap always holds the top k most frequent
#    elements seen so far.

import heapq

nums = [1, 1, 1, 2, 2, 3]
k = 2
# output: [1, 2]

# Time O(N log k): it's a time complexity of building the heap
#   - Iterate over the frequency dict: O(N) entries in the worst case
#   - For each (elem, freq): push into heap -> O(log k)
#   - Popping an element from heap if needed -> O(log k)
# Space O(N): in worst case all elements of nums are unique
def top_k_elements(nums, k):
    if not nums or len(nums) < k:
        return []

    counts = {}

    # Step 1: count frequencies
    for n in nums:
        if n not in counts:
            counts[n] = 1
            continue

        counts[n] += 1

    # Step 2: find top K with a min-heap of size k
    min_heap = []
    for num, freq in counts.items():
        # Pushes the new item to the end of the list
        # rearranging the list to ensure the smalles
        # item is always at the first position
        # preserving the min-heap property
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            # If the length of the heap > k,
            # remove the element with the smallest frequency
            heapq.heappop(min_heap)

    top_k = [num for freq, num in min_heap]

    return top_k


print(top_k_elements(nums, k))
