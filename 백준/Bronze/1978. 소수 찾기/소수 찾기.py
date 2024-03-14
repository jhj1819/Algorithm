def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, x):
    	if x % i == 0:
        	return False
    return True

N = int(input())
numbers = list(map(int,input().split()))
count = 0
for num in numbers:
    if is_prime(num):
        count += 1

print(count)