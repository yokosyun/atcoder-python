import numpy as np
import math

a = int(input())
b = int(input())
n = int(input())

lcm = np.lcm.reduce([a, b])

print(math.ceil(n / lcm) * lcm)