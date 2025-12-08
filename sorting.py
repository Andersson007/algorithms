def bubble_sort(nums):

    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        if not swapped:
            return nums

    return nums


def insertion_sort(nums):

    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1

    return nums

# Time O(N log N): best/average; O(N^2) worst
#   when constantly picking a bad pivot like the smallest
#   or largest element in the input array
# Space O(lon N): due to recursion
def quick_sort(nums):

    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]

    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)


def merge_sort(nums):

    return nums


print(bubble_sort([8, 10 , 1, 2, 25, 5, 15, 0]))
print(insertion_sort([8, 10 , 1, 2, 25, 5, 15, 0]))
print(quick_sort([8, 10 , 1, 2, 25, 5, 15, 0]))
print(merge_sort([8, 10 , 1, 2, 25, 5, 15, 0]))
