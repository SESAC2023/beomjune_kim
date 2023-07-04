import sys
from collections import deque
sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False] * (n + 1)

graph2 = [[] for i in range(n+1)]
visited2 = [False] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, x, visited):
    visited[x] = True
    print(x, end=' ')
    for y in graph[x]:
        # 인접 노드인 y가 아직 방문하지 않은 노드라면
        if not visited[y]:
            dfs(graph, y, visited)

def bfs(graph, x, visited):
    queue = deque([x])
    visited[x] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



dfs(graph, r, visited)
print()
bfs(graph2, r, visited2)