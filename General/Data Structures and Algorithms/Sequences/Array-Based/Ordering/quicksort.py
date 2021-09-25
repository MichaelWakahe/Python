"""
Python implementation of Quicksort.

Worst case runtime complexity: O(N^2)
Average case runtime complexity: O(N Log N)
Auxiliary Space: O(Log N)

Adapted from: Data Structures and Algorithms with Python text by Kent D. Lee and Steve Hubbard.
Video illustration: https://www.youtube.com/watch?v=JS524MqKM0Q
"""

import random


def partition(seq, start, stop):
    # pivotIndex comes from the start location in the list.
    pivotIndex = start
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1

    while i <= j:
        # while i <= j and seq[i] <= pivot:
        while i <= j and not pivot < seq[i]:
            i = i + 1

        # while i <= j and seq[j] > pivot:
        while i <= j and pivot < seq[j]:
            j = j - 1

        if i < j:
            tmp = seq[i]
            seq[i] = seq[j]
            seq[j] = tmp
            i += 1
            j -= 1

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    seq[pivotIndex], seq[j] = seq[j], pivot

    # Returning end pointer to divide the array into 2
    return j


def quicksort_recursively(seq, start, stop):
    if start >= stop - 1:
        return

    # pivot_index ends up in between the two halves where the pivot value is in its final location.
    pivot_index = partition(seq, start, stop)

    quicksort_recursively(seq, start, pivot_index)
    quicksort_recursively(seq, pivot_index + 1, stop)


def quicksort(seq):
    # Optional: randomize the sequence first
    # for i in range(len(seq)):
    #     j = random.randint(0, len(seq) - 1)
    #     tmp = seq[i]
    #     seq[i] = seq[j]
    #     seq[j] = tmp

    quicksort_recursively(seq, 0, len(seq))


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Array length is {len(arr)}")

quicksort(arr)
print(f"\nSorted array is: {arr}")
