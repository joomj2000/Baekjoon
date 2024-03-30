import sys
from collections import deque
def DFS(Graph, V, visited,result):
    visited[V] =True
    result+=1
    #print(V,end=' ')
    for i in Graph[V]:
        if not visited[i]:
            DFS(Graph,i,visited,result)
    return result

def BFS(Graph, start, visited):
    queue=deque([start])
    visited[start]=True
    result=0
    while queue:
        result+=1
        V=queue.popleft()
        #print(V,end=' ')
        for i in Graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
    return result

if __name__ == "__main__":
    node=int(sys.stdin.readline())
    line=int(sys.stdin.readline())
    Graph=[]
    for _ in range(node+1):
        Graph.append([])

    for _ in range(line):
        node1, node2 = map(int, sys.stdin.readline().split(' '))
        Graph[node1].append(node2)
        Graph[node2].append(node1)

    for i in range(node+1):
        Graph[i].sort()

    visited = [False] * (node + 1)
    result=0
    print(BFS(Graph,1,visited)-1)
    #result=DFS(Graph,1,visited,result)
    #print(result)
    # print('')
    # visited = [False] * (N + 1)
    # BFS(Graph,V,visited)




