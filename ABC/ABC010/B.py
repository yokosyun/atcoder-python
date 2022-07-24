n = int(input())
a = list(map(int, input().split()))

n_remove = 0
for n_leaves in a:
    while n_leaves % 2 == 0 or n_leaves % 3 == 2:
        n_remove += 1
        n_leaves -= 1
print(n_remove)