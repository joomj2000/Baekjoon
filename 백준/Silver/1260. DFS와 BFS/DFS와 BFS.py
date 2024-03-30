import sys
from collections import deque
def DFS(Graph, V, visited):
    visited[V] =True
    print(V,end=' ')
    for i in Graph[V]:
        if not visited[i]:
            DFS(Graph,i,visited)

def BFS(Graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        V=queue.popleft()
        print(V,end=' ')
        for i in Graph[V]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

if __name__ == "__main__":
    N,M,V =map(int,sys.stdin.readline().split(' '))
    Graph=[]
    for _ in range(N+1):
        Graph.append([])

    for _ in range(M):
        node1, node2 = map(int, sys.stdin.readline().split(' '))
        Graph[node1].append(node2)
        Graph[node2].append(node1)

    for i in range(N+1):
        Graph[i].sort()

    visited = [False] * (N + 1)
    DFS(Graph,V,visited)
    print('')
    visited = [False] * (N + 1)
    BFS(Graph,V,visited)
