"""
Python implementation of Quicksort.

Worst case runtime complexity: O(N^2)
Average case runtime complexity: O(N Log N)
Auxiliary Space: O(Log N)

Adapted from: Data Structures and Algorithms with Python text by Kent D. Lee and Steve Hubbard.
Video illustration: https://www.youtube.com/watch?v=JS524MqKM0Q
"""


def partition(seq, start, stop):
    pivotIndex = start  # pivotIndex comes from the start location in the list.
    pivot = seq[pivotIndex]
    i = start + 1
    j = stop - 1
    print(f"start is {start}, stop is {stop}")

    while i <= j:
        # Increment the start pointer till it finds an element greater than pivot (seq[i] <= pivot)
        while i <= j and not pivot < seq[i]:
            i = i + 1

        # Decrement the end pointer till it finds an element less than pivot (seq[j] > pivot)
        while i <= j and pivot < seq[j]:
            j = j - 1

        if i < j:
            print(f"i is {i}, seq[i] is {seq[i]}, j is {j}, seq[j] is {seq[j]}")
            seq[i], seq[j] = seq[j], seq[i]
            i = i + 1
            j = j + 1

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    print(f"i is {i}, j is {j}, seq[pivotIndex] is {seq[pivotIndex]}, seq[j] is {seq[j]}")
    seq[pivotIndex], seq[j] = seq[j], pivot

    print(f"Array is now {seq}, pivot_index to be returned is {j}")

    # Returning end pointer to divide the array into 2
    return j


def quicksort_recursively(seq, start, stop):
    if start >= stop - 1:
        return

    # pivot_index ends up in between the two halves where the pivot value is in its final location.
    pivot_index = partition(seq, start, stop)

    print(f"Calling recursive on first half, start is {start}, pivot_index is {pivot_index}")
    quicksort_recursively(seq, start, pivot_index)
    print(f"Calling recursive on second half, start is {start}, pivot_index is {pivot_index}")
    quicksort_recursively(seq, pivot_index + 1, stop)


def quicksort(seq):

    quicksort_recursively(seq, 0, len(seq))


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Array length is {len(arr)}")

quicksort(arr)
print(f"\nSorted array is: {arr}")
