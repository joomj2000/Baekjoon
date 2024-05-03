import sys

N,S=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
cnt=0

if S==0: #S가 0인경우는 공집합을 뺀다
    cnt-=1

for i in range(1<<N): #총 2^N개의 경우의 수 확인
    #print('i',i)
    temp=0
    for j in range(N):
        if i & (1<<j):#한칸씩 왼쪽으로 옮기며 총 N칸 대조
            temp+=num[j]
    if temp==S:
        cnt+=1

print(cnt)
