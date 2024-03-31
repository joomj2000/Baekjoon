import sys


def DFS(Graph, V, visited):
    #visited[V] = 0
    for i in Graph[V]:
        if visited[i] == -1:
            visited[i] = visited[V] + 1
            DFS(Graph, i, visited)


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    target1, target2 = map(int, sys.stdin.readline().split())
    m = int(sys.stdin.readline())

    Graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        node1, node2 = map(int, sys.stdin.readline().split())
        Graph[node1].append(node2)
        Graph[node2].append(node1)

    visited = [-1] * (n + 1)
    visited[target1]=0
    DFS(Graph, target1, visited)
    print(visited[target2])
