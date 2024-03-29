import sys
K,N =map(int,sys.stdin.readline().split(' '))
LAN=[]
for _ in range(K) :
    LAN.append(int(sys.stdin.readline()))
start=1
end=max(LAN)
while(start<=end): #이진탐색
    mid=(start+end)//2
    result=0
    for i in LAN:
        result+=(i//mid)
    if result>=N:
        start=mid+1
    else :
        end=mid-1
print(end)