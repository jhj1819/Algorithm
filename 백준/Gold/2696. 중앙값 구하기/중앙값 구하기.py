from queue import PriorityQueue
import sys

T = int(input())

for _ in range(T):
    M = int(input())
    numbers = []
    for _ in range(M // 10 + 1):
        numbers += list(map(int, input().split()))
    answer = []
    count = 0

    max_pq = PriorityQueue()
    min_pq = PriorityQueue()
    max_pq.put(sys.maxsize)
    min_pq.put(sys.maxsize)

    for i in range(len(numbers)):
        if i % 2 == 0:
            count += 1
            arr = sorted([numbers[i], min_pq.get(), -max_pq.get()])
            answer.append(arr[1])
            min_pq.put(arr[1])
            max_pq.put(-arr[0])
            min_pq.put(arr[2])
        else:
            arr = sorted([numbers[i], min_pq.get(), -max_pq.get()])
            max_pq.put(-arr[1])
            max_pq.put(-arr[0])
            min_pq.put(arr[2])

    print(count)
    for i in range(len(answer) // 10 + 1):
        end = min(len(answer), 10 * (i + 1))
        print(" ".join(map(str, answer[10 * i:end])))
