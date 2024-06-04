import sys
from itertools import combinations
import bisect


N=int(sys.stdin.readline())
result=[]
water=list(map(int,sys.stdin.readline().split()))
water.sort()
#print(water)
start=0
end=len(water)-1
result=float('inf')
result_water=[]
while start<end:
    target=water[start]+water[end]
    if abs(result)>abs(target):
        result=target
        result_water=[water[start],water[end]]
    if target==0:
        print(*sorted([water[start],water[end]]))
        exit()
    elif target>0:
        end-=1
    else:
        start+=1
print(*sorted(result_water))
