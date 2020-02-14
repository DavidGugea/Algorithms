import time
from concurrent import futures

class normalInsertionSort(object):
    def __init__(self, n):
        self.n = n
        self.startTime = time.perf_counter()
        self.threadExecutor = futures.ThreadPoolExecutor(max_workers = len(self.n) ** 2)
    def insertionSort(self):
        for i in range(3):
            print()
        print("-"*25)
        print("Normal insertion sort.")
        print("ARRAY BEFORE SORT : {0}".format(self.n))
        for i in range(1, len(self.n)):
            if self.n[i] < self.n[i-1]:
                try:
                    # Submit the function to the thread executor
                    thread = self.threadExecutor.submit(self.insertionSort_threadChunk, self.n, i)
                    # The thread returns a new modified |n| array that will replace self.n 
                    self.n = thread.result()
                except RuntimeError as _runtime_:
                    self.n = self.insertionSort_threadChunk(self.n, i)

        print("ARRAY AFTER SORT : {0}".format(self.n))
        print("Time needed : {0}".format(time.perf_counter() - self.startTime))
        print("-"*25)
        for i in range(3):
            print()
    def insertionSort_threadChunk(self, n, i):
        for j in range(i, 0, -1):
            if n[j] < n[j-1]:
                # Swap elements
                n[j], n[j-1] = n[j-1], n[j]
            else:
                break

        return n
class newInsertionSort(object):
    def __init__(self, n):
        self.n = n
        self.startTime = time.perf_counter()
        self.threadExecutor = futures.ThreadPoolExecutor(max_workers=len(self.n)**2)
    def insertionSort(self):
        for i in range(3):
            print()
        print("-"*25)
        print("New insertion sort")
        print("ARRAY BEFORE SORT : {0}".format(self.n))
        
        for i in range(1, len(self.n)):
            self.key = self.n[i]
            j = i-1
            try:
                # Submit the function to the thread executor
                thread = self.threadExecutor.submit(self.insertionSort_threadChunk, self.n, i, j, self.key)
                # The thread returns a new modified |n| array that will replace self.n 
                self.n = thread.result()
            except RuntimeError as _runtime_:
                self.n = insertionSort_threadChunk(self.n, i, j, self.key)
                

        print("ARRAY AFTER SORT : {0}".format(self.n))
        print("Time needed : {0}".format(time.perf_counter() - self.startTime))
        print("-"*25)
        for i in range(3):
            print()
    def insertionSort_threadChunk(self, n, i, j, key):
        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -= 1

        n[j+1] = key

        return n

while True:
    RANGE_STOP = eval(input("RANGE : "))+1

    n1 = list(range(0, RANGE_STOP, 1))[::-1]
    n2 = list(range(0, RANGE_STOP, 1))[::-1]
    _insertion_class_ = normalInsertionSort(n1)
    _insertion_class_.insertionSort()
    for i in range(10):
        print()
    _insertion_class_ = newInsertionSort(n2)
    _insertion_class_.insertionSort()
