import time
from numpy.random import randint, seed

seed(1)

N = 10_000

random_numbers = randint(0, 10000, N)

print(max(random_numbers))
print(min(random_numbers))

print("Random array:")
print(random_numbers)


def heap_sort(_arr: list):
    arr = list(_arr)
    limit = len(arr)

    def left(i: int):
        return 2*i + 1

    def right(i: int):
        return 2*i + 2

    def exists(i: int):
        return i < limit

    def swap(i, j):
        c = arr[i]
        arr[i] = arr[j]
        arr[j] = c

    def max_heapify(i: int):
        l = left(i)
        r = right(i)
        largest = i
        for j in [l, r]:
            if exists(j) and arr[j] > arr[largest]:
                largest = j

        if largest != i:
            swap(i, largest)
            max_heapify(largest)

    for i in reversed(range(N)):
        max_heapify(i)

    for i in range(len(arr)-1):
        swap(0, limit-1)
        limit -= 1
        max_heapify(0)

    return arr


t1 = time.time()
sorted_numbers = heap_sort(random_numbers)
t2 = time.time()
sorted_numbers2 = sorted(random_numbers)
t3 = time.time()

print(f"Heapsort time: {t2 - t1}")
print(f"Python's sort time: {t3 - t2}")

print(sorted_numbers)
print(sorted_numbers == sorted_numbers2)
