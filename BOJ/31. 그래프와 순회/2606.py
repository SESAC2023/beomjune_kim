import sys
sys.setrecursionlimit(int(1e6))

input=sys.stdin.readline

n = int(input())
m = int(input())


graph = [[] for i in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)


def dfs(x):
    visited[x] = True
    #print(x) #현재 방문한 노드를 출력
    global cnt
    cnt += 1
    # 현재 노드 (x)의 인접노드를 확인하며
    for y in graph[x]:
        # 인접 노드인 y가 아직 방문하지 않은 노드라면
        if not visited[y]:
            dfs(y)

cnt = 0
dfs(1)
print(cnt-1)

