def partition(arr, start, end, pivot_index):
    pointer_division = start
    pivot_val = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    for i in range(start, end):
        if arr[i] <= pivot_val:
            arr[pointer_division], arr[i] = arr[i], arr[pointer_division]
            pointer_division+=1
    arr[end], arr[pointer_division] = arr[pointer_division], arr[end]
        
