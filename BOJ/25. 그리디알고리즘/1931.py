n = int(input())
time_list = []
for i in range(n):
    time_list.append(list(map(int, input().split(' '))))

time_list.sort(key= lambda x: (x[1], x[0]))

cnt = 1
end = time_list[0][1]

for i in range(1, n):
    if time_list[i][0] >= end:
        cnt += 1
        end = time_list[i][1]

print(cnt)