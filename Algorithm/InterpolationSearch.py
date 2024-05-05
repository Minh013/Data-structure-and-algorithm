def interpolation_search(value, arr):
    lo = 0
    hj = len(arr) - 1
    res = -1
    comp = 1
    index = -1
    while(lo <= hj):
        print("Comparison", comp)
        print("lowest index of the array:", lo)
        print(arr[lo])
        print("Highest index of the array:", hj)
        print(arr[hj])
        comp = comp + 1
        # The use of the formula
        res = lo + (((hj - lo) * (value - arr[lo]))//(arr[hj] - arr[lo]))
        print("result = ", res)

        # Check data found
        if(arr[res] == value):
            index = res
            break
        else:
            if(arr[res] < value):
                lo = res + 1
            else:
                hj = res - 1

    print("Total comparison:", comp - 1)
    return index
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
location = interpolation_search(4, arr)
if(location != 1):
    print("Element found at location: ", (location + 1))
else:
    print("Element was not found")
