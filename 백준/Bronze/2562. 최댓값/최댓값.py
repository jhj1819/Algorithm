numbers = []
for i in range(9):
    numbers.append(int(input()))
for i in range(9):
    if max(numbers) == numbers[i]:
        num = i+1
print(max(numbers))
print(num)
