n, k = map(int, input().split())
tem_data = list(map(int, input().split()))

curr_tem = sum(tem_data[:k])  # 0으로 하면 최대 기온이 음수일 때 문제
max_sum = curr_tem

for i in range(len(tem_data) - k):
    curr_tem = curr_tem - tem_data[i] + tem_data[i+k]  # -i일 + i+k일
    max_sum = max(max_sum, curr_tem)

print(max_sum)


