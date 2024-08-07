# 그래프의 각 인덱스는 보드의 각 칸 
# 값은 이동할 수 있는 다음 칸(들)
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

# 각 칸의 점수를 저장한 리스트.
score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

# 주사위 10번 던진 값을 입력받음.
dice = list(map(int, input().split()))

# 최대 점수를 저장할 변수.
answer = 0

def backtracking(depth, result, horses):
    """
    주어진 depth에서 말의 위치를 변경하며 최대 점수를 계산하는 함수.
    depth: 현재 몇 번째 주사위를 던졌는지 (0~9)
    result: 현재까지의 점수 합계
    horses: 네 마리 말의 현재 위치
    """
    global answer
    
    # 기저 조건: 10번의 주사위 던지기가 끝난 경우
    if depth == 10:
        answer = max(answer, result)  # 최대 점수를 업데이트
        return

    # 네 마리 말 각각에 대해 이동을 시도
    for i in range(4):
        x = horses[i]  # 현재 말의 위치 저장

        # 현재 위치가 2갈래 길(10, 20, 30)인 경우
        if len(graph[x]) == 2:
            x = graph[x][1]  # 파란 길로 진입
        else:
            x = graph[x][0]  # 빨간 길로 진입

        # 주사위 값 만큼 이동 (이미 1칸 이동했으므로 1 덜 이동)
        for _ in range(1, dice[depth]):
            x = graph[x][0]

        # 목적지에 도착했거나, 아직 목적지가 아니고 다른 말과 겹치지 않는 경우
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  # 이전 말의 위치 저장
            horses[i] = x  # 현재 말 위치 갱신

            # 다음 depth로 이동하며 결과 점수 갱신
            backtracking(depth + 1, result + score[x], horses)

            # 원래 위치로 복원
            horses[i] = before

# 초기 호출: 깊이 0, 점수 0, 모든 말의 위치 0에서 시작
backtracking(0, 0, [0, 0, 0, 0])

# 최종 결과 출력
print(answer)
