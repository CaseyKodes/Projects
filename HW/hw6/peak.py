def find_peak_point(arr, left, right):
    # Base case: if the array has only one element, it is the peak
    if left == right:
        return left

    mid = (left + right) // 2

    # If the mid element is less than the next element, the peak is to the right
    if arr[mid] < arr[mid + 1]:
        return find_peak_point(arr, mid + 1, right)
    # If the mid element is greater than or equal to the next element, the peak is to the left
    else:
        return find_peak_point(arr, left, mid)

# Example usage:
arr = [1, 2, 7, 4, 3]
peak_index = find_peak_point(arr, 0, len(arr)-1)
print("Peak point:", peak_index)