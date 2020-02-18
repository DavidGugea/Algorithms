n = list(range(1, 6))[::-1]

def selectionSort(arr):
    tracker = 0
    len_ = len(arr)
    returnArray = list()

    while tracker <= len_+1:
        min_ = min(arr)
        
        returnArray.append(min_)

        del arr[arr.index(min_)]
       
        tracker += 1
        len_ -= 1 

        print("arr : {0} // min_ : {1}".format(arr, min_))
        print("tracker : {0} // len_ : {1}".format(tracker, len_))
        print("returnArray : {0}".format(returnArray))

    returnArray.append(arr[0])

    return returnArray

print(selectionSort(n))
