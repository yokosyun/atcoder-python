# https://www.geeksforgeeks.org/quick-sort/


def quick_sort(data_list):
    if len(data_list) < 1:
        return data_list

    list_small = []
    list_big = []
    current = data_list[-1]

    for ind in range(len(data_list) - 1):
        if data_list[ind] < current:
            list_small.append(data_list[ind])
        else:
            list_big.append(data_list[ind])

    small = quick_sort(list_small)
    big = quick_sort(list_big)

    return small + [current] + big


if __name__ == "__main__":
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = quick_sort(DATA.copy())
    print(sorted_data)
