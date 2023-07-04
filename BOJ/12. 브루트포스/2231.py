import sys

input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N):
    find_num = list(map(int, str(i)))
    find_num_sum = sum(find_num) + i
    if N == find_num_sum:
        result = i
        break

print(result)


