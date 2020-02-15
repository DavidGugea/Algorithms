import time

n0 = list(range(1, 11))[::-1]
n1 = [10, 7, 8, 9, 1, 5]
n2 = [4, 5, 3, 1, 2, 7, 6]
n3 = [3, 5, 4, 1, 2]


def partition(arr, low, high):
    i = low
    print(low, arr)
    pivot = arr[low]

    # 0 10
    for j in range(i, high+1):
        if arr[j] < pivot:

            # increment i
            i += 1
            # Swap elements arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

            continue
        else:
            continue

    # Swap the pivot with the index | i |
    arr[i], arr[low] = arr[low], arr[i]

    return i

start = time.perf_counter()
"""
print("Before : {0}".format(n2))
for i in range(2):
    print()

a0 = partition(n2, 0, len(n2)-1)
print("a0 : {0}".format(a0))
print("array : {0}".format(n2))

a1 = partition(n2, a0+1, len(n2)-1)
print("a1 : {0}".format(a1))
print("array : {0}".format(n2))

a2 = partition(n2, a1+1, len(n2)-1)
print("a2 : {0}".format(a2))
print("array : {0}".format(n2))

a3 = partition(n2, 0, a0-1)
print("a3 : {0}".format(a3))
print("array : {0}".format(n2))

for i in range(2):
    print()

print("After : {0}".format(n2))
print()
print("Time needed : {0}".format(time.perf_counter() - start))
""" 

def quickSort(n, low, high):
    try:
        while low < high or low == high + 1:
            partitionIndex = partition(n, low, high)

            if low != high + 1:
                quickSort(n, partitionIndex, high)
                quickSort(n, low, partitionIndex)
            else:
                try:
                    quickSort(n, low, partitionIndex)
                except Exception:
                    try:
                        quickSort(n, low, partitionIndex)
                    except Exception:
                        pass

                break

            print("low : {0} , high: {1}".format(low, high))
            time.sleep(0.5)
    except Exception as _error_:
        print("Error : {0}".format(_error_))
        print("high : {0}".format(high))
        print("low : {0}".format(low))
        print("n : {0}".format(n))
        time.sleep(1000000000000000000000)

quickSort(n2, 0, len(n2)-1)


"""
for i in range(2):
    print()

for i in range(2):
    print()

a0 = partition(n2,  0, len(n2)-1)
print("Index from the function : {0}".format(a0))
print(n2)
"""
