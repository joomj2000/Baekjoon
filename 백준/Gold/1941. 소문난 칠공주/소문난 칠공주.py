from itertools import combinations
from collections import deque
import sys
princess=[]
answer=0
for _ in range(5):
    temp=list(sys.stdin.readline().strip())
    princess.append(temp)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
positions = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(positions, 7))

def check_num(comb): #다솜파의 수를 체크하는 함수
    is_S = 0
    for x, y in comb:
        if princess[x][y] == 'S': #이다솜파라면 is_S증가
            is_S += 1
            
    if is_S>=4: #이다솜파의 수가 4이상이면 True반환
        return True
    return False

def check_adjacent(comb): #인접한지 구하는 함수
    visit = [False]*7
    q = deque()
    q.append(comb[0])
    visit[0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in comb:
                next = comb.index((nx, ny))
                if not visit[next]:
                    q.append((nx, ny))
                    visit[next] = True

    if False in visit:
        return False
    else:
        return True

for comb in combs:
    if check_num(comb): #다솜파의 수를 체크
        if check_adjacent(comb): #인접한지 검사
            answer += 1

print(answer)