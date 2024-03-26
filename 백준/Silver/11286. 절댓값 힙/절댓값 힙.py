import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
queue= PriorityQueue()
for _ in range(N):
    n=int(sys.stdin.readline())
    if(n==0):
        if queue.empty():
            print('0')
            continue
        priority, value = queue.get()
        print(value)
    else:
        queue.put((abs(n),n))