import time 

def partition(arr, low, high):
    i = low
    pivot = arr[low]

    for j in range(low, high+1):
        if arr[j] < pivot:
            # Increment i
            i += 1
            # Swap i and j index values
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot with the i index value
    arr[i], arr[low] = arr[low], arr[i]

    # Return partition split index
    return i
def quickSort(arr, low, high):
    if low < high:
        partitionSplitIndex = partition(arr, low, high)

        quickSort(arr, low, partitionSplitIndex-1)
        quickSort(arr, partitionSplitIndex+1, high)

    return arr

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("ARRAY BEFORE SORT : {0}".format(n))
start = time.perf_counter()
try:
    quickSort(n, 0, len(n)-1)
except RecursionError as _rec_:
    pass
print("ARRAY AFTER SORT : {0}".format(n))

for i in range(5):
    print()

print("Time needed : {0}".format(time.perf_counter() - start))
