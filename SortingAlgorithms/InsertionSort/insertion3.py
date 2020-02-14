import time
from concurrent import futures

n = list(range(1, 11))[::-1]


def insertionSort(n):
    threadExecutor = futures.ThreadPoolExecutor(max_workers = len(n) ** 2)
    
    # Run this function when iterating backwards from an item 
    def insertionSort_BubbleBackwards(n, i):
        for j in range(i, 0, -1):
            if n[j] < n[j-1]:
                n[j], n[j-1] = n[j-1], n[j]

        # Retun the array
        return n

    for i in range(1, len(n), 1):
        if n[i] < n[i-1]:
            # Submit function to the thread with the args : n ( the list ) and i ( the index where n[i] < n[i-1] )
            thread = threadExecutor.submit(insertionSort_BubbleBackwards, n, i)
            print("Thread : {0}".format(thread))
            print("Thread result : {0}".format(thread.result()))
        else:
            break

    return n

start = time.perf_counter()
print("LIST BEFORE : {0}".format(n))
print("LIST AFTER : {0}".format(insertionSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter()-start))

input("Press any key to close the programm ... ")
