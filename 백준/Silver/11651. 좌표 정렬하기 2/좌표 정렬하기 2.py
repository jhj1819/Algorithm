n = int(input())

pointList = []
for _ in range(n):
    y,x = map(int, input().split())
    pointList.append((x,y))

pointList.sort()
for point in pointList:
    print(point[1],point[0])