import sys
sys.setrecursionlimit(100000)
from collections import deque

def DFS(Graph,x,y,N,H):
    if x<=-1 or x>=N or y <=-1 or y>=N:
        return False
    if Graph[x][y]>H:
        Graph[x][y]=-1
        DFS(Graph,x-1,y,N,H)
        DFS(Graph,x,y-1,N,H)
        DFS(Graph,x+1,y,N,H)
        DFS(Graph,x,y+1,N,H)
        return True
    return False

if __name__ == "__main__":
    N=int(sys.stdin.readline())

    Graph=[]
    for i in range(N):
        Graph.append(list(map(int,sys.stdin.readline().split(' '))))
        #Graph.append([])
    H=0
    max_height=max(map(max,Graph))
    #print(min_height)
    max_result=0
    while H<=max_height:
        #print(H)
        temp_Graph = [row[:] for row in Graph]
        #print(temp_Graph)
        result=0
        for i in range(N):
            for j in range(N):
                if DFS(temp_Graph,i,j,N,H)==True:
                    result+=1

        if max_result<result:
            max_result=result
        H+=1
    print(max_result)

    #print(Graph)
    # for _ in range(line):
    #     node1, node2 = map(int, sys.stdin.readline().split(' '))
    #     Graph[node1].append(node2)
    #     Graph[node2].append(node1)
    #
    # for i in range(node+1):
    #     Graph[i].sort()
    #
    # visited = [False] * (node + 1)
    # result=0
    # print(BFS(Graph,1,visited)-1)
    #
    #



