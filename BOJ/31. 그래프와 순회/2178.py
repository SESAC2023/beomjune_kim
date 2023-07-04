
import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split(' '))

graph = []

for i in range(n):
    line = input().strip()
    current = []
    for x in line:
        current.append(int(x))
    graph.append(current)

print(graph)

visited = [[0] * m for i in range(n)]
distance = [[0] * m for i in range(n)]

q = deque()
q.append((0,0))
visited[0][0] = True

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny > m:
            continue
        if graph[nx][ny] == 0:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))
            distance[nx][ny] = distance[x][y] + 1

print(distance[n-1][m-1])