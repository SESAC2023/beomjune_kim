import sys
sys.setrecursionlimit(int(1e6))
input=sys.stdin.readline

n, m, r = map(int, input().split(' '))
order = 1

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
answer = [0] * (n+1)

for i in range(m):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

def dfs(x):
    global order
    visited[x] = True
    answer[x] = order
    order += 1
    for y in graph[x]:
        if not visited[y]:
            dfs(y)

dfs(r)

for i in range(1, n+1):
    print(answer[i])



