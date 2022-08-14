A, B, C, D = list(map(int, input().split()))
takahashi = B / A
aoki = D / C
if takahashi == aoki:
    print("DRAW")
elif takahashi > aoki:
    print("TAKAHASHI")
else:
    print("AOKI")
