if __name__ == "__main__":
    N, L = map(int, input().split())
    s = [input() for _ in range(N)]
    res = sorted(s)
    print("".join(res))
