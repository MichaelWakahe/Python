"""
Python implementation of Insertion Sort.

Worst case runtime complexity: O(N^2)
Auxiliary Space: O(1)

Adopted from https://www.geeksforgeeks.org/insertion-sort
Video illustration: https://youtu.be/JU767SDMDvA
"""


def insertion_sort(array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        print(f"\n---i is now {i}---\n")

        key = array[i]
        print(f"Before traversing, key is {key}, array is {array}")

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position.
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
        print(f"After traversing, j is {j}, array is {array}")


# Driver code to test above
arr = [12, 11, 13, 5, 6]

insertion_sort(arr)
print(f"\nSorted array is {arr}")
