import sys
sys.setrecursionlimit(int(1e6))

input=sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

