import sys
input = sys.stdin.readline

n = int(input())

x = 0
y = 0

result = []
for x in range(2000):
    for y in range(2000):
        if 5*x + 3*y == n:
            result = [x, y]
            break

if result == []:
    print(-1)
else:
    print(sum(result))
