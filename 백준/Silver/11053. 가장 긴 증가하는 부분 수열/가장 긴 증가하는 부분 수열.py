import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n+1)

for i in range(len(sequence)):
    for j in range(i): #이전까지의 수가 현재보다 작으면 dp테이블 값 조회
        if sequence[j] < sequence[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
