n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]
a = min(n, m)
answer = 0


def is_valid(x, y, a):
    if graph[y][x] == graph[y + a][x] == graph[y][x + a] == graph[y + a][x + a]:
        return True
    return False


is_find = False

while a > 0:
    for x in range(0, m - a+1):
        for y in range(0, n - a+1):
            if is_valid(x, y, a-1):
                answer = a*a
                is_find = True  # 2중 반복문을 break하나로 빠져나가려는 실수..
                break
        if is_find:
            break
    if is_find:
        break
    a -= 1

print(answer)