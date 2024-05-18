import sys
import heapq

def dijkstra(s):
    dist=[1000001]*(N+1)
    heap=[]
    visited=set()
    dist[s]=0
    heapq.heappush(heap,(0,s))
    while heap:
        wight,node1=heapq.heappop(heap)
        #print(wight,node1)
        for node2 in Graph[node1]:
            #print('node2=',node2)
            if node2 not in visited and dist[node2]>wight+1:
                dist[node2]=wight+1
                #print('dist',node2,dist[node2])
                heapq.heappush(heap,(dist[node2],node2))
                visited.add(node2)
    dist[0]=-1
    #print(dist)
    return max(dist)

N=int(sys.stdin.readline())
Graph=[[]for _ in range(N+1)]
result=[]
while True:
    v1,v2=map(int,sys.stdin.readline().split())
    if v1==-1 and v2==-1:
        break
    Graph[v1].append(v2)
    Graph[v2].append(v1)

for i in range(1,N+1):
    result.append(dijkstra(i))

min_result=min(result)
print(min_result,result.count(min_result))
for j in range(len(result)):
   if result[j]==min_result:
       print(j+1,end=' ')


# print(result)