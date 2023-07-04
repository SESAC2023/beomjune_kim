import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for z in range(j + 1, N):
            card_sum = nums[i] + nums[j] + nums[z]
            if card_sum <= M:
                result = max(result, card_sum)

print(result)