import sys
from collections import deque

def action(p, deque): #언어 AC 실행
    cnt = 0
    for i in p:
        if i == 'R': #뒤집기 일때 cnt증가
            cnt += 1
        elif i == 'D': #버리기 일때
            if len(deque) == 0: #deque가 비어있으면 에러 출력후 return
                print('error')
                return
            if cnt % 2 == 0: # 뒤집어져 있지 않은 상태일때 첫번째 수 버리기
                deque.popleft()
            else: # 뒤집어져 있는 상태일때 마지막 수 버리기
                deque.pop()

    # 출력형식에 맞게 출력
    print('[', end='')
    while len(deque) > 1:
        if cnt % 2 == 0:
            print(deque.popleft(), end=',')
        else:
            print(deque.pop(), end=',')
    if len(deque) == 1:
        print(deque.pop(), end='')
    print(']')


if __name__ == "__main__":
    T = int(sys.stdin.readline()) #테스트 케이스 개수
    deque = deque([]) #deque 선언

    for _ in range(T):
        p = sys.stdin.readline().strip() #수행할 함수 입력
        n = int(sys.stdin.readline())
        number = sys.stdin.readline().strip()[1:-1] #대괄호로 둘러싸인 입력일때 값만 추출
        if n != 0:
            number_list = list(map(int, number.split(',')))#문자열로 입력받은 number을 ','로 split하여 number_list에 넣음
            deque.extend(number_list) #number_list의 모슨요소를 덱에 추가

        action(p, deque)#언어 AC 실행
