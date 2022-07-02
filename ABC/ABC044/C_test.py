def nCk(n, k):
    ans = 1
    for j in range(0, k):
        ans *= (n - j) / (k - j)
    return ans


def next(data_list, start_ind, pre_sum, pre_mul):
    sum_list = []
    mul_list = []

    for ind in range(start_ind, len(data_list)):

        for cnt in range(1, int((data_list[ind][1])) + 1):
            cur_mul = pre_mul * nCk(int(data_list[ind][1]), cnt)
            cur_sum = pre_sum + data_list[ind][0] * cnt

            if cur_sum > 0:
                return sum_list, mul_list
            sum_list += [cur_sum]  # append current sum
            mul_list += [cur_mul]

            if ind != (len(data_list) - 1):
                a, b = next(
                    data_list, ind + 1, cur_sum, cur_mul
                )  # append next sum list
                sum_list += a
                mul_list += b

    return sum_list, mul_list


if __name__ == "__main__":
    from collections import Counter
    import numpy as np

    N, A = list(map(int, input().split()))
    x = list(map(int, input().split()))

    x = np.array(x) - A
    count_dict = Counter(x)
    count_list = list(sorted(count_dict.items()))

    dict_a = np.empty((len(count_list), 2))

    for i in range(len(count_list)):
        dict_a[i][0] = count_list[i][0]
        dict_a[i][1] = count_list[i][1]

    sum_list, mul_list = next(dict_a, 0, 0, 1)

    total = 0
    for ind in range(len(sum_list)):
        if sum_list[ind] == 0.0:
            total += mul_list[ind]
    print(int(total))
