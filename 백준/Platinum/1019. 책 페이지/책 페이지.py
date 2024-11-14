n = input()  # 5674
numbers = []
count = dict()
for i in range(10):
    count[i] = 0


def f(a, b):
    for i in range(10):
        count[i] += int(a * b * pow(10, b - 1))  # b*pow(10, b) // 10

    for j in range(a):
        count[j] += int(pow(10, b))


zero_count = 0
for i in range(len(n)):
    zero_count += pow(10, i)

k = len(n)
while k > 0:
    divisor = int(pow(10, len(n) - 1))
    quotient = int(n) // divisor  # 몫
    numbers.append(quotient * divisor)

    divisor = int(n) - quotient * divisor  # 나머지
    count[quotient] += divisor + 1
    n = n[1:]
    k -= 1

for num in numbers:
    exponent = len(str(num)) - 1
    n = num // pow(10, exponent)  # num이 5000이면 n 은 5
    f(n, exponent)

count[0] -= zero_count

for c in count:
    print(count[c], end=' ')
