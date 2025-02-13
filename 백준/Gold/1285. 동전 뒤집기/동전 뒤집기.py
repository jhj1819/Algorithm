n = int(input())
board = [list(map(lambda x: 0 if x == 'H' else 1, input().strip())) for _ in range(n)]

# 각 열을 비트마스크로 변환 (LSB가 위쪽 행)
col_masks = [0] * n
for j in range(n):
    for i in range(n):
        col_masks[j] |= (board[i][j] << i)

min_total = float('inf')

for row_mask in range(1 << n):
    total = 0
    for j in range(n):
        xor = row_mask ^ col_masks[j]
        cnt = bin(xor).count('1') 
        total += min(cnt, n - cnt)
        if total >= min_total:  # 조기 종료
            break
    if total < min_total:
        min_total = total

print(min_total)