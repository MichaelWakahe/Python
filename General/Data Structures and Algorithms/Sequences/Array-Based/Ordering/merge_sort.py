"""
Python implementation of Merge Sort.

Worst case runtime complexity: O(N Log N)
Average case runtime complexity: O(N Log N)
Auxiliary Space: O(N)

It is a stable algorithm.

Video illustration: https://youtu.be/4VqmGXwpLqc
"""

from typing import List


def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid

    # Merge the two lists while each has more elements
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i = i + 1
        else:
            lst.append(seq[j])
            j = j + 1

    # Copy in the rest of the start to mid sequence
    while i < mid:
        lst.append(seq[i])
        i = i + 1

    # Many merge sort implementations copy the rest of the sequence from j to stop at this point.
    # This is not necessary since in the next part of the code the same part of the sequence would be copied right back
    # to the same place.
    # while j < stop:
    #   lst.append(seq[j])
    #   j+=1
    # Copy the elements back to the original sequence
    for i in range(len(lst)):
        seq[start + i] = lst[i]


def merge_sort_recursively(seq, start, stop):
    # We must use >= here only when the sequence we are sorting
    # is empty. Otherwise start == stop-1 in the base case.
    if start >= stop - 1:
        return

    mid = (start + stop) // 2

    merge_sort_recursively(seq, start, mid)
    merge_sort_recursively(seq, mid, stop)
    merge(seq, start, mid, stop)


def merge_sort(seq):
    merge_sort_recursively(seq, 0, len(seq))


# Driver code to test above
my_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Array length is {len(my_arr)}")

merge_sort(my_arr)
print(f"\nSorted array is: {my_arr}")


"""
An alternative implementation is below.
"""


def merge_arrays(arr1: List, arr2: List) -> List:
    merged_lst = []

    j = k = 0

    while j < len(arr1) and k < len(arr2):
        if arr1[j] < arr2[k]:
            merged_lst.append(arr1[j])
            j = j + 1
        else:
            merged_lst.append(arr2[k])
            k = k + 1

    if j < len(arr1):
        merged_lst = merged_lst + arr1[j:]

    if k < len(arr2):
        merged_lst = merged_lst + arr2[k:]

    return merged_lst


def mergesort(arr: List) -> List:
    if len(arr) == 1:
        return arr

    arr1 = arr[:len(arr) // 2]
    arr2 = arr[len(arr) // 2:]

    arr1 = mergesort(arr1)
    arr2 = mergesort(arr2)

    return merge_arrays(arr1, arr2)


# Driver code to test above
my_arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Array length is {len(my_arr)}")

my_arr = mergesort(my_arr)
print(f"\n2nd Sorted array is: {my_arr}")
