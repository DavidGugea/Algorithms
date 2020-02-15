import time
from concurrent import futures

class sorting(object):
    def __init__(self):
        pass
    def bubbleSortAlgorithm_noThreading(self, arr):
        self.arr = arr
        
        # outer loop ( counter loop ) > # < inner loop ( comparasion loop ) #
        for i in range(0, len(self.arr)):
            swapped = False
            for j in range(0, len(self.arr)-1-i):
                if self.arr[j] > self.arr[j+1]:
                    # Swap elements
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    swapped = True
                    continue
    
            # If any of the elements has been swapped, stop the whole array 
            if not swapped:
                break
            else:
                continue

        return self.arr
    def bubbleSortAlgorithm_withThreading(self, arr):
        self.arr = arr
        # Initialize the threading executor 
        self.bubbleSortAlgorithm_threadExecutor = futures.ThreadPoolExecutor(max_workers = len(self.arr)**2) 

        for i in range(0, len(self.arr)): 
            # Submit thread to the threadExecutor
            self.thread = self.bubbleSortAlgorithm_threadExecutor.submit(self.bubbleSortAlgorithm_threadingChunk, self.arr, i)
            self.arr = self.thread.result()[0]
            if not self.thread.result()[1]:
                continue
            else:
                continue
    
        return self.arr 
    def bubbleSortAlgorithm_threadingChunk(self, arr, i):
        swapped = False
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                continue

        # Return values in an array
        return [arr, swapped]
    def insertionSortAlgorithm_noThreading(self, arr):
        self.arr = arr

        for i in range(1, len(self.arr)):
            self.key = self.arr[i]
            j = i-1

            while j >= 0 and self.key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                # Decrement iteration value
                j -= 1
            
            arr[j+1] = self.key

        return self.arr
    def insertionSortAlgorithm_withThreading(self, arr):
        self.arr = arr
        # Initialize the threading executor
        self.insertionSortAlgorithm_threadExecutor = futures.ThreadPoolExecutor(max_workers=len(self.arr)**2)

        for i in range(1, len(self.arr)):
            self.key = self.arr[i]
            j = i - 1

            # Add function to the executor  
            self.insertionThread = self.insertionSortAlgorithm_threadExecutor.submit(self.insertionSortAlgorithm_threadingChunk, self.arr, self.key, j)
            arr = self.insertionThread.result() # assign the array value to the insertion thread result that returns an array

        return self.arr
    def insertionSortAlgorithm_threadingChunk(self, arr, key, j):
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key
        
        return arr
    def quickSortAlgorithm(self, arr):
        self.arr = arr

        def partition(arr, low, high):
            i = low
            pivot = arr[low]

            for j in range(low, high+1):
                if arr[j] < pivot:
                    # Increment i
                    i += 1
                    # Swap [i] and [j] index values
                    arr[i], arr[j] = arr[j], arr[i]

            # Swap the pivot with the [i] index value
            arr[i], arr[low] = arr[low], arr[i]

            # Return the partition split index value
            return i
        def quickSort(arr, low, high):
            try:
                if low < high:
                    partitionSplitIndexValue = partition(arr, low, high)

                    quickSort(arr, low, partitionSplitIndexValue-1)
                    quickSort(arr, partitionSplitIndexValue+1, high)
                    
                return arr
            except RecursionError as _rec_:
                print("Recursion error.")


        return quickSort(self.arr, 0, len(self.arr)-1)
    def compare(self, arr):
        # Initialize array
        self.arr = arr

        # BUBBLING ARRAYS 
        self.bubblingArray_noThreading = self.arr.copy()
        self.bubblingArray_withThreading = self.arr.copy()
        
        # INSERTION ARRAYS
        self.insertionArray_noThreading = self.arr.copy()
        self.insertionArray_withThreading = self.arr.copy()

        # QUICK SORT ARRAY ( | The quick sort algorithm cannot use threading because it already uses recursion | )
        self.quickSort_Array = self.arr.copy()
        
        for i in range(5):
            print() 

        print("Array before bubble sort with no threading : {0}".format(self.bubblingArray_noThreading))
        self.start = time.perf_counter()
        self.bubbleSortAlgorithm_noThreading(self.bubblingArray_noThreading)
        self.bubbleSortTime_noThreading = time.perf_counter() - self.start
        print("Array after bubble sort with no threading : {0}".format(self.bubblingArray_noThreading))
         
        for i in range(5):
            print() 

        print("Array before bubble sort with threading : {0}".format(self.bubblingArray_withThreading))
        self.start = time.perf_counter()
        self.bubbleSortAlgorithm_withThreading(self.bubblingArray_withThreading)
        self.bubbleSortTime_withThreading = time.perf_counter() - self.start
        print("Array after bubble sort with threading : {0}".format(self.bubblingArray_withThreading))

        for i in range(5):
            print() 

        print("Array before insertion sort with no threading : {0}".format(self.insertionArray_noThreading))
        self.start = time.perf_counter()
        self.insertionSortAlgorithm_noThreading(self.insertionArray_noThreading)
        self.insertionSortTime_noThreading = time.perf_counter() - self.start
        print("Array after insertion sort with threading : {0}".format(self.insertionArray_noThreading))

        for i in range(5):
            print() 

        print("Array before insertion sort with threading : {0}".format(self.insertionArray_withThreading))
        self.start = time.perf_counter()
        self.insertionSortAlgorithm_withThreading(self.insertionArray_withThreading)
        self.insertionSortTime_withThreading = time.perf_counter() - self.start
        print("Array after insertion sort with threading : {0}".format(self.insertionArray_withThreading))

        for i in range(5):
            print() 

        print("Array before quick sort :  {0}".format(self.quickSort_Array))
        self.start = time.perf_counter()
        self.quickSortAlgorithm(self.quickSort_Array)
        self.quickSortTime = time.perf_counter() - self.start
        print("Array after quick sort : {0}".format(self.quickSort_Array))

        for i in range(5):
            print() 

        print("Bubbling sort with no threading : {0}".format(self.bubbleSortTime_noThreading))
        print("Bubbling sort with threading    : {0}".format(self.bubbleSortTime_withThreading))
        print()
        print("Insertion sort with no threading : {0}".format(self.insertionSortTime_noThreading))
        print("Insertion sort with threading    : {0}".format(self.insertionSortTime_withThreading))
        print()
        print("Quick sort : {0}".format(self.quickSortTime))


RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1))[::-1]  # reverse array from 1 to the RANGE_STOP variable

# Create object
sortingObject = sorting()

print("ARRAY BEFORE SORTING : {0}".format(n))
start = time.perf_counter()
sortingObject.bubbleSortAlgorithm_noThreading(n)
print("ARRAY AFTER SORTING : {0}".format(n))
print("Time needed : {0}".format(time.perf_counter() - start))

for i in range(50):
    print() 

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1))[::-1]

sortingObject.compare(n)
