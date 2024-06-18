'''
n!크기의 1차원 배열 선언 -1로 초기화 
k는 1 부터 시작해서 1씩 증가하며 다음숫자를 0에서 시작하여 이전 숫자 +k에 수를 적음
만약 이전숫자+k가 범위를 벗어나는 경우 배열의 끝까지 수를 채움
수가 끝까지 다 썼을때 해당 인덱스 - n으로 시작해서 n에서 1씩 빠지며 숫자채우기
해당수가 인덱스 범위 밖이거나 써진 값이 -1이 아닐때 n에서 1씩 감소하며 숫자 채우기
다시 2부터 1씩 증가하며 반복..

'''
def solution(n):
    N = n * (n + 1) // 2
    answer = [-1] * N
    directions = [(1, 0), (0, 1), (-1, -1)]  # 아래, 오른쪽, 위
    direction_index = 0
    x, y = 0, 0
    number = 1
    answer[0] = number
    number += 1

    def get_index(x, y):
        return x * (x + 1) // 2 + y

    while number <= N:
        dx, dy = directions[direction_index]
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny <= nx and answer[get_index(nx, ny)] == -1:
            x, y = nx, ny
        else:
            direction_index = (direction_index + 1) % 3
            dx, dy = directions[direction_index]
            x, y = x + dx, y + dy
        
        answer[get_index(x, y)] = number
        number += 1

    return answer
