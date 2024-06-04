import sys

# 입력 받기
input = sys.stdin.read
data = input().split()

# 용액의 개수
N = int(data[0])

# 용액 리스트
water = list(map(int, data[1:]))

# 정렬된 용액 리스트
water.sort()

# 두 포인터 초기화
left, right = 0, N - 1

# 초기 값 설정
answer = float('inf')
result = [0, 0]

# 두 포인터가 겹치지 않을 때까지 반복
while left < right:
    mix = water[left] + water[right]

    # 현재 용액의 합이 0에 더 가까우면 갱신
    if abs(mix) < abs(answer):
        answer = mix
        result = [water[left], water[right]]

    # 합이 0이면 정답 출력 후 종료
    if mix == 0:
        break
    # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
    elif mix > 0:
        right -= 1
    # 합이 0보다 작으면 왼쪽 포인터를 오른쪽으로 이동
    else:
        left += 1

# 결과 출력
print(*sorted(result))
