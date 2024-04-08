import sys
T=int(sys.stdin.readline())
d=[0]*12
d[1]=1
d[2]=2
d[3]=4
for _ in range(T):
    n=int(sys.stdin.readline())
    for i in range(4,n+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    print(d[n])
