import sys
from itertools import combinations

def back_tracking(round):
    global answer
    if round==15:
        answer=1
        for i in res:
            if i.count(0)!=3:
                answer=0
                break
        return
    t1,t2=game[round]
    for x,y in ((0,2),(1,1),(2,0)):
        if res[t1][x]>0 and res[t2][y]>0:
            res[t1][x]-=1
            res[t2][y]-=1
            back_tracking(round+1)
            res[t1][x]+=1
            res[t2][y]+=1

result=[]
game=list(combinations(range(6),2))
for _ in range(4):
    temp=list(map(int,sys.stdin.readline().split()))
    res=[temp[i:i+3] for i in range(0,16,3)]
    answer=0
    back_tracking(0)
    result.append(answer)
print(*result)


