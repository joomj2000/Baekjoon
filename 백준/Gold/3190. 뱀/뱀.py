import sys
from collections import deque


N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
apple=[]
turn=deque()
snake=deque()
go=[(0,1),(1,0),(0,-1),(-1,0)] # 이동 방향 오른쪽, 아래, 왼쪽, 위
snake.append((1,1))
for _ in range(K): #사과 좌표 저장
    x,y=map(int,sys.stdin.readline().split())
    apple.append((x,y))

L= int(sys.stdin.readline())
i=0
for _ in range(L): #사과 좌표 저장
    x,y=map(str,sys.stdin.readline().split())
    turn.append((int(x),y))

#print(apple, turn)
time=0
next_turn=turn.popleft()
while True:
    #print(time, snake)
    time+=1
    x, y = snake[-1]  # snake의 머리 좌표
    x += go[i][0]
    y += go[i][1]

    # 종료 조건
    if (x, y) in snake:  # 머리가 뱀에 닿는 경우
        #print('snake', snake)
        print(time)
        break

    if (x,y) not in apple: # 사과가 아니라면 꼬리 이동
        #print('snake=',snake)
        #print('apple')
        snake.popleft()
        #print('snake=', snake)
    else :
        for a in range(len(apple)):
            if (x,y)==apple[a]:
                apple.pop(a)
                break

    snake.append((x, y))

    if x>N or x<=0 or y>N or y<=0 : #맵밖으로 나가는 경우
        #print('x,y',x,y)
        #print(snake)
        print(time)
        break


    if next_turn!=0 and time ==next_turn[0]:
        if next_turn[1]=='D':
            i=(i+1)%4
            #print(i)
        else:
            i=(i-1)%4
        #print(next_turn[1],i)
        if len(turn)!=0:
            next_turn=turn.popleft()
        else:
            next_turn=0
        #print(time)




