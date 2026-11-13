#!/usr/bin/python
# Bubble Sort.
# Take in an array of integers, return its sorted version.
# using the Bubble Sort algorithm.
# * We iterate through the array and check if the
#   current number is smaller or equal to the next number.
# * If yes, we move forward to the next one.
# * If not, then we swap the numbers.
# * We track if we swapped any numbers.
# * If yes, we have to reiterate just to check if the
#   array is sorted.
# * If we didn't do any swaps, it means the array is sorted.
# ! Whenever we get the largest number in our array,
#   it's gonna be swapt all the way to the right. So we can
#   optimize it a bit - we don't need to iterate through the
#   entire array each time.

arr = [100, 2, 8, 1024, 10, 10, 20, 6, 55]


# O(N^2) Time where N is a length of the input array
#  as we are looping through the array multiple times
#  in average case, i.e. we'll be doing a bunch of for-loops
#  through the array.
# O(1) Space as we sort the array in place.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no swaps, the list is sorted
        if not swapped:
            break

    return arr


print(bubble_sort(arr))
