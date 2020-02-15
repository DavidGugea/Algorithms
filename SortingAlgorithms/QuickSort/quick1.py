def quickSort(A):
    quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    p = partition(A, low, hi)

    # low hi and pi are indexes of the array

    quick_sort2(A, low, p-1)
    quick_sort2(A, p+1, hi)
def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        # That means that low is bigger than middle so we will choose low
        # otherwise it will stay "hi" as it's default value
        pivot = low

    return pivot
def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]

    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low
