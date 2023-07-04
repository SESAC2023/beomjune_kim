import sys
from collections import deque
sys.setrecursionlimit(int(1e6))

input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

q = deque() #큐를 생성
q.append(r) #큐에 시작노드 넣기
visited[r] = True

answer = [0] * (n+1)
order = 1

while q:
    x = q.popleft()
    answer[x] = order
    order += 1
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            q.append(y)

for i in range(1, n+1):
    print(answer[i])


