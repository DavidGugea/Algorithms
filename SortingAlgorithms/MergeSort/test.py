def mergeSort(arr):
    if len(arr) > 1:
        # Split it into halves 
        middle = len(arr) //2
        L = arr[:middle]
        R = arr[middle:]

        mergeSort(L)
        mergeSort(R)
       
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

        # Add left overs
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


n = list(range(1, 6, 1))[::-1]
mergeSort(n)
print(n)
