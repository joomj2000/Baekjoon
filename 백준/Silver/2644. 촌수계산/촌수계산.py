import sys
from collections import deque

def BFS(Graph, start):
    visited = [-1] * (n + 1)
    queue=deque([start])
    visited[start]=0
    while queue:
        V=queue.popleft()
        for i in Graph[V]:
            if visited[i]==-1:
                visited[i]=visited[V]+1
                queue.append(i)
    return visited


if __name__ == "__main__":
    n=int(sys.stdin.readline())
    target1,target2=map(int,sys.stdin.readline().split(' '))
    m = int(sys.stdin.readline())
    Graph=[]
    for _ in range(n+1):
        Graph.append([])
    for _ in range(m):
        node1, node2 = map(int, sys.stdin.readline().split(' '))
        Graph[node1].append(node2)
        Graph[node2].append(node1)

    print(BFS(Graph,target1)[target2])
    #print(result)