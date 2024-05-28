from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    applicant = defaultdict(list)

    # 지원자 정보를 미리 처리하여 조합 생성
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for n in range(5):
            for comb in combinations(range(4), n):
                t_c = conditions[:]
                for idx in comb:
                    t_c[idx] = '-'
                key = ''.join(t_c)
                applicant[key].append(score)

    #
    # 각 키에 대해 점수를 정렬하여 저장
    for key in applicant.keys():
        applicant[key].sort()

    # 쿼리 처리
    for q in query:
        q = q.replace(" and ", " ")
        conditions = q.split()
        key = ''.join(conditions[:-1])
        target_score = int(conditions[-1])

        # 해당 조건에 맞는 지원자 점수 리스트를 가져옴
        if key in applicant:
            scores = applicant[key]

            # 이진 검색을 통해 target_score 이상인 점수의 시작 인덱스 찾기
            idx = bisect_left(scores, target_score)
            count = len(scores) - idx
            answer.append(count)
        else:
            answer.append(0)

    return answer
