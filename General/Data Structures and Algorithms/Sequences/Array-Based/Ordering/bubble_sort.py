"""
Python implementation of Bubble Sort.

Worst case runtime complexity: O(N^2)
Auxiliary Space: O(1)

Adopted from https://www.geeksforgeeks.org/bubble-sort
Video illustration: https://youtu.be/xli_FI7CuzA
"""


def bubble_sort(array):
    n = len(array)

    # Traverse through all array elements
    for i in range(n):
        print(f"\n---i is now {i}---\n")

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            print(f"Before swap, j is {j}, array is {array}")

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

            print(f"After swap attempt, array is {array}\n")


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Array length is {len(arr)}")

bubble_sort(arr)
print(f"\nSorted array is: {arr}")
