def find_inversion_count(arr: list) -> int:

    def modified_merge(l_inv, r_inv, l, r) -> (int, list):
        i, j = 0, 0
        sum_inv = 0
        result = []
        n = len(l)
        m = len(r)

        while i < n or j < m:
            if j >= m or (i < n and l[i] < r[j]):
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
                len_l = n - i
                sum_inv += len_l

        return sum_inv + l_inv + r_inv, result

    def modified_merge_sort(a: list) -> (int, list):
        n = len(a)
        if n <= 1:
            return 0, a

        left = a[:n//2]
        right = a[n//2:]

        l_inv_count, left = modified_merge_sort(left)
        r_inv_count, right = modified_merge_sort(right)

        return modified_merge(l_inv_count, r_inv_count, left, right)

    inv_count, _ = modified_merge_sort(arr)
    return inv_count


print(find_inversion_count([5, 4, 3, 2, 1]))