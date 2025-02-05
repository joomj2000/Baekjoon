from collections import deque
N,M=map(int,input().split())
tomato=[]
#tomato=[[0]*N for _ in range(M)]

mature=[(0,1),(1,0),(0,-1),(-1,0)]

visited=set()
queue=deque()
empty=0
# for i in range(N):
#     for j in range(M):
#         n=int(input())
#         if n==1:
#             queue.append((i,j))

for _ in range(M):
    tomato.append(list(map(int,input().split())))

#print(tomato)
for i in range(M):
    for j in range(N):
        #print(i,j)
        if tomato[i][j]==1:
            queue.append((i,j,0))
            visited.add((i,j))
        elif tomato[i][j]==-1:
            empty+=1


#
result_day=0

#not_mature=N*M-len(queue)
mature_count=0
while(queue):
    x,y,day=queue.popleft()
    mature_count+=1
    if day>result_day:
        result_day=day

    # day_cnt+=1
    # if day_cnt==last_day_cnt:
    #     day_cnt=0
    #     result_cnt+=1
    for a,b in mature:
        if x+a>=0 and x+a<M and y+b>=0 and y+b<N and (tomato[x+a][y+b]==0) and ((x+a,y+b) not in visited):
            tomato[x + a][y + b]=1
            queue.append((x+a,y+b,day+1))
            visited.add((x+a,y+b))


#print(not_mature, mature_count)
if empty+mature_count!=N*M:
    print(-1)
else:
    print(result_day)


'''
3 3
1 -1 -1 
-1 0 -1
-1 -1 1

'''