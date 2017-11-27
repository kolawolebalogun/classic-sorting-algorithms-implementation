import math
import time


# Given an array [10,9,8,7,6,5,4,3,2,1]
# Sort the array in Ascending order
def merge(left_arr: list, right_arr: list):
    arr = []
    while len(left_arr) and len(right_arr):
        if left_arr[0] <= right_arr[0]:
            arr.append(left_arr.pop(0))
        else:
            arr.append(right_arr.pop(0))
    arr += left_arr + right_arr
    return arr


def merge_sort(arr: list):
    arr_length = len(arr)
    if arr_length < 2:
        return arr
    halved = math.floor(len(arr) / 2)
    left_arr, right_arr = arr[0: halved], arr[halved:]
    arr = merge(merge_sort(left_arr), merge_sort(right_arr))
    return arr


if __name__ == "__main__":
    start = time.time()
    print(merge_sort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]))
    print('{:f}'.format(time.time() - start))
