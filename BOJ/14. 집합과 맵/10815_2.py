import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split(' ')))

f = int(input())
find_list = list(map(int, input().split(' ')))

num_dict = {}
for i in range(len(num_list)):
    num_dict[num_list[i]] = 0

for j in find_list:
    if j not in num_dict:
        print(0, end= ' ')
    else:
        print(1, end= ' ')