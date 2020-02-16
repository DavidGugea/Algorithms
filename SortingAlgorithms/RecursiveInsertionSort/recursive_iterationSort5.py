import time

RANGE_STOP = eval(input("RANGE STOP > "))

def recursive_insertionSort(arr, l):
    if l <= 1:
        return

    recursive_insertionSort(arr, l-1)

    last = arr[l-1]
    j = l-2

    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last

n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("Array before sort : {0}".format(n))
recursive_insertionSort(n, len(n))
print("Array after sort : {0}".format(n))
