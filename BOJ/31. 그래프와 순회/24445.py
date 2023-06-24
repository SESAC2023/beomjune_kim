import sys
from collections import deque
# 재귀 깊이 한도 해제
sys.setrecursionlimit(int(1e6))

# 빠르게 입력받기
input = sys.stdin.readline

#정점 개수 N 간선 개수 N 시작노드 R
n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) #양방향이기때문에 두개 다 넣어줘야함
    graph[v].append(u) #단방향이면 하나만 넣어주기

for i in range(1, n+1):
    graph[i].sort(reverse=True)


visited = [False] * (n + 1)
answer = [0] * (n + 1)

def bfs(x):
    global order
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()
        answer[v] = order
        order += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

order = 1

bfs(r)

for i in range(1, n+1):
    print(answer[i])

