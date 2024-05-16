def solution(n, info):
    answer = [-1]  # 초기 값을 -1로 설정하여 이길 방법이 없는 경우를 처리
    max_diff = -1  # 초기 최대 점수 차이

    def backtracking(score, ry_score_list, nums):
        nonlocal max_diff, answer

        # 종료 조건
        if score == 11 or nums <= 0:
            if nums > 0:  # 남은 화살을 다 쏘지 못한 경우 처리
                ry_score_list[10] += nums

            ap_score, ry_score = 0, 0
            for i in range(11):
                if info[i] == 0 and ry_score_list[i] == 0:
                    continue
                if ry_score_list[i] > info[i]:
                    ry_score += 10 - i
                else:
                    ap_score += 10 - i

            if ry_score > ap_score:
                diff = ry_score - ap_score
                if diff > max_diff:
                    max_diff = diff
                    answer = ry_score_list[:]
                elif diff == max_diff:
                    if ry_score_list[::-1] > answer[::-1]:
                        answer = ry_score_list[:]

            if nums > 0:  # 남은 화살을 다 쏘지 못한 경우 원상 복구
                ry_score_list[10] -= nums
            return

        # 이길 경우
        if nums > info[score]:
            ry_score_list[score] = info[score] + 1
            backtracking(score + 1, ry_score_list, nums - (info[score] + 1))
            ry_score_list[score] = 0

        # 질 경우
        backtracking(score + 1, ry_score_list, nums)

    backtracking(0, [0] * 11, n)

    return answer


