arr = [64,34,90, 25, 12, 22, 11]

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j] , arr[i]
    return arr

print(bubblesort(arr))






