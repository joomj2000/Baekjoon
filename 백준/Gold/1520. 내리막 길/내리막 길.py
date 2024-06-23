import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

dp = [[-1] * N for _ in range(M)]  # 메모이제이션을 위한 DP 테이블

def dfs(x, y):
    if x == M - 1 and y == N - 1:  # 도착점에 도달한 경우
        return 1
    if dp[x][y] != -1:  # 이미 방문한 적이 있는 경우
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[x][y]:
            dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]

print(dfs(0, 0))
