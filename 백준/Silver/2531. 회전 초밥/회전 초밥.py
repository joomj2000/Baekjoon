import sys
from collections import deque
N,d,k,c=map(int,sys.stdin.readline().split())
sushi_list=[]
for _ in range(N):
    sushi_list.append(int(sys.stdin.readline().strip()))

end=0
max_sushi=0
cnt=0
eat=deque()

for i in range(k-1):
    eat.append(sushi_list[i])

for j in range(N):
    eat.append(sushi_list[(j + k - 1) % N])
    #print(j,eat)
    cnt=0
    if c not in eat:
        cnt=1
    if max_sushi<len(set(eat))+cnt:
        max_sushi=len(set(eat))+cnt
        #print('max',eat)
    eat.popleft()
    #eat.discard(sushi_list[(j+k-1)%N])



# for i in range(N):
#     cnt=0
#     eat=set()
#     eat.add(sushi_list[i])
#
#     K=k
#     end = (i + 1) % N
#     while K>1:
#         eat.add(sushi_list[end])
#         #print(i,end)
#         #print(eat)
#         end=(end+1)%N
#         K-=1
#
#     if c not in eat:
#         cnt=1
#     if max_sushi<len(eat)+cnt:
#         #print(eat)
#         max_sushi=len(eat)+cnt
print(max_sushi)