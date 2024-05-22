import sys
from collections import deque

N=int(sys.stdin.readline())
work=deque()
for _ in range(N):
    work.append(list(map(int,sys.stdin.readline().split())))
#print(work)
done_time=[0]*(N) #시간을 저장할 배열
# while True:
#     target=work.popleft()

for j in range(N):
    i=2
    wait_time=0
    for _ in range(work[j][1]):
        prev=work[j][i]
        if wait_time<done_time[prev-1]:
            wait_time=done_time[prev-1]
        i+=1

    done_time[j]=wait_time+work[j][0]
print(max(done_time))