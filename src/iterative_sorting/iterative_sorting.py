# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    print(len(arr))
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap

        ephemeral = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = ephemeral

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(0, len(arr) - 1):
        get_rid_of_linting_error = i
        get_rid_of_linting_error += 1
        for j in range(0, len(arr) -1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr