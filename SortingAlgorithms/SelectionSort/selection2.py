def selectionSort(arr):
    tracker = 0
    len_ = len(arr)+1
    returnArray = list()

    while tracker <= len_:
        min_ = min(arr)
        returnArray.append(min_)
        
        del arr[arr.index(min_)]
        
        tracker += 1
        len_ -= 1 
    returnArray.append(arr[0])
    
    return returnArray 

n = list(range(1, 6))[::-1]
print(selectionSort(n))
