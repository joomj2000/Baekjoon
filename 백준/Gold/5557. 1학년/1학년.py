import sys
from collections import deque

N = int(sys.stdin.readline())
nums = deque(map(int, sys.stdin.readline().split()))
result = nums.pop()
queue = {}
queue[nums.popleft()] = 1
while nums:
    #print(queue)
    n = nums.popleft()
    temp={}
    # print(n)
    #temp = list(queue.keys())
    for q in queue:
        # print(q)
        if n + q <= 20:
            temp[n + q] = temp.get(n + q, 0) + queue[q]
            # temp.append(n+q)
        if q - n >= 0:
            temp[q - n] = temp.get(q - n, 0) + queue[q]
            # temp.append(q-n)
    # print(temp)
    queue=temp

# cnt=0
# #print(result)
# for q in queue:
#     if q==result:
#         cnt+=1
#

#print(queue)
print(queue[result])
