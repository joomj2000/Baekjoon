import sys
sys.setrecursionlimit(10**8)

def DFS(Graph,V,visited):
    #visited[V]=1
    for i in Graph[V]:
        if visited[i]==0: #부모노드가 정의되어있지 않은경우
            visited[i]=V #탐색을 시작한 노드로 부모노드 정의
            DFS(Graph,i,visited)
#
# def BFS(Graph,start,visited):
#     for i in Graph[V]:
#         if visited[]

if __name__ == "__main__":
    n = int(sys.stdin.readline()) #n은 노드의 수
    Graph=[]
    for _ in range(n+1):
        Graph.append([])

    for _ in range(n-1):
        node1,node2=map(int,sys.stdin.readline().split(' '))
        Graph[node1].append(node2)
        Graph[node2].append(node1)
    visited=[0]*(n+1)
    DFS(Graph,1,visited)
    for i in visited[2:]:
        print(i)
