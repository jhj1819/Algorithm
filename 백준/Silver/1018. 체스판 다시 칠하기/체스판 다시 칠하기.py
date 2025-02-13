n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

def calc_paints_count(x, y):
    white_paints = 0
    black_paints = 0
    for row in range(y, y + 8):
        for col in range(x, x + 8):
            is_white = (col + row) % 2 == 0
            if is_white:
                if board[row][col] == 'B':
                    white_paints += 1
                else:
                    black_paints += 1
            else:
                if board[row][col] == 'W':
                    white_paints += 1
                else:
                    black_paints += 1

    return min(white_paints, black_paints)


answer = float('inf')
for y in range(n - 7):
    for x in range(m - 7):
        answer = min(answer, calc_paints_count(x, y))

print(answer)
