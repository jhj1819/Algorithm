import sys
input = sys.stdin.read

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - \
           (p2[1] - p1[1]) * (p3[0] - p1[0])

def convex_hull(points):
    points = sorted(points)  # x 오름차순, x 같으면 y 오름차순

    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # 첫 점과 끝 점은 upper/lower에서 중복됨 → set으로 중복 제거
    convex = lower[:-1] + upper[:-1]
    convex = list(set(convex))  # 중복 제거
    return len(convex)

def solution():
    data = input().split()
    N = int(data[0])
    points = [tuple(map(int, data[i:i+2])) for i in range(1, 2*N, 2)]
    print(convex_hull(points))

solution()
