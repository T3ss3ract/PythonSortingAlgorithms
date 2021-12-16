def timsort(arr):
    n = len(arr)
    for i in range(0, n, 32):
        insertion_sort(arr, i, min((i+31), (n-1)))
    size = 32
    while size < n:
        for left in range(0, n, 2*size):
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            merge(arr, left, mid, right)
        size = 2*size
    return arr

def insertion_sort(arr, left, right):
    for i in range(left+1, right+1):
        temp = arr[i]
        j = i-1
        while j >= left and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp

def merge(arr, left, mid, right):
    len1, len2 = mid-left+1, right-mid
    L, R = [], []
    for i in range(0, len1):
        L.append(arr[left+i])
    for i in range(0, len2):
        R.append(arr[mid+1+i])
    i, j, k = 0, 0, left
    while i < len1 and j < len2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [5, 21, 7, 23, 19, 74, 11, 105, 324, 1, 64]
print(timsort(arr))
