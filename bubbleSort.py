
def bubbleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr)-1):
            if (arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
            
arr = [9,8,6,6,5,4,3,2,1,0]
bubbleSort(arr)
print(arr)