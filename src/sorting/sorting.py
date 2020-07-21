import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    add_second_here = int(len(arrA))

    for i in range(len(arrA)):
        merged_arr[i] = arrA[i]

    for i in range(len(arrB)):
        merged_arr[add_second_here] = arrB[i]
        add_second_here += 1

    return sorted(merged_arr)

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    
    # if length of list is NOT 1, divide:
    if len(arr) <= 1:
        return arr

    mid = math.floor(len(arr) / 2)
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    # Merge arrays together comparing left values and sorting
    return merge(left_arr, right_arr)
    


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#     pass


# def merge_sort_in_place(arr, l, r):
#     # Your code here
#     pass

