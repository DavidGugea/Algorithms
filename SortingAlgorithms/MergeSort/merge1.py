def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Dividing the mid of the array 
        L = arr[:mid] # Dividing the array elements 
        R = arr[mid:] # into 2 halves 

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1 # Increment index
            else:
                arr[k] = R[j]
                j += 1 # Increment index 
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

n = list(range(1, 6))[::-1] # Reverted list with all the elements from 1 to 6
print("Array before merge sort : {0}".format(n))
mergeSort(n)
print("Array after merge sort : {0}".format(n))
