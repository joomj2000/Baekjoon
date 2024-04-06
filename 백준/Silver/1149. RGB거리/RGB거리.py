import sys

N=int(sys.stdin.readline())
cost=[]
for i in range(N):
    R,G,B=map(int,sys.stdin.readline().split(' '))
    cost.append([R,G,B])

for n in range(1,N):
    cost[n][0]=min(cost[n-1][1]+cost[n][0],cost[n-1][2]+cost[n][0])
    cost[n][1] = min(cost[n - 1][0]+cost[n][1] , cost[n - 1][2]+cost[n][1] )
    cost[n][2] = min(cost[n - 1][0]+cost[n][2] , cost[n - 1][1]+cost[n][2] )

print(min(cost[N-1][0],cost[N-1][1],cost[N-1][2]))
