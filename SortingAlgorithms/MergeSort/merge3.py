def mergeSort(arr):
    if len(arr) > 1:
        for i in range(3):
            print()
            
        mid = len(arr) // 2 # split

        L = arr[:mid]
        R = arr[mid:]

        print("L : {0}".format(L))
        print("R : {0}".format(R))
        print("arr : {0}".format(arr))

        print("MERGE SORT L. // R: {0} | L :{1} // arr  : {2}".format(R, L, arr))
        print("MERGE SORT R. // R: {0} | L :{1} // arr  : {2}".format(R, L, arr))
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0 

        # L = [5, 4]
        # R = [3, 2, 1]
        # arr = [5, 4, 3, 2, 1]

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i] # Replace values
                i += 1 # Increment index for the L left side array
                k += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1


        # *< Left over values >* #
                
        
        for i in range(3):
            print()

while True:
    try:
        RANGE_STOP = eval(input("RANGE STOP > "))
        n = list(range(1, RANGE_STOP+1, 1))[::-1]


        mergeSort(n)
        break
    except Exception as _error_:
        pass

for i in range(10):
    print()


print("Array after merge sort : {0}".format(n))
