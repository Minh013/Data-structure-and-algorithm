def selection_sort(arr, size):
    for i in range(size):
        low = i
        for j in range(i + 1, size):
            if arr[j] < arr[low]:
                low = j
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp


arr = [4, 6, 1, 8, 5, 3]
size = len(arr)
print("Before sorting array: ")
print(arr)
print("After sorting array: ")
selection_sort(arr, size)
print(arr)
