def buble_sort(array, size):
    for i in range(size):
        swaps = 0
        for j in range(0, size - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swaps = 1
            if swaps == 0:
                break


array = [2, 1, 4, 5, 3, 7, 6]
size = len(array)
print("Array before sorting", array)
buble_sort(array, size)
print("Array after sorting")
print(array)
