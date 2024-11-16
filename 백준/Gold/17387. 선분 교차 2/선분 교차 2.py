x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)


def ccw(p1, p2, p3):
    k = (p1[1] - p2[1]) * (p2[0] - p3[0]) - (p1[0] - p2[0]) * (p2[1] - p3[1])
    if k > 0:
        return 1
    elif k < 0:
        return -1
    else:
        return 0


ccw1 = ccw(p1, p2, p3)
ccw2 = ccw(p1, p2, p4)
ccw3 = ccw(p3, p4, p1)
ccw4 = ccw(p3, p4, p2)

answer = 0


def is_overlapping(p1, p2, p3, p4):
    if max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0]) and \
            max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1]):
        return True
    return False


if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:  # 평행인 경우
        if is_overlapping(p1, p2, p3, p4):  # 평행한 경우, 겹치는 부분이 있는지 확인
            answer = 1
    else:
        answer = 1

print(answer)
