import math
from functools import reduce

n = int(input())
alist = list(map(int, input().split()))

differences = [abs(alist[i] - alist[0]) for i in range(1, n)]

print(reduce(math.gcd, differences))