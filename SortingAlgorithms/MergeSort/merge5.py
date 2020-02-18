import time

"""
<!DOCTYPE html>
<html lang="de">
    <head>
         <meta charset="UTF-8">
         <title>Wab developer</title>
    </head>
    <body>
        <h1>Yes</h1>
    </body>
</html>

"""

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        L = arr[:middle]
        R = arr[middle:]

        print("arr : {0} // L : {1} // R : {2} // middle : {3}".format(arr, L, R, middle))

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            # i for L
            # j for R
            # k for arr
            # EXAMPLE : L = [4, 5] r = [1, 2, 3]
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

while True:
    try:
        RANGE_STOP = eval(input("RANGE STOP > "))
        if RANGE_STOP <= 0:
            raise Exception
        break
    except Exception as _error_:
        continue

array = list(range(1, RANGE_STOP + 1, 1))[::-1] # Reverse list after initiating it
start = time.perf_counter()
mergeSort(array)
print("Array now : {0}".format(array))
print("Time needed : {0}".format(time.perf_counter() - start))
