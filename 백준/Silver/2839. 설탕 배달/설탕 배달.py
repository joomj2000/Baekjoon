import sys

N=int(sys.stdin.readline())
cnt=0

while(N>=3):
    if N%5==0:
        k=N//5
        N%=5
        cnt+=k
    else:
        while(N%5!=0 and N>=3):
            N-=3
            cnt+=1

if N!=0:
    print(-1)
else:
    print(cnt)
