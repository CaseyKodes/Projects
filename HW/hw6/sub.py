def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = float('-inf')
    max_left = 0
    max_right = 0
    total = 0

    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0

    for j in range(mid + 1, high + 1):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(arr, low, high):
    if low == high:
        return low, high, arr[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = \
        find_max_subarray(arr, low, mid)
    right_low, right_high, right_sum = \
        find_max_subarray(arr, mid + 1, high)
    cross_low, cross_high, cross_sum = \
        find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum
    

# Example usage:
arr = [1, 1, 2, 16, -5, 4]
start, end, max_sum = find_max_subarray(arr, 0, len(arr)-1)
print("Full array: ", arr)
print("Maximum subarray:", arr[start:end + 1], "with sum:", max_sum)