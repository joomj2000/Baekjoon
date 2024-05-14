import math
from collections import deque

def solution(lines):
    answer = 1
    throughput=deque()
    
    for line in lines:
        end_time=line.split()[1]
        processing_time=float(line.split()[2].split('s')[0])
        H=int(end_time.split(':')[0])
        M=int(end_time.split(':')[1])
        S=float(end_time.split(':')[2])
        end_time=H*3600+M*60+S
        start_time=round(end_time-processing_time+0.001,3)
        throughput.append((start_time,end_time))
    
    while throughput:
        s_t,e_t=throughput.popleft()
        answer=max(answer,sum(x[0]<e_t+1 for x in throughput)+1)
    
    
#     queue=deque()
#     for i in range(len(throughput)):
#         times=throughput[i]
#         for time in times:
#             for j in range(i,len(throughput)):   #i 이후의 값들중 1초 안에시작하는애들을 queue에 넣음     
#                 if throughput[j] not in queue and throughput[j][0]<time+1:
#                     queue.append(throughput[j])
#             # while queue:
#             #     last=queue.popleft()
#             #     if last[1]>=time or time<=last[0]<time+1: #포함
#             #         queue.appendleft(last)
#             #         break
#             queue_len=len(queue)

#             if queue_len>answer:
#                 answer=queue_len    
        
        
    return answer