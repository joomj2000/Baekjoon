def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])  # 우선 구간 종료 기준으로 sort 후
    p = -30001  # 포인터 초기화

    for route in routes:
        if p < route[0]:
            p = route[1]
            answer += 1

    return answer