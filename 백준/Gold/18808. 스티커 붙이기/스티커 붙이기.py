n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]


def rotate_sticker(sticker):
    return [list(row[::-1]) for row in zip(*sticker)]


def attach(x, y, sticker, graph):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                graph[x + i][y + j] = 1


def can_attach(x, y, sticker, graph):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1 and graph[x + i][y + j] == 1:  # sticker의 범위는 x+i가 아니라 i
                return False
    return True


for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    is_attach = False
    for _ in range(4):
        for x in range(n - len(sticker) + 1):
            for y in range(m - len(sticker[0]) + 1):
                if can_attach(x, y, sticker, graph):
                    attach(x, y, sticker, graph)
                    is_attach = True
                    break
            if is_attach: break
        if is_attach: break
        sticker = rotate_sticker(sticker)

print(sum(sum(row) for row in graph))
