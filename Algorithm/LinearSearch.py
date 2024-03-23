def linear_search(arr, n, value):
    count = 0
    for i in range(n):
        if arr[i] == value:
            print("The element is found at position ", (i + 1))
            # count = count + 1
    if count == 0:
        print("The element is not present in the array")

arr = [1, 2, 13, 12, 60, 6, 100, 86, 90, 101]
n = len(arr)
value = 13
linear_search(arr, n, value)