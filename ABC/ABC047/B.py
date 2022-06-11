import numpy as np

if __name__ == "__main__":
    w, h, n = list(map(int, input().split()))
    data_list = [list(map(int, input().split())) for _ in range(n)]
    block = np.zeros((h, w))

    for data in data_list:
        if data[2] == 1:
            block[:, : data[0]] = 1
        elif data[2] == 2:
            block[:, data[0] :] = 1
        elif data[2] == 3:
            block[: data[1], :] = 1
        elif data[2] == 4:
            block[data[1] :, :] = 1

    print(np.sum(block == 0))
