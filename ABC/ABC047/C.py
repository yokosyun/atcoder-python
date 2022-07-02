from collections import deque

if __name__ == "__main__":
    s = deque(list(input()))

    cnt = 0
    pre_left = s.popleft()
    while s:
        left = s.popleft()
        if pre_left != left:
            cnt += 1
            pre_left = left

    print(cnt)
