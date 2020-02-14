import time 
n = list(range(1, 2000))[::-1]

"""
def insertionSort(n):
    for a0 in range(len(n)**2): 
        for i in range(1, len(n), 1):
            if n[i] < n[i-1]:
                for j in range(i, , -1):
                    if n[j] < n[j-1]:
                        # 3 4
                        n[j], n[j-1] = n[j-1], n[j]
        
    return n
"""

def insertionSort(n):
    for i in range(1, len(n), 1):
        if n[i] < n[i-1]:
            for j in range(i, 0, -1):
                if n[j] < n[j-1]:
                    n[j], n[j-1] = n[j-1], n[j]
    
    return n

start = time.perf_counter()
print("LIST BEFORE : {0}".format(n))
print("LIST AFTER : {0}".format(insertionSort(n)))
print()
print("Time needed : {0}".format(time.perf_counter()-start))
