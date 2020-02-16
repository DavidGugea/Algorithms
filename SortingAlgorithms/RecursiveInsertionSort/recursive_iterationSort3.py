RANGE_STOP = eval(input("RANGE STOP > "))
n = list(range(1, RANGE_STOP+1, 1))[::-1] # Create and then reverse the array, so it's completly unsorted

def recursive_iterationSort(arr, length):
    if length <= 1:
        return 

    recursive_iterationSort(arr, length-1)
    
    last = arr[length-1]
    j = length-2
    
    print("j : {0} // length : {1}".format(j, length))
    print("last = arr[length-1] = {0} // j = length ( {1} ) - 2 = {2}".format(
        last,
        length,
        j
    ))

    print()

    print("while j >= 0 and arr[j] > last:\narr[j+1] = arr[j]\n j-=1")

    print()
    while j >= 0 and arr[j] > last:
        print("arr[j] : {0} // arr[j+1] : {1} // arr : {2}".format(
            arr[j],
            arr[j+1],
            arr))
        arr[j+1] = arr[j]
        j -= 1
        print("arr[j] : {0} // arr[j+1] : {1} // arr : {2}".format(
            arr[j],
            arr[j+1],
            arr))
    
    print("j : {0}".format(j))
    print("arr[j+1] = {0} = last ( {1} )".format(
        arr[j+1],
        last
    ))
    arr[j+1] = last
    print("arr[j+1] = last. Array : {0}".format(arr))

    for i in range(3):
        print()

print("Array before : {0}".format(n))

for i in range(3):
    print()

recursive_iterationSort(n, len(n))

for i in range(3):
    print() 

print("Array after : {0}".format(n))
