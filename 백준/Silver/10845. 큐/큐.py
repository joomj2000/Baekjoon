import sys
from collections import deque
queue=deque([])
N = int(sys.stdin.readline())

for _ in range(N):
    command=sys.stdin.readline()
    if 'push' in command:
        num=int(command.split(' ')[1])
        queue.append(num)
    elif 'pop' in command:
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        print(0 if len(queue) > 0 else 1)
    elif 'front' in command:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in command:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
