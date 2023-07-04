n, m = map(int, input().split(' '))
ans = []
cnt = 0
for i in range(n):
    ans.append(int(input()))

ans.sort(reverse=True)
for i in ans:
    cnt += m // i
    m %= i

print(cnt)