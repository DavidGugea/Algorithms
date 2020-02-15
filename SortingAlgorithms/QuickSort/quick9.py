import time 

def partition(arr, low, high):
    i = low
    pivot = arr[low]

    for j in range(low, high+1):
        if arr[j] < pivot:
            # Increment i
            i += 1
            # Swap i and j
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the i index value with the pivot
    arr[i], arr[low] = arr[low], arr[i]

    # Return partition split index
    return i
def partition2(arr, low, high):
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 )

def quickSort(arr, low, high):
    try:
        if low < high:
            partitionSplitIndex = partition2(arr, low, high)

            quickSort(arr, low, partitionSplitIndex-1)
            quickSort(arr, partitionSplitIndex+1, high)
    except RecursionError as _rec_:
        print("RECURSION ERROR")

    return arr

RANGE_STOP = eval(input("RANGE > "))
n = list(range(1, RANGE_STOP+1))[::-1]

print("Array before sort : {0}".format(n))
start = time.perf_counter()
quickSort(n, 0, len(n)-1)
print("Time needed : {0}".format(time.perf_counter() - start))
print("Array after sort : {0}".format(n))
