import sys
from queue import PriorityQueue
queue=PriorityQueue()
N= int(sys.stdin.readline())
for _ in range(N):
    x=int(sys.stdin.readline())
    if x==0:
        if queue.empty():
            print('0')
            continue
        print(abs(queue.get()))
    else:
        queue.put(-x)