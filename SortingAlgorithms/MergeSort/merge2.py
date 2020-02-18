arr = list(range(1, 6))[::-1]

for i in range(3):
    print()

def mergeSort(arr):
    if len(arr) > 1:
        # Dividing the mid of the array 
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves 
        L = arr[:mid] 
        R = arr[mid:]
        
        print("mid = len(arr) // 2 //  len(arr) : {0} // len(arr)//2 : {1} // mid : {2}".format(
            len(arr),
            len(arr)//2,
            mid
        ))
        print("L = arr[:mid] = {0} ( len = {1} )".format(
            L,
            len(L)
        ))
        print("R = arr[mid:] = {0} ( len = {1} )".format(
            R,
            len(R)
        ))

        for i in range(2):
            print()
       
        mergeSort(L) # Sorting the first half of the array  
        mergeSort(R) # Sorting the last half of the array 


        i = j = k = 0


        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print(" i : {0} // j : {1} // k : {2}".format(i, j, k))
            print(" L : {0} // R : {1} // arr : {2}".format(
                L,
                R,
                arr
            ))
            if L[i] < R[j]:
                print("L[i] < R[j] || {0} < {1} || i = {2} // j = {3} // k = {4}".format(
                    L[i], R[j],
                    i, j, k
                ))

                arr[k] = L[i]
                i += 1
                print("Array now : {0}. i incremented by 1 : {1}".format(arr, i)) 
            else:
                print("L[i] > R[j] || {0} > {1} || i = {2} // j = {3} // k = {4}".format(
                    L[i], R[j],
                    i, j, k
                ))               
                arr[k] = R[j]
                j += 1
                print("Array now : {0}. j incremented by 1 : {1}".format(arr, j))
            k += 1
          

        
        # Checking if any element was left
        print("Checking for left elements. k : {0}".format(k))

        
        while i < len(L):
            print("i : {0} // k : {1} // arr : {2} // L :{3}".format(
                i,
                k,
                arr,
                L
            ))
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            print("j : {0} // k : {1} // arr : {2} // R :{3}".format(
                j,
                k,
                arr,
                R
            ))

            arr[k] = R[j]
            j += 1
            k += 1

        print("Array now : {0}. L : {1}, R : {2}".format(arr, L, R))

        
        for i in range(10):
            print()   

print("Array before merge sort : {0}".format(arr))
mergeSort(arr)
print("Array after merge sort : {0}".format(arr))
