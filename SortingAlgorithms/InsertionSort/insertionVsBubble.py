import time

# FOR RANGE_STOP 10001 -- > BUBBLE ALGORITHM IS FASTER THAN INSERTION ALGORITHM < --

RANGE_STOP = 10001
nB = list(range(1, RANGE_STOP+1))[::-1]
nI = list(range(1, RANGE_STOP+1))[::-1]

# Bubble sort algorithm
def bubbleSort(n):
    for i in range(0, len(n), 1):
        for j in range(0, len(n)-i-1, 1):
            if n[j] > n[j+1]:
                # Swap elements
                n[j], n[j+1] = n[j+1], n[j]

    return n

# Insertion sort algorithm
def insertionSort(n):
    for i in range(1, len(n), 1):
        if n[i] < n[i-1]:
            for j in range(i, 0, -1):
                swapped = False
                if n[j] < n[j-1]:
                    n[j], n[j-1] = n[j-1], n[j]
                    swapped = True 
                
                if not swapped:
                    break

    return n


print("ARRAY BEFORE : {0}".format(nB))

for i in range(3):
    print()

print("-----------------------------")
print("BUBBLE SORT : ")
startBubbleSort = time.perf_counter()
print("Array sorted with bubble sort : {0}".format(bubbleSort(nB)))
print("Time needed for bubble sort : {0}".format(time.perf_counter()-startBubbleSort))
print("-----------------------------")

for i in range(3):
    print()


print("-----------------------------")

print("INSERTION SORT : ")
startInsertionSort = time.perf_counter()
print("Array sorted with insertionSort sort : {0}".format(insertionSort(nI)))
print("Time needed for insertion sort : {0}".format(time.perf_counter()-startInsertionSort))

print("-----------------------------")

for i in range(3):
    print()
