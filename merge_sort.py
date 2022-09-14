def merge(arr, start, mid, end):
    print("in merge")
    print(start, mid, end)
    new_arr = [None] * (end - start + 1)
    print(len(new_arr))
    pointer1 = start
    pointer2 = mid + 1
    counter2 = 0
    print("pointer1: "+str(pointer1))
    print("pointer2: "+str(pointer2))
    print("counter: "+str(counter2))
    while (pointer1<=mid) and (pointer2<=end):
        print("pointer1: "+str(pointer1))
        print("pointer2: "+str(pointer2))
        print("counter: "+str(counter2))
        print(new_arr)
        if arr[pointer1] <= arr[pointer2]:
            new_arr[counter2] = arr[pointer1]
            pointer1+=1
            counter2+=1
        else:
            new_arr[counter2] = arr[pointer2]
            pointer2+=1
            counter2+=1
    while pointer1 <= mid:
        new_arr[counter2] = arr[pointer1]
        pointer1+=1
        counter2+=1
    while pointer2 <= end:
        new_arr[counter2] = arr[pointer2]
        pointer2+=1
        counter2+=1
    arr[start:end+1] = new_arr



def merge_sort(arr, start, end):
    if start >= end:
        return
    else:
        midpoint = int(start + (end - start)/2)
        print("indices")
        print(midpoint)
        print(start)
        print(end)
        merge_sort(arr, start, midpoint)
        merge_sort(arr, midpoint+1, end)
        merge(arr, start, midpoint, end)




arr = [2, 20, 15, 4, 7, 13, 200, -2, 6]
start = 0
end = 8
mid = 4
arr2 = [2, 4, 7, 15, 20, -2,6, 13, 2000]
merge(arr2, 0, 4, 8)
merge_sort(arr, start, end)

