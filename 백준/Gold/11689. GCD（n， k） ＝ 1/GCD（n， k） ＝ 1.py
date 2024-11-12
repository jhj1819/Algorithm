import math

n = int(input())
answer = n

i = 2
divisor = dict()
while n > 1:
    n_ = n
    for i in range(2, int(math.sqrt(n_)+1)):
        if n % i == 0:
            if i not in divisor:
                divisor[i] = 0
            divisor[i] += 1
            n = n // i
            break
    if n_ == n:
        if n not in divisor:
            divisor[n] = 0
        divisor[n] += 1
        break

for d in divisor:
    answer *= (1-1/d)

print(int(answer))




