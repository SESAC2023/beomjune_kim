n = int(input())

time = []
time += map(int, input().split(' '))
time.sort()
cnt = 0
j = 0
for i in range(len(time), 0, -1):
    cnt += i * time[j]
    j += 1

print(cnt)