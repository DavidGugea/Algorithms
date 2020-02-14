import time
from concurrent import futures

n = list(range(1, 5000))[::-1]

def insertionSort(n):
    # Initialize thread pool executor
    threadExecutor = futures.ThreadPoolExecutor(max_workers = len(n) ** 2)

    # Create a function for the insertion sort to submit to the threadExecutor. We will use this function when n[i] < n[i-1]
    def insertionSort_BubbleBackwards(n, i):
        for j in range(i, 0, -1):
            if n[j] < n[j-1]:
                # Swap elements
                n[j], n[j-1] = n[j-1], n[j]
            else:
                break

        # Return the modified array
        return n
    
    for i in range(1, len(n), 1):
        swapped = False
        if n[i] < n[i-1]:
            # Submit function to the executor
            swapped = True
            try:
                thread = threadExecutor.submit(insertionSort_BubbleBackwards, n, i)
                n = thread.result() # the thread returns a new modified (n) array
            except RuntimeError:
                n = insertionSort_BubbleBackwards(n, i)
        if not swapped:
            break

    return n


start = time.perf_counter()
print("ARRAY BEFORE : {0}".format(n))
print("ARRAY AFTER  : {0}".format(insertionSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter()-start))
