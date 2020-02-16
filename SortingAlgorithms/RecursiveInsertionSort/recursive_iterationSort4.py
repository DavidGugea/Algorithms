import time

RANGE_STOP = eval(input("RANGE STOP > "))

def recursive_iterationSort(arr, n):
    if n <= 1:
        return

    recursive_iterationSort(arr, n-1)

    last = arr[len(arr)-1]
    j = len(arr)-2

    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last

n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("Array before : {0}".format(n))

start = time.perf_counter()
recursive_iterationSort(n, len(n))

for i in range(3):
    print()

print("Array after : {0}".format(n))
print("Time needed : {0}".format(time.perf_counter() - start))
