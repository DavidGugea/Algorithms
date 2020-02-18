import time
from concurrent import futures

class compareObject(object):
    def __init__(self):
        pass
    def bubbleSort_noThreading(self, arr):
        self.arr = arr

        for i in range(0, len(self.arr)+1, 1):
            swapped = False
            for j in range(0, len(self.arr)-i-1, 1):
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
        self.threadingExecutor = futures.ThreadPoolExecutor(max_workers = len(self.arr)**2)

        for i in range(0, len(self.arr)+2, 1):
            # Submit the method to the threading Executor
            self.thread = self.threadingExecutor.submit(self.bubbleSort_threadingChunk, i, self.arr)
            self.arr = self.thread.result()[0]

            if not self.thread.result()[1]:
                break
            else:
                continue 

        return self.arr
    def bubbleSort_threadingChunk(self, i, arr):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True 

        return [arr, swapped]
    def recursiveBubbleSort(self, arr):
        self.arr = arr

        def bubble(arr):
            for i, num in enumerate(arr):
                try:
                    if num > arr[i+1]:
                        arr[i] = arr[i+1]
                        arr[i+1] = num
                        bubble(arr)
                except IndexError:
                    pass

        bubble(self.arr)
        return self.arr
    def insertionSort_noThreading(self, arr):
        self.arr = arr

        for i in range(0, len(self.arr), 1):
            self.key = self.arr[i]
            self.j = i-1
            
            while self.j >= 0 and self.key < self.arr[self.j]:
                self.arr[self.j+1] = self.arr[self.j]
                self.j -= 1

            self.arr[self.j + 1] = self.key

        return self.arr 
    def insertionSort_withThreading(self, arr):
        self.arr = arr
        self.threadingExecutor = futures.ThreadPoolExecutor(max_workers = len(self.arr)**2) 

        for i in range(0, len(self.arr) , 1):
            self.thread = self.threadingExecutor.submit(self.insertionSort_threadingChunk, self.arr, i)
            self.arr = self.thread.result()

        return self.arr
    def insertionSort_threadingChunk(self, arr, i):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1 

        arr[j+1] = key 

        return arr
    def recursiveInsertionSort(self, arr):
        self.arr = arr

        def recursiveFunction(arr, n):
            if n <= 1:
                return

            recursiveFunction(arr, n-1)

            last = arr[n-1]
            j = n-2

            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = last

        recursiveFunction(self.arr, len(self.arr))
    def quickSort(self, arr):
        self.arr = arr
    
        def partition(arr, low, high):
            i = low
            pivot = arr[high]
            
            for j in range(low, high, 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1 

            arr[i], arr[high] = arr[high], arr[i]
            return i
        def quickSort_ALG(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quickSort_ALG(arr, pi+1, high)
                quickSort_ALG(arr, low, pi-1)

        quickSort_ALG(self.arr, 0, len(self.arr)-1)
        
        return self.arr 
    def mergeSort(self, arr):
        self.arr = arr

        def mergeSort_ALG(arr):
            if len(arr) > 1:
                middle = len(arr) // 2

                L = arr[:middle]
                R = arr[middle:]

                mergeSort_ALG(L)
                mergeSort_ALG(R)

                i = j = k = 0
                
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                        k += 1
                    else:
                        arr[k] = R[j] 
                        j += 1
                        k += 1
                
                # Leftovers 
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1 
            
        mergeSort_ALG(self.arr)
        return self.arr


compare = compareObject()

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]

compare.mergeSort(n)
print(n)
