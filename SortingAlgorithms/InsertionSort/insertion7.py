import time

n = list(range(1, 11))[::-1]

def insertionSort(n):
    for i in range(1, len(n), 1):
        key = n[i]
        j = i-1

        while j >= 0 and key < n[j]:
            print("Array : {0} // j : {1}".format(n, j)) 
            n[j+1] = n[j]
            j -= 1

        n[j+1] = key
        
    
    return n

print("LIST BEFORE INSERTION SORT : {0}".format(n))
startTimer = time.perf_counter()
print("LIST AFTER INSERTIONS SORT : {0}".format(insertionSort(n)))
print("Time needed : {0}".format(time.perf_counter() - startTimer))
