# Write a Python program for Linear search
# linear_search([1,2,3,5,8], 6) -> False
# linear_search([1,2,3,5,8], 5) -> True

def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high and not found:
        middle = (low + high) // 2
        if arr[middle] == value:
            found = True
        else:
            if value < arr[middle]:
                high = middle - 1
            else:
                low = middle + 1
    return found


def linear_search(arr, value):
    for i in arr:
        if i == value:
            return True
    return False


print(binary_search([1, 2, 3, 5, 8], 6))
