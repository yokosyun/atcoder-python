n = int(input())

hh = n // 3600
n -= hh * 3600
mm = n // 60
n -= mm * 60
ss = n

print(str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2))
