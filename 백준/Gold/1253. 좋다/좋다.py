import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
result=0

for i in range(len(nums)):
    start=1 if i==0 else 0
    #start=0
    end=i-1 if i==len(nums)-1 else len(nums)-1
    while True:
        if start>=end or start<0 or end>=len(nums):
            break
        #print(nums[i],nums[start],nums[end])
        if nums[start]+nums[end]>nums[i]:
            end-=1
            if end==i:
                end-=1
        elif nums[start]+nums[end]<nums[i]:
            start+=1
            if start==i:
                start+=1
        else:
            result+=1
            #print(start,end)
            #print(nums[i])
            break

print(result)