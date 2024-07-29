# 최대힙/최소힙 두개로 삭제하는데 문제는 ... 큐가 다 비워졌을때
# 2개 삽입하고 최소2개 최대1개 뺼때... 최소에서 2개뺀게 최대에서 적용안되는 문제 ...
# 이걸 연동시키기 위해 num_dict 만들어서 현재 삭제할 원소가 있는지, 몇개있는지를 계속 동기화시킨다..
#주의할점, 최대힙의 경우 음수로 계산해야한다는점...
import sys
import heapq

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    max_heap = []
    min_heap = []
    num_dict = dict()

    for i in range(n):
        command, val_str = input().split()
        val = int(val_str)

        if command == 'I':
            heapq.heappush(max_heap, -val)
            heapq.heappush(min_heap, val)
            if val in num_dict:
                num_dict[val] += 1
            else:
                num_dict[val] = 1
        else:  # D일때
            while min_heap and max_heap:
                if val == -1:  # 최솟값 삭제
                    get_num = heapq.heappop(min_heap)

                    if num_dict[get_num] > 0:
                        num_dict[get_num] -= 1
                        break

                else:  # 최댓값 삭제
                    get_num = -heapq.heappop(max_heap)
                    if num_dict[get_num] > 0:
                        num_dict[get_num] -= 1
                        break

    while min_heap and num_dict[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and num_dict[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        min_val = min_heap[0]
        max_val = -max_heap[0]
        print(f"{max_val} {min_val}")