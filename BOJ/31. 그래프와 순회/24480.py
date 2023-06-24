import sys
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

visited = [False] * (n+1)

answer = [0] * (n + 1)

def dfs(x):
    global order
    visited[x] = True
    # print(x) #현재 방문한 노드를 출력
    answer[x] = order
    order += 1
    # 현재 노드 (x)의 인접노드를 확인하며
    for y in graph[x]:
        # 인접 노드인 y가 아직 방문하지 않은 노드라면
        if not visited[y]:
            dfs(y)
order = 1
dfs(r)

for i in range(1, n+1):
    print(answer[i])




