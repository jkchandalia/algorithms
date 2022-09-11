def partition(arr, start, end, pivot_index):
    #Lumoto's algorithm
    pointer_division = start
    pivot_val = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    for i in range(start, end):
        if arr[i] <= pivot_val:
            arr[pointer_division], arr[i] = arr[i], arr[pointer_division]
            pointer_division+=1
    arr[end], arr[pointer_division] = arr[pointer_division], arr[end]
    return pointer_division
        

def partition2(arr, start, end, pivot_index):
    #Hoare's algorithm
    pointer_less = start
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    pointer_more = end - 1
    print(arr[end])
    i = pointer_less
    while pointer_less <= pointer_more:
        if arr[i] <= arr[end]:
            arr[pointer_less], arr[i] = arr[i], arr[pointer_less]
            pointer_less+=1
            i+=1
        elif arr[i] > arr[end]:
            arr[pointer_more], arr[i] = arr[i], arr[pointer_more]
            pointer_more-=1
        print(arr)
    print(pointer_less)
    print(pointer_more)
    arr[pointer_less], arr[end] = arr[end], arr[pointer_less]
    print(arr)
    return pointer_more

arr2 =  [2, 5, -3, 20, 16, 1, 11, -10, 30, 50, 3, 4]
partition2(arr2, 0, 11, 6)