'''
6 4
0100
1110
1000
0000
0111
0000
'''
import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
maps=[]
answer=-1
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
for _ in range(n):
    maps.append(list(map(int,sys.stdin.readline().strip())))
visited=set()
queue = deque()
queue.append((0, 0, 0, 0))
#visited.add((0,0,0))
while queue:  # 큐가 빌때까지 반복
    x, y, is_break, cnt = queue.popleft()
    #print(visited)
    if x >= n or x < 0 or y >= m or y < 0 :
        continue
    if x == n - 1 and y == m - 1:  # 끝에 도달
        answer = cnt+1
        break
    cnt += 1
    for j in range(4):  # 사방탐색(queue append)
        nx=x + dx[j]
        ny= y + dy[j]
        if n > nx >= 0 and m > ny >= 0:
            if maps[nx][ny]!= 0 :  # 벽인 경우
                if is_break==0 and (nx,ny,1) not in visited: #벽을 부술수 있는 경우
                    queue.append((nx, ny, is_break+1, cnt))
                    visited.add((nx, ny, is_break+1))  # 방문처리
            elif (nx,ny,is_break) not in visited: #벽이 아닌경우
                queue.append((nx, ny, is_break, cnt))
                visited.add((nx, ny, is_break))  # 방문처리

print(answer)