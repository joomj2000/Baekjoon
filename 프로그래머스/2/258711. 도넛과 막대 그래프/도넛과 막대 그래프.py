'''
나가는 방향의 간선이 0인 노드를 찾으면 막대 그래프 +1.
나가는 방향의 간선이 2인 노드를 찾으면 8자 그래프 +1.

추가된 노드에서 나가는 방향 간선 개수 - 막대 그래프 개수 - 8자 그래프 개수는 도넛 그래프 개수.

'''
from collections import defaultdict
from collections import deque 
def solution(edges):
    node = defaultdict(lambda: [0, 0])  # [in_count, out_count]
    set_edge=set()
    for edge in edges:
        node[edge[0]][1]+=1
        node[edge[1]][0]+=1
        set_edge.add(edge[0])
        set_edge.add(edge[1])

        
    for i in set_edge: #더해진 노드 찾기 
        if node[i][0]==0 and node[i][1]>=2:
            total_graph=node[i][1]
            added_node=i
            break
    
    #print(node)
    for edge in edges:
        if edge[0]==added_node:
            node[edge[1]][0]-=1
    #print(node)
                      
    answer = [added_node,0,0,0]
    for n1,value in node.items():
        if n1==added_node or n1==0:
            continue
        if value[1]==0:
            answer[2]+=1
        elif value[1]==2:
            answer[3]+=1

    print(total_graph)
    answer[1]=total_graph-(answer[2]+answer[3])            

    
    return answer