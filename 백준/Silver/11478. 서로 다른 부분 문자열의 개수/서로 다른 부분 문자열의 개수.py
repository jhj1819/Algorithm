str = input()
n = len(str)

str_set = set()

for i in range(n):
    for j in range(i,n):
        str_set.add(str[i:j+1])

print(len(str_set))
