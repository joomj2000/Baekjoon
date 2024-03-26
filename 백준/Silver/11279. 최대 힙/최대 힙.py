import sys
import heapq
heap=[] #힙 생성 
N= int(sys.stdin.readline())
for _ in range(N):
    x=int(sys.stdin.readline())
    if x==0:
        if len(heap)==0:
            print('0')
            continue
        print(abs(heapq.heappop(heap)))
    else:
        heapq.heappush(heap,-x)