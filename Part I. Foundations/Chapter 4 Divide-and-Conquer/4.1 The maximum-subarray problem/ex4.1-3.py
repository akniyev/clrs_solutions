import random


def brute_force_maximum_subarray(arr: list) -> (int, int, float):
    n = len(arr)

    if n <= 1:
        return 0, 0, arr[0] if n == 0 else 0

    max_sum = arr[0]
    max_i = 0
    max_j = 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                max_i, max_j = i, j
    return max_i, max_j, max_sum


def divide_and_conquer_subarray(arr: list) -> (int, int, float):
    infinity = float('inf')

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
        if low == high:
            return low, high, arr[low]
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


n = 10000

test_array = [random.randint(-100, 100) for _ in range(n)]

ans2 = divide_and_conquer_subarray(test_array)
print(ans2)

ans1 = brute_force_maximum_subarray(test_array)
print(ans1)

print(ans1 == ans2)
