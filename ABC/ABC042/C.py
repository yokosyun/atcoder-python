if __name__ == "__main__":
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    N, K = map(str, input().split())
    D = list(map(str, input().split()))

    availables = [num for num in nums if num not in D]

    N = list(N)
    res = N.copy()
    whole_change = False

    for ind in range(len(N)):
        if whole_change:
            res[ind] = availables[0]
        else:
            if N[ind] not in availables:
                whole_change = True
                res[ind] = (
                    availables[1]
                    if ind == 0 and availables[0] == "0"
                    else availables[0]
                )
                for val in availables:
                    if val > N[ind]:
                        res[ind] = val
                        break

    res = "".join(res)
    N = "".join(N)

    if res < N:
        res += str(availables[0])
    print(res)
