import sys
from collections import deque

def find_road():
    queue=deque()
    queue.append((1,0))
    while(queue):
        #print(queue)
        current_location,tries=queue.popleft()
        visited.add(current_location)
        #print(current_location)
        if current_location>=100 :
            print(tries)
            break

        ladder_or_snakes=[]
        for num_ladders in ladders:
            if current_location<num_ladders[0]<=current_location+6:
                x1,y1=num_ladders
                #print('ladders=',ladders[num_ladders])
                #num_ladders+=1
                ladder_or_snakes.append(x1)
                #result+=1
                if y1 not in visited:
                    #visited.add(x1)
                    queue.append((y1,tries+1))

        for num_snakes in snakes:
            if current_location< num_snakes[0]<=current_location+6:
                x2,y2=num_snakes
                #print('s',current_location,tries)
                #num_snakes+=1
                #result+=1
                ladder_or_snakes.append(x2)
                if y2 not in visited:
                    #visited.add(x2)
                    #print(y2,tries+1)
                    queue.append((y2,tries+1))

        cnt=6 #사다리나 뱀을 타지 않고 최대로 이동
        while(cnt>0):
            #if current_location+cnt
            if current_location+cnt not in ladder_or_snakes:
                if current_location+cnt>=100:
                    print(tries+1)
                    return
                if current_location+cnt not in visited:
                    queue.append((current_location+cnt,tries+1))

            cnt-=1

N,M=map(int,sys.stdin.readline().split())
result=0
ladders=[]
snakes=[]
visited=set()
for _ in range(N): # 사다리 리스트
    ladders.append(list(map(int,sys.stdin.readline().split())))
for _ in range(M): # 뱀 리스트
    snakes.append(list(map(int,sys.stdin.readline().split())))

ladders.sort()
#ladders=deque(ladders)
snakes.sort()
#snakes=deque(snakes)
find_road()
#print(visited)