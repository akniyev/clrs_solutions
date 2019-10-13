import random
import time

infinity = float('inf')


def brute_force_maximum_subarray(arr: list, low: int = None, high: int = None) -> (int, int, float):
    low = 0 if low is None else low
    high = len(arr)-1 if high is None else high

    n = high - low + 1

    if n <= 1:
        return low, high, arr[low] if n == 1 else 0

    max_sum = -infinity
    max_i = low
    max_j = low

    for i in range(low, high + 1):
        current_sum = 0
        for j in range(i, high + 1):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_i, max_j = i, j
    return max_i, max_j, max_sum


def divide_and_conquer_subarray(arr: list) -> (int, int, float):

    def cross_max_subarray(low: int, high: int, mid: int) -> (int, int, float):
        left_low = low
        left_max_sum = -infinity

        left_sum = 0
        for i in range(mid, low - 1, -1):
            left_sum += arr[i]
            if left_sum > left_max_sum:
                left_max_sum = left_sum
                left_low = i

        right_high = high
        right_max_sum = -infinity

        right_sum = 0
        for i in range(mid+1, high+1):
            right_sum += arr[i]
            if right_sum > right_max_sum:
                right_max_sum = right_sum
                right_high = i
        return left_low, right_high, left_max_sum + right_max_sum

    def r(low: int, high: int) -> (int, int, float):
        if high - low < 40:
            return brute_force_maximum_subarray(arr, low, high)
        mid = (low + high) // 2

        left_low, left_high, left_sum = r(low, mid)
        right_low, right_high, right_sum = r(mid+1, high)
        cross_low, cross_high, cross_sum = cross_max_subarray(low, high, mid)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    return r(0, len(arr)-1)


if __name__ == "__main__":
    array_length = 10

    test_array = [random.randint(-100, 100) for _ in range(array_length)]

    start1 = time.time()
    ans1 = divide_and_conquer_subarray(test_array)
    end1 = time.time()
    print(ans1, end1 - start1)

    start2 = time.time()
    ans2 = brute_force_maximum_subarray(test_array)
    end2 = time.time()
    print(ans2, end2 - start2)

    print(ans1 == ans2)
