import ex4_1_3
import random
import time


def linear_time_maximum_subarray(arr: list) -> (int, int, float):
    n = len(arr)
    current_max_sum = arr[0]
    min_i = 0
    max_i = 0

    sum_from_min_to_j = arr[0]
    max_sum_to_j = arr[0]
    max_to_j_min = 0

    for j in range(1, n):
        sum_from_min_to_j += arr[j]

        max_sum_to_j += arr[j]
        max_to_j1 = max_sum_to_j
        for j1 in range(max_to_j_min, j):
            max_to_j1 -= arr[j1]
            if max_to_j1 > max_sum_to_j:
                max_sum_to_j = max_to_j1
                max_to_j_min = j1 + 1

        if max_sum_to_j >= sum_from_min_to_j and max_sum_to_j >= current_max_sum:
            current_max_sum = max_sum_to_j
            sum_from_min_to_j = max_sum_to_j
            min_i = max_to_j_min
            max_i = j
        elif sum_from_min_to_j >= max_sum_to_j and sum_from_min_to_j >= current_max_sum:
            current_max_sum = sum_from_min_to_j
            max_i = j

    return min_i, max_i, current_max_sum


if __name__ == "__main__":
    array_length = 5000

    test_array = [random.randint(-100, 100) for _ in range(array_length)]
    # test_array = [97, -14, -84, -64, -33, 63, -29, 73, 99, -57]

    # print(test_array)

    start1 = time.time()
    ans1 = ex4_1_3.divide_and_conquer_subarray(test_array)
    end1 = time.time()
    print(ans1, end1 - start1)

    start2 = time.time()
    ans2 = linear_time_maximum_subarray(test_array)
    end2 = time.time()
    print(ans2, end2 - start2)

    print(ans1 == ans2)