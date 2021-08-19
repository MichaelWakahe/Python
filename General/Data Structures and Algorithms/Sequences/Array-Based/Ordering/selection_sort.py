"""
Python implementation of Selection Sort.

Worst case runtime complexity: O(N^2)
Auxiliary Space: O(1)

Adopted from https://www.geeksforgeeks.org/selection-sort
Video illustration: https://youtu.be/g-PGLbMth_g
"""


def selection_sort(array):
    # Traverse through all array elements
    for i in range(len(A)):
        print(f"\n---i is now {i}---\n")

        # Find the minimum element in remaining unsorted array
        min_index = i
        print(f"Before traversing, array is {array}")
        for j in range(i + 1, len(A)):

            if A[min_index] > A[j]:
                min_index = j

        # Swap the found minimum element with the first element
        # Note: if 'A[min_index]' was lesser than all the values in the unsorted array, then 'min_index == i'
        A[i], A[min_index] = A[min_index], A[i]
        print(f"After swapping, array is {array}")


# Driver code to test above
A = [64, 25, 12, 22, 11]

selection_sort(A)

print(f"Sorted array: {A}")
