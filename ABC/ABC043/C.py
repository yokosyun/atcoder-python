from collections import deque
from decimal import Decimal, ROUND_HALF_UP
import numpy as np


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    # y = (x-a1)^2 + (x-a2)^2 + (x-an)^2 ...
    # y = n * (x - 1/n(a1 + a2 + ... + an))^2 - 1/n * (a1+a2+...+an)^2 + (a1^2 + a2^2 + ... + an^2)

    x = sum(a) / n
    x = int(Decimal(str(x)).quantize(Decimal("0"), rounding=ROUND_HALF_UP))
    y = sum((x - np.array(a)) ** 2)

    print(int(y))
