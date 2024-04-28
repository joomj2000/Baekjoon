import sys
from collections import deque

N,S=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
#print(num)
min_len=N+1
end=0
#result=deque([])
result=0

for start in range(N):
    #cnt=0
    # if end>=N:
    #     break
    while(end<N and result<S):
        result+=num[end]
        #print(start,end,result)
        #cnt+=1
        end+=1
    #print(result)
    #result.append(num[end])
    # if result<S:
    #     print(0)
    #     exit()
    if result>=S and min_len>end-start:
        min_len= end - start
    result-=num[start]
    #result.popleft()

if min_len>N:
    print(0)
else:
    print(min_len)
