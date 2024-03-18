from collections import Counter

N = int(input())
card = list(map(int, input().split()))

M = int(input())
target_card = list(map(int, input().split()))

card_count = Counter(card)# 카드의 등장 횟수를 계산하여 딕셔너리로 저장

for num in target_card: # 타겟 카드의 등장 횟수를 조회하여 출력
    print(card_count[num], end=' ')
