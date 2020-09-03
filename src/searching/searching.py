def linear_search(arr, target):
    # Your code here
    # for i in range(len(arr)):
    #     if i == target:
    #         return i
    # return False
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i = i+1
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lower = 0
    upper = len(arr)-1

    while lower <= upper:
        mid = (lower + upper) // 2
        if arr[mid] == target:
            pos = mid
            return pos
        else:
            if arr[mid] < target:
                lower = mid+1
            else:
                upper = mid - 1
    return -1
