import sys
from collections import deque

def move():
    queue=deque()
    queue.append(maps[0])
    visited.add(tuple(maps[0])) #방문처리
    while(queue):
        #print(queue)
        x,y=queue.popleft()
        visited.add((x,y)) #방문처리
        if x==maps[n+1][0] and y==maps[n+1][1]: #페스티벌 도착
            return "happy"
        for maps_x, maps_y in maps:
            #print(maps_x,maps_y)
            if (maps_x,maps_y) not in visited and abs(maps_x-x)+abs(maps_y-y)<=1000:
               # cola-=(abs(maps_x-x)+abs(maps_y-y))//50
                queue.append([maps_x,maps_y])
    return "sad"



dx=[-1000,1000,0,0]
dy=[0,0,1000,-1000]
t=int(sys.stdin.readline())
for _ in range(t):
    maps=[]
    visited=set()
    n=int(sys.stdin.readline())
    for _ in range(2+n):
        maps.append(list(map(int,sys.stdin.readline().split())))
    print(move())
