def binary_search(arr, low, high, value):
    middle = (high + low) // 2
    if low <= high:
        if arr[middle] == value:
            print("Found at index", middle)
        elif value < arr[middle]:
            binary_search(arr, low, middle - 1, value)
        elif value > arr[middle]:
            binary_search(arr, middle + 1, high, value)
    if low > high:
        print("Can't search value", value)


arr = [1, 2, 3, 4 ,5 ,6, 7, 8]
n = len(arr)
low = 0
high = n - 1
value = 10
binary_search(arr, low, high, value)
