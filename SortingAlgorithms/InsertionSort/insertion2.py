import time

n = list(range(1, 11))[::-1]

def insertionSort(n):
    for i in range(1, len(n), 1):
        if n[i] < n[i-1]:
            for j in range(i, 0, -1):
                if n[j] < n[j-1]:
                    n[j], n[j-1] = n[j-1], n[j]
    return n
    
start = time.perf_counter()
print("LIST BEFORE : {0}".format(n))
print("LIST AFTER : {0}".format(insertionSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter()-start))

input("Press any key to close the programm.")
