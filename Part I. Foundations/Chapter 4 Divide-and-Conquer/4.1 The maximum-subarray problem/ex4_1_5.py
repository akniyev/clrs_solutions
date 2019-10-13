import ex4_1_3
import random
import time


def linear_time_maximum_subarray(arr: list) -> (int, int, float):
    n = len(arr)
    min_i = 0
    max_i = 0
    max_sum = arr[0]
    current_sum = max_sum
    current_min_i = min_i

    for j in range(1, n):
        current_sum += arr[j]

        max_sum1 = current_sum
        for j1 in range(current_min_i, j):
            max_sum1 -= arr[j1]
            if max_sum1 > current_sum:
                current_min_i = j1
                current_sum = max_sum1

        v1 = max_sum
        v2 = current_sum
        v3 = arr[j]

        if v2 > v1 and v2 > v3:
            min_i = current_min_i
            max_i = j
            max_sum = current_sum

        elif v3 > v1 and v3 > v2:
            min_i = j
            max_i = j
            max_sum = arr[j]
            current_sum = arr[j]


    return min_i, max_i, max_sum


if __name__ == "__main__":
    array_length = 10

    test_array = [random.randint(-100, 100) for _ in range(array_length)]
    test_array = [97, -14, -84, -64, -33, 63, -29, 73, 99, -57]

    print(test_array)

    start1 = time.time()
    ans1 = ex4_1_3.divide_and_conquer_subarray(test_array)
    end1 = time.time()
    print(ans1, end1 - start1)

    start2 = time.time()
    ans2 = linear_time_maximum_subarray(test_array)
    end2 = time.time()
    print(ans2, end2 - start2)

    print(ans1 == ans2)