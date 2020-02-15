# This function takes last element as pivot, places 
# the pivot element at its correct position in sorted 
# array, and places all smaller (smaller than pivot) 
# to left of pivot and all greater elements to right 
# of pivot 
def partition(arr,low,high): 
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
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)


arr0 = [10, 7, 8, 9, 1, 5]
arr1 = [10, 7, 8, 9, 1, 5]

for i in range(2):
    print()

print(arr0)
x = partition(arr0, 0, len(arr0)-1)
print(x)
print("Array after : {0}".format(arr0))


for i in range(2):
    print()

def partition2(arr, low, high):
    i = low
    pivot = arr[low]

    for j in range(low, high+1):
        if arr[j] < pivot:
            # Increment i
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot with the i value
    temp = arr.index(pivot)
    arr[temp], arr[i] = arr[i], arr[temp]

    # Return i
    return i

print("Array before : {0}".format(arr1))
x = partition2(arr1, 0, len(arr1)-1)
print(x)
print("Array after : {0}".format(arr1))

for i in range(2):
    print()
