from itertools import permutations

def solution(n, weak, dist):
    # weak 리스트를 두 배로 확장하여 원형 문제를 선형 문제로 변환
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    answer = len(dist) + 1  # 답의 초기값을 dist의 길이보다 1 큰 값으로 설정
    
    # weak의 모든 시작점에 대해 탐색
    for start in range(length):
        # 친구를 배치하는 모든 순열에 대해 탐색
        for friends in permutations(dist):
            count = 1  # 배치된 친구 수
            position = weak[start] + friends[count - 1]  # 첫 번째 친구가 점검할 수 있는 마지막 위치
            
            for index in range(start, start + length):
                if position < weak[index]:  # 점검할 수 있는 위치를 넘어갔다면
                    count += 1  # 새로운 친구를 추가
                    if count > len(dist):  # 친구가 더 이상 없으면 종료
                        break
                    position = weak[index] + friends[count - 1]  # 새로운 친구가 점검할 수 있는 마지막 위치
            answer = min(answer, count)  # 최소값 갱신
    
    if answer > len(dist):
        return -1
    return answer
