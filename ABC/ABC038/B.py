h1, w1 = list(map(int, input().split()))
h2, w2 = list(map(int, input().split()))
if h1 in [h2, w2] or w1 in [h2, w2]:
    print("YES")
else:
    print("NO")
