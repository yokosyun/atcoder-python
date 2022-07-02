if __name__ == "__main__":
    N, x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    sum = 0
    for ind in range(N - 1):
        sub = a[ind + 1] + a[ind] - x
        if sub > 0:
            if a[ind + 1] >= sub:
                sum += sub
                a[ind + 1] -= sub
            else:
                sum += a[ind + 1]
                a[ind + 1] -= a[ind + 1]

    sub = a[1] + a[0] - x
    if sub > 0:
        sum += sub

    print(sum)
