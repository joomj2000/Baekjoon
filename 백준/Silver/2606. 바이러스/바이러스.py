import sys

def DFS():
    while(stack):
        current=stack.pop()
        global cnt
        if current not in visited:
            visited.append(current)
            cnt+=1
        for j in range(N+1):
            if adj_matrix[current][j] and j not in visited:
                stack.append(j)

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
cnt=0
adj_matrix=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    start,end=map(int,sys.stdin.readline().split())
    adj_matrix[start][end]=1
    adj_matrix[end][start]=1

stack=[1]
visited=[]
DFS()
print(cnt-1)