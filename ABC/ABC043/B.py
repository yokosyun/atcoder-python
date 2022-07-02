from collections import deque

if __name__ == "__main__":
    s = list(input())

    que = deque()
    for data in s:
        if data == "B":
            if len(que):
                que.pop()
        else:
            que.append(data)
    out = "".join(que)

    print(out)
