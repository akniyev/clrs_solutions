import ex4_1_3
import random
import time


def linear_time_maximum_subarray(arr: list) -> (int, int, float):
    n = len(arr)
    suffix_max_sum = arr[0]
    suffix_i = 0

    max_sum = arr[0]
    min_i = 0
    max_i = 0

    for j in range(1, n):
        if suffix_max_sum + arr[j] < arr[j]:
            suffix_max_sum = arr[j]
            suffix_i = j
        else:
            suffix_max_sum += arr[j]

        if suffix_max_sum > max_sum:
            max_sum = suffix_max_sum
            min_i = suffix_i
            max_i = j

    return min_i, max_i, max_sum


if __name__ == "__main__":
    array_length = 5000000

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