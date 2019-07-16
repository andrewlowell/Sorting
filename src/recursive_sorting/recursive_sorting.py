# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    if elements == 0:
      merged_arr = []
    elif len(arrA) == 0:
      merged_arr = arrB
    elif len(arrB) == 0:
      merged_arr = arrA
    else:
      if arrA[0] < arrB[0]:
        merged_arr = [arrA[0]] + merge(arrA[1:], arrB)
      else:
        merged_arr = [arrB[0]] + merge(arrB[1:], arrA)

    
    return merged_arr

print(merge([2, 3, 5, 7, 9, 12, 45, 67, 89], [4, 6, 8, 13, 16, 26, 35]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:
      div = len(arr) // 2
      arr = merge(merge_sort(arr[:div]), merge_sort(arr[div:]))

    return arr

print(merge_sort([2, 5, 3, 8, 5, 8, 23, 67, 43, 89, 234, 567, 234, 12, 67, 34, 6, 3, 1]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
