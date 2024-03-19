import sys

N=int(sys.stdin.readline())
clock = []
for _ in range(N):
    start, end=map(int, sys.stdin.readline().split())
    clock.append([start, end])
clock=sorted(clock,key=lambda x: (x[1], x[0])) #끝나는 시간을 기준으로 정렬
cnt=0 #진행되는 회의의 개수
meeting_end=clock[0][0]

for start,end in clock:
    if start>=meeting_end:#회의가 끝나는 시간이후에 시작하는 회의일경우 -> 회의 진행
        cnt+=1
        meeting_end=end #회의가 끝나는 시간 업데이트
print(cnt)

