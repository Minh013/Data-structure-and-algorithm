# Traverse, Update, Search, Display...
# Insertion Operation
def insert_array():
    array = [0, 0, 0]
    x = 0
    print("My empty array")
    for x in range(len(array)):
        print("Array", [x], " = ", array[x])
    print("Let's insert some elements")
    for x in range(len(array)):
        array.append(x)
        array[x] = x + 1
    for x in range(len(array)):
        print("Array", [x], " = ", array[x])


# Deletion Operation
def delete_array():
    array = [0, 0, 0, 0]
    n = len(array)
    print("Before deletion")
    for x in range(n):
        array.append(x)
        array[x] = x + 2
        print("Array", [x], " = ", array[x])
    for x in range(1, n - 1):
        array[x] = array[x + 1]
        n = n - 1
    print("After deletion")
    for x in range(n):
        print("Array", [x], " = ", array[x])


# (1,4,3,5,4,6,10,9,7] i = 4
# Search Operation
def search_element(arr, n, value):
    for i in range(n):
        if arr[i] == value:
            return i
    return -1

# Traversal operation

def show_array():
    a = [1, 2, 3, 4]
    n = len(a)
    print("Array elements are:")
    for x in range(n):
        print("Array", [x], "=", a[x])


def update_array():
    a = [1, 2, 3, 4]
    n = len(a)
    print("Array elements are:")
    for x in range(n):
        print("Array", [x], "=", a[x])
    a[2] = 10
    print("The array elements after updation: ")
    for y in range(n):
        print("Array", [y], "=", a[y])


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 10]
    print("Array elements are:")
    for x in range(len(arr)):
        print("Array", [x], " = ", arr[x])
    value = 2
    n = len(arr)
    index = search_element(arr, n, value)
    if index != -1:
        print("Element", value, "found at position =", str(index + 1))
    else:
        print("Element was not found in the array")

    show_array()
    update_array()
    # insert_array()
    # delete_array()


