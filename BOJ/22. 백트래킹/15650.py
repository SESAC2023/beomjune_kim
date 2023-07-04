import sys
input=sys.stdin.readline

n, m = map(int, input().split(' '))
s = []
visited = [False] * (n+1)

k = 0
def dfs(start):
    global k
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)