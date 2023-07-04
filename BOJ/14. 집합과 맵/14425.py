import sys
input=sys.stdin.readline
n, m = map(int, input().split())

cnt = 0
str_list = []
for i in range(n+m):
    str_list.append(input())

str_dict = {}

for j in range(n):
    str_dict[str_list[j]] = 0

for k in range(m):
    if str_list[n+k] in str_dict:
        cnt += 1

print(cnt)