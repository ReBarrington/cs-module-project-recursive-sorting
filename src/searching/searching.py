import math

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # if empty, return -1
    if not arr:
        return -1

    middle = round((start + end) / 2)

    # base case
    if target == arr[middle]:
        return middle

    else:
    
        if target > arr[middle]:
            start = middle + 1
            return binary_search(arr, target, start, end)
        
        elif target < arr[middle]:
            end = middle - 1
            return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
