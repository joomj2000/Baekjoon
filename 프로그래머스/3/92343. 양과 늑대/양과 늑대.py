def solution(info, edges):
    visited = [0] * len(info)  # 방문 상태를 기록하는 리스트, 초기에는 모두 방문하지 않음 (0)
    answer = []  # 가능한 경로에서 양의 수를 저장할 리스트
    
    def dfs(sheep, wolf):
        # 현재 양의 수가 늑대의 수보다 많으면
        if sheep > wolf:
            answer.append(sheep)  # 현재 양의 수를 answer에 추가
        else:
            return  # 양의 수가 늑대의 수보다 적거나 같으면 종료
        
        # 모든 간선을 순회
        for p, c in edges:
            # 부모 노드가 방문되었고, 자식 노드가 방문되지 않았을 때
            if visited[p] and not visited[c]:
                visited[c] = 1  # 자식 노드를 방문 상태로 설정
                if info[c] == 0:  # 자식 노드가 양이면
                    dfs(sheep + 1, wolf)  # 양의 수를 증가시키고 dfs 호출
                else:  # 자식 노드가 늑대이면
                    dfs(sheep, wolf + 1)  # 늑대의 수를 증가시키고 dfs 호출
                visited[c] = 0  # 자식 노드를 미방문 상태로 되돌림

    # 루트 노드부터 시작
    visited[0] = 1  # 루트 노드를 방문 상태로 설정
    dfs(1, 0)  # 루트 노드는 항상 양이므로, 양 1마리와 늑대 0마리로 dfs 시작
    
    # 가능한 경로에서 최대 양의 수를 반환
    return max(answer)
