a = int(input())
b = int(input())
diff = min(abs(b - a), 10 - a + b, 10 - b + a)
print(diff)
