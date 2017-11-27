import time


# Given an array [1,9,8,7,6,5,4,3,2,10]
# Sort the array in Ascending order
def quick_sort(arr: list, start_index, end_index):
    if start >= end_index:
        return arr
    pivot, pivot_index = arr[end_index], 0
    for i in range(end_index):
        if arr[i] <= pivot:
            arr.insert(pivot_index, arr.pop(i))
            pivot_index += 1
    arr.insert(pivot_index, arr.pop(end_index))

    quick_sort(arr, start_index, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end_index)

    return arr


if __name__ == "__main__":
    unsorted = [1, 5, 10, 8, 2, 6, 4, 7, 9, 3]
    start = time.time()
    print(quick_sort(unsorted, 0, len(unsorted) - 1))
    print('{:f}'.format(time.time() - start))
