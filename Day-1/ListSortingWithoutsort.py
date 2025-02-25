def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize in case the list is already sorted
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break
    return arr

# Test the function
input_list = [64, 25, 12, 22, 11,30,35]
sorted_list = bubble_sort(input_list)
print(f"Sorted list: {sorted_list}")
