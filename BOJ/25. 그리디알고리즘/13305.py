import sys
input=sys.stdin.readline

n = int(input())
dist = list(map(int, input().split(' ')))
cost = list(map(int, input().split(' ')))

res = 0
c = cost[0]
for i in range(n-1):
    if c > cost[i]:
        c = cost[i]
    res += c * dist[i]

print(res)