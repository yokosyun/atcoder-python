import numpy as np


n, m = list(map(int, input().split()))
an = [list(map(int, input().split())) for _ in range(m)]

network = np.identity(n)
network = network * -1

for a, b in an:
    network[a - 1][b - 1] = 1
    network[b - 1][a - 1] = 1


def get_friends(data_list, my_self):
    friends_list = []
    for idx in range(len(data_list)):
        if data_list[idx] == 1 and idx != my_self:
            friends_list.append(idx)
    return friends_list


for i in range(n):
    ans = set()
    for j in range(n):
        if network[i][j] == 1:
            friend_of_friends = get_friends(network[:][j], i)
            for f in friend_of_friends:
                if network[i][f] == 0:
                    ans.add(f)
    print(len(ans))
