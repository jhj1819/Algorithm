from collections import deque

n, k = map(int, input().split())

pan = list(input())

cnt = 0
for p in pan:
    if p == 'H':
        cnt += 1

dq = deque()
visited = {}
dq.append((cnt, 0))  # c 첫 세팅
visited[cnt] = 0  # 그냥 여기까지 가는 최소횟수 저장할까
answer = -1
while dq:
    o_cnt, t = dq.popleft()
    if o_cnt == 0:
        answer = t
        break
    for i in range(k+1):
        # i개를 o에서 넘기고 j개를 x에서 넘긴다..
        if i > o_cnt:  # o개수가 부족하면 안됨
            continue
        if k-i > n - o_cnt:  # x개수 부족하면 안됨
            continue
        if o_cnt + k - i*2 in visited:
            continue
        visited[o_cnt + k - i*2] = True
        dq.append((o_cnt + k - i*2, t+1))

print(answer)

