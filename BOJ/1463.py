import sys
input=sys.stdin.readline
sys.setrecursionlimit((int(1e5)))

d = [0] * (int(1e6)+1)

def dp(x):
    # 1 종료조건
    if x == 1:
        return 0
    if d[x] != 0: #x에 대해 계산한적이 있다면
        return d[x]
    #(2) 점화식에 따라 계산 => d[x] =
    current = dp(x - 1)
    if x % 3 == 0:
        current = min(current, dp(x // 3))
    if x % 2 == 0:
        current = min(current, dp(x // 2))
    # (3) 계산한 결과를 DP 테이블에 기록하고, 반환
    d[x] = current
    return d[x]

n = int(input())
print(dp(n))

