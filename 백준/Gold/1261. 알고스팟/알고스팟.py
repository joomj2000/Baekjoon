import sys
from collections import deque


def BFS():
    queue=deque()
    queue.append((0,0,0))
    while queue:
        #print(queue)
        x,y,b=queue.popleft()
        #print(b)
        #visited[x][y]=b
        # if b>B:
        #     return min(result)
        if x==M-1 and y==N-1:
            result.append(b)

        # if x>=M or y>=N:
        #     continue

        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            if 0<=n_x<M and 0<=n_y<N:
                if maps[n_x][n_y]==1 and b+1<visited[n_x][n_y]:
                    queue.append((n_x,n_y,b+1))
                    visited[n_x][n_y]=b+1
                elif maps[n_x][n_y] == 0 and b<visited[n_x][n_y]:
                    queue.append((n_x, n_y, b))
                    visited[n_x][n_y] = b

    return 0


N,M=map(int,sys.stdin.readline().split())
maps=[]
dx=[1,-1,0,0]
dy=[0,0,-1,1]
result=[]
visited=[]
for i in range(M):
    maps.append(list(map(int,sys.stdin.readline().strip())))
    visited.append([200]*N)
B=0
#print(visited)
for i in range(M):
    B+=maps[i].count(1)

#print(B)
BFS()
if N==M==1:
    print(maps[0][0])
else:
    print(visited[M-1][N-1])
#print(visited)
