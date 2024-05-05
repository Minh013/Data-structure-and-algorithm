def insertion_sort(arr, size):
    for i in range(1, size):
        value = arr[i]
        j = i
        while(j > 0) and (arr[j - 1] > value):
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = value


arr = [10, 3, 5, 2, 1]
n = len(arr)
print("Array before sorting")
print(arr)
insertion_sort(arr, n)
print("Array after sorting")
print(arr)
