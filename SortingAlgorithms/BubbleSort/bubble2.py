import time
n = list(range(1, 6))[::-1]

def bubbleSort(n):
    for i in range(0, len(n)):
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

    return n


start = time.perf_counter()
print("LIST BEFORE : {0}".format(n))
print("LIST AFTER  : {0}".format(bubbleSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter() - start))
