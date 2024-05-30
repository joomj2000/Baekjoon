import sys
from collections import deque
# def BFS(node):
#     queue=deque()
#     queue.append(node)
#     visited_1.add(node)
#     is_two=False
#     while queue:
#         #print(queue)
#         v=queue.popleft()
#         for child in Graph[v]:
#             if is_two==False:
#                 if child not in visited_1:
#                     if child not in visited_2:
#                         visited_2.add(child)
#                         queue.append(child)
#                         is_two=True
#                 else:
#                     return "NO"
#             else:
#                 if child not in visited_2:
#                     if child not in visited_1:
#                         visited_1.add(child)
#                         queue.append(child)
#                         is_two=False
#                 else:
#                     return "NO"
#     return "YES"

def BFS(node):
    queue=deque()
    queue.append(node)
    color[node]=1
    #visited.add(node)
    is_two=False
    while queue:
        #print(queue)
        v=queue.popleft()
        for child in Graph[v]:
            if color[child]==0:
                #visited.add(child)
                color[child]=color[v]*-1
                queue.append(child)
            else:
                if color[child]==color[v]:
                    return "NO"
    return "YES"



K=int(sys.stdin.readline())
for _ in range(K):
    V,E=map(int,sys.stdin.readline().split())
    Graph=[[] for _ in range(V+1)]
    color=[0]*(V+1)
    visited_1 = set()
    visited_2=set()
    for _ in range(E):
        v1,v2=map(int,sys.stdin.readline().split())
        Graph[v1].append(v2)
        Graph[v2].append(v1)
    #print(Graph)

    for i in range(1,V+1):
        if color[i]==0:
            result=BFS(i)
            if result=="NO":
                break
    print(result)