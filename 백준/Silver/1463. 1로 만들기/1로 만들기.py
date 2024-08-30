n = int(input())

queue =[]
queue.append(n)
dic = dict()
dic[n] = 0

while queue:
    current = queue.pop(0)
    if current == 1:
        break

    if current%3 == 0:
        if current/3 not in dic:
            dic[current/3] = dic[current] + 1
            queue.append(current/3)

    if current%2 ==0:
        if current/2 not in dic:
            dic[current/2] = dic[current] + 1
            queue.append(current / 2)

    if current-1 not in dic:
        dic[current-1] = dic[current] + 1
        queue.append(current-1)

print(dic[1])