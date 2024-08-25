import bisect

n = int(input())
connections = []

for _ in range(n):
    a, b = map(int, input().split())
    connections.append((a, b))

connections.sort()

b_positions = [b for _, b in connections]
lis_list = [b_positions[0]]
lis_log = []
for connection in connections:
    if connection[1] > lis_list[-1]:
        lis_list.append(connection[1])
        lis_log.append((connection[0], len(lis_list)))
    else:
        pos = bisect.bisect_left(lis_list, connection[1])
        lis_list[pos] = connection[1]
        lis_log.append((connection[0], pos + 1))

lis_order = len(lis_list)
not_lis = []
for log in lis_log[::-1]:
    if log[1] == lis_order:
        lis_order -= 1
    else:
        not_lis.append(log[0])

print(n - len(lis_list))
not_lis.sort()
for lis in not_lis:
    print(lis)
