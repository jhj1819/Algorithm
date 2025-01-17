import sys

input = sys.stdin.read


def floyd_warshall(n, edges):
    INF = float('inf')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for a, b, c in edges:
        graph[a][b] = min(graph[a][b], c)

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return graph


def main():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    edges = [(int(data[i * 3 + 2]), int(data[i * 3 + 3]), int(data[i * 3 + 4])) for i in range(m)]

    result = floyd_warshall(n, edges)

    for i in range(1, n + 1):
        print(" ".join('0' if result[i][j] == float('inf') else str(result[i][j]) for j in range(1, n + 1)))


if __name__ == "__main__":
    main()
