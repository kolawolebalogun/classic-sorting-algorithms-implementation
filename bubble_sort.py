import time


# Given an array [10,9,8,7,6,5,4,3,2,1]
# Sort the array in Ascending order
def bubble_sort(arr: list):
    start = time.time()
    swapped = True
    length = len(arr) - 1

    while swapped:
        swapped = False
        for i in range(length):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swapped = True

    done = time.time() - start
    print('{:f}'.format(done))


if __name__ == "__main__":
    bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
