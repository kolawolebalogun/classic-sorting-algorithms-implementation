import time


# Given an array [10,9,8,7,6,5,4,3,2,1]
# Sort the array in Ascending order
def insertion_sort(arr: list):
    start = time.time()
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                popped = arr.pop(i)
                arr.insert(j, popped)

    done = time.time() - start
    print(arr)
    print('{:f}'.format(done))


if __name__ == "__main__":
    insertion_sort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1])
