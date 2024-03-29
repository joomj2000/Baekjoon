import sys
N,M =map(int,sys.stdin.readline().split(' '))
tree_height=list(map(int,sys.stdin.readline().split(' ')))
start=1
end=max(tree_height)
while(start<=end): #이진 탐색
    mid=(start+end)//2
    result=0
    for i in tree_height:
        if i>mid:
            result+=(i-mid)
    if result>=M:
        start=mid+1
    else :
        end=mid-1
print(end)