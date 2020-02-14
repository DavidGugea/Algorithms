import time

n = list(range(1, 11))[::-1]

def insertionSort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i-1
        
        while j >= 0 and key < n[j]:
            # n = [4, 3, 2, 1]
            # [3, 2, 1, 1]
            n[j+1] = n[j]
            j-=1

        n[j+1] = key

    return n
def insertionSort2(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        """
            Key : 9 // i : 1 // j : 0
            Key : 8 // i : 2 // j : 1
            Key : 7 // i : 3 // j : 2
            Key : 6 // i : 4 // j : 3
            Key : 5 // i : 5 // j : 4
            Key : 4 // i : 6 // j : 5
            Key : 3 // i : 7 // j : 6
            Key : 2 // i : 8 // j : 7
            Key : 1 // i : 9 // j : 8

            [9, 8, 7, 6, 5, 4, 3, 2, 1]
        """

        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -= 1

        n[j+1] = key

    return n

    return None

print(insertionSort2(n))
