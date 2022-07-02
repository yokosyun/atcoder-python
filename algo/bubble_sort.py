def bubble_sort_ascending(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def bubble_sort_descending(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == "__main__":
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = bubble_sort_descending(DATA.copy())

    print(f"{DATA}  →  {sorted_data}")