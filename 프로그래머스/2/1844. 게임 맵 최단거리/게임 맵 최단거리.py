from collections import deque
def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    distance=[[10001]*m for _ in range(n)]
    queue=deque()
    queue.append((0,0,0))
    D=0
    while queue:
        x,y,d=queue.popleft()
        if x<0 or y<0 or x>=n or y>=m or maps[x][y]==0:
            continue
        distance[x][y]=min(distance[x][y],d+1)
        D=distance[x][y]
        maps[x][y]=0
        queue.append((x+1,y,D))
        queue.append((x,y+1,D))
        queue.append((x-1,y,D))
        queue.append((x,y-1,D))
    
    if distance[n-1][m-1]==10001:
        answer=-1
    else:
        answer=distance[n-1][m-1]
    
    return answer