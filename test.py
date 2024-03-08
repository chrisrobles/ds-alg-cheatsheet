def deleteMiddle(arr, i, length):
    for index in range(i, length-1):
        arr[index] = arr[index+1]
    arr[length-1] = 0
arr = list(range(5))
deleteMiddle(arr, 0,5)
print(arr)
