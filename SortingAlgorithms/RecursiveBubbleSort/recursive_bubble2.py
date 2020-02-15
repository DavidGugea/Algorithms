import time

def recursive_bubbleSort(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i+1] < num:
                # Swap elements
                arr[i] = arr[i+1]
                arr[i+1] = num
                recursive_bubbleSort(arr)
        except IndexError as _i_:
            pass 
    # Return array
    return arr

RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1]
print("ARRAY BEFORE SORT : {0}".format(n))
start = time.perf_counter()
print("ARRAY AFTER SORT : {0}".format(recursive_bubbleSort(n)))
for i in range(5):
    print() 
print("Time needed : {0}".format(time.perf_counter() - start))
