def insertionSortRecursive(arr,n): 
    # base case 
    if n<=1: 
        return
    # Sort first n-1 elements 
    insertionSortRecursive(arr,n-1) 
    '''Insert last element at its correct position 
        in sorted array.'''
       
   
    print("n : {0}".format(n))
    print("arr : {0}".format(arr))

    last = arr[n-1] 
    j = n-2
      
      # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position  
    while (j>=0 and arr[j]>last): 
        arr[j+1] = arr[j] 
        j = j-1
  
    arr[j+1]=last

   
n = list(range(1, 6, 1))[::-1] # [ 5, 4, 3, 2, 1]
insertionSortRecursive(n, len(n))
print(n)
