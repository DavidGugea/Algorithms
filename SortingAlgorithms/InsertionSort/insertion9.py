import time

n = list(range(1, 6))[::-1]

def insertionSort(n):
    for i in range(1, len(n), 1):
        key = n[i]
        j = i - 1

        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -= 1

        n[j+1] = key
        print("ARRAY : {0}".format(n))

    return n

start = time.perf_counter()
print("ARRAY BEFORE SORT : {0}".format(n))
print("ARRAY AFTER SORT : {0}".format(insertionSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter() - start))
