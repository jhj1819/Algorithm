def calculate_rank(people):
    n = len(people)
    rankings = []
    for i in range(n):
        bigger_count = 1
        for j in range(n):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                bigger_count += 1
        rankings.append(bigger_count)
    return rankings


def main():
    n = int(input())
    people = [tuple(map(int, input().split())) for _ in range(n)]
    answer = calculate_rank(people)
    print(*answer)


if __name__ == "__main__":
    main()
