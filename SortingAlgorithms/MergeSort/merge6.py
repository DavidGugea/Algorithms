import time

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        L = arr[:middle]
        R = arr[middle:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            # i = > L
            # j = > R
            # k = > arr
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                k += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


RANGE_STOP = eval(input("RANGE STOP > "))
arr = list(range(1, RANGE_STOP+1, 1))[::-1] # Reverse array after initiating it
print("Array before merge sort : {0}".format(arr))
mergeSort(arr)
print("Array after merge sort : {0}".format(arr))
