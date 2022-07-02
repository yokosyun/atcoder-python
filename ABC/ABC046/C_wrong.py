import math

if __name__ == "__main__":
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    a_pre = data[0][0]
    b_pre = data[0][1]
    for ind in range(1, len(data)):
        p13 = math.ceil(a_pre / data[ind][0])
        p24 = math.ceil(b_pre / data[ind][1])
        base = max(p13, p24)
        a_pre = base * data[ind][0]
        b_pre = base * data[ind][1]

    print(a_pre + b_pre)
