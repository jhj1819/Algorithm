N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def f(rows):
    pre = 0
    count = 0  # 몇번째 연속된 칸인지..

    for i in range(len(rows)):
        if pre == 0:  # 처음
            pre = rows[i]
            count += 1
        elif pre == rows[i]:  # 같은 높이면 count +1
            count += 1
        elif rows[i] - pre == 1:  # 1칸 높으면
            if count >= L:
                count = 1
                pre = rows[i]
            else:
                return False
        elif pre - rows[i] == 1:  # 1칸 낮으면
            for j in range(L):
                if i + j >= N:
                    return False
                if rows[i + j] != pre - 1:
                    return False
            pre = pre - 1
            count = -L + 1
        else:  # 2칸이상 차이
            return False
    return True


answer = 0
for rows in graph:
    if f(rows):
        answer += 1

graph2 = [list(i) for i in zip(*graph)]
for rows in graph2:
    if f(rows):
        answer += 1

print(answer)

# 경우에따라 왼->오 는 가능하지만 오->왼은 불가능 할수도 -> 그럼 양쪽에서 한번씩 체크? 왼쪽과 오른쪽 모두 경사로를 써야하는 문제 발생 -> 내려갈때 올라갈때 경우 나누기
