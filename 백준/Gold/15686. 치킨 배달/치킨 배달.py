import sys
from itertools import combinations


N,M=map(int,sys.stdin.readline().split())
home=[]
chicken=[]
for i in range(N):
    temp=list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if temp[j]==1:
            home.append((i,j))
        if temp[j]==2:
            chicken.append((i,j))

combs=list(combinations(chicken,M))
#print(combs)

chicken_distance=[]
answer=10000


#print(home, chicken)

for comb in combs:
    chicken_distance = []
    for i in range(len(home)):
        distance = 10000
        for c in comb:
            result= abs(c[0]-home[i][0])+abs(c[1]-home[i][1])
            distance=min(distance,result)
        chicken_distance.append(distance)
    #print(chicken_distance)
    answer=min(answer,sum(chicken_distance))

print(answer)