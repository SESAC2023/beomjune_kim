import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split(' ')))

f = int(input())
find_list = list(map(int, input().split(' ')))

num_list.sort()
for i in find_list:
    start, end = 0, n-1
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if i < num_list[mid]:
            end = mid - 1
        elif i > num_list[mid]:
            start = mid + 1
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')





'''
result = []
for i in range(f):
    if find_list[i] in num_list:
        result.append(1)
    else:
        result.append(0)

for i in range(len(result)):
    print(result[i], end=' ')
'''