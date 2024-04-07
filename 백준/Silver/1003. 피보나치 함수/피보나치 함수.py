import sys

d=[0]*41
d[1]=1
d[2]=1
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(3,N+1):
        d[i]=d[i-1]+d[i-2]
    if N==0:
        print('1',end=' ')
    else:
        print(d[N-1],end=' ')
    print(d[N])
