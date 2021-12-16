def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    arr1 = [7, 3, 4, 5, 1, 23, 32, 1, 14, 15, 17, 90, 103, 43, 51, 38, 202]
    print(arr1)
    _sorted = quicksort(arr1)
    print(_sorted)
