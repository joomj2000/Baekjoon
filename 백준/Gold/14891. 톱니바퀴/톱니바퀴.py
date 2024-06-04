import sys
from collections import deque
sys.setrecursionlimit(1000000000)

def rotation(num,d):
    #print(num,visited,d)
    visited.add(num)
    if num-1>=0 and num-1 not in visited:
        if Gear[num-1][2]!=Gear[num][6]:
            rotation(num-1,d*-1)
    if num+1<4 and num+1 not in visited:
        if Gear[num+1][6]!=Gear[num][2]:
            rotation(num + 1, d * -1)
    if d==1:
        #print('d',Gear[num])
        n=Gear[num].pop()
        Gear[num].appendleft(n)
       # print('D',Gear[num])
    else:
        n=Gear[num].popleft()
        Gear[num].append(n)

Gear=[]
for i in range(4):
    Gear.append(deque(map(int,sys.stdin.readline().strip())))
# one=list(map(int,sys.stdin.readline().split()))
# two=list(map(int,sys.stdin.readline().split()))
# three=list(map(int,sys.stdin.readline().split()))
# four=list(map(int,sys.stdin.readline().split()))
K=int(sys.stdin.readline())
#print(Gear[0])
for _ in range(K):
    visited=set()
    num,direction=map(int,sys.stdin.readline().split())
    rotation(num-1,direction)
   # print(Gear)

result=0
if Gear[0][0]==1:
    result+=1
if Gear[1][0]==1:
    result+=2
if Gear[2][0]==1:
    result+=4
if Gear[3][0]==1:
    result+=8

print(result)