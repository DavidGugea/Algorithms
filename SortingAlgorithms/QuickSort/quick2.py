import time

n = [10, 80, 30, 90, 40, 50, 70]
l0 = list(range(1, 10001))[::-1]

# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr, low, high):
    i = low - 1    # index of smaller element
    pivot = arr[low] # pivot

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # incremet index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # swap

    for x in range(2):
        print()

    """  
    print("low : {0} // high : {1}".format(low, high))
    print("i : {0} // high : {1} // arr : {2}".format(
        i,
        high,
        arr))
    """
    
    for x in range(2):
        print()
    
    # arr[i+1], arr[high] = arr[high], arr[i+1]
    arr[i+1], arr[low] = arr[low], arr[i+1]
    return ( i )


# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index
# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[i] is now at the
        # right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition
        # and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    else:
        print("LOW IS NOT LOWER THAN HIGH. LOW : {0} // HIGH : {1}".format(low, high))
    return arr

print("ARRAY BEFORE QUICK SORT : {0}".format(n))
for i in range(10):
    print()
print(quickSort(n, 0, len(n)-1))
        
