import time

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        print("Arr : {0} // L : {1} // R : {2} // mid : {3}".format(
            arr,
            L,
            R,
            mid))
        print("Merge sort L and R")

        mergeSort(L)
        mergeSort(R)
    
        i = j = k = 0
        print("i = j = k = 0")
        while i < len(L) and j < len(R):
            print("L : {0} // R : {1} // arr : {2} // i : {3} // j : {4} // k : {5}".format(
                L,
                R,
                arr,
                i,j, k))
            if L[i] < R[j]:
                print("L[i] < R[j] => {0} < {1}".format(L[i], R[j]))
                arr[k] = L[i]
                i += 1
                k += 1
                print("arr[k] = L[i] i += 1 k += 1. ARR NOW : {0}".format(arr))
            else:
                print("L[i] > R[j] => {0} > {1}".format(L[i], R[j]))
                arr[k] = R[j]
                j += 1
                k += 1
                print("arr[k] = R[j] j += 1 k += 1. ARR NOW : {0}".format(arr))

        print("*************** LEFT OVERS ***************")
        print("i : {0} // j : {1} // k : {2}".format(
            i, j, k)
        )
        while i < len(L):
            print("arr[k] = L[i] . i += 1 // k += 1. arr[{0}] = L[{1}] == > arr[{0}] = {2}".format(k, i, L[i])) 
            arr[k] = L[i] 
            i+=1
            k+=1
            print("Array now : {0}".format(arr))
          
        while j < len(R):
            print("arr[k] = R[j] . j += 1 // k += 1. arr[{0}] = R[{1}] == > arr[{0}] = {2}".format(k, j, R[j])) 
            arr[k] = R[j] 
            j+=1
            k+=1
            print("Array now : {0}".format(arr))
        

        for i in range(10):
            print()
            




start = time.perf_counter()
mergeSort(n)
print("Time needed : {0}".format(time.perf_counter() - start))
