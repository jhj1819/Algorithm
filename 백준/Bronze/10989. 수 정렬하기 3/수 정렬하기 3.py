## 메모리 초과... 리스트의 크기를 줄이기 위해 계수정렬 이용
import sys

input = sys.stdin.readline
n = int(input())
count_dict = dict()

for _ in range(n):
    i = int(input())
    if i not in count_dict:
        count_dict[i] = 0
    count_dict[i] += 1

arr = list(count_dict.keys())
arr.sort()

for a in arr:
    for _ in range(count_dict[a]):
        print(a)
