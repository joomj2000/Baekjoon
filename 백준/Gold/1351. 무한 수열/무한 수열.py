import sys

def DFS(n):
    if n not in dp:
        dp[n] = DFS(n // P) + DFS(n // Q)
    return dp[n]


N, P, Q = map(int, sys.stdin.readline().split())
#print(N,P,Q)
dp = {0: 1}

print(DFS(N))