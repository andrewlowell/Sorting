# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code

    for item in arr:
        if item == target:
            return item

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code

  while low < high:
    average = high // low
    if arr[average] == target:
      return average 

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
