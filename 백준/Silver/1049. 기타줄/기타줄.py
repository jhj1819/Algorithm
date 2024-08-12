n, m = map(int, input().split())
answer = 0
six_cost = float('inf')
one_cost = float('inf')

for _ in range(m):
    a, b = map(int, input().split())
    six_cost = min(six_cost, a)
    one_cost = min(one_cost, b)

if one_cost < six_cost/6:
    answer = one_cost * n
elif (n % 6) * one_cost > six_cost:
    answer = (n//6) * six_cost + six_cost
else:
    answer = (n//6) * six_cost + (n % 6) * one_cost

print(answer)