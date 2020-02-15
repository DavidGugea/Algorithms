def partition(arr, low, high):
    i = low
    pivot = arr[low]

    for j in range(low, high+1):
        if arr[j] < pivot:
            # Increment i
            i += 1
            # Swap [i] with [j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot with the i index
    arr[i], arr[low] = arr[low], arr[i]

    # Return partition split index
    return i

def quickSort(arr, low, high):
    if low < high:
        partitionSplitIndex = partition(arr, low, high)

        quickSort(arr, low, partitionSplitIndex-1)
        quickSort(arr, partitionSplitIndex+1, high)

n0 = [10, 7, 8, 9, 1, 5]
n = list(range(1, 51))[::-1]

print("Array before sort : {0}".format(n))
quickSort(n, 0, len(n)-1)
print("Array after sort : {0}".format(n))

"""
x = partition(n, 0, len(n)-1)
print("Partition split index : {0}".format(x))
"""
