import sys

N,M=map(int,sys.stdin.readline().split())
byte=[0]+list(map(int,sys.stdin.readline().split()))
cost=[0]+list(map(int,sys.stdin.readline().split()))

DP=[[0]*(sum(cost)+1) for _ in range(N+1)]
#DP.append([0 for _ in range(N)])
result=10e9
for i in range(N+1):
    for j in range(sum(cost)+1):

        if cost[i]>j:
            DP[i][j]=DP[i-1][j]

        else:
            #DP[i][j]=DP[i-1][j]+byte
            DP[i][j]=max(DP[i-1][j-cost[i]]+byte[i],DP[i-1][j])

        if M<=DP[i][j]:
            result=min(result,j)
#print(DP)
print(result)