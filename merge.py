def merge(arr, start, mid, end):
    new_arr = [] * len (end - start)
    pointer1 = start
    pointer2 = mid + 1
    for i range(end-start):
        if arr[pointer1] <= arr[pointer2]:
            new_arr[i] = arr[pointer1]
            pointer1+=1
        else:
            new_arr[i] = arr[pointer2]
            pointer+=1
    arr[start:end] = new_arr