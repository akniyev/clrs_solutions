import numpy as np


def merge(a: list, b: list) -> list:
    """Merges two sorted lists into one sorted list"""
    i = 0
    j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len(a):
        result.append(a[i])
        i += 1

    while j < len(b):
        result.append(b[j])
        j += 1

    return result


def merge_sort(a: list) -> list:
    n = len(a)
    if n <= 1:
        return a

    l = a[:n//2]
    r = a[n//2:]

    return merge(merge_sort(l), merge_sort(r))


def check_sorting(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True


def binary_search(sorted_a: list, x, epsilon=0.0000001) -> int:
    """Returns the index of x in a sorted array a or -1"""
    a = sorted_a

    def b_search(l: int, r: int) -> int:
        if l > r:
            return -1
        m = (l + r) // 2
        if abs(a[m] - x) < epsilon:
            return m
        elif x < a[m]:
            return b_search(l, m-1)
        else:
            return b_search(m+1, r)

    return b_search(0, len(a)-1)


def find_two_elements_with_sum(sorted_a: list, x) -> ():
    """Finds two elements whose sum equals to x, return a tuple with the indeces or None"""
    for index, el in enumerate(sorted_a):
        j = binary_search(sorted_a, x - el)
        print(j)
        if j > -1 and j != index:
            return index, j
    return None


l = [0.01359524283229141, 0.15990499895078036, 0.237477611348496, 0.4854106838760738, 0.4855394348778018, 0.525587547808596, 0.7561888021044003, 0.8973476665183093, 0.9693065311979743, 0.9961379391386296]
print(l)
print(find_two_elements_with_sum(l, 0.4854106838760738 + 0.8973476665183093))