# Python program for implementation of Insertion Sort 
  
n = list(range(1, 6))[::-1]

# Function to do insertion sort 
def insertionSortWebsite(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key        
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j + 1] = key

    return arr
def insertionSort2(n):
    for i in range(1, len(n)):
        j = i - 1
        while j >= 0 and n[i] < n[j]:
            n[j+1] = n[j] # swap elements
            j -= 1
        n[j + 1] = n[i]

    return n

print(insertionSort(n))
