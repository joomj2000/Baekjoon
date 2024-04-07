# import sys
#
# N,S,M=map(int,sys.stdin.readline().strip().split(' '))
# d=[S]
# V_list = [int(x) for x in sys.stdin.readline().strip().split()]
# for i in range(1,N+1):
#     V = V_list[i-1]
#     temp=[]
#     for j in range(len(d)):
#         if V+d[j]<=M:
#             up=V+ d[j]
#             temp.append(up)
#         if d[j]-V>=0:
#             down= d[j] -V
#             temp.append(down)
#     d=temp
#
#
# if len(d)==0:
#     print(-1)
# else:
#     print(max(d))
#


import sys

N, S, M = map(int, sys.stdin.readline().strip().split())
current_max_volume = {S}

V_list = list(map(int, sys.stdin.readline().strip().split()))

for V in V_list:
    next_max_volume = set()
    for volume in current_max_volume:
        if volume + V <= M:
            next_max_volume.add(volume + V)
        if volume - V >= 0:
            next_max_volume.add(volume - V)
    current_max_volume = next_max_volume

if not current_max_volume:
    print(-1)
else:
    print(max(current_max_volume))
