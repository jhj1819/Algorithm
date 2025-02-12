import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    R, C, M = map(int, input().split())
    sharks = defaultdict(dict)
    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        sharks[(r-1, c-1)] = (s, d-1, z)  # 0-based

    directions = [(-1,0), (1,0), (0,1), (0,-1)]  # 상, 하, 우, 좌
    total = 0

    for king_col in range(C):
        # 1. 낚시왕이 상어 포획
        target = None
        min_row = R
        for (x, y), (_, _, z) in sharks.items():
            if y == king_col and x < min_row:
                min_row = x
                target = (x, y)
        if target is not None:
            total += sharks[target][2]
            del sharks[target]

        # 2. 상어 이동
        new_sharks = defaultdict(dict)
        for (x, y), (s, d, z) in sharks.items():
            # 원래 방향 및 속도 유지
            orig_s = s
            orig_d = d
            nx, ny = x, y
            
            # 방향에 따른 이동 계산
            if orig_d < 2:  # 상하 이동 (d=0: 상, d=1: 하)
                cycle = (R - 1) * 2
                s %= cycle
                if orig_d == 0:  # 상승
                    if x >= s:
                        nx = x - s
                    else:
                        s -= x
                        if s <= R - 1:
                            nx = s
                            orig_d = 1  # 방향 전환: 하강
                        else:
                            nx = 2 * (R - 1) - s
                else:  # 하강
                    if (R - 1) - x >= s:
                        nx = x + s
                    else:
                        s -= (R - 1) - x
                        if s <= R - 1:
                            nx = (R - 1) - s
                            orig_d = 0  # 방향 전환: 상승
                        else:
                            nx = s - (R - 1)
                nx = max(0, min(nx, R - 1))
            else:  # 좌우 이동 (d=2: 우, d=3: 좌)
                cycle = (C - 1) * 2
                s %= cycle
                if orig_d == 2:  # 우측
                    if (C - 1) - y >= s:
                        ny = y + s
                    else:
                        s -= (C - 1) - y
                        if s <= C - 1:
                            ny = (C - 1) - s
                            orig_d = 3  # 방향 전환: 좌측
                        else:
                            ny = s - (C - 1)
                else:  # 좌측
                    if y >= s:
                        ny = y - s
                    else:
                        s -= y
                        if s <= C - 1:
                            ny = s
                            orig_d = 2  # 방향 전환: 우측
                        else:
                            ny = 2 * (C - 1) - s
                ny = max(0, min(ny, C - 1))

            # 같은 위치에서 크기 큰 상어만 남김
            key = (nx, ny)
            if key not in new_sharks or new_sharks[key][2] < z:
                new_sharks[key] = (orig_s, orig_d, z)
        
        sharks = new_sharks

    print(total)

if __name__ == "__main__":
    main()
