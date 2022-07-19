def sold(t, n, an, m, bm):
    if m > n:
        return "no"

    for b in bm:
        flag = False
        while len(an):
            val = an.pop(0)
            if b >= val and b <= val + t:
                flag = True
                break
        if flag == False:
            return "no"
    return "yes"


t = int(input())
n = int(input())
an = list(map(int, input().split()))
m = int(input())
bm = list(map(int, input().split()))

print(sold(t, n, an, m, bm))
