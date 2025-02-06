def ccw(p1, p2, p3):
    return (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0])

def main():
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    p3 = tuple(map(int, input().split()))
    result = ccw(p1, p2, p3)
    result = 1 if result > 0 else -1 if result < 0 else 0
    print(result)

if __name__ == "__main__":
    main()