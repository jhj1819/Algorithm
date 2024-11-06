n = int(input())
graph = [list(map(int, input().split())) for row in range(n)]
white_count, blue_count = 0, 0


def func(r, c, size):
    global white_count, blue_count
    color = graph[r][c]
    for r_ in range(r, r + size):
        for c_ in range(c, c + size):
            if color != graph[r_][c_]:
                func(r, c, size // 2)
                func(r + size // 2, c, size // 2)
                func(r, c + size // 2, size // 2)
                func(r + size // 2, c + size // 2, size // 2)
                return
    if color == 1:
        blue_count += 1
    else:
        white_count += 1
    return


func(0, 0, n)
print(white_count)
print(blue_count)
