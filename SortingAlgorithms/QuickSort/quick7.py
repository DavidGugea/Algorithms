class partitions(object):
    def __init__(self):
        pass
    def partition_type_1(self, arr, low, high):
        print("Array before : {0}".format(arr))
        i = low - 1
        pivot = arr[high]
        
        for j in range(low, high):
            if arr[j] < pivot:
                # Increment  | i |
                i += 1
                # Swap i with j
                arr[i], arr[j] = arr[j], arr[i]

        # Swap pivot with i value
        arr[i+1], arr[high] = arr[high], arr[i+1]

        print("Partition index merge : {0}".format(i+1))
        print("Array after : {0}".format(arr))

        return (i + 1)
    def partition_type_2(self, arr, low, high):
        print("Array before : {0}".format(arr))
        i = low
        pivot = arr[low]

        for j in range(low, high+1):
            if arr[j] < pivot:
                # Increment i value
                i += 1
                # Swap i with j
                arr[i], arr[j] = arr[j], arr[i]
        
        # Swap the pivot value with the | i | value
        arr[i], arr[low] = arr[low], arr[i]
        print("Partition index merge : {0}".format(i))
        print("Array after : {0}".format(arr))

        return i
    def quickSort(self, arr, low, high):
        if low < high:
            partition = self.partition_type_2(arr, low, high)

            self.quickSort(arr, low, partition-1)
            self.quickSort(arr, partition+1, high)
    
        return arr

partitionsObject = partitions()

n0 = [10, 7, 8, 9, 1, 5]
n1 = [10, 7, 8, 9, 1, 5]
n2 = [10, 7, 8, 9, 1, 5]

partitionsObject.partition_type_1(n0, 0, len(n0)-1)

for i in range(3):
    print()

partitionsObject.partition_type_2(n1, 0, len(n1)-1)

for i in range(5):
    print()

print("Array before sort : {0}".format(n2))
partitionsObject.quickSort(n2, 0, len(n2)-1)
print("Array after sort : {0}".format(n2))
