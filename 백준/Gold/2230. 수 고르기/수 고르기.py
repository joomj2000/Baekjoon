import sys


N,M=map(int,sys.stdin.readline().split())
num_list=[int(sys.stdin.readline()) for _ in range(N)]
num_list.sort()
start=end=0
result=2000000000
while start<N and end<N:
    diff= num_list[end]-num_list[start]
    if diff<M:
        end+=1
    else:
        result=min(result,diff)
        start+=1
# while True:
#     if end >= len(num_list) or end <= start or start < 0:
#         break
#     if num_list[end] - num_list[start] < M:
#         if (start,end + 1) not in visited:
#             end += 1
#             visited.add((start, end))
#         elif (start-1,end) not in visited:
#             start-=1
#             visited.add((start,end))
#         else:
#             break
#     else:
#         if (start,end-1) not in visited:
#             end -= 1
#             visited.add((start, end))
#         elif (start+1,end) not in visited:
#             start+=1
#             visited.add((start,end))
#         else:
#             break
#
#
#
#
#     #for start in range(N):
#     end=(start+len(num_list)-1)//2
#     visited=set()
#     while True:
#         if end>=len(num_list) or end<=start or start<0:
#             break
#         if num_list[end]-num_list[start]<M:
#             if end+1 not in visited:
#                 end+=1
#                 visited.add((start,end))
#             elif
#
#             else:
#                 break
#         elif num_list[end]-num_list[start]>=M:
#             if end-1 not in visited:
#                 if result<num_list[end]-num_list[start]:
#                     result=num_list[end]-num_list[start]
#                 #result.append(num_list[end]-num_list[start])
#                 end-=1
#                 visited.add(end)
#             elif start+1 not in visited:
#
#             else:
#                 break
print(result)

