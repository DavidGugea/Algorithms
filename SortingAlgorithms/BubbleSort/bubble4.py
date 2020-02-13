import time
from concurrent import futures

n = list(range(1, 10000))[::-1]


def thread(n, i):
    for j in range(0, len(n)-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
        
    return n
def bubbleSort(n):
    executor = futures.ThreadPoolExecutor(max_workers=pow(len(n), 2))  

    for i in range(0, len(n)):
        executor_thread = executor.submit(thread, n, i)
        n = executor_thread.result()

    return n

start = time.perf_counter()
print("LIST BEFORE : {0}".format(n))
print("LIST AFTER : {0}".format(bubbleSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter() - start))
