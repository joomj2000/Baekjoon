import sys
N =int(sys.stdin.readline())
money=list(map(int,sys.stdin.readline().split(' ')))
M=int(sys.stdin.readline())
start=1
end=max(money)
while(start<=end): #이진 탐색
    mid=(start+end)//2
    result=0
    for i in money:
        if mid>i:
            result+=i
        else:
            result+=mid
    if result>M:
        end = mid - 1
    else :
        start = mid + 1
print(end)