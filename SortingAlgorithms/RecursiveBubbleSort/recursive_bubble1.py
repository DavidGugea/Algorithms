import time
RANGE_STOP = eval(input("RANGE STOP > "))

def bubble_sort(arr): 
    for i, num in enumerate(arr):
        try:
            # 5 3 7 # == > i = 0 ( num = 5 )
            if arr[i+1] < num:
                # if 3 < 5
                arr[i] = arr[i+1] # 5 5
                arr[i+1] = num # 3 5
                bubble_sort(arr)
        except IndexError:
            pass

    return arr

n = list(range(1, RANGE_STOP+1))[::-1]
print("ARRAY BEFORE SORT : {0}".format(n))
start = time.perf_counter()
print("ARRAY AFTER SORT  : {0}".format(bubble_sort(n)))
print("Time needed : {0}".format(time.perf_counter() - start))
