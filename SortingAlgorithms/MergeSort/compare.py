import time
from concurrent import futures

class sortingAlgorithms(object):
    def __init__(self):
        pass
    def bubbleSort_noThreading(self, arr):
        self.arr = arr

        for i in range(0, len(self.arr)+1, 1):
            swapped = False
            for j in range(0, len(self.arr)-1-i, 1):
                if self.arr[j] > self.arr[j+1]:
                    # Swap elements
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True

            if not swapped:
                break 
            else:
                continue
        
        return self.arr
    def bubbleSort_withThreading(self, arr):
        self.arr = arr
        self.threadingExecutor = futures.ThreadPoolExecutor(max_workers=len(self.arr)**2) 

        for i in range(0, len(self.arr)+1, 1):
            self.thread = self.threadingExecutor.submit(self.bubbleSort_threadingChunk, self.arr, i)
            self.arr = self.thread.result()[0]
            if not self.thread.result()[1]:
                break
            else:
                continue

        return self.arr
    def bubbleSort_threadingChunk(self, arr, i):
        swapped = False
        for j in range(0, len(arr)-i-1, 1):
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        return [arr, swapped]
    def recursiveBubbleSort(self, arr):
        self.arr = arr;

        def bubble(array):
            for i, num in enumerate(array):
                try:
                    if array[i+1] < array[i]:
                        # Swap values
                        array[i] = array[i+1]
                        array[i+1] = num
                        # Recall bubble
                        bubble(array)
                except IndexError as _ix_:
                    pass

        return bubble(self.arr)
    def insertionSort_noThreading(self, arr):
        self.arr = arr

        for i in range(0, len(self.arr), 1):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    # Swap elements
                    self.arr[j], self.arr[j-1] = self.arr[j-1], self.arr[j]
        
        return self.arr
    def insertionSort_noThreading_secondType(self, arr):
        self.arr = arr

        for i in range(0, len(self.arr), 1):
            self.key = self.arr[i]
            self.j = i - 1

            while self.j >= 0 and self.arr[self.j] > self.key:
                self.arr[self.j + 1] = self.arr[self.j]
                self.j -= 1

            self.arr[self.j+1] = self.key

        return self.arr
    def insertionSort_withThreading(self, arr):
        self.arr = arr
        self.threadExecutor = futures.ThreadPoolExecutor(max_workers = len(self.arr)**2)

        for i in range(0, len(self.arr), 1):
            # Submit thread to the executor 
            self.thread = self.threadExecutor.submit(self.insertionSort_threadingChunk, i, self.arr)
            # Returns an array
            self.arr = self.thread.result()

        return self.arr
    def insertionSort_threadingChunk(self, i, arr):
        self.threadingArr = arr

        self.key = self.threadingArr[i]
        self.j = i - 1
        
        while self.j >= 0 and self.threadingArr[self.j] > self.key:
            self.threadingArr[self.j+1] = self.threadingArr[self.j]
            self.j -= 1

        self.threadingArr[self.j + 1] = self.key

        return self.threadingArr
    def recursiveInsertionSort(self, arr): 
        self.arr = arr

        # The "func" function will be used for the recursive insertion sort, so we avoid calling a self.* kind of method more times at once ( recursion ) 
        def func(arr, n):
            if n <= 1:
                return

            func(arr, n-1)

            last = arr[n-1]
            j = n-2

            while j >= 0 and arr[j] > last:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = last

        return func(self.arr, len(self.arr))
    def quickSort(self, arr):
        self.arr = arr

        def partition(arr, low, high):
            i = low
            pivot = arr[high]


            # 4 5 3 8 9 7
            for j in range(low, high, 1):
                if arr[j] < pivot:
                    # Swap elements
                    arr[i], arr[j] = arr[j], arr[i]
                    # Increment i
                    i += 1

            # Swap *i* index value with the pivot  
            arr[i], arr[high] = arr[high], arr[i]
            
            return i
        def quickSort_ALGORITHM(arr, low, high):
            if low < high:
                partitionIndexSplitter = partition(arr, low, high)

                quickSort_ALGORITHM(arr, low, partitionIndexSplitter-1)
                quickSort_ALGORITHM(arr, partitionIndexSplitter+1, high)

        return quickSort_ALGORITHM(self.arr, 0, len(self.arr)-1)
    def mergeSort(self, arr):
        self.arr = arr

        def mergeSort_ALGORITHM(array):
            if len(array) > 1:
                # Split it into halves 
                middle = len(array) //2
                L = array[:middle]
                R = array[middle:]

                mergeSort_ALGORITHM(L)
                mergeSort_ALGORITHM(R)

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        array[k] = L[i]
                        i += 1
                        k += 1 
                    else:
                        array[k] = R[j]
                        j += 1
                        k += 1 

                # Add left overs
                while i < len(L):
                    array[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    array[k] = R[j]
                    j += 1
                    k += 1
        
        mergeSort_ALGORITHM(self.arr)
        return self.arr

compareObject = sortingAlgorithms()

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1))[::-1]

start = time.perf_counter()
compareObject.mergeSort(n)

print(n)
print("Time needed : {0}".format(time.perf_counter() - start))
