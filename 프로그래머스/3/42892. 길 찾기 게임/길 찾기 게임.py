import sys
sys.setrecursionlimit(10000)

def solution(nodeinfo):
    from collections import defaultdict
    import sys
    sys.setrecursionlimit(10000)
    
    answer = [[], []]
    
    # 노드 정보를 (x, y, index) 형태로 정리
    for i in range(len(nodeinfo)):
        nodeinfo[i] = nodeinfo[i] + [i + 1]
    
    # y값 기준으로 정렬 (높이순 정렬), y가 같으면 x 값 기준 정렬
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    
    left = [-1] * (len(nodeinfo) + 1)
    right = [-1] * (len(nodeinfo) + 1)
    
    # 그래프 만들기
    def make_graph(start, nodes):
        x, y, index = start
        nodes.remove(start)
        
        left_subtree = [node for node in nodes if node[0] < x]
        right_subtree = [node for node in nodes if node[0] > x]
        
        if left_subtree:
            left_child = left_subtree[0]
            left[index] = left_child[2]
            make_graph(left_child, left_subtree)
        
        if right_subtree:
            right_child = right_subtree[0]
            right[index] = right_child[2]
            make_graph(right_child, right_subtree)
    
    make_graph(nodeinfo[0], nodeinfo.copy())
    
    # 그래프 순회하기 (전위 순회 & 후위 순회)
    def preorder(node):
        if node != -1:
            answer[0].append(node)  # 전위 순회
            preorder(left[node])
            preorder(right[node])
    
    def postorder(node):
        if node != -1:
            postorder(left[node])
            postorder(right[node])
            answer[1].append(node)  # 후위 순회
    
    root = nodeinfo[0][2]
    preorder(root)
    postorder(root)
    
    return answer
