from functools import cmp_to_key
import heapq

# 비교 함수
def comp(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        if a[2] < b[2]:
            return -1
        elif a[2] > b[2]:
            return 1
        else:
            return 0

# 입력
n = int(input())
lecture_info_list = []
for _ in range(n):
    num, start, end = map(int, input().split())
    lecture_info_list.append((num, start, end))

# 정렬 (강의 시작 시간 기준)
lecture_info_list.sort(key=cmp_to_key(comp))

# 최소 힙을 이용해 방의 끝나는 시간을 관리
min_heap = []

for lecture_info in lecture_info_list:
    start, end = lecture_info[1], lecture_info[2]
    if min_heap and min_heap[0] <= start:  # 현재 수업 시작 시간보다 일찍 끝나는 강의실이 있다면 그 강의실 재사용
        heapq.heapreplace(min_heap, end)  # 가장 빨리 끝나는 강의실을 새 강의 종료 시간으로 갱신
    else:  # 모든 강의실이 꽉 찼다면 새로운 강의실 추가
        heapq.heappush(min_heap, end)

print(len(min_heap))
