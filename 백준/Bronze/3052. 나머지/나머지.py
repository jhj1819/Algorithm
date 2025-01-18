numbers = []
remainder =[]
for i in range(10):
    numbers.append(int(input()))
for i in range(10):
    remainder.append(numbers[i]%42)

num=[0]*42
for i in range(10):
    num[remainder[i]] = 1
print(sum(num))
