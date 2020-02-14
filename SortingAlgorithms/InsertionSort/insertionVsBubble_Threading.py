import time, math
from concurrent import futures

RANGE_STOP = eval(input("Range : "))
nB = list(range(1, RANGE_STOP+1, 1))[::-1]
nI = list(range(1, RANGE_STOP+1, 1))[::-1]

class bubble(object):
    def __init__(self, n):
        # Create the thread executor and make the list global with self in the class 
        self.n = n
        self.threadExecutor = futures.ThreadPoolExecutor(max_workers=len(self.n)**2)
        self.startTime = time.perf_counter()
    def bubbleSort(self):
        for i in range(3):
            print()
            
        print("---------------------------------")
        print("BUBBLE SORT : ")
        print("ARRAY BEFORE BUBBLE SORT : {0}".format(self.n))
        
        for i in range(0, len(self.n), 1):
            try:
                # Submit the function to the thread executor
                thread = self.threadExecutor.submit(self.bubbleSortThread, self.n, i)
                # The thread returns a list so we will equal that modifed | n | array with out | n | array
                self.n = thread.result()
            except RuntimeError as _runtime_:
                self.n = self.bubbleSortThread(self.n, i)

        print("ARRAY AFTER SORT : {0}".format(self.n))
        print("Time needed : {0}".format(time.perf_counter()-self.startTime))
        print("---------------------------------")

        for i in range(3):
            print()
    def bubbleSortThread(self, n, i):
        for j in range(0, len(n)-1-i, 1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]

        return n
class insertion(object):
    def __init__(self, n):
        self.n = n
        self.threadExecutor = futures.ThreadPoolExecutor(len(self.n)**2)
        self.startTime = time.perf_counter()
    def insertionSort(self):
        for i in range(3):
            print()

        print("------------------------------------------")
        print("Insertion sort: ")
        print("ARRAY BEFORE INSERTION SORT : {0}".format(self.n))
        
        for i in range(1, len(self.n), 1):
            if self.n[i] < self.n[i-1]:
                try:
                    # Submit the function to the thread executor
                    thread = self.threadExecutor.submit(self.insertionSortThread, self.n, i)
                    # The thread returns a list so we will equal that modifed | n | array with out | n | array
                    self.n = thread.result()
                except RuntimeError as _runtime_:
                    self.n = self.insertionSortThread(self.n, i)

        print("Array AFTER INSERTION SORT : {0}".format(self.n))
        print("Time needed : {0}".format(time.perf_counter() - self.startTime))

        print("------------------------------------------")
        for i in range(3):
            print()
    def insertionSortThread(self, n, i):
        for j in range(i, 0, -1):
            if n[j] < n[j-1]:
                n[j], n[j-1] = n[j-1], n[j]

        return n

bubbleObject = bubble(nB)
bubbleObject.bubbleSort()
for i in range(5):
    print()
insertionObject = insertion(nI)
insertionObject.insertionSort()