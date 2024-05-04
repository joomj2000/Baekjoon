import sys

def Prim():
    dist=[1000000000]*N
    #print(dist)
    dist[0]=0
    for i in range(N):
        min_cost = 1000000000
        min_j = -1
        for j in range(N):
            if j not in visited and dist[j]<min_cost:
                min_cost=dist[j] #값 갱신
                min_j=j
        visited.add(min_j)
        #print(Graph)

        for k in range(N): #min_j로 이동해서 더 짧은 거리가 있는지 갱신
            if k not in visited and Graph[min_j][k]<dist[k]:
                dist[k]=Graph[min_j][k]


    return sum(dist)



N=int(sys.stdin.readline())
Graph=[]
visited=set()
for i in range(N):
    temp=list(map(int,sys.stdin.readline().strip().split()))
    #print(temp)
    Graph.append(temp)
print(Prim())
