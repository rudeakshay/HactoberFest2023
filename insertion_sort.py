def insertion_sort(arr):
    """
    Sorts a list in ascending order using the Insertion Sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key in its correct position
        arr[j + 1] = key

# Example usage:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(unsorted_list)
print("Sorted list:", unsorted_list)
